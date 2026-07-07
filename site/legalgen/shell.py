# -*- coding: utf-8 -*-
"""Shell (CSS + nav + rodapé) das páginas legais/internas do MyDose v3.
Reutiliza os tokens e a identidade da nova-identidade-v3.html."""

CSS = r"""
:root{
  --blue:#415FF5; --magenta:#C64FCA; --orange:#F56442; --green:#63AC39;
  --navy:#191E47; --plum:#592C5A;
  --g1:linear-gradient(100deg,#415FF5 0%,#C64FCA 52%,#F56442 100%);
  --serif:"Fraunces",Georgia,serif;
  --sans:"Figtree",-apple-system,"Segoe UI",sans-serif;
  --logo:"Quicksand",var(--sans);
  --bg:#F6F4F2; --ink:#1E1D1D; --card:#FFFFFF; --muted:#565452; --gray:#848484;
  --line:rgba(30,29,29,.1); --line-strong:rgba(30,29,29,.22);
  --chip:#F6F4F2; --footer:#1E1D1D;
  --shadow:0 20px 60px -20px rgba(25,30,71,.25);
  --r:20px;
}
[data-theme="dark"]{
  --bg:#101226; --ink:#F6F4F2; --card:#1B1E3E; --muted:#B9BCD8; --gray:#8E92B4;
  --line:rgba(246,244,242,.11); --line-strong:rgba(246,244,242,.3);
  --chip:#252950; --footer:#0B0D1E;
  --shadow:0 20px 60px -20px rgba(0,0,0,.55);
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;overflow-x:clip}
body{font-family:var(--sans);color:var(--ink);background:var(--bg);font-size:16px;line-height:1.6;
  -webkit-font-smoothing:antialiased;transition:background .35s,color .35s}
a{color:inherit;text-decoration:none}
button{font-family:inherit;cursor:pointer;border:0;background:none;color:inherit}
::selection{background:var(--blue);color:#fff}
.wrap{max-width:1180px;margin:0 auto;padding:0 22px}
.grad{background:var(--g1);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}

/* nav */
nav{position:sticky;top:0;z-index:40;background:color-mix(in srgb,var(--bg) 86%,transparent);
  backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.nav-in{display:flex;align-items:center;justify-content:space-between;height:64px;gap:14px}
.wordmark{font-family:var(--logo);font-weight:700;font-size:23px;letter-spacing:-.02em;color:var(--ink)}
.wordmark span{background:var(--g1);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.nav-right{display:flex;align-items:center;gap:11px}
.lang-seg{display:inline-flex;align-items:center;gap:2px;background:var(--chip);border-radius:99px;padding:3px;box-shadow:inset 0 0 0 1.5px var(--line)}
.lang-seg a{padding:5px 9px;border-radius:99px;font-size:11.5px;font-weight:800;color:var(--gray);line-height:1;letter-spacing:.02em;transition:background .2s,color .2s}
.lang-seg a.on{background:var(--ink);color:var(--bg)}
.lang-seg a:hover:not(.on){color:var(--ink)}
.theme-btn{width:36px;height:36px;border-radius:50%;display:grid;place-items:center;font-size:15px;border:1px solid var(--line)}
.theme-btn:hover{border-color:var(--line-strong)}
.btn-back{font-size:13.5px;font-weight:700;padding:9px 15px;border-radius:99px;background:var(--ink);color:var(--bg);
  display:inline-flex;align-items:center;gap:7px;transition:transform .15s,opacity .2s}
.btn-back:hover{transform:translateY(-1px);opacity:.92}
@media(max-width:680px){.btn-back .bk-txt{display:none}.btn-back{width:36px;height:36px;padding:0;justify-content:center;border-radius:50%}}

/* doc header */
.doc-head{padding:54px 0 20px}
.doc-head .eyebrow{font-size:12px;font-weight:800;letter-spacing:.15em;text-transform:uppercase;color:var(--gray)}
.doc-head h1{font-family:var(--serif);font-weight:600;font-size:clamp(32px,5vw,52px);line-height:1.05;margin-top:14px;letter-spacing:-.02em;text-wrap:balance}
.doc-head .upd{margin-top:16px;font-size:13.5px;color:var(--muted);display:inline-flex;align-items:center;gap:8px;
  background:var(--card);border:1px solid var(--line);padding:7px 13px;border-radius:99px}
.doc-head .upd b{color:var(--ink);font-weight:700}

/* official-version note */
.langnote{margin:8px 0 0;max-width:760px;font-size:13.5px;color:var(--muted);background:var(--card);border:1px solid var(--line);
  border-left:3px solid var(--blue);border-radius:0 12px 12px 0;padding:12px 16px}

/* layout */
.doc-wrap{display:grid;gap:40px;padding:14px 0 40px}
@media(min-width:940px){.doc-wrap{grid-template-columns:230px 1fr}}
.toc{align-self:start}
@media(min-width:940px){.toc{position:sticky;top:88px}}
.toc h6{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--gray);margin-bottom:12px}
.toc ol{list-style:none;display:flex;flex-direction:column;gap:2px;counter-reset:t}
.toc a{display:block;font-size:13px;color:var(--muted);padding:6px 10px;border-radius:9px;border-left:2px solid transparent;line-height:1.35;transition:color .15s,background .15s,border-color .15s}
.toc a:hover{color:var(--ink);background:var(--card)}
.toc a.active{color:var(--ink);border-left-color:var(--blue);background:var(--card);font-weight:600}
@media(max-width:939px){.toc{display:none}}

.doc{max-width:760px;min-width:0}
.doc h2{font-family:var(--serif);font-weight:600;font-size:clamp(21px,2.7vw,27px);letter-spacing:-.01em;margin:42px 0 4px;
  scroll-margin-top:88px;line-height:1.2}
.doc h2:first-child{margin-top:0}
.doc h2 .cap{display:block;font-family:var(--sans);font-size:12px;font-weight:800;letter-spacing:.13em;text-transform:uppercase;color:var(--blue);margin-bottom:6px}
.doc h3{font-family:var(--serif);font-weight:600;font-size:18px;margin:26px 0 2px}
.doc p{margin:14px 0;color:var(--ink)}
.doc .lead{font-size:17.5px;color:var(--muted);line-height:1.7}
.doc ul,.doc ol{margin:12px 0 12px 4px;padding-left:22px;display:flex;flex-direction:column;gap:8px}
.doc li{padding-left:4px}
.doc strong,.doc b{font-weight:700}
.doc a.inl{color:var(--blue);font-weight:600;word-break:break-word}
.doc code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.86em;background:var(--chip);padding:2px 6px;border-radius:6px;
  border:1px solid var(--line);word-break:break-all}
.callout{margin:18px 0;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;box-shadow:var(--shadow)}
.callout.warn{border-left:3px solid var(--orange)}
.callout .cl-t{font-weight:800;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--orange);margin-bottom:7px}
.contact-card{margin:18px 0;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px 24px;box-shadow:var(--shadow);
  display:flex;flex-wrap:wrap;gap:10px 34px}
.contact-card div{min-width:150px}
.contact-card .k{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--gray)}
.contact-card .v{font-weight:650;margin-top:4px}
.contact-card a{color:var(--blue)}

/* footer (do v3) */
footer{background:var(--footer);color:#cfcac6;padding:60px 0 30px;font-size:14.5px;margin-top:20px}
.foot-grid{display:grid;gap:34px}
@media(min-width:860px){.foot-grid{grid-template-columns:1.4fr 1fr 1fr 1fr 1fr}}
footer .wordmark{color:#fff;font-size:26px}
footer .tagline{margin-top:13px;color:#9b9591;max-width:280px;font-size:13.5px}
footer h6{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#8a8480;margin-bottom:13px}
footer ul{list-style:none;display:flex;flex-direction:column;gap:9px}
footer a:hover{color:#fff}
.foot-social{display:flex;gap:9px;margin-top:15px}
.foot-social a{width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,.09);display:grid;place-items:center;color:#cfcac6;transition:background .2s,transform .2s,color .2s}
.foot-social a:hover{background:var(--blue);color:#fff;transform:translateY(-2px)}
.foot-bottom{display:flex;flex-wrap:wrap;gap:8px 20px;justify-content:space-between;margin-top:40px;padding-top:22px;
  border-top:1px solid rgba(255,255,255,.1);color:#8a8480;font-size:12.5px}
"""

