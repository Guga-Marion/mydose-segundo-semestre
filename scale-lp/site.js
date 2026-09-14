/* MyDose Scale — landing. O @ do hero leva para a máquina de onboarding (/comecar).
   O resto é apresentação: stepper do produto, exemplos por área, galeria e viewer. */
(() => {
'use strict';
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
document.documentElement.classList.add('js');

/* ---------- nav ---------- */
const nav = $('#nav');
const sticky = $('.sticky'), entry = $('#primeiro-passo');
const onScroll = () => { nav.classList.toggle('scrolled', scrollY > 30); sticky.classList.toggle('show', scrollY > entry.offsetTop + 200); };
addEventListener('scroll', onScroll, { passive: true }); onScroll();

/* ---------- @ do Instagram → onboarding ---------- */
const COMECAR = 'https://scale.mydoseapp.com/comecar?handle=';
function comecar(input, feedback) {
  const raw = (input.value || '').trim().replace(/^@/, '');
  if (!raw) { if (feedback) feedback.textContent = 'Coloque o seu @ do Instagram para começar.'; input.focus(); return; }
  if (!/^[a-zA-Z0-9_.]{1,30}$/.test(raw)) { if (feedback) feedback.textContent = 'Use só o seu @, com letras, números, ponto ou sublinhado. Não precisa do link.'; input.focus(); return; }
  if (feedback) feedback.textContent = '';
  location.assign(COMECAR + encodeURIComponent(raw));
}
const mainInput = $('#profile-input'), fb = $('#profile-feedback');
$('#primeiro-passo').addEventListener('submit', e => { e.preventDefault(); comecar(mainInput, fb); });
$('[data-entry-2]').addEventListener('submit', e => { e.preventDefault(); comecar($('#profile-input-2'), null); });
$$('[data-focus-entry]').forEach(a => a.addEventListener('click', e => {
  e.preventDefault();
  $('#inicio').scrollIntoView({ behavior: reduced ? 'auto' : 'smooth', block: 'start' });
  setTimeout(() => mainInput.focus({ preventScroll: true }), reduced ? 0 : 550);
}));

/* ---------- typewriter do H1 ---------- */
(() => {
  const el = $('#tw'); if (!el) return;
  const phrases = el.dataset.phrases.split('|');
  if (reduced) { $('#h1').classList.add('tw-static'); return; }
  // reserva a altura da frase mais longa: o H1 não muda de tamanho enquanto digita (zero layout shift)
  const h1 = $('#h1');
  const reserve = () => { const cur = el.textContent; let max = 0; phrases.forEach(f => { el.textContent = f; max = Math.max(max, h1.offsetHeight); }); el.textContent = cur; h1.style.minHeight = max + 'px'; };
  reserve(); addEventListener('resize', reserve, { passive: true });
  let i = 0, txt = phrases[0], del = false;
  const step = () => {
    const full = phrases[i];
    if (!del) { txt = full.slice(0, txt.length + 1); el.textContent = txt; if (txt === full) { del = true; return setTimeout(step, 2200); } return setTimeout(step, 46 + Math.random() * 40); }
    txt = full.slice(0, txt.length - 1); el.textContent = txt;
    if (!txt) { del = false; i = (i + 1) % phrases.length; return setTimeout(step, 320); }
    setTimeout(step, 26);
  };
  setTimeout(step, 2600);
})();

/* ---------- parallax da paisagem (hero) ---------- */
const land = $('.hero .land-svg');
if (land && !reduced) {
  const L = { far: $('#l-far', land), mid: $('#l-mid', land), lake: $('#l-lake', land), near: $('#l-near', land), fore: $('#l-fore', land) };
  const F = { far: .04, mid: .07, lake: .1, near: .14, fore: .2 };
  let tick = false;
  const par = () => { const y = Math.min(scrollY, 900); for (const k in L) if (L[k]) L[k].style.transform = `translateY(${-(y * F[k]).toFixed(1)}px)`; tick = false; };
  addEventListener('scroll', () => { if (!tick) { tick = true; requestAnimationFrame(par); } }, { passive: true }); par();
}

/* ---------- reveals ---------- */
if (!reduced && 'IntersectionObserver' in window) {
  const io = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } }), { rootMargin: '0px 0px -8% 0px' });
  $$('.rv').forEach(el => io.observe(el));
  // rede de segurança: nada fica escondido se o observer não disparar
  setTimeout(() => $$('.rv:not(.in)').forEach(el => el.classList.add('in')), 3000);
} else $$('.rv').forEach(el => el.classList.add('in'));

