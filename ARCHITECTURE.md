# VanWild — Site Architecture

```
vanwild/
│
├── index.html                  ← Homepage (hero, guides overview, comparison, FAQ)
├── blog.html                   ← Blog listing with category filter
├── compare.html                ← Van vs Camper vs Skoolie comparison
├── about.html                  ← About page + build submission
│
├── css/
│   └── main.css                ← Global stylesheet (all pages link to this)
│
├── js/
│   └── main.js                 ← Global JS (nav, reveal, FAQ, hamburger)
│
├── guides/                     ← In-depth guide pages
│   ├── solar.html              ← Solar power setup + interactive calculator
│   ├── insulation.html         ← Insulation types, R-values, condensation
│   ├── budget.html             ← Cost breakdown by tier ($2K–$30K+)
│   ├── battery.html            ← Lithium vs AGM 5-year comparison
│   └── skoolie.html            ← Complete school bus conversion guide
│
├── builds/
│   └── index.html              ← Community builds gallery (filterable)
│
└── blog/                       ← Individual blog post pages (stub URLs)
    ├── transit-build-log.html
    ├── battle-born-review.html
    ├── winter-vanlife-tips.html
    ├── skoolie-rust-guide.html
    ├── free-camping-guide.html
    ├── baja-in-a-van.html
    ├── maxxair-vs-fantastic.html
    ├── van-electrical-mistakes.html
    └── skoolie-build-log-1.html
```

---

## Page Overview

| Page | URL | Description |
|------|-----|-------------|
| Homepage | `index.html` | Hero, guides summary, compare cards, roadmap, FAQ |
| Blog | `blog.html` | All posts, filterable by category |
| Compare | `compare.html` | Rig picker with scores, full comparison table |
| About | `about.html` | Origin story, principles, build submission |
| Solar Guide | `guides/solar.html` | Full solar guide + live sizing calculator |
| Insulation | `guides/insulation.html` | Materials, R-values, condensation control |
| Budget | `guides/budget.html` | Tier breakdown + line-item sample build |
| Batteries | `guides/battery.html` | Lithium vs AGM with 5-year math |
| Skoolie | `guides/skoolie.html` | Bus buying, build timeline, costs |
| Builds | `builds/index.html` | Community build gallery |

---

## Shared Assets

### `css/main.css`
- CSS custom properties (design tokens)
- Reset, typography, layout utilities
- Navigation (fixed, scroll-reactive)
- Buttons, cards, tags
- Page hero (inner pages)
- Article/guide layout (2-col with sidebar)
- Comparison & cost tables
- Blog card grid
- Scroll reveal animations
- Footer
- Full responsive breakpoints
- Print styles

### `js/main.js`
- Nav scroll class toggle
- Hamburger / mobile menu open-close
- Active nav link highlighting (by URL)
- Intersection Observer scroll reveal
- FAQ accordion
- Smooth anchor scroll with nav offset

---

## URL Convention

```
Root:   index.html, blog.html, compare.html, about.html
Guides: guides/[topic].html
Builds: builds/index.html
Posts:  blog/[slug].html
Assets: css/main.css, js/main.js
```

All internal links use **relative paths** so the site works locally
and can be hosted in any subfolder without changes.

---

## Responsive Strategy

- **Fluid typography**: `clamp()` on all font sizes — no breakpoint font overrides needed
- **CSS Grid with `auto-fit + minmax`**: Cards reflow automatically
- **Mobile nav**: Hidden at ≤640px, replaced with hamburger + fullscreen overlay
- **Article sidebar**: Hidden at ≤960px (content takes full width)
- **Footer**: 2-col at mobile, full grid at desktop

---

## Ad Revenue Notes (for monetization)

Best ad placement spots per page:
- **In-article** between H2 sections (highest engagement)
- **Sidebar widget** (desktop only — above fold)
- **Below hero** before main content
- **After article** before CTA banner

Recommended: Google AdSense (auto-ads), or Mediavine once traffic reaches 50K sessions/month for higher RPM.
