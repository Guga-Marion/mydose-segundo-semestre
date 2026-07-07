# -*- coding: utf-8 -*-
"""Helpers para montar blocos de conteúdo das páginas legais."""

def h2(text, tid, cap=None):
    c = '<span class="cap">%s</span>' % cap if cap else ''
    return '    <h2 id="%s">%s%s</h2>\n' % (tid, c, text)

def h3(text):
    return '    <h3>%s</h3>\n' % text

def p(html, lead=False):
    cls = ' class="lead"' if lead else ''
    return '    <p%s>%s</p>\n' % (cls, html)

def ul(items):
    return '    <ul>%s</ul>\n' % ''.join('<li>%s</li>' % i for i in items)

def ol(items):
    return '    <ol>%s</ol>\n' % ''.join('<li>%s</li>' % i for i in items)

def callout(title, html, warn=True):
    cls = 'callout warn' if warn else 'callout'
    return '    <div class="%s"><div class="cl-t">%s</div>%s</div>\n' % (cls, title, html)

def contact(rows):
    # rows: list of (k, v_html)
    inner = ''.join('<div><div class="k">%s</div><div class="v">%s</div></div>' % (k, v) for k, v in rows)
    return '    <div class="contact-card">%s</div>\n' % inner

def raw(html):
    return '    %s\n' % html

def faq(items, empty_msg=""):
    inner = ''.join('<details class="faq"><summary>%s <span class="plus">+</span></summary><p class="a">%s</p></details>' % (q, a) for q, a in items)
    em = '<p class="faq-empty">%s</p>' % empty_msg if empty_msg else ''
    return '    <div class="faq-list">%s%s</div>\n' % (inner, em)
