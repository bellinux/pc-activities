/* ============================================================================
 * blocks-decoder.js — Extrae el código a BLOQUES desde un .ptj (Protobject)
 * o un .hex (micro:bit / MakeCode). ISOMORFO: el MISMO archivo corre en el
 * navegador (en vivo, sin Python) y en Node (CLI para la pipeline). Una sola
 * fuente de verdad, imposible que se desalineen.
 *
 * Port fiel de protobject/decode_blocks.py y microbit/decode_hex.py.
 * Etiquetas oficiales (es):
 *   protobject/_locale/es/{blockly_standard.js, custom_blocks.js, es_devices.js}
 *   microbit/_locales/es/{core,music,microphone}-strings.json
 *
 * NAVEGADOR (auto-carga locale via fetch; LZMA = global LZMA del lzma_worker):
 *   await BlocksDecoder.protobject(ptjText) -> string
 *   await BlocksDecoder.microbit(hexText)   -> string
 * NODE (se inyecta locale + LZMA; ver decode.js):
 *   BlocksDecoder.renderProtobject(ptjText, loc) -> string
 *   await BlocksDecoder.renderMicrobit(hexText, loc, lzmaFn) -> string
 *   BlocksDecoder.parseProtobjectLocale({blocklyStandardJs, customBlocksJs, esDevicesJs}) -> loc
 *   BlocksDecoder.parseMicrobitLocale({core, music, microphone}) -> loc
 * ========================================================================== */
