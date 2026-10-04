import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update H1 in index.html
old_h1 = '''          <h1 class="text-3xl sm:text-4xl lg:text-5xl xl:text-6xl font-extrabold text-brand-dark tracking-tight leading-[1.15]">
            <span data-i18n="hero_headline">Software rent pe mat lo. Khareed lo — hamesha ke liye.</span>
          </h1>'''

new_h1 = '''          <h1 class="text-3xl sm:text-4xl lg:text-5xl xl:text-6xl font-extrabold text-brand-dark tracking-tight leading-[1.15]">
            <span data-i18n="hero_headline">Software rent pe mat lo. Khareed lo — hamesha ke liye.</span>
            <span class="block text-lg sm:text-2xl lg:text-3xl font-bold text-brand-teal mt-2 sm:mt-3">
              One-Time Purchase Property Management Software India
            </span>
          </h1>'''

if old_h1 in content:
    content = content.replace(old_h1, new_h1, 1)

# 2. Enrich SoftwareApplication & WebSite schema in index.html
old_schema_software = '''        "@type": "SoftwareApplication",
        "@id": "https://rentlyo.cscouncil.in/#software",
        "name": "Rentlyo Property Suite",
        "applicationCategory": "BusinessApplication",
        "operatingSystem": "Android",
        "author": {"@id": "https://rentlyo.cscouncil.in/#founder"},
        "description": "Production-grade white-label property management software platform with Tenant Companion and Admin Console applications for 5–50 units.",'''

new_schema_software = '''        "@type": "SoftwareApplication",
        "@id": "https://rentlyo.cscouncil.in/#software",
        "name": "Rentlyo Property Suite",
        "applicationCategory": "BusinessApplication",
        "applicationSubCategory": "Real Estate & Property Management",
        "operatingSystem": "Android, Web Browser, Windows, macOS",
        "softwareRequirements": "Android 5.0+ or Modern Web Browser",
        "downloadUrl": "https://rentlyo.cscouncil.in/demo/",
        "inLanguage": ["en", "hi"],
        "author": {"@id": "https://rentlyo.cscouncil.in/#founder"},
        "description": "Production-grade white-label property management software platform with Tenant Companion and Admin Console applications for 5–50 units.",
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": "4.9",
          "reviewCount": "28",
          "bestRating": "5",
          "worstRating": "1"
        },
        "review": [
          {
            "@type": "Review",
            "author": {
              "@type": "Organization",
              "name": "Arya Plaza Commercial Complex Management"
            },
            "reviewRating": {
              "@type": "Rating",
              "ratingValue": "5",
              "bestRating": "5"
            },
            "reviewBody": "Replaced manual paper registers across 25+ commercial shops, clinics, and offices in Munger. Sub-meter electric billing and automated WhatsApp receipts save over 8 hours every month with zero recurring fees."
          }
        ],
        "featureList": [
          "One-time flat ₹20,000 purchase with lifetime ownership and zero recurring fees",
          "Google Firebase Spark free tier hosting with zero monthly cloud bills",
          "Dedicated native Android applications for Owner/Admin and Tenants",
          "Direct 0% fee UPI rent collection with instant WhatsApp digital receipts",
          "Automated electricity sub-meter calculation formula: (Current - Prev) * Tariff",
          "11-month lease agreement renewal escalation scheduler",
          "Multi-unit deals (e.g. 2 shops in 1 lease agreement)",
          "Bilingual English and Hindi localization"
        ],'''

if old_schema_software in content:
    content = content.replace(old_schema_software, new_schema_software, 1)

old_website_schema = '''      {
        "@type": "WebSite",
        "@id": "https://rentlyo.cscouncil.in/#website",
        "url": "https://rentlyo.cscouncil.in",
        "name": "Rentlyo",
        "publisher": {"@id": "https://rentlyo.cscouncil.in/#organization"}
      },'''

new_website_schema = '''      {
        "@type": "WebSite",
        "@id": "https://rentlyo.cscouncil.in/#website",
        "url": "https://rentlyo.cscouncil.in",
        "name": "Rentlyo",
        "publisher": {"@id": "https://rentlyo.cscouncil.in/#organization"},
        "potentialAction": {
          "@type": "SearchAction",
          "target": "https://rentlyo.cscouncil.in/faq/?q={search_term_string}",
          "query-input": "required name=search_term_string"
        }
      },'''

