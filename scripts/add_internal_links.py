import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add contextual internal links in Feature 4, 5, 7, 8 in Section 4
old_feat_4 = '''          <h3 class="font-bold text-brand-dark text-base" data-i18n="feat_4_title">Commercial + Residential Ek Saath</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed" data-i18n="feat_4_desc">
            Dukanein, commercial market complexes, residential flats aur rooms sab ek hi app se manage karein.
          </p>'''

new_feat_4 = '''          <h3 class="font-bold text-brand-dark text-base" data-i18n="feat_4_title">Commercial + Residential Ek Saath</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
            <a href="for-commercial-complex/" class="text-brand-teal font-semibold hover:underline">Commercial complexes</a>, <a href="for-shop-owners-market-complex/" class="text-brand-teal font-semibold hover:underline">market shops</a>, aur <a href="for-property-owners/" class="text-brand-teal font-semibold hover:underline">residential flats</a> sab ek hi app se manage karein.
          </p>'''

old_feat_5 = '''          <h3 class="font-bold text-brand-dark text-base" data-i18n="feat_5_title">Ek Lease, Kai Units (2 Dukaan, 1 Deal)</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed" data-i18n="feat_5_desc">
            Ek hi tenant deal me kai physical units (jaise 2 dukaan ya 1 dukaan + 1 godown) ko jodein.
          </p>'''

new_feat_5 = '''          <h3 class="font-bold text-brand-dark text-base" data-i18n="feat_5_title">Ek Lease, Kai Units (2 Dukaan, 1 Deal)</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
            Ek hi tenant deal me kai physical units (jaise 2 dukaan ya 1 dukaan + 1 <a href="for-warehouse-godown-owners/" class="text-brand-teal font-semibold hover:underline">godown</a>) ko aasaani se jodein.
          </p>'''

old_feat_7 = '''          <h3 class="font-bold text-brand-dark text-base" data-i18n="feat_7_title">Maintenance, Notice & Gate Pass</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed" data-i18n="feat_7_desc">
            Shikayat nivaran workflow, digital notices aur outpass/visitor gate pass ka suvidhajanak prabandh.
          </p>'''

new_feat_7 = '''          <h3 class="font-bold text-brand-dark text-base" data-i18n="feat_7_title">Maintenance, Notice & Gate Pass</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
            Shikayat nivaran workflow, digital notices aur <a href="for-society-management/" class="text-brand-teal font-semibold hover:underline">society gate pass / visitor log</a> ka suvidhajanak prabandh.
          </p>'''

old_feat_8 = '''          <h3 class="font-bold text-brand-dark text-base" data-i18n="feat_8_title">Visitor Log & PG Mess Menu</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed" data-i18n="feat_8_desc">
            Digital aagantuk log aur PG/hostel ka 4-meal weekly bhojan menu seedhe app me publish karein.
          </p>'''

new_feat_8 = '''          <h3 class="font-bold text-brand-dark text-base" data-i18n="feat_8_title">Visitor Log & PG Mess Menu</h3>
          <p class="text-xs sm:text-sm text-gray-600 leading-relaxed">
            Digital aagantuk log aur <a href="for-pg-hostel-owners/" class="text-brand-teal font-semibold hover:underline">PG & Hostel</a> ka 4-meal weekly bhojan menu seedhe app me publish karein.
          </p>'''

if old_feat_4 in content:
    content = content.replace(old_feat_4, new_feat_4, 1)
if old_feat_5 in content:
    content = content.replace(old_feat_5, new_feat_5, 1)
if old_feat_7 in content:
    content = content.replace(old_feat_7, new_feat_7, 1)
if old_feat_8 in content:
    content = content.replace(old_feat_8, new_feat_8, 1)

