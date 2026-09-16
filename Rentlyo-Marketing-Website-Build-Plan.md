# Rentlyo — Product Marketing Website: Complete Build Plan (v1.0)
### A conversion-focused, search-dominant landing site for a one-time-purchase property management platform

---

## 🎯 BUILD PROMPT — paste this to your AI coding assistant

> Build a production-grade marketing website for **Rentlyo**, a white-label property management platform sold as a **one-time purchase (₹20,000, lifetime use, zero recurring cost)**. Stack: **vanilla HTML + CSS + JavaScript with Tailwind** (compiled build, not the CDN script — see Section 9). No frameworks, no build complexity beyond Tailwind. This document is the single source of truth for site architecture, content, design system, SEO/GEO/AEO/AIO/SMO implementation, analytics wiring, and performance targets. Every product claim in Section 2 is verified against the actual Rentlyo codebase and README — **do not invent features, metrics, testimonials, or statistics that aren't in Section 2.** Section 3 explains why that rule is a conversion strategy, not a limitation. Build in the order given in Section 12.

---

## 1. Pre-launch blocker — fix before the site goes live

The repo at `github.com/aryanony/rentlyo` contains `client_config.json` with:
- `"ownerInitialPassword": "Rentlyo123"` — a real bootstrap admin password
- `"ownerPhone": "9308489230"` — a real phone number

The README's own security section correctly forbids exactly this. Marketing this product will drive traffic and technical scrutiny to the repo, so fix it first:

1. Replace `client_config.json` in the repo with a **sanitized `client_config.example.json`** — placeholder values only (`"ownerInitialPassword": "CHANGE_ME"`).
2. Add the real `client_config.json` to `.gitignore`.
3. Change that password anywhere it's actually in use.
4. Optional but recommended: purge it from git history (`git filter-repo` or BFG) — otherwise it stays readable in old commits.

