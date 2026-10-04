import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

initial_len = len(content)
print(f"Starting character count: {initial_len}")

# Locate #factsheet
s_fact_start = content.find('<!-- SECTION 11.5: SYSTEM FACTSHEET')
assert s_fact_start != -1, "Cannot find #factsheet start"

# Locate end of #faq
faq_id_idx = content.find('id="faq"')
assert faq_id_idx != -1, "Cannot find id=faq"
s_faq_end = content.find('</section>', faq_id_idx) + len('</section>')
assert s_faq_end != -1, "Cannot find #faq end"

factsheet_and_faq_full = content[s_fact_start:s_faq_end]

# Build the complete unified #faq section combining all rich questions & specs
unified_faq_section = '''<!-- SECTION 11: DIRECT ANSWERS, SYSTEM SPECIFICATIONS & FAQ (PAGE 10 & AEO HUB) -->
  <section id="faq" class="py-14 sm:py-20 lg:py-24 xl:py-28 bg-brand-surface border-t border-brand-border-light" itemscope itemtype="https://schema.org/FAQPage">
    <div class="max-w-4xl mx-auto px-3.5 sm:px-6 lg:px-8 space-y-8 sm:space-y-12">
      
      <!-- Section Header -->
      <div class="text-center space-y-3">
        <div class="badge-teal" data-i18n="final_eyebrow">DIRECT ANSWERS & SYSTEM SPECIFICATIONS</div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark" data-i18n="final_subtitle">
          Shuru karne se pehle aam sawal aur platform specifications:
        </h2>
        <p class="text-base text-gray-600 max-w-2xl mx-auto">
          Zameeni reality pe aadharit sidhe jawaab, technical formulas aur transparent specifications — koi hidden confusion nahi.
        </p>
      </div>

      <!-- Unified Accordion Container -->
      <div class="space-y-4">

        <!-- CATEGORY DIVIDER 1: PRICING, HOSTING & 5-YEAR ECONOMICS -->
        <div class="pt-2 pb-1 flex items-center gap-2 text-xs font-bold text-brand-gold-dark uppercase tracking-wider">
          <span class="w-2 h-2 rounded-full bg-brand-gold"></span>
          <span>Pricing, Cloud Hosting & Ownership Math</span>
        </div>

        <!-- FAQ 1: Hidden or Recurring Charges -->
        <div class="border-2 border-brand-gold/30 rounded-2xl overflow-hidden shadow-sm bg-white hover-lift transition-all duration-300" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
          <button type="button" class="faq-toggle w-full p-5 sm:p-6 text-left flex justify-between items-center bg-white hover:bg-brand-surface transition" aria-expanded="true">
            <span class="font-extrabold text-gray-900 text-sm sm:text-base flex items-center gap-2" itemprop="name">
              <span class="text-brand-gold font-bold">Q1.</span>
              <span data-i18n="obj_4_q">"One-time payment ke baad koi chhupe hue ya monthly charges hain?"</span>
            </span>
            <svg class="faq-icon w-5 h-5 text-gray-500 transform rotate-180 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-content p-5 sm:p-6 pt-0 text-xs sm:text-sm text-gray-700 leading-relaxed border-t border-gray-100" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
            <div itemprop="text" class="space-y-2">
              <p data-i18n="obj_4_a">
                Bilkul nahi. ₹20,000 ek baar dena hai, software aapka ho gaya. Koi monthly subscription nahi, koi per-tenant fee nahi, koi payment gateway cut nahi.
              </p>
              <p class="text-gray-500 text-xs">
                Standard Indian property SaaS charges ₹1,500/month (totaling ₹54,000 over 3 years and ₹90,000+ over 5 years). With Rentlyo, your net 5-year savings exceed ₹70,000+.
              </p>
            </div>
          </div>
        </div>

        <!-- FAQ 2: Why Cloud Hosting is ₹0 Forever -->
        <div class="border border-gray-200 rounded-2xl overflow-hidden shadow-sm bg-white hover-lift transition-all duration-300" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
          <button type="button" class="faq-toggle w-full p-5 sm:p-6 text-left flex justify-between items-center bg-white hover:bg-brand-surface transition" aria-expanded="false">
            <span class="font-extrabold text-gray-900 text-sm sm:text-base flex items-center gap-2" itemprop="name">
              <span class="text-emerald-600 font-bold">Q2.</span>
              <span>Why is Google cloud hosting ₹0 per month forever? How does it work?</span>
            </span>
            <svg class="faq-icon w-5 h-5 text-gray-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-content p-5 sm:p-6 pt-0 text-xs sm:text-sm text-gray-700 leading-relaxed border-t border-gray-100" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
            <p itemprop="text">
              Rentlyo is engineered on Google Firebase's permanent Spark Tier, which provides 50,000 document reads and 20,000 writes every single day for free. A typical building with 10 to 50 units consumes under 3,000 database operations daily (less than 10% of Google's free quota). Even as your property scales, hosting remains ₹0 with zero server management required.
            </p>
          </div>
        </div>

        <!-- CATEGORY DIVIDER 2: DATA SECURITY & HARDWARE MIGRATION -->
        <div class="pt-4 pb-1 flex items-center gap-2 text-xs font-bold text-brand-teal uppercase tracking-wider">
          <span class="w-2 h-2 rounded-full bg-brand-teal"></span>
          <span>Data Ownership, Security & Device Freedom</span>
        </div>

        <!-- FAQ 3: Data Safety & Private Database -->
        <div class="border-2 border-brand-teal/30 rounded-2xl overflow-hidden shadow-sm bg-white hover-lift transition-all duration-300" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
          <button type="button" class="faq-toggle w-full p-5 sm:p-6 text-left flex justify-between items-center bg-white hover:bg-brand-surface transition" aria-expanded="false">
            <span class="font-extrabold text-gray-900 text-sm sm:text-base flex items-center gap-2" itemprop="name">
              <span class="text-brand-teal font-bold">Q3.</span>
              <span data-i18n="obj_2_q">"Who owns the data? Data safe hai aur kahan store hota hai?"</span>
            </span>
            <svg class="faq-icon w-5 h-5 text-gray-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-content p-5 sm:p-6 pt-0 text-xs sm:text-sm text-gray-700 leading-relaxed border-t border-gray-100" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
            <div itemprop="text" class="space-y-2">
              <p data-i18n="obj_2_a">
                100% safe. Aapka data Google ke secure servers (Firebase Firestore) pe store hota hai — wahi security jo badi banks use karti hain.
              </p>
              <p class="text-gray-500 text-xs">
                Unlike subscription SaaS companies that pool all landlords into a shared database, Rentlyo provisions a strictly private database isolated to your property. Founder Aaryan Gupta or third parties cannot access or mine your tenant or financial records.
              </p>
            </div>
          </div>
        </div>

        <!-- FAQ 4: Non-Technical Landlord & Lost Phone -->
        <div class="border border-gray-200 rounded-2xl overflow-hidden shadow-sm bg-white hover-lift transition-all duration-300" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
          <button type="button" class="faq-toggle w-full p-5 sm:p-6 text-left flex justify-between items-center bg-white hover:bg-brand-surface transition" aria-expanded="false">
            <span class="font-extrabold text-gray-900 text-sm sm:text-base flex items-center gap-2" itemprop="name">
              <span class="text-brand-teal font-bold">Q4.</span>
              <span data-i18n="obj_1_q">"Main technical nahi hoon, phone kho gaya ya naya phone liya to kya hoga?"</span>
            </span>
            <svg class="faq-icon w-5 h-5 text-gray-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-content p-5 sm:p-6 pt-0 text-xs sm:text-sm text-gray-700 leading-relaxed border-t border-gray-100" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
            <div itemprop="text" class="space-y-2">
              <p data-i18n="obj_1_a">
                Haan, bilkul chalega. Sab kuch set-up karke diya jaata hai. Agar WhatsApp chala lete ho, to ye bhi aasaani se chala loge.
              </p>
              <p data-i18n="obj_3_a">
                Phone kho jaane par bhi koi tension nahi — data phone me nahi, cloud pe safe hai. Naye phone pe app download karo, apna number aur 6-digit PIN daalo — poora hisaab 2 second me waapas aa jayega.
              </p>
            </div>
          </div>
        </div>

        <!-- FAQ 5: Offline & Low Internet Connectivity -->
        <div class="border border-gray-200 rounded-2xl overflow-hidden shadow-sm bg-white hover-lift transition-all duration-300" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
          <button type="button" class="faq-toggle w-full p-5 sm:p-6 text-left flex justify-between items-center bg-white hover:bg-brand-surface transition" aria-expanded="false">
            <span class="font-extrabold text-gray-900 text-sm sm:text-base flex items-center gap-2" itemprop="name">
              <span class="text-brand-teal font-bold">Q5.</span>
              <span data-i18n="obj_5_q">"Kya internet ke bina chalega? Weak connectivity me hisaab kaise hoga?"</span>
            </span>
            <svg class="faq-icon w-5 h-5 text-gray-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-content p-5 sm:p-6 pt-0 text-xs sm:text-sm text-gray-700 leading-relaxed border-t border-gray-100" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
            <p itemprop="text" data-i18n="obj_5_a">
              App me basic data cache rehta hai, jisse aap bina internet ke bhi purana hisaab dekh sakte ho. Naya payment record karne ya live sync karne ke liye thoda internet connection zaroori hai.
            </p>
          </div>
        </div>

        <!-- CATEGORY DIVIDER 3: DAILY OPERATIONS, UPI & TENANTS -->
        <div class="pt-4 pb-1 flex items-center gap-2 text-xs font-bold text-amber-800 uppercase tracking-wider">
          <span class="w-2 h-2 rounded-full bg-amber-600"></span>
          <span>Daily Operations, UPI Rails & Tenant Workflows</span>
        </div>

        <!-- FAQ 6: Direct 0% Commission UPI Rails -->
        <div class="border border-gray-200 rounded-2xl overflow-hidden shadow-sm bg-white hover-lift transition-all duration-300" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
          <button type="button" class="faq-toggle w-full p-5 sm:p-6 text-left flex justify-between items-center bg-white hover:bg-brand-surface transition" aria-expanded="false">
            <span class="font-extrabold text-gray-900 text-sm sm:text-base flex items-center gap-2" itemprop="name">
              <span class="text-amber-600 font-bold">Q6.</span>
              <span>How does direct 0% commission UPI payment work?</span>
            </span>
            <svg class="faq-icon w-5 h-5 text-gray-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-content p-5 sm:p-6 pt-0 text-xs sm:text-sm text-gray-700 leading-relaxed border-t border-gray-100" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
            <p itemprop="text">
              Instead of routing funds through a 3rd-party payment gateway that deducts 2% to 3% plus GST on every transaction, Rentlyo utilizes direct NPCI UPI deep-linking (PhonePe, Google Pay, Paytm, BHIM). Rent transfers directly from your tenant's bank account straight into your registered bank account with 0% commission deductions.
            </p>
          </div>
        </div>

        <!-- FAQ 7: Electricity Sub-Meter Billing Formula -->
        <div class="border border-gray-200 rounded-2xl overflow-hidden shadow-sm bg-white hover-lift transition-all duration-300" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
          <button type="button" class="faq-toggle w-full p-5 sm:p-6 text-left flex justify-between items-center bg-white hover:bg-brand-surface transition" aria-expanded="false">
            <span class="font-extrabold text-gray-900 text-sm sm:text-base flex items-center gap-2" itemprop="name">
              <span class="text-amber-600 font-bold">Q7.</span>
              <span>How does electricity & water sub-meter calculation work?</span>
            </span>
            <svg class="faq-icon w-5 h-5 text-gray-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-content p-5 sm:p-6 pt-0 text-xs sm:text-sm text-gray-700 leading-relaxed border-t border-gray-100" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
            <p itemprop="text">
              Rentlyo calculates electric utility bills using the exact mathematical formula: <code class="px-1.5 py-0.5 rounded bg-gray-100 border border-gray-200 font-mono text-[11px] text-brand-dark">(Current kWh - Previous kWh) × Unit Tariff</code>. The system automatically rolls forward previous meter readings, eliminates manual calculation disputes, adds power charges to the live monthly ledger, and dispatches a verified breakdown directly to the tenant's WhatsApp.
            </p>
          </div>
        </div>

        <!-- FAQ 8: Tenant App Compulsion -->
        <div class="border border-gray-200 rounded-2xl overflow-hidden shadow-sm bg-white hover-lift transition-all duration-300" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
          <button type="button" class="faq-toggle w-full p-5 sm:p-6 text-left flex justify-between items-center bg-white hover:bg-brand-surface transition" aria-expanded="false">
            <span class="font-extrabold text-gray-900 text-sm sm:text-base flex items-center gap-2" itemprop="name">
              <span class="text-amber-600 font-bold">Q8.</span>
              <span data-i18n="obj_6_q">"Tenant ko app install karna compulsory hai kya?"</span>
            </span>
            <svg class="faq-icon w-5 h-5 text-gray-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-content p-5 sm:p-6 pt-0 text-xs sm:text-sm text-gray-700 leading-relaxed border-t border-gray-100" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
            <p itemprop="text" data-i18n="obj_6_a">
              Nahi, bilkul nahi! Agar tenant app use nahi karna chahta, to bhi sab chalta hai. Aap unka rent record karo — unhe turant WhatsApp pe professional digital receipt mil jaati hai.
            </p>
          </div>
        </div>

        <!-- FAQ 9: Supported Property Asset Types -->
        <div class="border border-gray-200 rounded-2xl overflow-hidden shadow-sm bg-white hover-lift transition-all duration-300" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
          <button type="button" class="faq-toggle w-full p-5 sm:p-6 text-left flex justify-between items-center bg-white hover:bg-brand-surface transition" aria-expanded="false">
            <span class="font-extrabold text-gray-900 text-sm sm:text-base flex items-center gap-2" itemprop="name">
              <span class="text-purple-600 font-bold">Q9.</span>
              <span>What property categories are supported?</span>
            </span>
            <svg class="faq-icon w-5 h-5 text-gray-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-content p-5 sm:p-6 pt-0 text-xs sm:text-sm text-gray-700 leading-relaxed border-t border-gray-100" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
            <p itemprop="text">
              Rentlyo provides dedicated workflow configurations for: <a href="for-commercial-complex/" class="text-brand-teal font-semibold hover:underline">commercial shopping plazas</a>, <a href="for-shop-owners-market-complex/" class="text-brand-teal font-semibold hover:underline">retail market complexes</a>, <a href="for-pg-hostel-owners/" class="text-brand-teal font-semibold hover:underline">PG & student hostels</a> (with 4-meal mess menus), <a href="for-property-owners/" class="text-brand-teal font-semibold hover:underline">residential apartment buildings</a>, <a href="for-warehouse-godown-owners/" class="text-brand-teal font-semibold hover:underline">warehouses & godowns</a>, <a href="for-coworking-spaces/" class="text-brand-teal font-semibold hover:underline">coworking spaces</a>, <a href="for-society-management/" class="text-brand-teal font-semibold hover:underline">housing societies / RWAs</a>, and mixed-use commercial+residential portfolios.
            </p>
          </div>
        </div>

        <!-- FAQ 10: Founder Warranty, Support & Bug Fixes -->
        <div class="border border-gray-200 rounded-2xl overflow-hidden shadow-sm bg-white hover-lift transition-all duration-300" itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">
          <button type="button" class="faq-toggle w-full p-5 sm:p-6 text-left flex justify-between items-center bg-white hover:bg-brand-surface transition" aria-expanded="false">
            <span class="font-extrabold text-gray-900 text-sm sm:text-base flex items-center gap-2" itemprop="name">
              <span class="text-emerald-700 font-bold">Q10.</span>
              <span>Who develops Rentlyo and guarantees deployment?</span>
            </span>
            <svg class="faq-icon w-5 h-5 text-gray-500 transition-transform duration-200 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
          </button>
          <div class="faq-content p-5 sm:p-6 pt-0 text-xs sm:text-sm text-gray-700 leading-relaxed border-t border-gray-100" itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
            <p itemprop="text">
              Rentlyo was created by software engineer Aaryan Gupta (+91 62056 50368), who is himself a commercial property owner managing Arya Plaza. Every deployment includes custom white-label app compilation with your property branding, a free promotional property website, a verified Google Business listing, 3 months of direct 1-on-1 founder support, and lifetime free fixes for any critical bugs.
            </p>
          </div>
        </div>

      </div>

    </div>
  </section>'''

content = content.replace(factsheet_and_faq_full, unified_faq_section, 1)
print("SUCCESS: Factsheet & FAQ merged into single unified #faq!")

# Clean up redundant APK button in Pricing
old_pricing_apk_btn = '<a href="downloads/rentlyo-admin.apk" download class="btn-secondary py-3.5 px-4 text-xs font-semibold flex items-center justify-center gap-1.5 w-full sm:w-auto">\n            <span>Admin Demo APK</span>\n          </a>'
new_pricing_apk_btn = '<a href="#live-demo" class="btn-secondary py-3.5 px-4 text-xs font-semibold flex items-center justify-center gap-1.5 w-full sm:w-auto">\n            <span>Try Live Demo Online →</span>\n          </a>'

if old_pricing_apk_btn in content:
    content = content.replace(old_pricing_apk_btn, new_pricing_apk_btn, 1)
    print("SUCCESS: Cleaned up Pricing section APK button!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"New index.html length: {len(content)}")
print("ALL MERGES COMPLETED SUCCESSFULLY!")