# 2. Add Arya Plaza case study link in Section 9
old_proof_btns = '''              <a href="https://aryaplaza.vercel.app/" target="_blank" rel="noopener" class="btn-gold text-xs sm:text-sm py-3 px-5 flex items-center gap-2">
                Visit Arya Plaza Live Portal ↗
              </a>
              <a href="downloads/Rentlyo-Brochure.pdf" download class="btn-outline-white text-xs sm:text-sm py-3 px-5 flex items-center gap-2">
                <svg class="w-4 h-4 text-brand-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                <span data-i18n="cta_download_brochure">Download Brochure (PDF)</span>
              </a>
              <a href="contact/" class="text-white hover:text-brand-gold text-xs sm:text-sm font-semibold underline underline-offset-4 transition">
                Book a Live Walkthrough Call →
              </a>'''

new_proof_btns = '''              <a href="case-study/arya-plaza-munger/" class="btn-gold text-xs sm:text-sm py-3 px-5 flex items-center gap-2 font-bold shadow-md hover:shadow-glow">
                <span>Read Full Case Study Analysis →</span>
              </a>
              <a href="https://aryaplaza.vercel.app/" target="_blank" rel="noopener noreferrer" class="btn-secondary text-xs sm:text-sm py-3 px-5 flex items-center gap-2">
                Visit Arya Plaza Live Portal ↗
              </a>
              <a href="downloads/Rentlyo-Brochure.pdf" download class="btn-outline-white text-xs sm:text-sm py-3 px-5 flex items-center gap-2">
                <svg class="w-4 h-4 text-brand-gold" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                <span data-i18n="cta_download_brochure">Download Brochure (PDF)</span>
              </a>'''

if old_proof_btns in content:
    content = content.replace(old_proof_btns, new_proof_btns, 1)

