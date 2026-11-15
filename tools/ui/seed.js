/* For screenshots of member pages: sign up a fresh account and add one item. Resolves to window.SEED.
   Extend it so every member page has something to show (the app's own main objects). */
(async function () {
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  async function until(fn, what, ms) {
    const end = Date.now() + (ms || 30000);
    while (Date.now() < end) { try { const v = fn(); if (v) return v; } catch (e) {} await sleep(150); }
    throw new Error('timed out waiting for: ' + what);
  }
  const $ = (s) => document.querySelector(s), $$ = (s) => Array.from(document.querySelectorAll(s));
  function type(input, value) {
    input.focus(); input.value = value;
    input.dispatchEvent(new Event('input', { bubbles: true })); input.dispatchEvent(new Event('change', { bubbles: true }));
  }
  try {
    if (location.hash !== '#auth/signup') window.UI_READY = false;
    location.hash = '#auth/signup';
    await until(() => window.UI_READY && $$('.au-card input').length >= 3, 'sign-up');
    const inputs = $$('.au-card input[type=text], .au-card input[type=email], .au-card input[type=password]');
    type(inputs[0], 'Sam Rivera'); type(inputs[1], 'shots' + Date.now() + '@example.com'); type(inputs[2], 'Hb-' + Math.random().toString(36).slice(2) + '-Kq7');
    const tick = $('.au-card input[type=checkbox]'); if (tick && !tick.checked) tick.click();
    $$('.anvil-role-btn-block button').find((b) => /Create account/.test(b.textContent)).click();
    await until(() => location.hash === '#home' && window.UI_READY, 'home', 60000);
    // some progress so Today, Learn and the lesson have something to show: two lessons done, one saved, a card graded
    const vis = (e) => !!e && e.getBoundingClientRect().width > 0;
    for (const id of ['what-investing-is', 'compounding']) {
      window.UI_READY = false; location.hash = '#lesson/' + id;
      await until(() => window.UI_READY && location.hash === '#lesson/' + id && $('.ls-finish .anvil-role-btn-primary button'), id);
      $('.ls-finish .anvil-role-btn-primary button').click();
      await until(() => vis($('.ls-tags .anvil-role-badge-good')), id + ' done');
    }
    $$('.ls-finish .anvil-role-btn button').find((b) => /Save for later/.test(b.textContent)).click();
    await sleep(1500);
    const rv = $$('.page-lesson .rv').find(vis);
    rv.querySelector('.anvil-role-rv-reveal button').click();
    await sleep(300);
    rv.querySelector('.anvil-role-btn-primary button').click();
    await sleep(1500);
    window.UI_READY = false; location.hash = '#home';
    await until(() => window.UI_READY && location.hash === '#home', 'home again', 30000);
    window.SEED = { home: '#home' };
    return window.SEED;
  } catch (e) {
    return { error: String(e && e.message || e) };
  }
})();
