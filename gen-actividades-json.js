#!/usr/bin/env node
/* Genera pipeline-equivalence/actividades.json: índice ordenado (1..17) que
 * alimenta el dashboard index.html. Orden = activities.json; título = frontmatter
 * real del .md; code = nombre de carpeta en reporte/actividades/ y de .ptj/.hex. */
"use strict";
const fs = require("fs"), path = require("path");
const ROOT = __dirname;

const SLUG2CODE = {
  "02.1-heart-beat": "corazon-forever-loop", "02.2-xylophone": "xilofono-inclinacion", 
  "02.3-led-xylophone": "xilofono-inclinacion-con-nota-led", "03.1-music-visualizer": "luci-discoteca-ruido",
  "14.1-ticklish-robot": "robot-risa-simpatica-al-ruido",
  "16.1-cookie-thief-alarm": "alarma-caja-galletas", "16.2-sunflower-alarm-clock": "despertador-por-la-manana",
  "16.3-bat-in-the-dark": "luces-de-fiesta-al-oscurecer", "16.4-robot-activation-challenge": "juego-toques", "16.5-my-robot-friend-heart": "corazon-variables-eventos", 
  "16.6-magic-birthday-candle": "flama-vela-con-soplo", "16.7-dont-spill-liquid-game": "nivel-con-ruido", 
  "17.1-magic-clap-switch": "luz-encendida-al-ruido", "17.2-cinematic-power-on": "luz-encendida-ruido-animacion",
  "19.1-digital-hot-potato": "papas-caliente-juego", 
  "22.1-dj-metronome": "metronomo-con-inclinacion", "22.2-scream-battle": "gritometro-tiempo-gritos"
};

function titulo(slug) {
  let md = fs.readFileSync(path.join(ROOT, "_activities", slug + ".es.md"), "utf8");
  md = md.replace(/^﻿/, "").replace(/\r\n/g, "\n").replace(/\r/g, "\n");   // CRLF/BOM-tolerant
  const fm = md.match(/^---\n([\s\S]*?)\n---/);
  if (!fm) return slug;
  const t = fm[1].match(/^title:\s*(.+)$/m);
  return t ? t[1].trim().replace(/^["']|["']$/g, "") : slug;
}

const order = JSON.parse(fs.readFileSync(path.join(ROOT, "activities.json"), "utf8")).activities;
const out = order.map((slug, i) => ({ num: i + 1, code: SLUG2CODE[slug], slug, title: titulo(slug) }));
fs.writeFileSync(path.join(ROOT, "pipeline-equivalence", "actividades.json"), JSON.stringify(out, null, 2) + "\n");
console.log(out.map(a => `${String(a.num).padStart(2)}. ${a.code.padEnd(34)} ${a.title}`).join("\n"));
