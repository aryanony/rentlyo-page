import os
import re

root_dir = r"c:\Users\aryn1\Documents\Rentlyo\WEB"

PAGE_SEO = {
    "index.html": {
        "title": "Rentlyo | One-Time Property Management Software India",
        "desc": "Own your property management software for a flat ₹20,000 one-time fee. Zero monthly subscriptions. Branded Owner & Tenant Android apps. Built by Aaryan Gupta.",
        "canonical": "https://rentlyo.cscouncil.in/",
        "is_404": False,
    },
    "pricing/index.html": {
        "title": "Rentlyo Pricing | One-Time ₹20,000 Fee, No Subscription",
        "desc": "Pay ₹20,000 once and own your rental software forever. Zero monthly subscription, zero server bills, unlimited tenants. 100% white-glove setup included.",
        "canonical": "https://rentlyo.cscouncil.in/pricing/",
        "is_404": False,
    },
    "demo/index.html": {
        "title": "Rentlyo Live Demo & APK Download | Test Before You Buy",
        "desc": "Test Rentlyo on your phone or browser before paying. Download Owner & Tenant APKs or test live web demos. Request credentials via WhatsApp: +91 62056 50368.",
        "canonical": "https://rentlyo.cscouncil.in/demo/",
        "is_404": False,
    },
    "features/index.html": {
        "title": "Rentlyo Features | Complete Rental Management Software",
        "desc": "Explore all 10 core features: dual apps, automated UPI receipts, sub-meter electric bills, 6-digit PIN security, and CA-ready PDF reports. Flat ₹20,000 once.",
        "canonical": "https://rentlyo.cscouncil.in/features/",
        "is_404": False,
    },
    "security/index.html": {
        "title": "Rentlyo Security | Private Firebase Database Architecture",
        "desc": "Zero vendor lock-in. Your rental data resides strictly in your private Google Firebase database with 256-bit encryption and cryptographic isolation rules.",
        "canonical": "https://rentlyo.cscouncil.in/security/",
        "is_404": False,
    },
    "case-study/arya-plaza-munger/index.html": {
        "title": "Arya Plaza Munger Case Study | 100% Digital Rent Proof",
        "desc": "See how Arya Plaza in Munger, Bihar replaced manual registers with Rentlyo. 7 commercial units operating on 100% digital hisaab with zero monthly software fees.",
        "canonical": "https://rentlyo.cscouncil.in/case-study/arya-plaza-munger/",
        "is_404": False,
    },
    "compare/rentlyo-vs-excel-register/index.html": {
        "title": "Rentlyo vs Excel & Registers | 2026 Landlord Comparison",
        "desc": "Compare Excel spreadsheets and paper registers against Rentlyo. Learn how automated WhatsApp receipts and sub-meter tracking eliminate monthly tenant disputes.",
        "canonical": "https://rentlyo.cscouncil.in/compare/rentlyo-vs-excel-register/",
        "is_404": False,
    },
    "compare/rentlyo-vs-subscription-software/index.html": {
        "title": "Rentlyo vs SaaS Subscriptions | One-Time vs Monthly Cost",
        "desc": "Compare ₹20,000 lifetime ownership against recurring SaaS subscriptions. Save over ₹1,60,000 over 5 years with zero per-unit fees and private cloud hosting.",
        "canonical": "https://rentlyo.cscouncil.in/compare/rentlyo-vs-subscription-software/",
        "is_404": False,
    },
    "contact/index.html": {
        "title": "Contact Rentlyo | Direct Founder Call & WhatsApp Desk",
        "desc": "Connect directly with creator Aaryan Gupta. Call or WhatsApp +91 62056 50368 for live product walkthroughs, custom branding, and deployment support.",
        "canonical": "https://rentlyo.cscouncil.in/contact/",
        "is_404": False,
    },
    "faq/index.html": {
        "title": "Rentlyo FAQ | Answers on ₹20,000 Pricing & Tech Setup",
        "desc": "Clear answers on Rentlyo one-time ₹20,000 pricing, private Firebase hosting, tenant data privacy, updates, and setup support. Answered by founder Aaryan.",
        "canonical": "https://rentlyo.cscouncil.in/faq/",
        "is_404": False,
    },
    "changelog/index.html": {
        "title": "Rentlyo Changelog | Public Version Releases & Updates",
        "desc": "Public release log for Rentlyo Property Management Platform. Review latest engine updates, security patches, sub-meter tools, and Android build history.",
        "canonical": "https://rentlyo.cscouncil.in/changelog/",
        "is_404": False,
    },
    "for-commercial-complex/index.html": {
        "title": "Commercial Property Management Software India | Rentlyo",
        "desc": "Streamline commercial shopping complexes and plazas. Consolidated multi-unit billing, electricity sub-meter calculation, and automated tenant WhatsApp receipts.",
        "canonical": "https://rentlyo.cscouncil.in/for-commercial-complex/",
        "is_404": False,
    },
    "for-shop-owners-market-complex/index.html": {
        "title": "Shop & Market Complex Rental Software India | Rentlyo",
        "desc": "Commercial market rental software for retail plazas and shopping centers. Automated rent reminders, deposit tracking, and utility sub-meters. ₹20,000 once.",
        "canonical": "https://rentlyo.cscouncil.in/for-shop-owners-market-complex/",
        "is_404": False,
    },
    "for-pg-hostel-owners/index.html": {
        "title": "PG & Hostel Management Software India (₹20,000) | Rentlyo",
        "desc": "Manage beds, student rent, 4-meal mess menus, and visitor gate passes with Rentlyo. Zero per-bed monthly fees. Flat ₹20,000 one-time fee with free setup.",
        "canonical": "https://rentlyo.cscouncil.in/for-pg-hostel-owners/",
        "is_404": False,
    },
    "for-property-owners/index.html": {
        "title": "Residential Landlord Rental Software India | Rentlyo",
        "desc": "Tired of paper registers and chasing rent on WhatsApp? Rentlyo delivers branded Android apps for residential landlords. Built by Aaryan Gupta. ₹20,000 once.",
        "canonical": "https://rentlyo.cscouncil.in/for-property-owners/",
        "is_404": False,
    },
    "for-warehouse-godown-owners/index.html": {
        "title": "Warehouse & Godown Lease Management Software | Rentlyo",
        "desc": "Commercial godown and warehouse rental software for Indian owners. Multi-shed lease tracking, 3-phase sub-metering, and step-up escalation schedules built-in.",
        "canonical": "https://rentlyo.cscouncil.in/for-warehouse-godown-owners/",
        "is_404": False,
    },
    "for-coworking-spaces/index.html": {
        "title": "Coworking Space Management Software India | Rentlyo",
        "desc": "One-time purchase coworking management software for Indian shared offices. Track flex desks, private cabin dues, and digital visitor passes with zero subscriptions.",
        "canonical": "https://rentlyo.cscouncil.in/for-coworking-spaces/",
        "is_404": False,
    },
    "for-society-management/index.html": {
        "title": "Housing Society & RWA Management Software | Rentlyo",
        "desc": "Housing society software for Indian RWAs and apartment associations with 10–50 flats. Maintenance billing, digital gate passes, and broadcast notice alerts.",
        "canonical": "https://rentlyo.cscouncil.in/for-society-management/",
        "is_404": False,
    },
    "blog/index.html": {
        "title": "Rentlyo Blog | Rental Management Guides for Landlords",
        "desc": "Practical rental management guides, sub-meter electric formulas, lease agreement templates, and software cost breakdowns for Indian property owners.",
        "canonical": "https://rentlyo.cscouncil.in/blog/",
        "is_404": False,
    },
    "blog/one-time-purchase-vs-subscription/index.html": {
        "title": "One-Time vs SaaS Rental Software | 5-Year Cost Breakdown",
        "desc": "A realistic 5-year mathematical comparison: one-time ₹20,000 purchase vs monthly SaaS rental subscriptions for Indian landlords managing 5 to 50 units.",
        "canonical": "https://rentlyo.cscouncil.in/blog/one-time-purchase-vs-subscription/",
        "is_404": False,
    },
    "blog/rent-agreement-checklist-indian-landlords/index.html": {
        "title": "Rent Agreement Checklist: 8 Clauses for Indian Owners",
        "desc": "Protect your rental property and cash flow with 8 essential lease agreement clauses for Indian landlords managing commercial shops, flats, and PG hostels.",
        "canonical": "https://rentlyo.cscouncil.in/blog/rent-agreement-checklist-indian-landlords/",
        "is_404": False,
    },
    "404.html": {
        "title": "Page Not Found (404) | Rentlyo Property Suite",
        "desc": "The requested property page or document was not found. Return to Rentlyo homepage or download our official 10-page property management brochure.",
        "canonical": "https://rentlyo.cscouncil.in/404.html",
        "is_404": True,
    }
}