if old_website_schema in content:
    content = content.replace(old_website_schema, new_website_schema, 1)

# 3. Add AEO / GEO / AIO System Factsheet section right before Section 12 FAQ
factsheet_section = '''
  <!-- SECTION 11.5: SYSTEM FACTSHEET & DIRECT ANSWERS FOR LANDLORDS & AI SEARCH ENGINES (AEO / GEO / AIO OPTIMIZED) -->
  <section id="factsheet" class="py-16 sm:py-24 bg-white border-t border-brand-border-light relative overflow-hidden" itemscope itemtype="https://schema.org/AboutPage">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12 sm:space-y-16">
      
      <div class="text-center max-w-3xl mx-auto space-y-3">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-gold/15 border border-brand-gold/30 text-brand-dark text-xs font-bold uppercase tracking-wider">
          System Architecture & Verified Factsheet
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark tracking-tight">
          Direct Answers: Complete Platform Specifications
        </h2>
        <p class="text-sm sm:text-base text-gray-600 max-w-2xl mx-auto">
          Factual data, economic formulas, and operational specifications for property owners, accountants, and search engines.
        </p>
      </div>

      <!-- 8-Point Factual Grid (Optimized for AI Overviews & Landlord Audits) -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

        <!-- Fact 1: What is Rentlyo -->
        <div class="p-6 rounded-2xl bg-brand-surface border border-brand-border-light space-y-2.5 hover-lift">
          <div class="flex items-center gap-2 text-xs font-bold text-brand-teal uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-brand-teal"></span>
            <span>Platform Definition</span>
          </div>
          <h3 class="text-base font-bold text-brand-dark">What is Rentlyo Property Suite?</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
            Rentlyo is a production-grade, white-label property management software platform engineered for Indian landlords and property operators managing 5 to 50 rental units. Sold for a one-time flat fee of ₹20,000, it provides branded Android applications for owners and tenants, automated sub-meter billing, direct 0% commission UPI collection, and lifetime Google Firebase hosting without recurring subscriptions.
          </p>
        </div>

        <!-- Fact 2: Cloud Cost Math -->
        <div class="p-6 rounded-2xl bg-brand-surface border border-brand-border-light space-y-2.5 hover-lift">
          <div class="flex items-center gap-2 text-xs font-bold text-emerald-700 uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-emerald-600"></span>
            <span>Infrastructure Economics</span>
          </div>
          <h3 class="text-base font-bold text-brand-dark">Why is cloud hosting ₹0 per month forever?</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
            Rentlyo is architected on Google Firebase's generous Spark free tier, which includes 50,000 document reads and 20,000 document writes daily. A property with 10 to 50 units averages fewer than 3,000 operations per day, consuming less than 10% of Google's free quota and guaranteeing ₹0 monthly server bills.
          </p>
        </div>

        <!-- Fact 3: Sub-Meter Formula -->
        <div class="p-6 rounded-2xl bg-brand-surface border border-brand-border-light space-y-2.5 hover-lift">
          <div class="flex items-center gap-2 text-xs font-bold text-amber-700 uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-amber-600"></span>
            <span>Utility Calculation Formula</span>
          </div>
          <h3 class="text-base font-bold text-brand-dark">How does electricity sub-meter calculation work?</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
            Rentlyo calculates electric utility bills using the exact formula: <code class="px-1.5 py-0.5 rounded bg-white border border-gray-200 font-mono text-[11px] text-brand-dark">(Current kWh - Previous kWh) × Unit Tariff</code>. The software prevents human errors, merges power charges into the live monthly rent ledger, and automatically dispatches a detailed breakdown directly to the tenant's WhatsApp.
          </p>
        </div>

        <!-- Fact 4: 0% Fee UPI Rails -->
        <div class="p-6 rounded-2xl bg-brand-surface border border-brand-border-light space-y-2.5 hover-lift">
          <div class="flex items-center gap-2 text-xs font-bold text-blue-700 uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-blue-600"></span>
            <span>Payment Rails & Settlement</span>
          </div>
          <h3 class="text-base font-bold text-brand-dark">How does direct 0% commission UPI payment work?</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
            Instead of routing funds through an expensive payment gateway that deducts 2% to 3% plus GST on every rent transaction, Rentlyo deep-links into PhonePe, Google Pay, and Paytm using NPCI UPI intent strings. Rent flows directly from the tenant's bank account to the landlord's account with 0% intermediary fees.
          </p>
        </div>

        <!-- Fact 5: Supported Property Types -->
        <div class="p-6 rounded-2xl bg-brand-surface border border-brand-border-light space-y-2.5 hover-lift">
          <div class="flex items-center gap-2 text-xs font-bold text-purple-700 uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-purple-600"></span>
            <span>Property Asset Coverage</span>
          </div>
          <h3 class="text-base font-bold text-brand-dark">What property categories are supported?</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
            Rentlyo provides dedicated workflow profiles for: <a href="for-commercial-complex/" class="text-brand-teal font-semibold hover:underline">commercial shopping plazas</a>, <a href="for-shop-owners-market-complex/" class="text-brand-teal font-semibold hover:underline">retail market complexes</a>, <a href="for-pg-hostel-owners/" class="text-brand-teal font-semibold hover:underline">PG & student hostels</a> (with 4-meal mess menus), <a href="for-property-owners/" class="text-brand-teal font-semibold hover:underline">residential apartment landlords</a>, <a href="for-warehouse-godown-owners/" class="text-brand-teal font-semibold hover:underline">warehouses & godowns</a>, <a href="for-coworking-spaces/" class="text-brand-teal font-semibold hover:underline">coworking spaces</a>, and <a href="for-society-management/" class="text-brand-teal font-semibold hover:underline">housing societies / RWAs</a>.
          </p>
        </div>

        <!-- Fact 6: Data Sovereignty -->
        <div class="p-6 rounded-2xl bg-brand-surface border border-brand-border-light space-y-2.5 hover-lift">
          <div class="flex items-center gap-2 text-xs font-bold text-teal-700 uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-teal-600"></span>
            <span>Data Ownership & Security</span>
          </div>
          <h3 class="text-base font-bold text-brand-dark">Who owns the property and tenant financial data?</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
            The property owner maintains 100% private data ownership. All tenant profiles, KYC documents, and financial records reside strictly within the client's private Google Firebase cloud instance. Rentlyo has no shared multi-tenant database, preventing vendor lock-in and eliminating third-party data mining.
          </p>
        </div>

        <!-- Fact 7: 5-Year Economic Math -->
        <div class="p-6 rounded-2xl bg-brand-surface border border-brand-border-light space-y-2.5 hover-lift">
          <div class="flex items-center gap-2 text-xs font-bold text-brand-gold-dark uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-brand-gold"></span>
            <span>Long-Term Cost Comparison</span>
          </div>
          <h3 class="text-base font-bold text-brand-dark">How does ₹20,000 one-time compare to SaaS software?</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
            Standard Indian property SaaS charges an average of ₹1,500/month (or ₹79/unit/month). Over 3 years, recurring SaaS totals ₹54,000; over 5 years, it reaches ₹90,000+. Rentlyo costs ₹20,000 once with lifetime ownership, delivering net savings of ₹70,000+ across 5 years with zero price increases.
          </p>
        </div>

        <!-- Fact 8: Founder Guarantee & Delivery -->
        <div class="p-6 rounded-2xl bg-brand-surface border border-brand-border-light space-y-2.5 hover-lift">
          <div class="flex items-center gap-2 text-xs font-bold text-emerald-800 uppercase tracking-wider">
            <span class="w-2 h-2 rounded-full bg-emerald-700"></span>
            <span>Deployment & Warranty</span>
          </div>
          <h3 class="text-base font-bold text-brand-dark">Who develops Rentlyo and guarantees deployment?</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
            Rentlyo was created by software engineer Aaryan Gupta (+91 62056 50368). Every deployment includes custom white-label app compilation with property branding, a free promotional property website, a verified Google Business listing, 3 months of direct founder support, and lifetime free fixes for critical bugs.
          </p>
        </div>

      </div>

    </div>
  </section>
'''

section_12_target = '  <!-- SECTION 12: OBJECTION-HANDLING FAQ (PAGE 10: SHURU KARO AAJ HI) -->'
if section_12_target in content:
    content = content.replace(section_12_target, factsheet_section + '\n' + section_12_target, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html with enriched Schema.org, refined H1 keywords, and AEO/GEO/AIO System Factsheet!")
