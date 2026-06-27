#!/usr/bin/env node
/* ============================================================================
 * decode.js — CLI Node para extraer el código a BLOQUES de un .ptj / .hex,
 * usando EL MISMO blocks-decoder.js que el navegador (una sola fuente).
 * Pensado para la pipeline: el paso "extraer" corre en Node; luego Python
 * hace el análisis (AST/PDG/equivalencia) como hasta ahora.
 *
 * Uso:
 *   node decode.js actividad.ptj
 *   node decode.js microbit/juego-toques.hex
 *   node decode.js a.ptj b.hex ...           (varios; separados por encabezado)
 *   node decode.js --json a.ptj              (no implementado aún: IR para pipeline)
 *
 * Importable:  const { decodeFile } = require('./decode.js')
 * ========================================================================== */
"use strict";
const fs = require("fs");
const path = require("path");
const BD = require("./blocks-decoder.js");
const { LZMA } = require("./lib/lzma_worker.min.js");

const ROOT = __dirname;
const readT = p => fs.readFileSync(path.join(ROOT, p), "utf8");
const readJ = p => { try { return JSON.parse(readT(p)); } catch (e) { return {}; } };

// Locale oficiales (se cargan una vez)
const PB_LOC = BD.parseProtobjectLocale({
  blocklyStandardJs: readT("protobject/_locale/es/blockly_standard.js"),
  customBlocksJs: readT("protobject/_locale/es/custom_blocks.js"),
  esDevicesJs: readT("protobject/_locale/es/es_devices.js"),
});
const MB_LOC = BD.parseMicrobitLocale({
  core: readJ("microbit/_locales/es/core-strings.json"),
  music: readJ("microbit/_locales/es/music-strings.json"),
  microphone: readJ("microbit/_locales/es/microphone-strings.json"),
});

// LZMA en Node = misma librería LZMA-JS bundleada que usa el navegador
function nodeLzma(bytes) {
  return new Promise((resolve, reject) => {
    try { LZMA.decompress(bytes, (res, err) => err ? reject(err) : resolve(res), () => {}); }
    catch (e) { reject(e); }
  });
}

async function decodeFile(file) {
  const ext = path.extname(file).toLowerCase();
  const data = fs.readFileSync(file, "utf8");
  if (ext === ".ptj") return BD.renderProtobject(data, PB_LOC);
  if (ext === ".hex") return await BD.renderMicrobit(data, MB_LOC, nodeLzma);
  throw new Error("extensión no soportada: " + ext + " (usa .ptj o .hex)");
}

module.exports = { decodeFile, PB_LOC, MB_LOC, nodeLzma };

if (require.main === module) {
  const args = process.argv.slice(2).filter(a => a !== "--json");
  if (!args.length) { console.error("uso: node decode.js <archivo.ptj|.hex> [...]"); process.exit(1); }
  (async () => {
    for (const f of args) {
      try {
        const out = await decodeFile(f);
        if (args.length > 1) process.stdout.write("===== " + f + " =====\n");
        process.stdout.write(out + "\n");
      } catch (e) { console.error("ERROR " + f + ": " + (e && e.message ? e.message : e)); process.exitCode = 1; }
    }
  })();
}
