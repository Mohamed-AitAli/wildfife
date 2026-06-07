#!/usr/bin/env python3
"""Apply unified nav, footer, and compliance updates to all static HTML pages."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://vanlife.website"

SKIP_DIRS = {"wordpress", "scripts", "mnt", ".git", "node_modules"}


def root_prefix(rel: Path) -> str:
    depth = len(rel.parent.parts)
    return "../" * depth if depth else ""


def page_section(rel: Path) -> str:
    parts = rel.parts
    if rel.name == "index.html" and len(parts) == 1:
        return "home"
    if parts[0] == "guides":
        return "guides"
    if parts[0] == "builds":
        return "builds"
    if parts[0] == "blog":
        return "blog"
    stem = rel.stem
    if stem in {"about", "contact", "compare", "privacy-policy"}:
        return stem
    if stem == "blog":
        return "blog"
    return "other"


def active(section: str, target: str) -> str:
    return ' class="active"' if section == target else ""


def build_nav(rel: Path) -> str:
    r = root_prefix(rel)
    section = page_section(rel)
    return f"""    <nav id="nav">
        <div class="container nav-inner">
            <a href="{r}index.html" class="logo">VAN<span>LIFE</span></a>
            <ul class="nav-links">
                <li><a href="{r}guides/index.html"{active(section, "guides")}>Guides</a></li>
                <li><a href="{r}builds/index.html"{active(section, "builds")}>Builds</a></li>
                <li><a href="{r}blog/index.html"{active(section, "blog")}>Blog</a></li>
                <li><a href="{r}about.html"{active(section, "about")}>About</a></li>
                <li><a href="{r}contact.html"{active(section, "contact")}>Contact</a></li>
            </ul>
            <a href="{r}guides/solar.html" class="btn btn-primary nav-cta btn-sm">Start Building →</a>
            <button class="hamburger" id="hamburger" aria-label="Menu" type="button">
                <span></span><span></span><span></span>
            </button>
        </div>
    </nav>

    <div class="mobile-menu" id="mobileMenu">
        <a href="{r}guides/index.html" class="mobile-link">GUIDES</a>
        <a href="{r}builds/index.html" class="mobile-link">BUILDS</a>
        <a href="{r}blog/index.html" class="mobile-link">BLOG</a>
        <a href="{r}about.html" class="mobile-link">ABOUT</a>
        <a href="{r}contact.html" class="mobile-link">CONTACT</a>
        <a href="{r}guides/solar.html" class="btn btn-primary">Start Building →</a>
    </div>"""


def build_footer(rel: Path) -> str:
    r = root_prefix(rel)
    return f"""    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="{r}index.html" class="logo">VAN<span>LIFE</span></a>
                    <p>Independent van, skoolie, and camper conversion guides. No sponsored content — just practical advice from real builds.</p>
                </div>
                <div class="footer-col">
                    <h4>Guides</h4>
                    <ul>
                        <li><a href="{r}guides/solar.html">Solar Power</a></li>
                        <li><a href="{r}guides/insulation.html">Insulation</a></li>
                        <li><a href="{r}guides/budget.html">Budget Planning</a></li>
                        <li><a href="{r}guides/battery.html">Batteries</a></li>
                        <li><a href="{r}guides/skoolie.html">Skoolie</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Explore</h4>
                    <ul>
                        <li><a href="{r}builds/index.html">Community Builds</a></li>
                        <li><a href="{r}blog/index.html">Blog</a></li>
                        <li><a href="{r}compare.html">Van vs Skoolie</a></li>
                        <li><a href="{r}about.html">About</a></li>
                        <li><a href="{r}contact.html">Contact</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Legal</h4>
                    <ul>
                        <li><a href="{r}privacy-policy.html">Privacy Policy</a></li>
                        <li><a href="{r}ads.txt">Ads.txt</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom">
                <span>© 2026 VanLife · vanlife.website</span>
            </div>
        </div>
    </footer>"""


COOKIE_BANNER = """
    <div id="cookie-banner" class="cookie-banner" hidden>
        <div class="container cookie-inner">
            <p>We use cookies for analytics and ads (Google Analytics & AdSense). See our <a href="{privacy}">Privacy Policy</a>.</p>
            <div class="cookie-actions">
                <button type="button" class="btn btn-outline btn-sm" data-consent="essential">Essential only</button>
                <button type="button" class="btn btn-primary btn-sm" data-consent="all">Accept</button>
            </div>
        </div>
    </div>"""


def canonical_url(rel: Path) -> str:
    if rel.name == "index.html" and len(rel.parent.parts) == 0:
        return SITE + "/"
    path = rel.as_posix().replace("index.html", "").rstrip("/")
    return f"{SITE}/{path}"


def asset_paths(rel: Path) -> tuple[str, str]:
    r = root_prefix(rel)
    return f"{r}css/main.css", f"{r}js/main.js"


def ensure_head_assets(html: str, rel: Path) -> str:
    css, js = asset_paths(rel)
    home_css = ""
    if rel.name == "index.html" and len(rel.parent.parts) == 0:
        home_css = f'\n    <link rel="stylesheet" href="css/home.css">'

    if "css/main.css" not in html:
        html = html.replace(
            "</head>",
            f'    <link rel="preconnect" href="https://fonts.googleapis.com">\n'
            f'    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            f'    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Syne:wght@400;600;700;800&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">\n'
            f'    <link rel="stylesheet" href="{css}">{home_css}\n</head>',
            1,
        )
    elif home_css and "css/home.css" not in html:
        html = html.replace(f'<link rel="stylesheet" href="{css}">', f'<link rel="stylesheet" href="{css}">{home_css}', 1)

    canon = canonical_url(rel)
    if 'rel="canonical"' in html:
        html = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{canon}">', html)
    else:
        html = html.replace("</head>", f'    <link rel="canonical" href="{canon}">\n</head>', 1)

    if js not in html:
        html = html.replace("</body>", f'    <script src="{js}"></script>\n</body>', 1)

    return html


def replace_block(html: str, start_pat: str, end_pat: str, replacement: str) -> str:
    pattern = re.compile(start_pat + r".*?" + end_pat, re.DOTALL | re.IGNORECASE)
    if pattern.search(html):
        return pattern.sub(replacement, html, count=1)
    return html


def process_file(path: Path) -> None:
    rel = path.relative_to(ROOT)
    html = path.read_text(encoding="utf-8")

    nav = build_nav(rel)
    footer = build_footer(rel)
    privacy = root_prefix(rel) + "privacy-policy.html"

    html = re.sub(
        r"<nav id=\"nav\">.*?</nav>\s*(?:<!--[^\n>]*-->\s*)?<div class=\"mobile-menu\" id=\"mobileMenu\">.*?</div>",
        nav,
        html,
        count=1,
        flags=re.DOTALL,
    )

    html = re.sub(r"<footer>.*?</footer>", footer, html, count=1, flags=re.DOTALL)

    html = re.sub(r"\s*<div class=\"marquee-section\"[^>]*>.*?</div>\s*", "\n", html, flags=re.DOTALL)

    if rel.name == "index.html" and len(rel.parent.parts) == 0:
        html = re.sub(r"\s*<style>.*?</style>\s*", "\n", html, count=1, flags=re.DOTALL)

    if "cookie-banner" not in html:
        html = html.replace("</body>", COOKIE_BANNER.format(privacy=privacy) + "\n</body>", 1)

    html = html.replace("47<span>+</span>", "5")
    html = html.replace("In-depth guides", "Core guides")
    html = html.replace("12K<span>+</span>", "Free")
    html = html.replace("Community members", "Facebook community")
    html = html.replace(
        "http://vanconversion.infinityfreeapp.com/wp-content/uploads/2026/02/Add_some_camping_4k_202512282033-scaled.jpeg",
        "builds/img/tran7.webp",
    )
    html = html.replace(
        "https://vanconversion.infinityfreeapp.com/wp-content/uploads/2026/02/Add_some_camping_4k_202512282033-scaled.jpeg",
        "builds/img/tran7.webp",
    )

    html = re.sub(r"<script>\s*// Nav scroll effect.*?</script>\s*", "", html, flags=re.DOTALL)
    html = re.sub(
        r"<script>\s*// ── form submission — runs after DOM is ready ──.*?</script>\s*",
        "",
        html,
        flags=re.DOTALL,
    )
    html = re.sub(r"<script>\s*// FAQ accordion.*?</script>\s*", "", html, flags=re.DOTALL)

    html = ensure_head_assets(html, rel)
    path.write_text(html, encoding="utf-8")
    print(f"updated {rel.as_posix()}")


def iter_html() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*.html"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def main() -> None:
    for path in iter_html():
        process_file(path)
    print("done")


if __name__ == "__main__":
    main()