/* ---------- produto no laptop: sidebar + stepper ---------- */
const ICONES = {
  home: '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/>',
  painel: '<path d="M3 3v18h18"/><rect x="7" y="11" width="3" height="6" rx="1"/><rect x="12.5" y="7" width="3" height="10" rx="1"/><rect x="18" y="13" width="3" height="4" rx="1"/>',
  studio: '<rect x="2" y="5" width="14" height="14" rx="3"/><path d="M16 10l6-3v10l-6-3"/>',
  pieces: '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
  scripts: '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/>',
  products: '<rect x="3" y="7" width="18" height="13" rx="2.5"/><path d="M9 7V5.5A2.5 2.5 0 0 1 11.5 3h1A2.5 2.5 0 0 1 15 5.5V7"/><path d="M3 12.5h18"/>',
  paginas: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.4 3.8 5.4 3.8 9S14.5 18.6 12 21c-2.5-2.4-3.8-5.4-3.8-9S9.5 5.4 12 3z"/>',
  trafego: '<path d="M3 3v18h18"/><path d="M7 14l4-4 4 4 5-6"/>',
  whatsapp: '<path d="M21 11.5a8.5 8.5 0 0 1-12.4 7.5L3 21l2-5.6A8.5 8.5 0 1 1 21 11.5z"/><path d="M8.8 9.4c.4 2.7 3 5.3 5.8 5.8l1.6-1.6"/>',
  chat: '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
  calendar: '<rect x="3" y="4" width="18" height="17" rx="2.5"/><path d="M3 9.5h18M8 2v4M16 2v4"/>'
};
const NAV = [
  ['home', 'Início'], ['painel', 'Painel'], ['studio', 'Estúdio de vídeo', { badge: 1 }], ['pieces', 'Artes'], ['scripts', 'Roteiros', { badge: 2 }],
  ['products', 'Produtos'], ['paginas', 'Páginas'], ['calendar', 'Calendário', { tag: 'NOVO' }], ['whatsapp', 'WhatsApp', { badge: 1 }], ['chat', 'Chat do time']
];
const TIME = [['helena', 'Helena', 'Estrategista'], ['pedro', 'Pedro', 'Roteirista'], ['gabriel', 'Gabriel', 'Editor de vídeo'], ['estela', 'Estela', 'Social designer'], ['sofia', 'Sofia', 'Produtos & Oferta']];
const STEP_NAV = { 1: 'home', 2: 'home', 3: 'chat', 4: 'studio', 5: 'calendar' };
const STEP_TITLE = { 1: 'Início', 2: 'Perfil e marca', 3: 'Chat do time', 4: 'Estúdio de vídeo', 5: 'Calendário' };

function renderSide(active) {
  const side = $('#side');
  side.innerHTML = `
    <div class="lg"><img class="sym" src="assets/symbol.svg" alt=""><img src="assets/logo-preto.svg" alt=""><span>BETA</span></div>
    <div class="cli"><img src="assets/time/dra-ana.jpg" alt=""><div><b>Dra. Ana</b><small>nutrição materno-infantil · @dra.ana</small></div></div>
    ${NAV.map(([k, l, o = {}]) => `<div class="it${k === active ? ' on' : ''}"><svg viewBox="0 0 24 24">${ICONES[k]}</svg><span>${l}</span>${o.tag ? `<span class="tg">${o.tag}</span>` : ''}${o.badge ? `<span class="bd">${o.badge}</span>` : ''}</div>`).join('')}
    <div class="time"><h5>SEU TIME</h5>${TIME.map(([a, n, p]) => `<div class="ag"><img src="assets/time/${a}.webp" alt=""><div><b>${n}</b><small>${p}</small></div><i></i></div>`).join('')}</div>`;
}

