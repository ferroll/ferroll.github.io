#!/usr/bin/env python3
"""Builds the localized site from tools/strings/<lang>.py.

    python3 tools/build.py

English pages are written to the repo root (index.html, support.html,
privacy.html); every other language goes to its own folder (/tr/, /de/, ...).
The root URLs never move: App Store Connect, Play Console and app-ads.txt
depend on them. Edit the strings, run this script, commit the output.
"""
import importlib.util, json, os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = 'https://ferroll.github.io'
CSS_VERSION = '1.5.3'
IG_URL = 'https://www.instagram.com/dev.yagiz/'
APP_STORE = 'https://apps.apple.com/app/id6759351512'
PLAY = 'https://play.google.com/store/apps/details?id=com.yagiz.Ferroll'

# (strings file / folder, <html lang>, name in its own language)
LANGS = [
    ('en', 'en', 'English'), ('tr', 'tr', 'Türkçe'), ('de', 'de', 'Deutsch'), ('es', 'es', 'Español'),
    ('fr', 'fr', 'Français'), ('it', 'it', 'Italiano'), ('pt-br', 'pt-BR', 'Português (Brasil)'),
    ('ru', 'ru', 'Русский'), ('ja', 'ja', '日本語'), ('ko', 'ko', '한국어'), ('zh-hans', 'zh-Hans', '简体中文'),
    ('zh-hant', 'zh-Hant', '繁體中文'), ('hi', 'hi', 'हिन्दी'), ('id', 'id', 'Bahasa Indonesia'), ('vi', 'vi', 'Tiếng Việt'),
]
PAGES = ['index.html', 'support.html', 'privacy.html']