# rótulos traduzíveis do nav e rodapé
UI = {
  "pt": {"back":"Voltar ao site","upd":"Última atualização","toc":"Nesta página",
         "official":"Esta é uma tradução de cortesia. A <b>versão em português</b> é a oficial e prevalece em caso de divergência.",
         "f_product":"Produto","f_who":"Para quem","f_company":"Empresa","f_legal":"Legal",
         "f_app":"O app","f_lab":"MyDose Lab","f_integr":"Integrações","f_plans":"Planos","f_live":"Aula ao vivo",
         "f_content":"Conteúdos & mídia","f_press":"MyDose na imprensa","f_channel":"Canal no YouTube",
         "tagline":"Seu operacional de IA para escalar na saúde. +Adesão · +Receita · −Tempo.","rights":"Take back control"},
  "en": {"back":"Back to site","upd":"Last updated","toc":"On this page",
         "official":"This is a courtesy translation. The <b>Portuguese version</b> is the official one and prevails in case of any discrepancy.",
         "f_product":"Product","f_who":"For whom","f_company":"Company","f_legal":"Legal",
         "f_app":"The app","f_lab":"MyDose Lab","f_integr":"Integrations","f_plans":"Plans","f_live":"Live class",
         "f_content":"Content & media","f_press":"MyDose in the press","f_channel":"YouTube channel",
         "tagline":"Your AI operating layer to scale in healthcare. +Adherence · +Revenue · −Time.","rights":"Take back control"},
  "es": {"back":"Volver al sitio","upd":"Última actualización","toc":"En esta página",
         "official":"Esta es una traducción de cortesía. La <b>versión en portugués</b> es la oficial y prevalece en caso de discrepancia.",
         "f_product":"Producto","f_who":"Para quién","f_company":"Empresa","f_legal":"Legal",
         "f_app":"La app","f_lab":"MyDose Lab","f_integr":"Integraciones","f_plans":"Planes","f_live":"Clase en vivo",
         "f_content":"Contenidos & medios","f_press":"MyDose en la prensa","f_channel":"Canal de YouTube",
         "tagline":"Tu capa operativa de IA para escalar en salud. +Adhesión · +Ingresos · −Tiempo.","rights":"Take back control"},
}

