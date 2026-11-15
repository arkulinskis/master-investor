/* The main user journeys, run inside the real app (Anvil App Server) by tools/ui_test.py through tools/live/drive.mjs.
   Resolves to {ok, log}. Keep log lines ASCII (the Windows console). */
(async function () {
  const log = [], t0 = Date.now();
  const say = (m) => log.push(((Date.now() - t0) / 1000).toFixed(1) + 's ' + m);
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  async function until(fn, what, ms) {
    const end = Date.now() + (ms || 20000);
    while (Date.now() < end) { try { const v = fn(); if (v) return v; } catch (e) {} await sleep(150); }
    throw new Error('timed out waiting for: ' + what);
  }
  const $ = (s) => document.querySelector(s);
  const $$ = (s) => Array.from(document.querySelectorAll(s));
  const vis = (e) => !!e && e.getBoundingClientRect().width > 0;
  const txt = (e) => (e ? e.textContent.trim().replace(/\s+/g, ' ') : '');
  const byText = (sel, text) => $$(sel).find((e) => vis(e) && txt(e) === text);
  async function click(sel, text) {
    const el = await until(() => (text ? byText(sel, text) : $$(sel).find(vis)), sel + (text ? ' "' + text + '"' : ''));
    el.scrollIntoView({ block: 'center' });
    el.click();
    return el;
  }
  function type(input, value) {
    input.focus();
    input.value = value;
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
  }
  function key(k) { document.dispatchEvent(new KeyboardEvent('keydown', { key: k, bubbles: true, cancelable: true })); }
  async function page(hash, ready, what) {
    if (location.hash !== hash) window.UI_READY = false;  // the old page stays until the router runs
    location.hash = hash;
    await until(() => window.UI_READY && location.hash.split('/')[0] === hash.split('/')[0] && ready(), what || hash, 30000);
    await sleep(300);
  }
  const ok = (cond, msg) => { if (!cond) throw new Error('FAILED: ' + msg); say('ok   ' + msg); };
  const shown = (sel) => $$(sel).filter(vis);

  try {
    // ---- landing (visitors): the spreadsheet hero hides its answer until Reveal
    await page('#landing', () => $('.lp-hero') && shown('.lg-row').length > 5, 'landing');
    ok($('.lp-hero a[href="#auth/signup"]'), 'landing: hero with a sign-up link');
    ok(!shown('.anvil-role-sx-value').length, 'landing: the answer cell starts hidden');
    await click('.anvil-role-sx-reveal button');
    await until(() => shown('.anvil-role-sx-value').length, 'hero revealed');
    ok(/49\.95/.test(txt($('.anvil-role-sx-value'))) && vis($('.sx-note')), 'landing: Reveal shows 49.95 and the explanation');
    ok(shown('a.lg-row').length === 9, 'landing: the ledger lists 9 tracks');
    ok(shown('.lp-try .rv').length === 3, 'landing: three sample cards');
    const card0 = shown('.lp-try .rv')[0];
    ok(!vis(card0.querySelector('.rv-answer')), 'sample card: answer hidden');
    card0.querySelector('.anvil-role-rv-reveal button').click();
    await until(() => vis(card0.querySelector('.rv-answer')), 'sample revealed');
    card0.querySelector('.anvil-role-btn-primary button').click();
    await until(() => /Sign in to keep/.test(txt(card0)), 'guest grade note');
    ok(true, 'sample card: reveal, then Got it tells guests to sign in to keep a schedule');

    // ---- learn: tracks, level filter, search
    await page('#learn', () => shown('.tc-card').length === 9, 'learn');
    ok(true, 'learn: nine track cards');
    await click('.anvil-role-seg button', 'Pro');
    await until(() => shown('.tc-card').length >= 1 && shown('.tc-card').length < 9, 'filtered');
    ok(true, 'learn: the level filter narrows the tracks');
    await click('.anvil-role-seg button', 'All levels');
    type($('.ln-search input'), 'duration');
    await click('.ln-search .anvil-role-btn button');
    await until(() => shown('.lr-row').length >= 1 && /duration/.test(location.hash), 'search results');
    ok(shown('.lr-row').some((r) => /Bonds/.test(txt(r))), 'learn: searching "duration" finds the bonds lesson');
    await click('.anvil-role-btn button', 'Back to all tracks');
    await until(() => shown('.tc-card').length === 9, 'back to tracks');

    // ---- track page
    await page('#track/valuation', () => shown('.lr-row').length >= 5, 'valuation track');
    ok(/Valuing a company/.test(txt($('.anvil-role-page-title'))), 'track: title and lesson sheet');
    await click('.tk-actions .anvil-role-btn-primary button');
    await until(() => location.hash === '#lesson/price-vs-value' && window.UI_READY && $('.anvil-role-ls-title'), 'first lesson');
    ok(true, 'track: Start opens the first lesson');

    // ---- lesson: markdown body, example, terms, reveal all
    await page('#lesson/dcf', () => $('.anvil-role-ls-body') && shown('.page-lesson .rv').length >= 6, 'dcf lesson');
    ok($$('.anvil-role-ls-body h3').length >= 1 && $$('.anvil-role-ls-body p').length >= 3, 'lesson: the markdown body renders headings and paragraphs');
    ok(vis($('.ls-example')) && shown('.tm-row').length >= 3, 'lesson: worked example and key terms');
    ok(vis($('.ls-calc')) && /tools\/dcf/.test($('.ls-calc').getAttribute('href')), 'lesson: link to the DCF calculator');
    ok(!shown('.page-lesson .rv-answer').length, 'lesson: answers start hidden');
    await click('.anvil-role-btn button', 'Reveal all');
    await until(() => shown('.page-lesson .rv-answer').length === shown('.page-lesson .rv').length, 'all revealed');
    ok(vis($('.ls-guest')), 'lesson: Reveal all opens every card; guests see the sign-up note');
    ok(/discount/i.test(txt($('.tk-next'))), 'lesson: next-lesson link');

    // ---- glossary + library
    await page('#glossary', () => shown('.tm-row').length > 100, 'glossary');
    type($('.gl-search input'), 'duration');
    await until(() => shown('.tm-row').length >= 1 && shown('.tm-row').length < 20, 'filtered glossary');
    ok(/duration/i.test(txt(shown('.tm-row')[0])), 'glossary: filters as you type');
    await page('#library', () => shown('.li-item').length >= 20, 'library');
    await click('.anvil-role-seg button', 'GitHub repos');
    await until(() => shown('.li-item').some((i) => /yfinance/i.test(txt(i))), 'repos');
    ok(/github\.com/.test(shown('.li-open')[0].getAttribute('href')), 'library: GitHub repos tab with links');
    type($('.lb-search input'), 'backtest');
    await until(() => shown('.li-item').length >= 1 && shown('.li-item').length < 15, 'library search');
    ok(true, 'library: search narrows the list');

    // ---- calculators
    await page('#tools/dcf', () => shown('.sh-row').length > 5, 'dcf calculator');
    ok(shown('.anvil-role-sh-mark').some((c) => /49\.95/.test(txt(c))), 'calculator: DCF defaults give 49.95 a share (matches the hero)');
    const rate = shown('.cx-field input')[2];
    type(rate, '10');
    await until(() => !shown('.anvil-role-sh-mark').some((c) => /49\.95/.test(txt(c))), 'recalculated');
    ok(true, 'calculator: changing the discount rate recalculates');
    type(rate, '2');
    await until(() => vis($('.cx .anvil-role-msg-error')), 'error');
    ok(/discount rate must be higher/i.test(txt($('.cx .anvil-role-msg-error'))), 'calculator: impossible inputs explain the problem');
    for (const name of ['Compound growth', 'Bond price', 'Option payoff', 'Sharpe ratio', 'Position size', 'Kelly']) {
      await click('.tl-tabs button', name);
      await until(() => shown('.cx .sh-row').length >= 2, name);
    }
    ok(true, 'calculator: every calculator opens and shows results');
    await click('.tl-tabs button', 'Option payoff');
    await until(() => $('.lc svg path'), 'chart');
    ok(/options/.test(location.hash), 'calculator: option payoff draws its chart, address follows the tab');

    // ---- practice as a guest: keys Space / 2 / 1
    await page('#practice', () => shown('.pr-deck').length === 3, 'practice menu');
    ok(vis($('.pr-guest')), 'practice: guests are told nothing is saved');
    await click('.pr-buttons button', 'Placement check: where should I start?');
    await until(() => vis($('.anvil-role-pr-question')) && /placement/.test(location.hash), 'session');
    ok(/Card 1 of 12/.test(txt($('.anvil-role-pr-count'))), 'practice: placement deck has 12 cards');
    for (let i = 0; i < 12; i++) {
      key(' ');
      await until(() => vis($('.pr-answer')), 'revealed ' + i);
      key(i < 6 ? '2' : '1');
      await sleep(150);
    }
    for (let i = 0; i < 8 && !vis($('.pr-done')); i++) {  // second looks at the missed cards
      key(' '); await until(() => vis($('.pr-answer')), 'second look'); key('2'); await sleep(150);
    }
    await until(() => vis($('.pr-done')) && vis($('.pr-place')), 'placement result');
    ok(/6 \/ 12/.test(txt($('.anvil-role-pr-score'))) && /Advanced/.test(txt($('.pr-place'))), 'practice: keys work; all Beginner + Intermediate right places you at Advanced');
    ok(shown('.pr-missed .rv').length === 6, 'practice: the missed cards are listed with answers');

    // ---- members-only page sends visitors to sign in, then back
    await page('#profile', () => true);
    await until(() => window.UI_READY && $$('.au-card input').length >= 2, 'redirected to sign in');
    ok(true, 'a members-only page asks visitors to sign in');
    await click('.au-card .ui-seg button', 'Create account');
    await until(() => $$('.au-card input[type=password]').length && $$('.au-card input').filter((i) => i.offsetParent).length >= 3, 'sign-up form');
    const inputs = $$('.au-card input[type=text], .au-card input[type=email], .au-card input[type=password]').filter((i) => i.offsetParent);
    type(inputs[0], 'Flow Tester'); type(inputs[1], 'flow' + Date.now() + '@example.com'); type(inputs[2], 'Hb-' + Math.random().toString(36).slice(2) + '-Kq7');
    const tick = $('.au-card input[type=checkbox]');
    if (tick && !tick.checked) tick.click();
    await click('.anvil-role-btn-block button', 'Create account');
    await until(() => location.hash === '#profile' && window.UI_READY && $('.pf-grid'), 'back on the page they wanted', 40000);
    ok(true, 'sign-up: signed in and sent on to the page they asked for');

    // ---- a member finishes a lesson and grades a card
    await page('#lesson/compounding', () => vis($('.anvil-role-ls-title')) && shown('.page-lesson .rv').length, 'compounding');
    await click('.ls-finish .anvil-role-btn-primary button');
    await until(() => vis($('.ls-tags .anvil-role-badge-good')), 'done badge');
    ok(true, 'lesson: Mark as done shows the Done badge');
    await click('.ls-finish .anvil-role-btn button', 'Save for later');
    await until(() => byText('.ls-finish .anvil-role-btn button', 'Saved'), 'saved');
    const rv = shown('.page-lesson .rv')[0];
    rv.querySelector('.anvil-role-rv-reveal button').click();
    await until(() => vis(rv.querySelector('.rv-grade')), 'grade buttons');
    rv.querySelector('.anvil-role-btn-primary button').click();
    await until(() => /Saved/.test(txt(rv.querySelector('.anvil-role-rv-graded'))), 'graded saved');
    ok(true, 'lesson: a member grade is saved to the review schedule');

    // ---- today: due cards, tracks, saved
    await page('#home', () => vis($('.anvil-role-hm-big')) && shown('.tp-row').length === 9, 'home');
    ok(parseInt(txt($('.anvil-role-hm-big')), 10) > 0, 'today: cards from the finished lesson are waiting');
    ok(shown('.hm-saved .lr-row').some((r) => /Compounding/.test(txt(r))), 'today: the saved lesson is listed');
    ok(/1 day streak/.test(txt($('.anvil-role-hm-streak'))), 'today: a 1 day streak');
    await click('.hm-due .anvil-role-btn button');
    await until(() => /practice\/due/.test(location.hash) && vis($('.anvil-role-pr-question')), 'due session');
    await click('.pr-actions .anvil-role-btn button', 'Reveal answer');
    await click('.pr-grade .anvil-role-btn-primary button');
    await sleep(400);
    await click('.pr-top .anvil-role-btn button');
    await until(() => vis($('.pr-done')), 'ended');
    ok(/1 \/ 1/.test(txt($('.anvil-role-pr-score'))), 'practice: a member reviews due cards and ends the session');

    // ---- profile: name, theme, sign out
    await page('#profile', () => $('.pf-grid'), 'profile');
    type($('.pf-grid input'), 'Flow Tester Two');
    await click('.pf-grid .anvil-role-btn-primary button', 'Save');
    await until(() => /Flow Tester Two/.test($('.pf-head').textContent), 'name saved');
    ok(true, 'profile: name saved');
    await click('.anvil-role-avatar button');
    await click('.ui-menu .ui-seg button', 'Dark');
    ok(document.documentElement.classList.contains('ui-dark'), 'menu: Dark switches the theme');
    await click('.ui-menu .ui-seg button', 'Auto');
    await click('.ui-menu button', 'Sign out');
    await until(() => location.hash === '#landing' && window.UI_READY && $('.ui-header .ui-btn.primary'), 'signed out');
    ok(true, 'sign out: back to the landing page as a visitor');

    say('PASSED');
    return { ok: true, log: log };
  } catch (e) {
    say(String(e && e.message || e));
    return { ok: false, log: log };
  }
})();