*(The `firebaseApiKey` in the same file is **not** a leak — Firebase web API keys are designed to be public and are protected by Firestore rules, exactly as the README states. Don't waste effort hiding it.)*

---

## 2. What Rentlyo actually is — the verified fact sheet

Every claim on the website must come from this list. It's long enough that nothing needs inventing.

### Two apps, one synchronized ledger
| | Tenant App | Admin Console |
|---|---|---|
| Live rent balance & dues | View | Manage |
| Lease terms & plain-language deal summary | View | Configure |
| Advance deposit & top-ups | View | Manage |
| Payment ledger & installments | Report | Confirm |
| Rent escalation tiers (step-up) | View | Configure |
| Maintenance requests | Create & track | Resolve |
| Utility sub-meter billing (electricity/water) | View history | Calculate & publish |
| Notices & announcements | Read | Publish |
| Gate passes & visitor logs | Use | Administer |
| Multi-property switching | Contextual | Yes |
| PDF / CSV / Excel reports | — | Yes |
| In-app OTA updates | Receive | Publish |

### Genuinely differentiating capabilities
- **UPI one-tap payment handoff** + WhatsApp receipt sharing
- **Multi-unit deal consolidation** — one lease across several merged units, occupancy stays accurate
- **Commercial / residential isolation** — mixed-use properties without cross-contamination
- **Rent engine**: advance consumption, partial-payment carryover, overdue accumulation, step-up tiers, status reconciliation — shared identically by both apps
- **White-label deployment engine**: one `client_config.json` + a one-click launcher → branded apps, icons, splash, Firebase bootstrap, both release APKs
- **6-digit PIN unlock**, secure local storage, Firestore rules enforcing role + ownership boundaries
- **Runs on Firebase's free tier** — no server bill, no API cost, no domain required by the buyer

### The cost story (the core sales argument)
₹20,000 once. No monthly fee. No per-tenant fee. No server cost. No API cost. No renewal.

---

## 3. Positioning & buyer psychology — persuasion grounded in truth

**Who buys this**: a property owner with 5–50 units who currently runs rent on a paper register or WhatsApp, is tired of disputes and chasing payments, and is *skeptical of software* because every tool they've seen wanted a monthly subscription.

**The single biggest objection isn't price — it's trust.** At ₹20,000 from an independent developer rather than a known company, the buyer's real question is *"will this actually work, and will this person disappear?"*

That's why this site's persuasion strategy is **radical concreteness, not hype**:

| Instead of | Use |
|---|---|
| "Revolutionary platform" | Real screenshots of every screen |
| "Trusted by thousands" *(false)* | "Running live at Arya Plaza, Munger — see it yourself" *(true)* |
| Invented statistics | The actual cost math: ₹20,000 once vs ₹1,999/mo forever |
| "Enterprise-grade AI-powered" | "Your tenant opens the app and sees exactly what they owe" |

Legitimate psychological levers, all truthful:
- **Loss aversion, honestly framed** — a 3-year cost comparison chart (₹20,000 vs ₹71,964 subscription). Real math, no exaggeration.
- **Ownership framing** — "You own it" beats "you subscribe." Powerful in Indian SMB markets specifically.
- **Anchoring** — show what comparable property-management SaaS costs annually, then the one-time price.
- **Proof over promise** — live demo property, real screenshots, downloadable demo APK.
- **Risk reversal** — offer a demo APK + a live walkthrough call before payment. This single element removes more friction than any copywriting.
- **Specificity as credibility** — "utility sub-meter billing with per-unit rate calculation" convinces more than "powerful features."

**On the "manipulative content" request — a deliberate departure, and why.** Manipulative tactics (fake countdown timers, invented scarcity, fabricated testimonials, made-up statistics) would actively *hurt* this product. This is a high-consideration ₹20,000 B2B purchase where buyers research, ask questions, and talk to each other. Manufactured urgency reads as a scam signal to exactly the cautious buyer you're targeting — and one exposed fake claim ends the resale business. Everything in this document is engineered to be *maximally persuasive and completely true*, which for this product and this buyer is simply the higher-converting strategy.

---

## 4. Site architecture

Single-page primary experience + supporting pages (needed for SEO breadth, per Section 8):

```
/                        → Main landing page (the conversion engine)
/features                → Deep feature breakdown, screenshot-led
/pricing                 → The one-time offer, cost comparison, what's included/excluded
/demo                    → Demo APK download + how to book a live walkthrough
/for-property-owners     → Buyer-intent page (owners with 5–50 units)
/for-pg-hostel-owners    → Buyer-intent page (PG/hostel: beds, mess menus, gate passes)
/for-commercial-complex  → Buyer-intent page (shops, multi-unit deals)
/faq                     → Full FAQ (also powers FAQPage schema)
/contact                 → Direct contact + purchase enquiry
/blog                    → Content engine (Section 8)
```

---

## 5. The landing page — section by section

1. **Hero** — Headline: ownership + outcome, e.g. *"Run your rent on software you own — not a subscription you rent."* Sub: one line on what it does. Two CTAs: **"Download Demo APK"** (primary) and **"See Pricing"**. Trust strip beneath: `One-time ₹20,000` · `No monthly fee` · `No server cost` · `Live at a real property`.
2. **The problem** — 4 cards: rent disputes, deposit confusion, manual registers, no visibility. Icon + one short line each.
3. **How it works** — 4-step numbered flow diagram (Add tenant → Tenant logs in → Rent calculates itself → Payment confirmed). Animated on scroll.
4. **The two apps** — side-by-side, real screenshots, the Section 2 capability table rendered as a clean comparison.
5. **Interactive cost calculator** *(signature element)* — buyer enters unit count + a subscription price they've been quoted; JS instantly shows 1/3/5-year cost vs Rentlyo's one-time ₹20,000, with an animated bar chart. This is the highest-conversion element on the page: the buyer does the math themselves, so they believe it.
6. **Screenshot gallery** — auto-advancing carousel, ~1.4 slides visible, real unmodified screenshots, captioned.
7. **Feature deep-dive** — grouped: Money (rent engine, advance, utilities, reports) · Operations (maintenance, notices, gate passes, visitors) · Trust (PIN, rules, roles) · Ownership (white-label, OTA updates, no recurring cost).
8. **Live proof** — Arya Plaza, Munger. Real property, real tenants, link to aryaplaza.vercel.app.
9. **Pricing** — one card, ₹20,000, everything included, explicit "what you'll never be charged for" list (no monthly, no per-tenant, no server, no API, no renewal). Below it: what the buyer *does* need (an Android phone, a free Firebase account — be upfront).
10. **Objection-handling FAQ** — the real questions: *"What if I need changes later?" "What happens if you stop supporting it?" "Do I need technical knowledge?" "Is my data safe?" "Can I use it for multiple properties?"*
11. **Final CTA** — demo download + WhatsApp + call.

---

## 6. Design system

Pull directly from the product's own `client_config.json` so site and product feel like one brand:

| Token | Hex |
|---|---|
| Primary (deep teal) | `#044040` |
| Secondary (gold) | `#CF9D30` |
| Accent | `#C58B2B` |
| Dark background | `#041B23` |
| Light surface | `#F8FAF9` |

**Assets available in repo** (`assets/`): `rentlyo-logo.svg`, `rentlyo-hor.svg`, `rentlyo-icon.svg` — use the SVGs (crisp at every size, tiny file size), PNG only as fallback.

**Typography**: one display face for headings, one highly-legible sans for body. Minimum 17px body text, 1.6 line-height — non-negotiable given the "any older or less-educated person can read it" requirement.

**Accessibility floor**: WCAG AA contrast minimum, visible focus states, real `<button>`/`<a>` elements, alt text on every image, `prefers-reduced-motion` respected on all animations.

**Bilingual**: a genuine Hindi toggle for the hero, problem, how-it-works, pricing, and FAQ sections. The buyer base for this product is substantially Hindi-first — this is a conversion feature, not a nicety.

---

## 7. Interactive & graphical elements

- Cost calculator (Section 5.5) — the centerpiece
- Animated 4-step process flow (SVG, animates on scroll)
- Architecture diagram — Admin ↔ Firebase ↔ Tenant, with labelled data flow
- Cost comparison bar chart (Chart.js or hand-rolled SVG)
- Screenshot carousel with auto-advance + swipe
- Scroll-reveal animations throughout (subtle, `prefers-reduced-motion`-aware)
- Feature cards with hover elevation
- Sticky mobile CTA bar ("Download Demo") after hero scroll-past

---

## 8. SEO / GEO / AEO / AIO

### Technical foundation
- Semantic HTML5, one `<h1>` per page, logical heading hierarchy
- Unique `<title>` (≤60 chars) + `<meta description>` (≤155) per page
- Canonical URLs, Open Graph + Twitter cards with a real preview image
- `sitemap.xml` (all pages) + `robots.txt` with explicit allows for `GPTBot`, `ClaudeBot`, `PerplexityBot`, `Google-Extended`, `CCBot`, `Bingbot`
- `llms.txt` + `llms-full.txt` — factual product reference for AI systems (Section 2 is the source content). Emerging GEO practice; almost no competitor in this niche has it.
- PWA manifest, favicon set

### Structured data (JSON-LD `@graph`)
`SoftwareApplication` (primary — with `applicationCategory: BusinessApplication`, `operatingSystem: Android`, and an `Offer` with `price: 20000`, `priceCurrency: INR`) + `Organization` + `WebSite` + `FAQPage` + `BreadcrumbList` + `Product`.

**Do not add `AggregateRating` or `Review` schema until real reviews exist** — fabricated ratings are a policy violation with real penalty risk.

### Keyword targets
- **Primary**: property management software India, rent management app, one time payment property software, tenant management app, lease management software India
- **Category**: PG management software, hostel management app, commercial property management software, rental ledger software, society management app
- **High-intent long-tail**: *"property management software without monthly subscription," "one time purchase rent management app India," "white label property management app," "rent collection app for landlords India," "PG hostel management software one time payment"*
- **Hindi/Hinglish**: किराया प्रबंधन ऐप, प्रॉपर्टी मैनेजमेंट सॉफ्टवेयर

### AEO — answer-engine optimization
Every FAQ answer must **lead with the direct answer in the first sentence**, detail after. Target the questions buyers actually type: *"What is the best one-time payment property management software?" "How much does property management software cost in India?" "Can I manage rent without a monthly subscription?"* Each gets a genuine, self-contained answer — this is what AI answer engines extract and cite.

### Content engine (`/blog`) — the long-term ranking lever
One post every 1–2 weeks. Topic bank: *"One-time purchase vs subscription property software: the real 5-year cost," "How to track a security deposit correctly," "Rent agreement checklist for Indian landlords," "How to bill electricity sub-meters fairly," "Managing a PG: the complete operations guide," "Commercial vs residential leasing: what changes."* Each post targets a real long-tail query and links to a buyer-intent page.

---

## 9. Performance targets

- **Compiled Tailwind** (`npx tailwindcss -o style.css --minify`) — never the CDN script in production; the CDN build is significantly heavier and blocks render.
- Lighthouse targets: Performance ≥ 95, Accessibility 100, Best Practices 100, SEO 100
- LCP < 2.0s, CLS < 0.1, INP < 200ms on a mid-range Android over 4G — this is the buyer's actual device
- All images WebP with explicit `width`/`height`; screenshots lazy-loaded below the fold
- SVG logos inline where small; defer all non-critical JS
- Self-host fonts or use `font-display: swap`
- Total initial payload target: under 500KB

---

## 10. Analytics & tooling

- **GTM container** in `<head>` + the `noscript` fallback immediately after `<body>` — all other tags fire through GTM, not hardcoded.
- **GA4 via GTM**, with these custom events: `demo_apk_download`, `pricing_view`, `calculator_used`, `whatsapp_click`, `call_click`, `faq_expand`, `screenshot_carousel_interact`, `blog_read_complete`.
- **Google Search Console** — verify via GTM or an HTML file, submit `sitemap.xml`, monitor Core Web Vitals and query data monthly.
- **Bing Webmaster Tools** — free, takes 5 minutes, and feeds Copilot/ChatGPT search results.
- Consider Microsoft Clarity (free) for heatmaps/session recordings — genuinely useful for finding where buyers drop off.

---

## 11. SMO & off-site distribution

- **Consistent identity** (name, logo, bio, contact) across: LinkedIn (company page), Instagram, Facebook, YouTube, X.
- **YouTube is the highest-leverage channel here** — a 5-minute "full walkthrough" video and a 60-second "how a tenant pays rent" clip. Video gets cited by AI answer engines and ranks in Google directly. Embed both on the site.
- **Marketplace listings** — Envato/CodeCanyon, Gumroad, IndiaMART, and relevant Indian SMB software directories. Each listing links back to the site.
- **Communities** — Indian landlord/property Facebook groups, relevant subreddits, local business WhatsApp groups. Share genuine value (the blog posts), not spam.
- **NAP consistency** — identical name/contact everywhere; it's a real ranking signal.

---

## 12. Build order

1. Section 1 — sanitize the repo credentials (before anything public)
2. Design system + Tailwind config with the brand tokens
3. Landing page structure + hero + trust strip
4. Problem → How it works → Two apps sections
5. **Cost calculator** (the conversion centerpiece — build it properly, test the math)
6. Screenshot gallery + feature deep-dive + live proof
7. Pricing + objection FAQ + final CTA
8. Supporting pages (`/features`, `/pricing`, `/demo`, 3 buyer-intent pages, `/faq`, `/contact`)
9. All SEO/GEO technical files (schema, sitemap, robots, llms.txt)
10. Hindi toggle
11. GTM + GA4 + Search Console + Bing wiring
12. Lighthouse pass — fix until targets in Section 9 are met
13. `/blog` scaffold + first 2 posts
14. Marketplace listings + YouTube walkthrough video

---

## 13. One commercial note, worth considering

Earlier market research put a product with this scope at ₹19,999 (basic) to ₹79,999 (unlimited units, multi-property). Rentlyo has since grown well past that baseline — utility sub-meter billing, gate passes, visitor logs, multi-property switching, and a full automated white-label deployment engine are all now shipped. A single flat ₹20,000 for everything is a genuinely strong buyer offer, and simplicity does convert — but it likely leaves real money on the table for larger buyers.

**A low-risk option that keeps the simple message**: keep ₹20,000 as the headline single price for a standard single-property deployment, and add one optional line — *"Managing multiple properties or 50+ units? Contact for a custom deployment quote."* No pricing-table complexity, no weakening of the one-time-payment story, but it stops undercharging the buyer who'd happily pay three times as much. Your call entirely — the site works either way.
