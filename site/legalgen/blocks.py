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