# 3. Add Section 9.5 (Solutions by Property Type & Internal Linking Hub)
section_9_5_html = '''
  <!-- SECTION 9.5: INDUSTRY VERTICALS & PROPERTY SOLUTIONS HUB (ADVANCED INTERNAL LINKING) -->
  <section id="verticals" class="py-16 sm:py-24 bg-brand-surface border-t border-brand-border-light relative overflow-hidden">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-16">
      
      <!-- Section Header -->
      <div class="text-center max-w-3xl mx-auto space-y-3">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-teal/10 border border-brand-teal/20 text-brand-teal text-xs font-bold uppercase tracking-wider">
          Tailored Architecture for Every Property Asset
        </div>
        <h2 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold text-brand-dark tracking-tight">
          One Engine. Custom Workflows for Your Exact Property.
        </h2>
        <p class="text-sm sm:text-base text-gray-600 max-w-2xl mx-auto">
          Different properties demand entirely different billing and operational rules. Rentlyo is built from the ground up to support commercial plazas, retail markets, student hostels, residential flats, industrial godowns, coworking spaces, and gated societies.
        </p>
      </div>

      <!-- 7 Property Verticals Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

        <!-- Vertical 1: Commercial Shopping Plazas -->
        <div class="p-6 rounded-2xl bg-white border border-brand-border-light shadow-sm hover-lift glass-sheen space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-12 h-12 rounded-xl bg-amber-50 border border-amber-200 text-amber-700 flex items-center justify-center shadow-sm">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
            </div>
            <div>
              <div class="text-[10px] font-bold text-amber-800 uppercase tracking-wider">Commercial Real Estate</div>
              <h3 class="text-lg font-bold text-brand-dark">Commercial Shopping Plazas</h3>
            </div>
            <p class="text-xs text-gray-600 leading-relaxed">
              Consolidated multi-floor shop rosters, individual electricity sub-meters, scheduled 11-month lease escalations, and commercial GST invoices.
            </p>
            <ul class="text-xs text-gray-500 space-y-1.5 pt-1">
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-brand-gold"></span>
                <span>Multi-shop lease bundles (2 shops in 1 deal)</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-brand-gold"></span>
                <span>Commercial power sub-meter formulas</span>
              </li>
            </ul>
          </div>
          <div class="pt-3 border-t border-gray-100">
            <a href="for-commercial-complex/" class="text-xs font-bold text-brand-teal hover:text-brand-gold transition inline-flex items-center gap-1.5">
              <span>Explore Commercial Solution</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
          </div>
        </div>

        <!-- Vertical 2: Market Complexes & Retail Shops -->
        <div class="p-6 rounded-2xl bg-white border border-brand-border-light shadow-sm hover-lift glass-sheen space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-12 h-12 rounded-xl bg-blue-50 border border-blue-200 text-blue-700 flex items-center justify-center shadow-sm">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
            </div>
            <div>
              <div class="text-[10px] font-bold text-blue-700 uppercase tracking-wider">Retail & Wholesale</div>
              <h3 class="text-lg font-bold text-brand-dark">Market Complexes & Shops</h3>
            </div>
            <p class="text-xs text-gray-600 leading-relaxed">
              Fast counter rent collection with dynamic UPI QR codes, daily and monthly transaction ledger, and instant WhatsApp PDF rent receipts for shopkeepers.
            </p>
            <ul class="text-xs text-gray-500 space-y-1.5 pt-1">
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
                <span>Direct UPI collection with zero bank commissions</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>
                <span>Automatic tenant WhatsApp receipt dispatch</span>
              </li>
            </ul>
          </div>
          <div class="pt-3 border-t border-gray-100">
            <a href="for-shop-owners-market-complex/" class="text-xs font-bold text-brand-teal hover:text-brand-gold transition inline-flex items-center gap-1.5">
              <span>Explore Market Complex Solution</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
          </div>
        </div>

        <!-- Vertical 3: PG & Student Hostels -->
        <div class="p-6 rounded-2xl bg-white border border-brand-border-light shadow-sm hover-lift glass-sheen space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-12 h-12 rounded-xl bg-indigo-50 border border-indigo-200 text-indigo-700 flex items-center justify-center shadow-sm">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
            </div>
            <div>
              <div class="text-[10px] font-bold text-indigo-700 uppercase tracking-wider">Hostels & Co-Living</div>
              <h3 class="text-lg font-bold text-brand-dark">PG & Student Hostels</h3>
            </div>
            <p class="text-xs text-gray-600 leading-relaxed">
              Bed-wise & room-wise occupancy tracking, weekly 4-meal mess menu broadcast, digital visitor logs, and automated parent communication.
            </p>
            <ul class="text-xs text-gray-500 space-y-1.5 pt-1">
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-indigo-500"></span>
                <span>Bed-level vacancy & advance deposit ledger</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-indigo-500"></span>
                <span>Integrated digital mess menu & curfew gate pass</span>
              </li>
            </ul>
          </div>
          <div class="pt-3 border-t border-gray-100">
            <a href="for-pg-hostel-owners/" class="text-xs font-bold text-brand-teal hover:text-brand-gold transition inline-flex items-center gap-1.5">
              <span>Explore PG & Hostel Solution</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
          </div>
        </div>

        <!-- Vertical 4: Residential Landlords (Flats) -->
        <div class="p-6 rounded-2xl bg-white border border-brand-border-light shadow-sm hover-lift glass-sheen space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-12 h-12 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-700 flex items-center justify-center shadow-sm">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 14v3m4-3v3m4-3v3M3 21h18M3 10h18M3 7l9-4 9 4M4 10h16v11H4V10z"/></svg>
            </div>
            <div>
              <div class="text-[10px] font-bold text-emerald-700 uppercase tracking-wider">Independent Apartments</div>
              <h3 class="text-lg font-bold text-brand-dark">Residential Landlords (5–50 Flats)</h3>
            </div>
            <p class="text-xs text-gray-600 leading-relaxed">
              Multi-flat portfolio management, Aadhaar tenant KYC vault, monthly society maintenance split, and polite automated rent reminder notices.
            </p>
            <ul class="text-xs text-gray-500 space-y-1.5 pt-1">
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <span>Zero arguments over past deposits or payments</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <span>Dedicated Tenant Companion App for renters</span>
              </li>
            </ul>
          </div>
          <div class="pt-3 border-t border-gray-100">
            <a href="for-property-owners/" class="text-xs font-bold text-brand-teal hover:text-brand-gold transition inline-flex items-center gap-1.5">
              <span>Explore Residential Landlord Solution</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
          </div>
        </div>

        <!-- Vertical 5: Warehouses & Godowns -->
        <div class="p-6 rounded-2xl bg-white border border-brand-border-light shadow-sm hover-lift glass-sheen space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-12 h-12 rounded-xl bg-amber-50 border border-amber-300 text-amber-800 flex items-center justify-center shadow-sm">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/></svg>
            </div>
            <div>
              <div class="text-[10px] font-bold text-amber-800 uppercase tracking-wider">Logistics & Industrial</div>
              <h3 class="text-lg font-bold text-brand-dark">Warehouses & Godowns</h3>
            </div>
            <p class="text-xs text-gray-600 leading-relaxed">
              Square-footage rate tracking, multi-year industrial lease agreements, 3-phase high-voltage power sub-meter billing, and security gate truck registers.
            </p>
            <ul class="text-xs text-gray-500 space-y-1.5 pt-1">
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-600"></span>
                <span>Sq. ft. rate matrix & industrial deposit escrow</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-600"></span>
                <span>Industrial power sub-meter with generator logs</span>
              </li>
            </ul>
          </div>
          <div class="pt-3 border-t border-gray-100">
            <a href="for-warehouse-godown-owners/" class="text-xs font-bold text-brand-teal hover:text-brand-gold transition inline-flex items-center gap-1.5">
              <span>Explore Warehouse Solution</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
          </div>
        </div>

        <!-- Vertical 6: Coworking Spaces -->
        <div class="p-6 rounded-2xl bg-white border border-brand-border-light shadow-sm hover-lift glass-sheen space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="w-12 h-12 rounded-xl bg-purple-50 border border-purple-200 text-purple-700 flex items-center justify-center shadow-sm">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
            </div>
            <div>
              <div class="text-[10px] font-bold text-purple-700 uppercase tracking-wider">Flexible Workspace</div>
              <h3 class="text-lg font-bold text-brand-dark">Coworking Spaces & Desks</h3>
            </div>
            <p class="text-xs text-gray-600 leading-relaxed">
              Hot-desk and private cabin rental passes, conference room booking credits, high-speed Wi-Fi token allocation, and flexible monthly memberships.
            </p>
            <ul class="text-xs text-gray-500 space-y-1.5 pt-1">
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-purple-500"></span>
                <span>Desk-level and team cabin occupancy status</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-purple-500"></span>
                <span>Recurring membership fees with auto invoice</span>
              </li>
            </ul>
          </div>
          <div class="pt-3 border-t border-gray-100">
            <a href="for-coworking-spaces/" class="text-xs font-bold text-brand-teal hover:text-brand-gold transition inline-flex items-center gap-1.5">
              <span>Explore Coworking Solution</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
          </div>
        </div>

        <!-- Vertical 7: Housing Societies & RWAs -->
        <div class="p-6 rounded-2xl bg-white border border-brand-border-light shadow-sm hover-lift glass-sheen space-y-4 flex flex-col justify-between md:col-span-2 lg:col-span-1">
          <div class="space-y-3">
            <div class="w-12 h-12 rounded-xl bg-teal-50 border border-teal-200 text-teal-700 flex items-center justify-center shadow-sm">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
            </div>
            <div>
              <div class="text-[10px] font-bold text-teal-700 uppercase tracking-wider">Gated Communities</div>
              <h3 class="text-lg font-bold text-brand-dark">Housing Societies & RWAs</h3>
            </div>
            <p class="text-xs text-gray-600 leading-relaxed">
              Flat-wise maintenance fee billing, guard gate-pass entry logs, common amenity maintenance fund tracking, and transparent RWA general meetings audit.
            </p>
            <ul class="text-xs text-gray-500 space-y-1.5 pt-1">
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-teal-500"></span>
                <span>Transparent society maintenance ledger</span>
              </li>
              <li class="flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-teal-500"></span>
                <span>Security gate pass & visitor management</span>
              </li>
            </ul>
          </div>
          <div class="pt-3 border-t border-gray-100">
            <a href="for-society-management/" class="text-xs font-bold text-brand-teal hover:text-brand-gold transition inline-flex items-center gap-1.5">
              <span>Explore Society Management</span>
              <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
            </a>
          </div>
        </div>

      </div>

      <!-- Comparison & Knowledge Deep Dive Hub -->
      <div class="p-8 sm:p-10 rounded-3xl bg-white border border-brand-border-light shadow-md space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-gray-100 pb-5">
          <div>
            <div class="text-xs font-bold text-brand-gold uppercase tracking-wider">Independent Analysis & Benchmarks</div>
            <h3 class="text-2xl font-bold text-brand-dark">Compare Rentlyo Against Industry Alternatives</h3>
          </div>
          <a href="downloads/Rentlyo-Brochure.pdf" download class="btn-primary text-xs py-2 px-4 whitespace-nowrap self-start sm:self-auto flex items-center gap-2">
            <svg class="w-3.5 h-3.5 text-brand-gold" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V7.414A2 2 0 0015.414 6L12 2.586A2 2 0 0010.586 2H6zm5 6a1 1 0 10-2 0v3.586l-1.293-1.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V8z" clip-rule="evenodd"/></svg>
            <span>Download 10-Page Brochure</span>
          </a>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <a href="compare/rentlyo-vs-subscription-software/" class="p-5 rounded-2xl bg-brand-surface border border-brand-border-light hover-lift group space-y-2.5">
            <div class="text-xs font-bold text-brand-teal uppercase tracking-wider">Cost Analysis</div>
            <h4 class="text-base font-bold text-brand-dark group-hover:text-brand-teal transition">Rentlyo vs. SaaS Subscriptions →</h4>
            <p class="text-xs text-gray-600 leading-relaxed">
              Why paying ₹1,500/month forever costs ₹54,000+ in 3 years vs. Rentlyo's one-time ₹20,000 lifetime ownership with zero recurring bills.
            </p>
          </a>

          <a href="compare/rentlyo-vs-excel-register/" class="p-5 rounded-2xl bg-brand-surface border border-brand-border-light hover-lift group space-y-2.5">
            <div class="text-xs font-bold text-amber-700 uppercase tracking-wider">Operational Audit</div>
            <h4 class="text-base font-bold text-brand-dark group-hover:text-amber-700 transition">Rentlyo vs. Excel Registers →</h4>
            <p class="text-xs text-gray-600 leading-relaxed">
              Why manual spreadsheets fail at electricity sub-meter calculation, tenant WhatsApp receipts, and deposit dispute proof.
            </p>
          </a>

          <a href="blog/rent-agreement-checklist-indian-landlords/" class="p-5 rounded-2xl bg-brand-surface border border-brand-border-light hover-lift group space-y-2.5">
            <div class="text-xs font-bold text-indigo-700 uppercase tracking-wider">Legal & Compliance</div>
            <h4 class="text-base font-bold text-brand-dark group-hover:text-indigo-700 transition">Rent Agreement Checklist 2026 →</h4>
            <p class="text-xs text-gray-600 leading-relaxed">
              10 mandatory clauses for Indian landlords under the Model Tenancy Act, security deposits, notice periods, and power sub-meters.
            </p>
          </a>
        </div>
      </div>

    </div>
  </section>
'''

section_10_target = '  <!-- SECTION 10: FOUNDER TRUST & ACCOUNTABILITY (MEET AARYAN GUPTA) -->'
if section_10_target in content:
    content = content.replace(section_10_target, section_9_5_html + '\n' + section_10_target, 1)

# 4. Ensure all external links have rel="noopener noreferrer"
content = re.sub(r'target="_blank"\s+rel="noopener"', 'target="_blank" rel="noopener noreferrer"', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully with Section 9.5 and contextual internal linking!")
