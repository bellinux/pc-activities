#!/usr/bin/env node
/* ============================================================================
 * gen-text-json.js — Paso 1 de la pipeline: genera, por cada actividad, una
 * carpeta en pipeline-equivalence/reporte/actividades/<code>/ con
 *   text_protobject.json  y  text_makecode.json
 * usando EL MISMO blocks-decoder.js (modo "solo estructura": sin comentarios,
 * LEDs colapsados). Esquema: { platform, extracted_text: [lineas...] }.
 * ========================================================================== */
"use strict";
const fs = require("fs");
const path = require("path");
const BD = require("./blocks-decoder.js");
const { PB_LOC, MB_LOC, nodeLzma } = require("./decode.js");

const ROOT = __dirname;
const OUT = path.join(ROOT, "pipeline-equivalence", "reporte", "actividades");
const STRUCT = { comments: false, leds: false };   // solo estructura

// slug -> code (code = nombre de carpeta y de los archivos .ptj/.hex)
const ACTS = {
  "02.1-xylophone": "xilofono-inclinacion", "02.2-music-visualizer": "luci-discoteca-ruido",
  "03.1-led-xylophone": "xilofono-inclinacion-con-nota-led", "04.1-heart-beat": "corazon-forever-loop",
  "14.1-ticklish-robot": "robot-risa-simpatica-al-ruido", "14.2-my-robot-friend-heart": "corazon-variables-eventos",
  "16.1-cookie-thief-alarm": "alarma-caja-galletas", "16.2-sunflower-alarm-clock": "despertador-por-la-manana",
  "16.3-bat-in-the-dark": "luces-de-fiesta-al-oscurecer", "16.4-robot-activation-challenge": "juego-toques",
  "16.5-magic-clap-switch": "luz-encendida-al-ruido", "17.1-magic-birthday-candle": "flama-vela-con-soplo",
  "19.1-digital-hot-potato": "papas-caliente-juego", "21.1-cinematic-power-on": "luz-encendida-ruido-animacion",
  "22.1-dj-metronome": "metronomo-con-inclinacion", "22.2-applause-battle": "aplausometro-tiempo-aplausos",
  "22.3-dont-spill-liquid-game": "nivel-con-ruido"
};

// Quita la cabecera FUENTE: y las líneas en blanco -> array de líneas de código
const toLines = text => text.split("\n").filter(l => l.trim() !== "" && !/^FUENTE:/.test(l));
const writeJson = (file, obj) => fs.writeFileSync(file, JSON.stringify(obj, null, 4) + "\n");

(async () => {
  let n = 0;
  for (const code of Object.values(ACTS)) {
    const dir = path.join(OUT, code);
    fs.mkdirSync(dir, { recursive: true });
    const ptj = fs.readFileSync(path.join(ROOT, "protobject", "equivalent-" + code + ".ptj"), "utf8");
    const hex = fs.readFileSync(path.join(ROOT, "microbit", code + ".hex"), "utf8");
    const pbLines = toLines(BD.renderProtobject(ptj, PB_LOC, STRUCT));
    const mbLines = toLines(await BD.renderMicrobit(hex, MB_LOC, nodeLzma, STRUCT));
    writeJson(path.join(dir, "text_protobject.json"), { platform: "Protobject", extracted_text: pbLines });
    writeJson(path.join(dir, "text_makecode.json"), { platform: "MakeCode", extracted_text: mbLines });
    console.log("✓ " + code + "  (pb " + pbLines.length + " l., mb " + mbLines.length + " l.)");
    n++;
  }
  console.log("\nListo: " + n + " actividades -> " + OUT);
})();
