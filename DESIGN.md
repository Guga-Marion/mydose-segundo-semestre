# Design — MyDose Identidade 2026 (oficial)

## Theme
Claro por padrão (#F6F4F2 quente-neutro), dark mode completo via tokens `[data-theme]`. Seções-poster em cores profundas (drench) alternam com respiros claros.

## Color
- Primárias: azul #415FF5 · magenta #C64FCA · laranja #F56442 · verde #63AC39
- Profundas (posters/drench): navy #191E47 · ameixa #592C5A · ferrugem #5E1F10 · floresta #223F11
- Pastéis: #8699FD/#D6DDFF · #F0B0F2/#F5E3F6 · #FF9F88/#FFEAE5 · #A5DC85/#DCEDD2
- Neutras: bg #F6F4F2 · ink #1E1D1D · cinza #848484
- Gradiente 1 (geral): azul→magenta→laranja · Gradiente 2: azul→violeta→rosa
- Grafismos filled: só cores primárias/secundárias/gradiente, NUNCA neutras. Neutras só em grafismos outlined.

## Typography
- Títulos grandes: **Americana BT** (400/700/800 + itálico 400) — self-hosted woff2 em site/assets/fonts/
- Texto e títulos menores: **Google Sans** (400/500/600/700 + itálico) — subset latin
- Palavras-ênfase em títulos: itálico Americana (cor sólida ou grad-text já estabelecido do sistema)

## Logo
Lockups oficiais em site/assets/brand/ (preto/branco/gradient-preto/gradient-branco). Nav 24px de altura; claro usa gradient-preto, escuro gradient-branco. Símbolo isolado = `<use href="#mk">` (recorte 0 0 290 290); branco = `#mk-w`.

## Grafismos (Assets-identidade — fonte da verdade)
Symbols inline: gf-spark (Sharp Star) · gf-dose (Cushion) · gf-petal (Pinwheel) · gf-arcs (Arc Segments) · gf-circles (Overlapping Circles) · gf-concave (Concave Star) · gf-diamond (Diamond Petals) · gf-tri (redesenhado — o arquivo original tem PNG de 2MB embutido!) · gf-mandala-o (Octagon Mandala outlined, para decor neutro). Pattern de fundo: pattern-base-form recolorido (tile 64px, classe .pattern). Máx. 1 grafismo complexo por composição.

## Components
Botões pill (18px/30px padding, azul primário; grad em destaque), cards 22-24px radius com inset line, chips pastel, marquee gradiente, eyebrow = grafismo + texto (sistema nomeado da marca), ícones = classe .gi com <use> colorido.

## Motion
Reveals .rv/.in em cascata, parallax data-par, twinkles, contadores, vídeo data-motion (play só visível), tilt no hero, tudo com prefers-reduced-motion. Ease-out expo. Novidades v6: mosaico do hero com stagger de entrada, mandala girando devagar no scroll.

## Layout
.wrap = min(1180px, 100% - 40px). Seções 88/130px de padding vertical. Grid 2D só quando necessário; mobile-first, zero overflow a 390px.
