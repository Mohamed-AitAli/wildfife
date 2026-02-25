# VanWild — Site Architecture
_Last updated: February 25, 2026_

---

## File Structure

```
vanwild/
│
├── index.html                          ← Homepage
├── about.html                          ← About page
├── compare.html                        ← Van comparison tool
├── contact.html                        ← Contact form + FAQ
├── privacy-policy.html                 ← Privacy Policy (AdSense-ready)
├── blog.html                           ← (legacy — use blog/index.html)
│
├── css/
│   └── main.css                        ← Global design system & all shared styles
│
├── js/
│   └── main.js                         ← Nav, FAQ accordion, reveal animations
│
├── guides/                             ← How-to reference guides
│   ├── solar.html                      ← Solar power sizing & installation
│   ├── insulation.html                 ← Insulation materials & methods
│   ├── budget.html                     ← Budget planning (4 tiers $2K–$30K+)
│   ├── battery.html                    ← LiFePO4 vs AGM comparison
│   └── skoolie.html                    ← School bus conversion guide
│
├── builds/                             ← Real community build documentation
│   ├── index.html                      ← Build gallery · img1–img6 (9:16 slots)
│   └── blog/                           ← Individual build posts
│       ├── transit-build.html          ← Mike · Ford Transit · $6,247 · img1–img7
│       ├── sprinter-remote-work.html   ← Sarah & James · Sprinter · $11,400 · img1–img5
│       ├── rodriguez-skoolie.html      ← Rodriguez family · 40ft Blue Bird · $24,800 · img1–img5
│       ├── promaster-budget-build.html ← Taylor · ProMaster budget · $3,800 · img1–img5
│       ├── revel-upgrade.html          ← Sam & Alex · Revel solar upgrade · $4,200 · img1–img4
│       └── short-bus-conversion.html   ← Jess · Short bus · $16,500 · img1–img5
│
└── blog/                               ← Editorial blog posts
    ├── index.html                      ← Blog listing with category filters
    ├── transit-build-log.html          ← Ford Transit every receipt
    ├── battle-born-review.html         ← Battle Born 100Ah 2-year review
    ├── winter-vanlife-tips.html        ← Vanlife in -18°F: 7 tips
    ├── skoolie-rust-guide.html         ← Skoolie rust removal step-by-step
    ├── free-camping-guide.html         ← Free camping across 34 states
    ├── baja-in-a-van.html              ← 2,000-mile Baja California trip
    ├── maxxair-vs-fantastic.html       ← Maxxair vs Fan-Tastic head-to-head
    ├── van-electrical-mistakes.html    ← 9 electrical mistakes to avoid
    └── skoolie-build-log-1.html        ← Skoolie build log week 1
```

---

## Page Count

| Section           | Count |
|-------------------|-------|
| Root pages        | 5     |
| Guides            | 5     |
| Builds gallery    | 1     |
| Build posts       | 6     |
| Blog listing      | 1     |
| Blog posts        | 9     |
| Asset files       | 2     |
| **Total**         | **29**|

---

## Design System

### Fonts (Google Fonts CDN)
| Variable         | Font       | Role                             |
|------------------|------------|----------------------------------|
| `--font-display` | Bebas Neue | Hero titles, display headings    |
| `--font-head`    | Syne 700/800 | Card titles, labels, UI        |
| `--font-body`    | Inter      | Body copy, descriptions          |

### Color Tokens
| Token            | Value                  | Role                        |
|------------------|------------------------|-----------------------------|
| `--orange`       | `#F4631E`              | Primary accent, CTAs        |
| `--orange-dark`  | `#C94F12`              | Hover states                |
| `--orange-light` | `rgba(244,99,30,0.10)` | Tint backgrounds, tags      |
| `--cream`        | `#F5F0E8`              | Page background             |
| `--sand`         | `#E8DFD0`              | Borders, dividers           |
| `--dark`         | `#1A1612`              | Dark sections, nav, footer  |
| `--mid`          | `#3A2F25`              | Secondary dark surfaces     |
| `--text`         | `#2C251D`              | Body copy                   |
| `--muted`        | `#7A6B5D`              | Secondary / captions        |
| `--white`        | `#FEFCF8`              | Cards, form panels          |

### Spacing Scale (fluid)
```
--space-xs:  clamp(8px,  1.5vw, 14px)
--space-sm:  clamp(14px, 2.5vw, 24px)
--space-md:  clamp(24px, 4vw,   48px)
--space-lg:  clamp(48px, 8vw,   96px)
--space-xl:  clamp(72px, 12vw, 140px)
```