for rel_path, data in PAGE_SEO.items():
    file_path = os.path.join(root_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    title = data["title"]
    desc = data["desc"]
    canonical = data["canonical"]
    is_404 = data["is_404"]

    # 1. Update <title>
    content = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", content, flags=re.DOTALL | re.IGNORECASE)

    # 2. Update meta description
    if re.search(r'<meta\s+name=["\']description["\']', content, re.IGNORECASE):
        content = re.sub(
            r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']\s*/?>',
            f'<meta name="description" content="{desc}">',
            content,
            flags=re.IGNORECASE
        )
    else:
        # insert after title
        content = content.replace(f"<title>{title}</title>", f"<title>{title}</title>\n  <meta name=\"description\" content=\"{desc}\">")

    # 3. Robots tag
    robots_tag = '<meta name="robots" content="noindex, follow">\n  <meta name="googlebot" content="noindex, follow">' if is_404 else '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">\n  <meta name="googlebot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">\n  <meta name="bingbot" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">'

    if re.search(r'<meta\s+name=["\']robots["\']', content, re.IGNORECASE):
        content = re.sub(
            r'<meta\s+name=["\']robots["\']\s+content=["\'].*?["\']\s*/?>',
            robots_tag,
            content,
            flags=re.IGNORECASE
        )
    else:
        # insert after description
        content = re.sub(
            r'(<meta\s+name=["\']description["\']\s+content=["\'].*?["\']\s*/?>)',
            r'\1\n  ' + robots_tag,
            content,
            flags=re.IGNORECASE
        )

    # 4. Canonical link
    if re.search(r'<link\s+rel=["\']canonical["\']', content, re.IGNORECASE):
        content = re.sub(
            r'<link\s+rel=["\']canonical["\']\s+href=["\'].*?["\']\s*/?>',
            f'<link rel="canonical" href="{canonical}">',
            content,
            flags=re.IGNORECASE
        )
    else:
        content = re.sub(
            r'(<meta\s+name=["\']description["\']\s+content=["\'].*?["\']\s*/?>)',
            r'\1\n  ' + f'<link rel="canonical" href="{canonical}">',
            content,
            flags=re.IGNORECASE
        )

    # 5. OpenGraph & Twitter tags
    og_image = "https://rentlyo.cscouncil.in/assets/rentlyo-hor.png"
    if re.search(r'<meta\s+property=["\']og:title["\']', content, re.IGNORECASE):
        content = re.sub(
            r'<meta\s+property=["\']og:title["\']\s+content=["\'].*?["\']\s*/?>',
            f'<meta property="og:title" content="{title}">',
            content,
            flags=re.IGNORECASE
        )
    if re.search(r'<meta\s+property=["\']og:description["\']', content, re.IGNORECASE):
        content = re.sub(
            r'<meta\s+property=["\']og:description["\']\s+content=["\'].*?["\']\s*/?>',
            f'<meta property="og:description" content="{desc}">',
            content,
            flags=re.IGNORECASE
        )
    if re.search(r'<meta\s+property=["\']og:url["\']', content, re.IGNORECASE):
        content = re.sub(
            r'<meta\s+property=["\']og:url["\']\s+content=["\'].*?["\']\s*/?>',
            f'<meta property="og:url" content="{canonical}">',
            content,
            flags=re.IGNORECASE
        )

    # Add Twitter cards if not present
    if '<meta name="twitter:card"' not in content:
        twitter_tags = f"""  <!-- Twitter Card Data -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{og_image}">"""
        # insert before </head>
        content = content.replace("</head>", f"{twitter_tags}\n</head>")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"UPDATED: {rel_path} | Title ({len(title)} chars) | Desc ({len(desc)} chars)")

print("SEO tags update complete!")