# páginas legais e seus nomes de arquivo por idioma (base pt = sem sufixo)
LEGAL_PAGES = ["privacidade","termos","cookies","lgpd","central-de-ajuda","contato"]
# só entram no rodapé as que já existem (evita link 404)
AVAILABLE = ["privacidade","termos"]
LEGAL_TITLES = {
  "privacidade":{"pt":"Política de Privacidade","en":"Privacy Policy","es":"Política de Privacidad"},
  "termos":{"pt":"Termos de Uso","en":"Terms of Use","es":"Términos de Uso"},
  "cookies":{"pt":"Política de Cookies","en":"Cookie Policy","es":"Política de Cookies"},
  "lgpd":{"pt":"LGPD","en":"LGPD (Data Protection)","es":"LGPD (Protección de Datos)"},
  "central-de-ajuda":{"pt":"Central de Ajuda","en":"Help Center","es":"Centro de Ayuda"},
  "contato":{"pt":"Contato","en":"Contact","es":"Contacto"},
}

def fname(page, lang):
    return page + (".html" if lang=="pt" else "-%s.html"%lang)

def home(lang):
    return "nova-identidade-v3.html" if lang=="pt" else "nova-identidade-v3-%s.html"%lang

def nav_html(page, lang):
    langs = ""
    for lg in ["pt","en","es"]:
        on = ' class="on" aria-current="true"' if lg==lang else ''
        href = "#" if lg==lang else fname(page, lg)
        langs += '<a%s href="%s">%s</a>' % (on, href, lg.upper())
    u = UI[lang]
    return ('<nav><div class="wrap nav-in">'
      '<a href="%s" class="wordmark" aria-label="MyDose">my<span>dose</span></a>'
      '<div class="nav-right">'
      '<div class="lang-seg" role="group" aria-label="Idioma / Language / Idioma">%s</div>'
      '<button class="theme-btn" id="themeBtn" aria-label="tema">🌙</button>'
      '<a class="btn-back" href="%s">‹ <span class="bk-txt">%s</span></a>'
      '</div></div></nav>') % (home(lang), langs, home(lang), u["back"])

