/* mi-chart.js: a small SVG line/area chart for the calculators (Components/LineChart wraps it).
   MIChart.draw(el, specJson)  spec = {
     series: [{name, points: [[x, y], ...], kind: "line" | "area", tone: "brand" | "ink" | "muted" | "accent" | "bad"}],
     x_label, y_label, x_fmt: "num" | "pct" | "money", y_fmt: same, zero: true (draw y = 0), marks: [{x, label}]
   }
   Colours come from the app's CSS variables, so light and dark both work. Redraws on resize. */
(function () {
  'use strict';
  var NS = 'http://www.w3.org/2000/svg';
  function mk(tag, attrs, parent) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }
  function fmt(v, kind) {
    var a = Math.abs(v);
    if (kind === 'pct') return (Math.round(v * 10) / 10) + '%';
    var s;
    if (a >= 1e9) s = (v / 1e9).toFixed(a >= 1e10 ? 0 : 1) + 'B';
    else if (a >= 1e6) s = (v / 1e6).toFixed(a >= 1e7 ? 0 : 1) + 'M';
    else if (a >= 1e4) s = Math.round(v / 1e3) + 'k';
    else if (a >= 100) s = String(Math.round(v));
    else s = String(Math.round(v * 100) / 100);
    return s;
  }
  function nice(lo, hi, n) {
    if (hi === lo) { hi = lo + 1; }
    var step = Math.pow(10, Math.floor(Math.log10((hi - lo) / n)));
    var err = (hi - lo) / n / step;
    if (err >= 7.5) step *= 10; else if (err >= 3.5) step *= 5; else if (err >= 1.5) step *= 2;
    var a = Math.floor(lo / step) * step, b = Math.ceil(hi / step) * step, out = [];
    for (var v = a; v <= b + step / 2; v += step) out.push(Math.round(v / step) * step);
    return out;
  }
  var TONE = { brand: '--c-brand', ink: '--c-ink', muted: '--c-muted', accent: '--c-accent', bad: '--c-bad', good: '--c-good' };
  var live = [];

  function draw(el, specJson) {
    var spec;
    try { spec = typeof specJson === 'string' ? JSON.parse(specJson || '{}') : specJson; } catch (e) { return; }
    el.__miSpec = spec;
    if (live.indexOf(el) < 0) live.push(el);
    while (el.firstChild) el.removeChild(el.firstChild);
    var series = (spec && spec.series) || [];
    if (!series.length) return;
    var W = Math.max(280, el.clientWidth || 600), H = Math.max(200, Math.min(320, Math.round(W * 0.48)));
    var pad = { l: 52, r: 14, t: 14, b: 34 };
    var xs = [], ys = [];
    series.forEach(function (s) { s.points.forEach(function (p) { xs.push(p[0]); ys.push(p[1]); }); });
    if (spec.zero) ys.push(0);
    var x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs);
    var yt = nice(Math.min.apply(null, ys), Math.max.apply(null, ys), 4);
    var y0 = yt[0], y1 = yt[yt.length - 1];
    var X = function (v) { return pad.l + (x1 === x0 ? 0 : (v - x0) / (x1 - x0)) * (W - pad.l - pad.r); };
    var Y = function (v) { return H - pad.b - (v - y0) / (y1 - y0) * (H - pad.t - pad.b); };
    var col = function (t) { return 'var(' + (TONE[t] || TONE.brand) + ')'; };
    var grid = 'var(--c-grid)', muted = 'var(--c-muted)';
    var svg = mk('svg', { viewBox: '0 0 ' + W + ' ' + H, width: '100%', height: H, role: 'img',
      'aria-label': spec.label || 'Chart' }, el);
    svg.style.display = 'block';
    var font = 'font-family:var(--font-data);font-size:11px';
    yt.forEach(function (v) {
      mk('line', { x1: pad.l, x2: W - pad.r, y1: Y(v), y2: Y(v), style: 'stroke:' + grid, 'stroke-width': 1 }, svg);
      var t = mk('text', { x: pad.l - 8, y: Y(v) + 4, 'text-anchor': 'end', style: font + ';fill:' + muted }, svg);
      t.textContent = fmt(v, spec.y_fmt);
    });
    var xt = nice(x0, x1, W < 420 ? 3 : 6).filter(function (v) { return v >= x0 - 1e-9 && v <= x1 + 1e-9; });
    xt.forEach(function (v) {
      mk('line', { x1: X(v), x2: X(v), y1: pad.t, y2: H - pad.b, style: 'stroke:' + grid, 'stroke-width': 1 }, svg);
      var t = mk('text', { x: X(v), y: H - pad.b + 18, 'text-anchor': 'middle', style: font + ';fill:' + muted }, svg);
      t.textContent = fmt(v, spec.x_fmt);
    });
    if (spec.zero && y0 < 0 && y1 > 0) mk('line', { x1: pad.l, x2: W - pad.r, y1: Y(0), y2: Y(0), style: 'stroke:' + muted, 'stroke-width': 1.2 }, svg);
    (spec.marks || []).forEach(function (m, i) {
      if (m.x < x0 || m.x > x1) return;
      mk('line', { x1: X(m.x), x2: X(m.x), y1: pad.t, y2: H - pad.b, style: 'stroke:' + muted, 'stroke-dasharray': '4 4' }, svg);
      var right = X(m.x) > W - 90;  /* near the right edge: label on the left of the line */
      var t = mk('text', { x: X(m.x) + (right ? -4 : 4), y: pad.t + 12 + 15 * i, 'text-anchor': right ? 'end' : 'start',
        style: font + ';fill:' + muted }, svg);
      t.textContent = m.label;
    });
    series.forEach(function (s) {
      if (!s.points.length) return;
      var d = s.points.map(function (p, i) { return (i ? 'L' : 'M') + X(p[0]).toFixed(1) + ' ' + Y(p[1]).toFixed(1); }).join(' ');
      var c = col(s.tone);
      if (s.kind === 'area') {
        var base = Y(Math.max(y0, 0));
        mk('path', { d: d + ' L' + X(s.points[s.points.length - 1][0]).toFixed(1) + ' ' + base + ' L' + X(s.points[0][0]).toFixed(1) + ' ' + base + ' Z',
          style: 'fill:' + c, 'fill-opacity': 0.14, stroke: 'none' }, svg);
      }
      mk('path', { d: d, fill: 'none', style: 'stroke:' + c, 'stroke-width': s.tone === 'muted' ? 2 : 2.5, 'stroke-linejoin': 'round',
        'stroke-dasharray': s.dash ? '6 5' : 'none' }, svg);
    });
  }
  var t = null;
  window.addEventListener('resize', function () {
    clearTimeout(t);
    t = setTimeout(function () {
      live = live.filter(function (el) { return el.isConnected; });
      live.forEach(function (el) { draw(el, el.__miSpec); });
    }, 150);
  });
  window.MIChart = { draw: draw };
})();