def load(code):
    path = os.path.join(ROOT, 'tools', 'strings', code.replace('-', '_') + '.py')
    spec = importlib.util.spec_from_file_location('s_' + code.replace('-', '_'), path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod.S


def url_for(code, page):
    """Root-relative URL of a page in a language ('/' and '/tr/' for the landing pages)."""
    base = '/' if code == 'en' else f'/{code}/'
    return base if page == 'index.html' else base + page


def fill(text, code):
    return (text.replace('{IG}', f'<a href="{IG_URL}">@dev.yagiz</a>')
                .replace('{SUPPORT}', 'support.html')
                .replace('{IOS}', '<span class="tag">iOS</span>')
                .replace('{AND}', '<span class="tag">Android</span>'))


def head(code, lang_attr, page, title, meta, og=None, extra=''):
    p = '' if code == 'en' else '../'
    alts = '\n'.join(f'<link rel="alternate" hreflang="{la}" href="{SITE}{url_for(c, page)}">' for c, la, _ in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{SITE}{url_for("en", page)}">'
    og_tags = ''
    if og:
        og_tags = f'''
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(og)}">
<meta property="og:image" content="{SITE}/assets/screens/01-tilt-roll-escape.jpg">
<meta property="og:type" content="website">'''
    return f'''<!DOCTYPE html>
<html lang="{lang_attr}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(meta)}">
<link rel="canonical" href="{SITE}{url_for(code, page)}">
{alts}
<link rel="icon" href="{p}assets/icon.png">
<link rel="apple-touch-icon" href="{p}assets/icon.png">
<link rel="stylesheet" href="{p}assets/style.css?v={CSS_VERSION}">{og_tags}{extra}
</head>
<body>
'''


def nav(code, page, S, brand_link=True):
    p = '' if code == 'en' else '../'
    c = S['common']
    opts = '\n'.join(
        f'        <option value="{url_for(lc, page)}" data-lang="{lc}"{" selected" if lc == code else ""}>{name}</option>'
        for lc, _, name in LANGS)
    brand = (f'<a class="brand" href="{url_for(code, "index.html")}" style="text-decoration:none"><img src="{p}assets/icon.png" alt="">Ferroll</a>'
             if brand_link else f'<span class="brand"><img src="{p}assets/icon.png" alt="">Ferroll</span>')
    return f'''<nav class="nav">
  <div class="wrap">
    {brand}
    <a href="support.html">{c["nav_support"]}</a>
    <a href="privacy.html">{c["nav_privacy"]}</a>
    <label class="langsel"><span class="sr-only">{c["language"]}</span>
      <select id="lang-select" aria-label="{c["language"]}">
{opts}
      </select>
    </label>
  </div>
</nav>
'''


def footer(code, page, S):
    c = S['common']
    current = ' aria-current="page"'
    langs = ' '.join(
        f'<a href="{url_for(lc, page)}" hreflang="{la}" lang="{la}" data-lang="{lc}"{current if lc == code else ""}>{name}</a>'
        for lc, la, name in LANGS)
    return f'''
<footer>
  <div class="wrap">
    <a href="{url_for(code, "index.html")}">{c["footer_home"]}</a>
    <a href="support.html">{c["footer_support"]}</a>
    <a href="privacy.html">{c["footer_privacy"]}</a>
    <p class="langs">{langs}</p>
    <p style="margin-top:14px">© 2026 Mustafa Yağız. {c["rights"]}</p>
  </div>
</footer>

<script>
// Remember an explicit language choice so the landing page doesn't redirect it away.
(function () {{
  function remember(l) {{ try {{ localStorage.setItem('ferroll.lang', l); }} catch (e) {{}} }}
  var sel = document.getElementById('lang-select');
  if (sel) sel.addEventListener('change', function () {{
    remember(sel.options[sel.selectedIndex].getAttribute('data-lang'));
    location.href = sel.value;
  }});
  document.querySelectorAll('footer .langs a').forEach(function (a) {{
    a.addEventListener('click', function () {{ remember(a.getAttribute('data-lang')); }});
  }});
}})();
</script>

</body>
</html>
'''


REDIRECT = '''
<script>
// First visit to the English landing page: send visitors to their browser's language.
// An explicit choice (stored by the language menu) always wins.
(function () {
  var map = %s;
  try { var saved = localStorage.getItem('ferroll.lang'); if (saved) { if (saved !== 'en' && map[saved]) location.replace(map[saved]); return; } } catch (e) {}
  if (document.referrer && document.referrer.indexOf(location.host) !== -1) return;
  var prefs = navigator.languages || [navigator.language || 'en'];
  for (var i = 0; i < prefs.length; i++) {
    var l = String(prefs[i]).toLowerCase(), code = null;
    if (l.indexOf('zh') === 0) code = /(tw|hk|mo|hant)/.test(l) ? 'zh-hant' : 'zh-hans';
    else if (l.indexOf('pt') === 0) code = 'pt-br';
    else code = l.split('-')[0];
    if (code === 'en') return;
    if (map[code]) { location.replace(map[code]); return; }
  }
})();
</script>'''


def build_index(code, la, S):
    I = S['index']; p = '' if code == 'en' else '../'
    extra = REDIRECT % json.dumps({lc: url_for(lc, 'index.html') for lc, _, _ in LANGS}) if code == 'en' else ''
    out = head(code, la, 'index.html', I['title'], I['meta'], og=I['og'], extra=extra)
    out += nav(code, 'index.html', S, brand_link=False)
    shots = ['01-tilt-roll-escape', '02-dodge-ghosts', '03-collect-gems', '05-endless-mode']
    shots_html = '\n'.join(f'      <img src="{p}assets/screens/{n}.jpg" alt="{html.escape(a)}" loading="lazy" width="1280" height="720">'
                           for n, a in zip(shots, I['shots']))
    cards = '\n'.join(f'''      <div class="card">
        <span class="emoji">{e}</span>
        <strong>{t}</strong>
        <p>{d}</p>
      </div>''' for e, t, d in I['features'])
    ci, ca = I['req_cols']
    rows = '\n'.join(
        f'        <tr><th>{k}</th><td>{a}</td><td>{b}</td></tr>' if b is not None else f'        <tr><th>{k}</th><td colspan="2">{a}</td></tr>'
        for k, a, b in I['req_rows'])
    about = '\n'.join(f'    <p>\n      {fill(t, code)}\n    </p>' for t in I['about'])
    out += f'''
<div class="wrap">

  <header class="hero">
    <h1 class="logo-title"><img class="logo" src="{p}assets/logo-wordmark.png" alt="Ferroll" width="467" height="252"></h1>
    <p class="tagline">{I["tagline"]}</p>
    <div class="stores">
      <a class="store" href="{APP_STORE}">
        <img src="{p}assets/badges/app-store.svg" alt="{html.escape(I["badge_ios"])}" width="120" height="40">
      </a>
      <a class="store" href="{PLAY}">
        <img src="{p}assets/badges/google-play.png" alt="{html.escape(I["badge_android"])}" width="564" height="168">
      </a>
    </div>
    <p class="platforms">{I["platforms"]}</p>
  </header>

  <section>
    <h2>{I["about_h"]}</h2>
{about}

    <div class="shots">
{shots_html}
    </div>

    <div class="features">
{cards}
    </div>
  </section>

  <section>
    <h2>{I["req_h"]}</h2>
    <div class="table-scroll">
      <table>
        <tr><th></th><th>{ci}</th><th>{ca}</th></tr>
{rows}
      </table>
    </div>
  </section>

  <section>
    <h2>{I["help_h"]}</h2>
    <p>
      {fill(I["help"], code)}
    </p>
    <p style="margin-top:22px">
      <a class="btn ghost" href="support.html">{I["help_btn"]}</a>
    </p>
  </section>

</div>
'''
    return out + footer(code, 'index.html', S)


def build_support(code, la, S):
    U = S['support']
    out = head(code, la, 'support.html', U['title'], U['meta']) + nav(code, 'support.html', S)
    secs = ''
    for h, items in U['sections']:
        det = ''
        for q, paras in items:
            body = '\n'.join(f'        <p>\n          {fill(t, code)}\n        </p>' for t in paras)
            det += f'''
      <details>
        <summary>{q}</summary>
{body}
      </details>
'''
        secs += f'''
  <section>
    <h2>{h}</h2>

    <div class="faq">{det}    </div>
  </section>
'''
    out += f'''
<div class="wrap">

  <section>
    <h2>{U["h"]}</h2>
    <p>
      {fill(U["intro"], code)}
    </p>

    <div class="callout">
      <p>{fill(U["contact"], code)}</p>
      <p>
        {fill(U["contact_note"], code)}
      </p>
    </div>
  </section>
{secs}
  <section>
    <h2>{U["stuck_h"]}</h2>
    <p>
      {fill(U["stuck"], code)}
    </p>
  </section>

</div>
'''
    return out + footer(code, 'support.html', S)


def build_privacy(code, la, S):
    V = S['privacy']
    out = head(code, la, 'privacy.html', V['title'], V['meta']) + nav(code, 'privacy.html', S)
    note = ''
    if V.get('translation_note'):
        note = f'\n    <p class="updated">{fill(V["translation_note"], code).replace("{EN}", url_for("en", "privacy.html"))}</p>'
    secs = ''
    for h, blocks in V['sections']:
        body = ''
        for kind, val in blocks:
            if kind == 'p':
                body += f'    <p>\n      {fill(val, code)}\n    </p>\n'
            elif kind == 'h3':
                body += f'\n    <h3>{val}</h3>\n'
            elif kind == 'ul':
                body += '    <ul>\n' + ''.join(f'      <li>{fill(x, code)}</li>\n' for x in val) + '    </ul>\n'
            elif kind == 'table':
                rows = [f'        <tr><th>{val[0][0]}</th><th>{val[0][1]}</th></tr>'] + \
                       [f'        <tr><td>{a}</td><td>{b}</td></tr>' for a, b in val[1:]]
                body += '    <div class="table-scroll">\n      <table>\n' + '\n'.join(rows) + '\n      </table>\n    </div>\n'
        secs += f'''
  <section>
    <h2>{h}</h2>
{body}  </section>
'''
    out += f'''
<div class="wrap">

  <section>
    <h2>{V["h"]}</h2>
    <p class="updated">{V["updated"]}</p>{note}

    <p>
      {fill(V["intro"], code)}
    </p>

    <div class="callout">
      <p>
        {fill(V["short"], code)}
      </p>
    </div>
  </section>
{secs}
</div>
'''
    return out + footer(code, 'privacy.html', S)


def main():
    for code, la, _ in LANGS:
        S = load(code)
        folder = ROOT if code == 'en' else os.path.join(ROOT, code)
        os.makedirs(folder, exist_ok=True)
        for page, fn in (('index.html', build_index), ('support.html', build_support), ('privacy.html', build_privacy)):
            open(os.path.join(folder, page), 'w').write(fn(code, la, S))
        print('built', code)


if __name__ == '__main__':
    main()