def _legal_links(lang):
    items = ""
    for p in LEGAL_PAGES:
        if p not in AVAILABLE:
            continue
        items += '<li><a href="%s">%s</a></li>' % (fname(p, lang), LEGAL_TITLES[p][lang])
    return items

def footer_html(lang):
    u = UI[lang]
    social = ('<div class="foot-social" aria-label="Social">'
      '<a href="https://www.youtube.com/@mydoseapp" target="_blank" rel="noopener" aria-label="YouTube"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.5 12 4.5 12 4.5s-7 0-8.9.6A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.8a3 3 0 0 0 2.1 2.1c1.9.6 8.9.6 8.9.6s7 0 8.9-.6a3 3 0 0 0 2.1-2.1A31 31 0 0 0 23.5 12 31 31 0 0 0 23 7.2ZM9.7 15.3V8.7L15.8 12l-6.1 3.3Z"/></svg></a>'
      '<a href="https://www.instagram.com/mydoseapp" target="_blank" rel="noopener" aria-label="Instagram"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.8.1 1.2.1 1.9.2 2.3.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1.1.4 2.3.1 1.3.1 1.6.1 4.8s0 3.6-.1 4.8c-.1 1.2-.2 1.9-.4 2.3a3.8 3.8 0 0 1-.9 1.4c-.4.4-.8.7-1.4.9-.4.2-1.1.4-2.3.4-1.3.1-1.6.1-4.8.1s-3.6 0-4.8-.1c-1.2-.1-1.9-.2-2.3-.4a3.8 3.8 0 0 1-1.4-.9 3.8 3.8 0 0 1-.9-1.4c-.2-.4-.4-1.1-.4-2.3-.1-1.3-.1-1.6-.1-4.8s0-3.6.1-4.8c.1-1.2.2-1.9.4-2.3.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1.1-.4 2.3-.4 1.3-.1 1.6-.1 4.8-.1Zm0 3.4a4.4 4.4 0 1 1 0 8.8 4.4 4.4 0 0 1 0-8.8Zm0 7.2a2.9 2.9 0 1 0 0-5.7 2.9 2.9 0 0 0 0 5.7Zm5.6-7.4a1 1 0 1 1-2.1 0 1 1 0 0 1 2.1 0Z"/></svg></a>'
      '<a href="https://www.linkedin.com/company/mydoseapp" target="_blank" rel="noopener" aria-label="LinkedIn"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M20.4 20.4h-3.5v-5.6c0-1.3 0-3-1.9-3s-2.1 1.4-2.1 2.9v5.7H9.4V9h3.4v1.6h.1c.5-.9 1.6-1.9 3.4-1.9 3.6 0 4.2 2.4 4.2 5.4v6.3ZM5.3 7.4a2 2 0 1 1 0-4.1 2 2 0 0 1 0 4.1Zm1.8 13H3.6V9h3.5v11.4Z"/></svg></a></div>')
    prod = ('<div><h6>%s</h6><ul>'
      '<li><a href="%s#produto">%s</a></li><li><a href="%s#lab">%s</a></li>'
      '<li><a href="%s#integracoes">%s</a></li><li><a href="%s#planos">%s</a></li>'
      '<li><a href="live.html">%s</a></li></ul></div>') % (u["f_product"],
        home(lang),u["f_app"],home(lang),u["f_lab"],home(lang),u["f_integr"],home(lang),u["f_plans"],u["f_live"])
    who = ('<div><h6>%s</h6><ul>'
      '<li><a href="nova-physical-v3%s.html">Physical</a></li>'
      '<li><a href="nova-mental-v3%s.html">Mental</a></li>'
      '<li><a href="nova-clinics-v3%s.html">Clinics</a></li></ul></div>') % (
        u["f_who"], "" if lang=="pt" else "-"+lang, "" if lang=="pt" else "-"+lang, "" if lang=="pt" else "-"+lang)
    comp = ('<div><h6>%s</h6><ul>'
      '<li><a href="blog.html">%s</a></li><li><a href="blog.html#imprensa">%s</a></li>'
      '<li><a href="https://www.youtube.com/@mydoseapp" target="_blank" rel="noopener">%s</a></li></ul></div>') % (
        u["f_company"], u["f_content"], u["f_press"], u["f_channel"])
    legal = '<div><h6>%s</h6><ul>%s</ul></div>' % (u["f_legal"], _legal_links(lang))
    return ('<footer><div class="wrap"><div class="foot-grid">'
      '<div><span class="wordmark">my<span>dose</span></span>'
      '<p class="tagline">%s</p>%s</div>'
      '%s%s%s%s'
      '</div><div class="foot-bottom"><span>© MyDose · %s</span>'
      '<span>feito com ética e ciência.</span></div></div></footer>') % (
        u["tagline"], social, prod, who, comp, legal, u["rights"])