const steps = $$('#steps .step');
const stepsBox = $('#steps');
let current = 1, timer = null, autoplay = !reduced;
const DUR = 7000;
function show(n, user) {
  current = n;
  steps.forEach(b => { const on = +b.dataset.step === n; b.setAttribute('aria-selected', String(on)); b.tabIndex = on ? 0 : -1; if (on) { const i = $('.bar i', b); i.style.animation = 'none'; void i.offsetWidth; i.style.animation = ''; } });
  $$('.view').forEach(v => v.classList.toggle('on', v.id === 'v-' + n));
  renderSide(STEP_NAV[n]);
  $('#top-title').textContent = STEP_TITLE[n];
  if (innerWidth <= 1080) { const b = steps[n - 1]; stepsBox.scrollTo({ left: b.offsetLeft - 16, behavior: reduced ? 'auto' : 'smooth' }); }
  if (user) { autoplay = false; stepsBox.classList.add('paused'); clearTimeout(timer); }
  if (autoplay) { clearTimeout(timer); timer = setTimeout(() => show(current % 5 + 1), DUR); }
}
steps.forEach(b => {
  b.addEventListener('click', () => show(+b.dataset.step, true));
  b.addEventListener('keydown', e => { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); const d = e.key === 'ArrowRight' ? 1 : -1; const n = ((current - 1 + d + 5) % 5) + 1; show(n, true); steps[n - 1].focus(); } });
});
document.documentElement.style.setProperty('--dur', DUR + 'ms');
renderSide('home');
// só roda o autoplay com o laptop visível
if (!reduced && 'IntersectionObserver' in window) {
  const vis = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting && autoplay && !timer) show(current); else if (!en.isIntersecting) { clearTimeout(timer); timer = null; } }), { threshold: .25 });
  vis.observe($('#laptop'));
} else { stepsBox.classList.add('paused'); }

// escala do app (desenhado em 1000×620) para a largura real da tela
const app = $('#app'), screen = $('.laptop .screen');
function fit() {
  const mobile = innerWidth <= 640;
  const s = mobile ? screen.clientWidth / 760 : screen.clientWidth / 1000;
  // no celular o app é ampliado e a sidebar sai de quadro: o conteúdo fica legível
  app.style.transform = mobile ? `translateX(${-208 * s}px) scale(${s})` : `scale(${s})`;
}
new ResizeObserver(fit).observe(screen); fit();

