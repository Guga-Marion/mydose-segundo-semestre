# -*- coding: utf-8 -*-
"""Gera as páginas legais do MyDose v3 em PT/EN/ES.
Uso: python3 build.py [privacidade|termos|...] [pt|en|es|all]"""
import sys, os, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shell import page, LEGAL_TITLES, fname

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  # site/

MODULES = {
  "privacidade":"content_privacidade",
  "termos":"content_termos",
  "cookies":"content_cookies",
  "lgpd":"content_lgpd",
  "central-de-ajuda":"content_ajuda",
  "contato":"content_contato",
}

def gen(pagekey, lang):
    mod = importlib.import_module(MODULES[pagekey])
    importlib.reload(mod)
    updated, blocks, toc = mod.content(lang)
    title = LEGAL_TITLES[pagekey][lang]
    html = page(pagekey, lang, title, updated, blocks, toc)
    path = os.path.join(OUT, fname(pagekey, lang))
    open(path, "w", encoding="utf-8").write(html)
    print("  ->", fname(pagekey, lang), "(%d KB)" % (len(html)//1024))

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv)>1 else "all"
    lang  = sys.argv[2] if len(sys.argv)>2 else "all"
    pages = list(MODULES) if which=="all" else [which]
    langs = ["pt","en","es"] if lang=="all" else [lang]
    for pg in pages:
        print(pg+":")
        for lg in langs:
            gen(pg, lg)