### Type Scale (fluid)
```
--fs-xs:   clamp(11px, 1.2vw, 13px)
--fs-sm:   clamp(13px, 1.5vw, 15px)
--fs-base: clamp(15px, 2vw,   17px)
--fs-md:   clamp(18px, 2.5vw, 24px)
--fs-lg:   clamp(26px, 4vw,   42px)
--fs-xl:   clamp(42px, 8vw,   96px)
--fs-xxl:  clamp(56px, 12vw, 140px)
```

---

## 9:16 Image Slots

All build pages use portrait (9:16) image placeholders. The placeholder hides automatically when a real image loads. To add a photo, just fill in the `src`:

```html
<!-- Empty slot (placeholder visible) -->
<img id="img1" src="" alt="...">

<!-- With your photo -->
<img id="img1" src="../../images/transit-hero.jpg" alt="...">
```

### Slot map per file

| File                                 | Slots     |
|--------------------------------------|-----------|
| `builds/index.html`                  | img1–img6 |
| `builds/blog/transit-build.html`     | img1–img7 |
| `builds/blog/sprinter-remote-work.html` | img1–img5 |
| `builds/blog/rodriguez-skoolie.html` | img1–img5 |
| `builds/blog/promaster-budget-build.html` | img1–img5 |
| `builds/blog/revel-upgrade.html`     | img1–img4 |
| `builds/blog/short-bus-conversion.html` | img1–img5 |

---

## Navigation Structure

### Primary Nav (present on all pages)
```
Solar · Insulation · Budget · Builds · Blog · About  |  [Start Building →]
```

### Footer Nav (all pages)
- **Guides:** Solar Power, Insulation, Budget, Batteries, Skoolie
- **More:** Builds, Blog, Compare, About, Contact, Privacy Policy

### Footer-only pages (not in primary nav)
- `contact.html`
- `privacy-policy.html`
- `compare.html`

---

## Shared Components (main.css + main.js)

| Component          | Class(es)                                         | Notes                              |
|--------------------|---------------------------------------------------|------------------------------------|
| Sticky nav         | `#nav` `.nav-inner` `.hamburger`                  | Shrinks on scroll                  |
| Mobile menu        | `.mobile-menu` `#mobileMenu`                      | Toggled by hamburger button        |
| Page hero          | `.page-hero` `.page-hero-content` `.breadcrumb`   | All inner pages                    |
| Marquee ticker     | `.marquee-section` `.marquee-track`               | Infinite CSS scroll animation      |
| Section header     | `.section-header` `.tag`                          | Label + display title pattern      |
| Article layout     | `.article-grid` `.article-content` `.article-sidebar` | Blog & build posts             |
| Sidebar widget     | `.sidebar-widget` `.sidebar-links` `.sidebar-link` | Right-column on article pages     |
| Callout box        | `.callout` `.callout-warn`                        | Info / warning blocks              |
| Cost table         | `.cost-table`                                     | Styled receipt/budget tables       |
| FAQ accordion      | `.faq-item` `.faq-q` `.faq-a`                     | JS expand/collapse                 |
| CTA banner         | `.cta-banner`                                     | Full-width dark orange CTA strip   |
| Reveal animation   | `.reveal` `.reveal-delay-1/2/3`                   | IntersectionObserver fade-in       |
| Buttons            | `.btn` + `.btn-primary` `.btn-outline` `.btn-ghost` `.btn-white` `.btn-sm` | |

---

## Relative Path Reference

| From                   | To root | To guides       | To builds           | To blog            |
|------------------------|---------|-----------------|---------------------|--------------------|
| Root `/`               | `./`    | `guides/X.html` | `builds/index.html` | `blog/index.html`  |
| `guides/`              | `../`   | `X.html`        | `../builds/`        | `../blog/`         |
| `builds/`              | `../`   | `../guides/`    | `index.html`        | `../blog/`         |
| `builds/blog/`         | `../../`| `../../guides/` | `../index.html`     | `../../blog/`      |
| `blog/`                | `../`   | `../guides/`    | `../builds/`        | `index.html`       |

---

## AdSense & Privacy Notes

- `privacy-policy.html` is fully AdSense-compliant: cookies, AdSense disclosure, CCPA, GDPR, children's privacy (COPPA), data retention, opt-out links
- Every page footer links to `privacy-policy.html` and `contact.html`
- **Before launch:** replace `vanwild.com` in canonical tags and policy text with real domain
- **Contact form:** currently client-side validation only — connect to Formspree, Netlify Forms, or equivalent before going live