/* ---------- exemplos por área ---------- */
const CASES = {
  nutricao: { cover: 'manifesto-oliva', detail: 'editorial-sage', label: 'Nutrição', title: 'Uma conversa sobre alimentação. Uma presença que acolhe.', text: 'Um tema que aparece no atendimento, apresentado em uma sequência para a pessoa ler, salvar e levar para a próxima conversa.', purpose: 'Educar sem transformar o post em uma consulta.' },
  fisioterapia: { cover: 'frase-partida', detail: 'convite-jade', label: 'Fisioterapia', title: 'A boa orientação também começa pela escuta.', text: 'Uma mensagem de acolhimento abre a conversa sobre o cuidado. Explore o formato e adapte a mensagem ao seu contexto.', purpose: 'Aproximar sem prometer recuperação ou expor pacientes.' },
  psicologia: { cover: 'pergunta-indigo', detail: 'trocas-bosque', label: 'Psicologia', title: 'Às vezes, uma frase abre espaço para uma conversa.', text: 'Uma peça de acolhimento, com respiro e uma mensagem simples. Sua comunicação pode ser humana sem expor histórias de pacientes.', purpose: 'Acolher sem prometer resultados ou expor pacientes.' },
  consultorio: { cover: 'convite-jade', detail: 'glossario-pedra', label: 'Consultório', title: 'O cuidado pode começar antes do primeiro encontro.', text: 'Uma orientação visual para quem está chegando ao consultório. Dúvidas frequentes viram conteúdo útil, fácil de encontrar e compartilhar.', purpose: 'Orientar quem está chegando, sem promessas.' }
};
const NAMES = { 'editorial-sage': 'Editorial · sage', 'pergunta-indigo': 'Pergunta · índigo', 'dado-destaque': 'Dado em destaque', 'declaracao-vinho': 'Declaração · vinho', 'capa-serie': 'Capa de série', 'manifesto-oliva': 'Manifesto · oliva', 'frase-partida': 'Frase partida · coral', 'trocas-bosque': 'Trocas · bosque', 'convite-jade': 'Convite · jade', 'glossario-pedra': 'Glossário · pedra' };
const src = (k, i = 0) => `assets/carrossel-${k}-${i}.webp`;
$$('[data-case]').forEach(b => b.addEventListener('click', () => {
  const c = CASES[b.dataset.case];
  $$('[data-case]').forEach(x => { x.setAttribute('aria-selected', String(x === b)); x.tabIndex = x === b ? 0 : -1; });
  $('#case-panel').setAttribute('aria-labelledby', b.id);
  $('#case-cover').src = src(c.cover); $('#case-detail').src = c.detail === 'editorial-sage' ? src('editorial-sage', 1) : src(c.detail);
  $('#case-label').textContent = c.label; $('#case-title').textContent = c.title; $('#case-text').textContent = c.text; $('#case-purpose').textContent = c.purpose;
  $$('.ready-visual button')[0].dataset.template = c.cover; $$('.ready-visual button')[1].dataset.template = c.detail; $('#case-open').dataset.template = c.cover;
}));

/* ---------- viewer ---------- */
const modal = $('#viewer'), img = $('#result-image'), vid = $('#result-video');
let prevFocus = null;
function open() { prevFocus = document.activeElement; if (!modal.open) modal.showModal(); $('#close-viewer').focus(); }
function showTemplate(key, slide) {
  vid.hidden = true; vid.pause(); vid.removeAttribute('src');
  img.hidden = false; img.src = slide === 1 && key === 'editorial-sage' ? src(key, 1) : src(key); img.alt = NAMES[key] || key;
  $('#viewer-kind').textContent = 'Carrossel · 4:5'; $('#viewer-title').textContent = NAMES[key] || key;
  $('#source-note').textContent = 'Peça real do acervo de templates. Marca fictícia de demonstração; conteúdo sujeito a revisão profissional.';
  open();
}
function showVideo(kind) {
  img.hidden = true; vid.hidden = false;
  const film = kind === 'film';
  vid.src = film ? 'https://scale.mydoseapp.com/assets/filme.mp4' : 'assets/reel.mp4'; vid.poster = 'assets/reel-poster.jpg';
  $('#viewer-kind').textContent = film ? 'Filme de apresentação · 2 min' : 'Gabriel · exemplo do acervo';
  $('#viewer-title').textContent = film ? 'Conheça o MyDose Scale' : 'O vídeo editado';
  $('#source-note').textContent = film ? 'O produto inteiro, em uma sessão de uso.' : 'Vídeo editado já existente no acervo.';
  open(); vid.play().catch(() => {});
}
document.addEventListener('click', e => {
  const t = e.target.closest('[data-template],[data-video]'); if (!t) return;
  if (t.dataset.video) showVideo(t.dataset.video); else showTemplate(t.dataset.template, +(t.dataset.slide || 0));
});
$('#close-viewer').addEventListener('click', () => modal.close());
modal.addEventListener('click', e => { if (e.target === modal) modal.close(); });
modal.addEventListener('close', () => { vid.pause(); if (prevFocus && prevFocus.isConnected) prevFocus.focus({ preventScroll: true }); });
})();