THEME_JS = r"""
<script>
(function(){
  var r=document.documentElement,b=document.getElementById('themeBtn');
  var sv=null;try{sv=localStorage.getItem('md-theme')}catch(e){}
  if(sv)r.setAttribute('data-theme',sv);
  else if(window.matchMedia&&matchMedia('(prefers-color-scheme:dark)').matches)r.setAttribute('data-theme','dark');
  function pin(){b.textContent=r.getAttribute('data-theme')==='dark'?'☀️':'🌙'}pin();
  b.addEventListener('click',function(){var d=r.getAttribute('data-theme')==='dark'?'light':'dark';
    r.setAttribute('data-theme',d);try{localStorage.setItem('md-theme',d)}catch(e){}pin()});
  // TOC scroll-spy
  var links=[].slice.call(document.querySelectorAll('.toc a'));
  var secs=links.map(function(a){return document.getElementById(a.getAttribute('href').slice(1))}).filter(Boolean);
  if('IntersectionObserver' in window && secs.length){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){
      if(e.isIntersecting){var id=e.target.id;links.forEach(function(a){a.classList.toggle('active',a.getAttribute('href')==='#'+id)})}})},
      {rootMargin:'-15% 0px -70% 0px'});
    secs.forEach(function(s){io.observe(s)});
  }
})();
</script>
"""

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
  "%3Cpath d='M50 2C56 32 68 44 98 50 68 56 56 68 50 98 44 68 32 56 2 50 32 44 44 32 50 2Z' fill='%23415FF5'/%3E%3C/svg%3E")

def page(pagekey, lang, title, updated, blocks, toc):
    """Monta o HTML completo de uma página legal."""
    u = UI[lang]
    lang_attr = {"pt":"pt-BR","en":"en","es":"es-419"}[lang]
    toc_html = ""
    if toc:
        lis = "".join('<li><a href="#%s">%s</a></li>' % (tid, tlabel) for tid,tlabel in toc)
        toc_html = '<nav class="toc" aria-label="%s"><h6>%s</h6><ol>%s</ol></nav>' % (u["toc"], u["toc"], lis)
    langnote = "" if lang=="pt" else '<p class="langnote">%s</p>' % u["official"]
    updrow = ('<div class="upd">%s: <b>%s</b></div>' % (u["upd"], updated)) if updated else ""
    return """<!DOCTYPE html>
<html lang="%(la)s">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%(title)s · MyDose</title>
<meta name="description" content="%(title)s do MyDose.">
<meta name="robots" content="noindex">
<link rel="icon" href="%(fav)s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..600;1,9..144,400..600&family=Figtree:wght@400;500;600;700;800&family=Quicksand:wght@600;700&display=swap" rel="stylesheet">
<style>%(css)s</style>
</head>
<body>
%(nav)s
<div class="wrap doc-head">
  <p class="eyebrow">%(title)s</p>
  <h1>%(title)s</h1>
  %(updrow)s
  %(langnote)s
</div>
<div class="wrap doc-wrap">
  %(toc)s
  <article class="doc">
%(blocks)s
  </article>
</div>
%(footer)s
%(js)s
</body>
</html>
""" % {"la":lang_attr,"title":title,"fav":FAVICON,"css":CSS,"nav":nav_html(pagekey,lang),
       "updrow":updrow,"langnote":langnote,"toc":toc_html,"blocks":blocks,
       "footer":footer_html(lang),"js":THEME_JS}