(function (root, factory) {
  const api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  if (root) root.BlocksDecoder = api;
})(typeof self !== "undefined" ? self : (typeof globalThis !== "undefined" ? globalThis : this), function () {
  "use strict";

  // ---------- mini-parser XML (navegador + Node, sin dependencias) ----------
  function decodeEntities(s) {
    return s.replace(/&(#x?[0-9a-fA-F]+|[A-Za-z]+);/g, (m, e) => {
      if (e[0] === "#") { const cp = (e[1] === "x" || e[1] === "X") ? parseInt(e.slice(2), 16) : parseInt(e.slice(1), 10); return isNaN(cp) ? m : String.fromCodePoint(cp); }
      return ({ amp: "&", lt: "<", gt: ">", quot: '"', apos: "'" })[e] || m;
    });
  }
  function makeNode(tag) {
    return {
      tag, localName: tag, tagName: tag, attrs: {}, children: [], _text: "",
      getAttribute(n) { return Object.prototype.hasOwnProperty.call(this.attrs, n) ? this.attrs[n] : null; },
      get textContent() { return this._text; }
    };
  }
  // Devuelve el elemento raíz <xml>. Produce nodos con la MISMA interfaz que el
  // DOM que usaba antes (children / getAttribute / textContent / localName).
  function parseXml(xml) {
    xml = String(xml).replace(/^﻿/, "").replace(/<\?[\s\S]*?\?>/g, "").replace(/<!--[\s\S]*?-->/g, "").replace(/<!DOCTYPE[^>]*>/gi, "");
    const docRoot = makeNode("#doc"), stack = [docRoot];
    const tokenRe = /<(\/)?([A-Za-z_][\w:.\-]*)((?:\s+[\w:.\-]+\s*=\s*(?:"[^"]*"|'[^']*'))*)\s*(\/)?>|([^<]+)/g;
    const attrRe = /([\w:.\-]+)\s*=\s*(?:"([^"]*)"|'([^']*)')/g;
    let m;
    while ((m = tokenRe.exec(xml))) {
      if (m[5] !== undefined) { stack[stack.length - 1]._text += decodeEntities(m[5]); }   // texto
      else if (m[1]) { if (stack.length > 1) stack.pop(); }                                 // cierre </t>
      else {                                                                                // apertura / auto-cierre
        const node = makeNode(m[2]);
        let a; attrRe.lastIndex = 0;
        while ((a = attrRe.exec(m[3]))) node.attrs[a[1]] = decodeEntities(a[2] !== undefined ? a[2] : a[3]);
        stack[stack.length - 1].children.push(node);
        if (!m[4]) stack.push(node);
      }
    }
    return docRoot.children[0];
  }

  // ---------- parsing Blockly (común) ----------
  const TAG = el => el.localName || el.tagName;
  function firstBlock(el) {
    let shadow = null;
    for (const ch of el.children) {
      const t = TAG(ch);
      if (t === "block") return ch;
      if (t === "shadow" && !shadow) shadow = ch;
    }
    return shadow;
  }
  function parts(el) {
    const f = {}, v = {}, s = {}; let n = null, c = null;
    for (const ch of el.children) {
      const t = TAG(ch);
      if (t === "field") f[ch.getAttribute("name")] = (ch.textContent || "").trim();
      else if (t === "value") v[ch.getAttribute("name")] = firstBlock(ch);
      else if (t === "statement") s[ch.getAttribute("name")] = firstBlock(ch);
      else if (t === "next") n = firstBlock(ch);
      else if (t === "comment") c = (ch.textContent || "").trim();
    }
    return { f, v, s, n, c };
  }
  const repl = (str, map) => Object.keys(map).reduce((a, k) => a.split(k).join(map[k]), str);

  // ============================================================================
  //  PROTOBJECT
  // ============================================================================
  function parseProtobjectLocale(texts) {
    const MSG = {};
    texts.blocklyStandardJs.replace(/Blockly\.Msg\["([^"]+)"\]\s*=\s*"((?:\\.|[^"\\])*)"/g, (m, k, val) => { MSG[k] = JSON.parse('"' + val + '"'); return m; });
    const CUST = (new Function(texts.customBlocksJs + "\nreturn locutions;"))().blocks;
    const DEV = (new Function(texts.esDevicesJs + "\nreturn locutions;"))();
    return { MSG, CUST, DEV };
  }

  const PB_CAT = { DibujoLED: "matrixDraw", "Inclinación": "smartphoneOrientation", ReproductorSonido: "audioPlayer",
    "BateríaMusical": "playDrum", NivelRuido: "noiseLevel", TecladoMusical: "playKeyboard",
    IntensidadLuz: "lightIntensity", "BotónTáctil": "touchButton", DibujarEscribir: "interactiveTurtleDraw" };
  // Categoría por TIPO de componente (robusto: independiente del nombre/idioma del prefijo).
  const PB_TYPE = { MatrixDraw: "matrixDraw", NoiseLevel: "noiseLevel", AudioPlayer: "audioPlayer",
    TouchButton: "touchButton", SmartphoneOrientation: "smartphoneOrientation", PlayDrum: "playDrum",
    PlayKeyboard: "playKeyboard", LightIntensity: "lightIntensity", InteractiveWriteDraw: "interactiveTurtleDraw" };
  let _comps = {};   // name -> type (del JSON de componentes del .ptj en curso)
  const pbCat = d => (_comps[d.comp] && PB_TYPE[_comps[d.comp]]) || PB_CAT[d.base];
  function midiNote(n) {
    n = parseInt(n, 10); if (isNaN(n)) return String(n);
    const names = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si"];
    return names[((n % 12) + 12) % 12] + (Math.floor(n / 12) - 1);
  }
  function pbMatrix(csv) {
    const v = csv.split(",");
    if (v.length !== 49) return ["[matriz " + v.length + "]"];
    const rows = [];
    for (let r = 0; r < 7; r++) { let s = ""; for (let c = 0; c < 7; c++) s += (v[r * 7 + c] !== "0" && v[r * 7 + c] !== "") ? "#" : "."; rows.push(s); }
    return rows;
  }
  const par = x => (x.startsWith("(") && x.endsWith(")")) ? x : "(" + x + ")";
  function pbDev(t) {
    const rest = t.slice("protobject_".length), p = rest.split("_");
    const comp = p[0], base = comp.replace(/\d+$/, "");
    if (rest.endsWith("_get")) return { comp, base, action: "get", kind: "get" };
    if (rest.endsWith("_change")) return { comp, base, action: "change", kind: "change" };
    return { comp, base, action: p.length > 1 ? p[1] : "", kind: "set" };
  }

  function pbExpr(el, L) {
    if (!el) return "?";
    const t = el.getAttribute("type"), { f, v } = parts(el);
    const E = k => pbExpr(v[k], L), M = L.MSG;
    if (t === "math_number") return f.NUM || "?";
    if (t === "logic_boolean") return f.BOOL === "TRUE" ? (M.LOGIC_BOOLEAN_TRUE || "true") : (M.LOGIC_BOOLEAN_FALSE || "false");
    if (t === "text") return '"' + (f.TEXT || "") + '"';
    if (t === "variables_get") return f.VAR || "?";
    if (t === "math_arithmetic") return "(" + E("A") + " " + ({ ADD: "+", MINUS: "−", MULTIPLY: "×", DIVIDE: "÷", POWER: "^" }[f.OP] || f.OP) + " " + E("B") + ")";
    if (t === "logic_compare") return "(" + E("A") + " " + ({ EQ: "=", NEQ: "≠", LT: "<", LTE: "≤", GT: ">", GTE: "≥" }[f.OP] || f.OP) + " " + E("B") + ")";
    if (t === "logic_operation") return "(" + E("A") + " " + (f.OP === "AND" ? (M.LOGIC_OPERATION_AND || "y") : (M.LOGIC_OPERATION_OR || "o")) + " " + E("B") + ")";
    if (t === "logic_negate") return par((M.LOGIC_NEGATE_TITLE || "no %1").replace("%1", E("BOOL")));
    if (t === "math_round") { const k = { ROUND: "MATH_ROUND_OPERATOR_ROUND", ROUNDUP: "MATH_ROUND_OPERATOR_ROUNDUP", ROUNDDOWN: "MATH_ROUND_OPERATOR_ROUNDDOWN" }[f.OP] || "MATH_ROUND_OPERATOR_ROUND"; return par((M[k] || "redondear") + " " + E("NUM")); }
    if (t === "math_random_int") return par((M.MATH_RANDOM_INT_TITLE || "%1..%2").replace("%1", E("FROM")).replace("%2", E("TO")));
    if (t === "math_constrain") return par(repl(M.MATH_CONSTRAIN_TITLE || "limitar %1 %2 %3", { "%1": E("VALUE"), "%2": E("LOW"), "%3": E("HIGH") }));
    if (t === "color_light") return par(L.CUST.color.clarityAt + " " + E("LEVEL") + " %");
    if (t === "colour_picker") return f.COLOUR || "color";
    if (t === "sounds_list") { const sid = (f.VAR || "").split(".")[0]; return "'" + (L.CUST.sounds[sid] || sid) + "'"; }
    if (t === "protobject_milliseconds") return L.CUST.timing.milliseconds;
    if (t === "control_note") return midiNote(f.VAR);
    if (t === "control_drum") return ({ "0": L.CUST.music.drumBass, "1": L.CUST.music.drumTom, "2": L.CUST.music.drumHi }[f.VAR]) || ("tambor " + f.VAR);
    if (t && t.startsWith("protobject_") && t.endsWith("_get")) {
      const d = pbDev(t), loc = L.DEV[pbCat(d)] || {}, prop = f.property || "";
      const pk = ({ lightIntensity: "light" })[prop] || prop;
      return par((loc[pk] || loc[prop] || prop) + " in " + d.comp);
    }
    return t;
  }

  function pbDevBody(comp, base, action, fields, values, L) {
    const cat = pbCat({ comp, base }), d = L.DEV[cat] || {}, E = k => pbExpr(values[k], L);
    const enC = (d.onTxt || d.inTxt || "en") + " " + comp;
    if (cat === "matrixDraw") {
      if (action === "drawOnXY") return d.drawOn + " " + E("VAR") + " " + d.yTxt + " " + E("VAR2") + " " + d.withColour + " " + E("VAR3") + " " + enC;
      if (action === "draw") return { head: d.draw + " " + d.withColour + " " + E("VAR2") + " " + enC, matrix: values.VAR };
      if (action === "clear") return d.clear + " " + enC;
      if (action === "background") return d.setBg + " " + E("VAR") + " " + enC;
    }
    if (cat === "audioPlayer") {
      if (action === "play") return d.play + " " + E("VAR") + " " + enC;
      if (action === "stop") return d.stop + " " + comp;
    }
    if (cat === "playKeyboard" || cat === "playDrum") {
      if (action === "play") { const vr = values.VAR, picker = vr && ["control_note", "control_drum"].includes(vr.getAttribute("type")); return (picker ? d.play : d.playNumber) + " " + E("VAR") + " " + enC; }
      if (action === "stop") return d.stop + " " + enC;
    }
    if (cat === "interactiveTurtleDraw") {
      if (action === "setSize") return d.setSize + " " + E("VAR") + " " + enC;
      if (action === "writeText") return d.write + " " + E("VAR") + " " + enC;
      if (action === "clear") return d.clear + " " + enC;
    }
    return action + " " + Object.keys(values).map(E).join(" ") + " " + enC;
  }

  function pbRenderBlock(block, indent, out, L, O) {
    const M = L.MSG, C = L.CUST, pad = "  ".repeat(indent);
    while (block) {
      const t = block.getAttribute("type"), { f, v, s, n, c } = parts(block);
      const E = k => pbExpr(v[k], L);
      let head = null, matrix = null;
      if (t === "main_loop") head = C.loops.mainLoop;
      else if (t === "on_start") head = C.playPressed;
      else if (t === "protobject_sleep") head = C.timing.delayOf + " " + E("VAR") + " " + (f.timingType === "ms" ? C.timing.milliseconds : C.timing.seconds);
      else if (t === "controls_repeat_ext") head = (M.CONTROLS_REPEAT_TITLE || "repetir %1").replace("%1", E("TIMES"));
      else if (t === "controls_for") head = repl(M.CONTROLS_FOR_TITLE || "contar %1 %2 %3 %4", { "%1": f.VAR || "i", "%2": E("FROM"), "%3": E("TO"), "%4": E("BY") });
      else if (t === "controls_whileUntil") head = (f.MODE === "WHILE" ? (M.CONTROLS_WHILEUNTIL_OPERATOR_WHILE || "repetir mientras") : (M.CONTROLS_WHILEUNTIL_OPERATOR_UNTIL || "repetir hasta")) + " " + E("BOOL");
      else if (t === "variables_set") head = repl(M.VARIABLES_SET || "establecer %1 a %2", { "%1": f.VAR || "?", "%2": E("VALUE") });
      else if (t === "math_change") head = repl(M.MATH_CHANGE_TITLE || "añadir %2 a %1", { "%1": f.VAR || "?", "%2": E("DELTA") });
      else if (t === "controls_if") {
        let i = 0, first = true;
        while (("IF" + i) in v || ("DO" + i) in s) {
          const cond = ("IF" + i) in v ? E("IF" + i) : "?";
          const kw = first ? (M.CONTROLS_IF_MSG_IF || "si") : (M.CONTROLS_IF_MSG_ELSEIF || "sino si");
          let line = pad + kw + " " + cond + ":";
          if (first && c && O.comments) line += "   // " + c.replace(/\n/g, " ");
          out.push(line); first = false;
          if (s["DO" + i]) pbRenderBlock(s["DO" + i], indent + 1, out, L, O);
          i++;
        }
        if (s.ELSE) { out.push(pad + (M.CONTROLS_IF_MSG_ELSE || "sino") + ":"); pbRenderBlock(s.ELSE, indent + 1, out, L, O); }
        block = n; continue;
      }
      else if (t && t.startsWith("protobject_") && t.endsWith("_change")) {
        const d = pbDev(t), ev = (L.DEV[pbCat(d)] || {})[(f.property || "") + "Ev"] || f.property;
        head = C.events.on + " " + d.comp + " " + ev;
      }
      else if (t && t.startsWith("protobject_")) {
        const d = pbDev(t), r = pbDevBody(d.comp, d.base, d.action, f, v, L);
        if (r && r.head) { head = r.head; matrix = r.matrix; } else head = r;
      }
      else head = "(" + t + ")";
      const bodies = Object.values(s).filter(Boolean);
      const showMatrix = matrix && O.leds;
      let line = pad + head + ((bodies.length || showMatrix) ? ":" : "");
      if (c && O.comments) line += "   // " + c.replace(/\n/g, " ");
      out.push(line);
      if (showMatrix) { const mf = parts(matrix).f; for (const row of pbMatrix(mf.btmMatrix || "")) out.push(pad + "    " + row); }
      for (const b of bodies) pbRenderBlock(b, indent + 1, out, L, O);
      block = n;
    }
  }

  function renderProtobject(ptjText, L, opts) {
    const O = { comments: true, leds: true, ...(opts || {}) };
    const inner = JSON.parse(ptjText.trim().slice(ptjText.indexOf("(") + 1, ptjText.lastIndexOf(")")));
    const nl0 = inner.indexOf("\n");
    try { _comps = {}; JSON.parse(inner.slice(0, nl0)).forEach(c => { _comps[c.name] = c.type; }); } catch (e) { _comps = {}; }
    const xml = inner.slice(nl0 + 1);
    const root = parseXml(xml), out = ["FUENTE: Protobject (bloques, etiquetas oficiales es)", ""];
    for (const ch of root.children) if (["block", "shadow"].includes(TAG(ch))) { pbRenderBlock(ch, 0, out, L, O); out.push(""); }
    return out.join("\n");
  }

  // ============================================================================
  //  MICRO:BIT
  // ============================================================================
  function parseMicrobitLocale(jsons) {
    const STR = Object.assign({}, jsons.core || {}, jsons.music || {}, jsons.microphone || {});
    const BK = { on_start: "al iniciar", repeat: "repetir {0} veces", for: "para {0} de 0 a {1}", while: "mientras {0}",
      set: "fijar {0} a {1}", change: "cambiar {0} por {1}", if: "si {0} entonces", elseif: "si no, si {0} entonces", else: "si no" };
    const NOTE = { 131:"Do3",139:"Do#3",147:"Re3",156:"Re#3",165:"Mi3",175:"Fa3",185:"Fa#3",196:"Sol3",208:"Sol#3",220:"La3",233:"La#3",247:"Si3",
      262:"Do",277:"Do#",294:"Re",311:"Re#",330:"Mi",349:"Fa",370:"Fa#",392:"Sol",415:"Sol#",440:"La",466:"La#",494:"Si",
      523:"Do5",554:"Do#5",587:"Re5",622:"Re#5",659:"Mi5",698:"Fa5",740:"Fa#5",784:"Sol5",831:"Sol#5",880:"La5",932:"La#5",988:"Si5" };
    const SYM = { device_forever:"basic.forever", device_show_leds:"basic.showLeds", device_show_number:"basic.showNumber",
      device_pause:"basic.pause", device_clear_display:"basic.clearScreen", device_plot:"led.plot", device_unplot:"led.unplot",
      device_set_brightness:"led.setBrightness", device_acceleration:"input.acceleration", device_get_light_level:"input.lightLevel",
      device_get_sound_level:"input.soundLevel", device_get_running_time:"input.runningTime", input_on_sound:"input.onSound",
      device_gesture_event:"input.onGesture", input_logo_event:"input.onLogoEvent", music_playable_play:"music.play",
      music_playable_play_default_bkg:"music._playDefaultBackground", music_tone_playable:"music.tonePlayable", device_beat:"music.beat",
      device_builtin_melody_playable:"music.builtInMelody", soundExpression_builtinPlayableSoundEffect:"music.builtinPlayableSoundEffect",
      music_stop_all_sounds:"music.stopAllSounds", device_ring:"music.ringTone", device_stop_melody:"music.stopMelody",
      device_random:"Math.randomRange", math_constrain_value:"Math.constrain", serial_writevalue:"serial.writeValue" };
    return { STR, BK, NOTE, SYM };
  }

  function enumEs(val, L) { if (val == null) return "?"; let s = L.STR[val + "|block"] || L.STR[val] || val.split(".").pop(); return s.replace(/^\{[^}]*\}/, "").trim(); }
  function leds(str) { return str.replace(/`/g, "").split("\n").map(x => x.trim()).filter(x => x && /^[#. ]+$/.test(x)); }
  function pxtFill(block, L) {
    const t = block.getAttribute("type"), { f, v } = parts(block), sym = L.SYM[t];
    let tmpl = sym ? L.STR[sym + "|block"] : null;
    if (!tmpl) return null;
    tmpl = tmpl.split("||")[0];
    let out = tmpl.replace(/[%$](\w+)(?:=\w+)?/g, (m, name) => (v[name] ? mbExpr(v[name], L) : (name in f ? enumEs(f[name], L) : "")));
    return out.replace(/\|/g, " ").replace(/\s+/g, " ").trim();
  }
  function mbExpr(el, L) {
    if (!el) return "?";
    const t = el.getAttribute("type"), { f, v } = parts(el), E = k => mbExpr(v[k], L);
    if (t === "math_number" || t === "math_whole_number") return f.NUM || "?";
    if (t === "math_number_minmax") return f.SLIDER || "?";
    if (t === "timePicker") return f.ms || "?";
    if (t === "logic_boolean") return f.BOOL === "TRUE" ? "verdadero" : "falso";
    if (t === "text") return '"' + (f.TEXT || "") + '"';
    if (t === "variables_get" || t === "variables_get_reporter") return f.VAR || "?";
    if (t === "math_arithmetic") return "(" + E("A") + " " + ({ ADD: "+", MINUS: "−", MULTIPLY: "×", DIVIDE: "÷", POWER: "^" }[f.OP] || f.OP) + " " + E("B") + ")";
    if (t === "logic_compare") return "(" + E("A") + " " + ({ EQ: "=", NEQ: "≠", LT: "<", LTE: "≤", GT: ">", GTE: "≥" }[f.OP] || f.OP) + " " + E("B") + ")";
    if (t === "logic_operation") return "(" + E("A") + " " + ({ AND: "y", OR: "o" }[f.OP] || f.OP) + " " + E("B") + ")";
    if (t === "logic_negate") return par("no " + E("BOOL"));
    if (t === "math_js_round") return par("redondeo " + E("ARG0"));
    if (t === "device_note") { const nm = f.name; const k = parseInt(nm, 10); return (L.NOTE[k] || nm + " Hz"); }
    const pf = pxtFill(el, L);
    return pf != null ? par(pf) : t;
  }
  function mbRenderBlock(block, indent, out, L, O) {
    const B = L.BK, pad = "  ".repeat(indent);
    while (block) {
      const t = block.getAttribute("type"), { f, v, s, n, c } = parts(block), E = k => mbExpr(v[k], L);
      if (t === "controls_if") {
        let i = 0, first = true;
        while (("IF" + i) in v || ("DO" + i) in s) {
          const cond = ("IF" + i) in v ? E("IF" + i) : "?";
          let line = pad + (first ? B.if : B.elseif).replace("{0}", cond) + ":";
          if (first && c && O.comments) line += "   // " + c.replace(/\n/g, " ");
          out.push(line); first = false;
          if (s["DO" + i]) mbRenderBlock(s["DO" + i], indent + 1, out, L, O);
          i++;
        }
        if (s.ELSE) { out.push(pad + B.else + ":"); mbRenderBlock(s.ELSE, indent + 1, out, L, O); }
        block = n; continue;
      }
      if (t === "device_show_leds") {
        const ledHead = pad + (pxtFill(block, L) || "mostrar LEDs");
        const cm = (c && O.comments) ? "   // " + c.replace(/\n/g, " ") : "";
        if (O.leds) { out.push(ledHead + ":" + cm); for (const row of leds(f.LEDS || "")) out.push(pad + "    " + row); }
        else { out.push(ledHead + cm); }
        block = n; continue;
      }
      let head;
      if (t === "pxt-on-start") head = B.on_start;
      else if (t === "controls_repeat_ext") head = B.repeat.replace("{0}", E("TIMES"));
      else if (t === "pxt_controls_for") head = B.for.replace("{0}", E("VAR")).replace("{1}", E("TO"));
      else if (t === "device_while") head = B.while.replace("{0}", E("COND"));
      else if (t === "variables_set") head = B.set.replace("{0}", f.VAR || "?").replace("{1}", E("VALUE"));
      else if (t === "variables_change") head = B.change.replace("{0}", f.VAR || "?").replace("{1}", E("VALUE"));
      else head = pxtFill(block, L) || ("(" + t + ")");
      const bodies = Object.values(s).filter(Boolean);
      let line = pad + head + (bodies.length ? ":" : "");
      if (c && O.comments) line += "   // " + c.replace(/\n/g, " ");
      out.push(line);
      for (const b of bodies) mbRenderBlock(b, indent + 1, out, L, O);
      block = n;
    }
  }

  // hex -> bytes de datos (0x00/0x0D/0x0E)
  function hexData(text) {
    const out = [];
    for (const raw of text.split("\n")) {
      const l = raw.trim();
      if (l[0] !== ":") continue;
      const count = parseInt(l.substr(1, 2), 16), rt = parseInt(l.substr(7, 2), 16);
      if (rt === 0x00 || rt === 0x0D || rt === 0x0E) for (let i = 0; i < count; i++) out.push(parseInt(l.substr(9 + i * 2, 2), 16));
    }
    return Uint8Array.from(out);
  }
  const MAGIC = [0x41, 0x14, 0x0E, 0x2F, 0xB8, 0x2F, 0xA2, 0xBB];
  function findMagic(b) { for (let i = 0; i + 8 <= b.length; i++) { let ok = true; for (let j = 0; j < 8; j++) if (b[i + j] !== MAGIC[j]) { ok = false; break; } if (ok) return i; } return -1; }
  const u16 = (b, p) => b[p] | (b[p + 1] << 8);
  const u32 = (b, p) => (b[p] | (b[p + 1] << 8) | (b[p + 2] << 16) | (b[p + 3] << 24)) >>> 0;
  async function mbExtractBlocksXml(hexText, lzmaFn) {
    const blob = hexData(hexText), p0 = findMagic(blob);
    if (p0 < 0) throw new Error("micro:bit: no es un .hex con código MakeCode incrustado");
    let p = p0 + 8;
    const metaLen = u16(blob, p), textLen = u32(blob, p + 2); p += 8;
    p += metaLen;
    const text = blob.slice(p, p + textLen);
    const out = await lzmaFn(text);                 // Array/typed de bytes o string
    const raw = (typeof out === "string") ? out : new TextDecoder("utf-8").decode(Uint8Array.from(out, x => x & 0xff));
    // <headerJSON><filesJSON> concatenados: leer el segundo objeto
    let depth = 0, start = raw.indexOf("{"), i = start, inStr = false, esc = false, ends = [];
    for (; i < raw.length; i++) { const ch = raw[i]; if (inStr) { if (esc) esc = false; else if (ch === "\\") esc = true; else if (ch === '"') inStr = false; } else { if (ch === '"') inStr = true; else if (ch === "{") depth++; else if (ch === "}") { depth--; if (depth === 0) { ends.push(i); } } } if (ends.length === 2) break; }
    const files = JSON.parse(raw.slice(ends[0] + 1, ends[1] + 1));
    return files["main.blocks"] || "";
  }
  async function renderMicrobit(hexText, L, lzmaFn, opts) {
    const O = { comments: true, leds: true, ...(opts || {}) };
    const xml = await mbExtractBlocksXml(hexText, lzmaFn);
    if (!xml) throw new Error("micro:bit: sin main.blocks");
    const root = parseXml(xml), out = ["FUENTE: micro:bit / MakeCode (bloques, etiquetas oficiales es-ES)", ""];
    for (const ch of root.children) if (["block", "shadow"].includes(TAG(ch))) { mbRenderBlock(ch, 0, out, L, O); out.push(""); }
    return out.join("\n");
  }

  // ============================================================================
  //  Comodidades NAVEGADOR: auto-carga locale (fetch) + LZMA global
  // ============================================================================
  let _pb = null, _mb = null;
  async function pbLocaleBrowser() {
    if (_pb) return _pb;
    const b = "protobject/_locale/es/";
    const [bs, cb, dv] = await Promise.all(["blockly_standard.js", "custom_blocks.js", "es_devices.js"]
      .map(f => fetch(b + f, { cache: "no-store" }).then(r => r.text())));
    return _pb = parseProtobjectLocale({ blocklyStandardJs: bs, customBlocksJs: cb, esDevicesJs: dv });
  }
  async function mbLocaleBrowser() {
    if (_mb) return _mb;
    const b = "microbit/_locales/es/";
    const [c, mu, mi] = await Promise.all(["core-strings.json", "music-strings.json", "microphone-strings.json"]
      .map(f => fetch(b + f, { cache: "no-store" }).then(r => r.ok ? r.json() : {}).catch(() => ({}))));
    return _mb = parseMicrobitLocale({ core: c, music: mu, microphone: mi });
  }
  function browserLzma(bytes) {
    const G = (typeof self !== "undefined") ? self : (typeof window !== "undefined") ? window : (typeof globalThis !== "undefined") ? globalThis : {};
    return new Promise((resolve, reject) => {
      const lz = G.LZMA;
      if (!lz || !lz.decompress) return reject(new Error("LZMA no disponible (carga lib/lzma_worker.min.js)"));
      try { lz.decompress(bytes, (res, err) => err ? reject(err) : resolve(res), () => {}); } catch (e) { reject(e); }
    });
  }

  // ---------- API ----------
  return {
    // primitivas (para Node / pipeline)
    parseXml, parseProtobjectLocale, parseMicrobitLocale, renderProtobject, renderMicrobit,
    // comodidades navegador (auto-cargan locale; LZMA global)
    protobject: (ptjText, loc) => loc ? Promise.resolve(renderProtobject(ptjText, loc)) : pbLocaleBrowser().then(L => renderProtobject(ptjText, L)),
    microbit: (hexText, loc, lzmaFn) => (loc ? Promise.resolve(loc) : mbLocaleBrowser()).then(L => renderMicrobit(hexText, L, lzmaFn || browserLzma)),
  };
});
