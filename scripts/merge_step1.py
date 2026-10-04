import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

initial_len = len(content)
print(f"Original index.html character count: {initial_len}")

# ==============================================================================
# MERGE 1: Integrate Payment & Device Flexibility directly into #features, 
# then remove standalone Section 5.
# ==============================================================================

# Find where Feature 10 ends before </div> <!-- end grid --> in #features
# Let's locate Feature 10
feat10_needle = '<!-- Feature 10: 6-Digit PIN Lock -->'
assert feat10_needle in content, "Feature 10 needle not found"

# In Section 5, we have the two columns:
# Column 1: Kaise Bhi Pay Karo (0% Gateway Deductions)
# Column 2: Kisi Bhi Device Pe (Cross-Device Freedom)
# Let's extract them and build a cohesive showcase inside #features.

# Let's inspect the exact Section 5 code to remove it cleanly
sec5_pattern = r'<!-- SECTION 5: KOI ROK-TOK NAHI [^>]*-->\s*<section class="py-12[^"]*bg-brand-surface border-b border-brand-border-light">.*?</section>'
sec5_match = re.search(sec5_pattern, content, re.DOTALL)
assert sec5_match is not None, "Section 5 regex match failed"
sec5_full_text = sec5_match.group(0)

# Build the enhanced flexibility module to embed right below the 10 feature cards in #features
features_flex_addon = '''
      <!-- UNIVERSAL FLEXIBILITY & PLATFORM SUPPORT (Embedded Showcase) -->
      <div class="pt-8 border-t border-brand-border-light">
        <div class="text-center max-w-3xl mx-auto space-y-2 mb-8 sm:mb-10">
          <div class="badge-gold" data-i18n="flex_eyebrow">KOI ROK-TOK NAHI • ZERO RESTRICTIONS</div>
          <h3 class="text-2xl sm:text-3xl font-extrabold text-brand-dark" data-i18n="flex_title">
            Jaise chaho pay karo. Jis bhi device pe chalao.
          </h3>
          <p class="text-xs sm:text-sm text-gray-600 max-w-2xl mx-auto leading-relaxed">
            Zero payment gateway transaction deductions, zero single-device lock-in. The way you already operate, just digitized effortlessly.
          </p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 sm:gap-8">
          <!-- Flexibility Card 1: Universal Payment Rails -->
          <div class="p-6 sm:p-8 rounded-3xl bg-brand-surface border border-brand-border-light shadow-card hover-lift space-y-5 flex flex-col justify-between">
            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <div class="w-12 h-12 rounded-2xl bg-emerald-50 border border-emerald-200 text-emerald-600 flex items-center justify-center shadow-sm">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"/></svg>
                </div>
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-100 text-emerald-800 text-[11px] font-bold">
                  <svg class="w-3.5 h-3.5 text-emerald-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                  0% Gateway Commission
                </span>
              </div>

              <div>
                <h4 class="text-xl font-bold text-brand-dark" data-i18n="flex_pay_title">Kaise Bhi Pay Karo</h4>
                <p class="text-xs sm:text-sm text-gray-600 leading-relaxed mt-1" data-i18n="flex_pay_desc">
                  UPI ho, cash ho, cheque ho, bank transfer ho — tenant jo bhi tarika use kare, app sab record kar leta hai. Kisi ek payment gateway pe atke nahi rehna.
                </p>
              </div>

              <!-- 4 Rails -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 pt-1">
                <div class="p-3 rounded-xl bg-white border border-emerald-200/70 flex items-start gap-2.5">
                  <div class="w-8 h-8 rounded-lg bg-emerald-500 text-white flex items-center justify-center shrink-0 shadow-xs">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                  </div>
                  <div>
                    <div class="text-xs font-bold text-emerald-950">UPI Instant Pay</div>
                    <div class="text-[10px] text-emerald-800 font-medium">GPay • PhonePe • Paytm</div>
                  </div>
                </div>

                <div class="p-3 rounded-xl bg-white border border-amber-200/70 flex items-start gap-2.5">
                  <div class="w-8 h-8 rounded-lg bg-amber-500 text-white flex items-center justify-center shrink-0 shadow-xs">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"/></svg>
                  </div>
                  <div>
                    <div class="text-xs font-bold text-amber-950">Cash (Rokad)</div>
                    <div class="text-[10px] text-amber-800 font-medium">1-Tap WhatsApp Receipt</div>
                  </div>
                </div>

                <div class="p-3 rounded-xl bg-white border border-blue-200/70 flex items-start gap-2.5">
                  <div class="w-8 h-8 rounded-lg bg-blue-500 text-white flex items-center justify-center shrink-0 shadow-xs">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                  </div>
                  <div>
                    <div class="text-xs font-bold text-blue-950">Bank Cheque</div>
                    <div class="text-[10px] text-blue-800 font-medium">Cheque No. & Clearance</div>
                  </div>
                </div>

                <div class="p-3 rounded-xl bg-white border border-purple-200/70 flex items-start gap-2.5">
                  <div class="w-8 h-8 rounded-lg bg-purple-500 text-white flex items-center justify-center shrink-0 shadow-xs">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
                  </div>
                  <div>
                    <div class="text-xs font-bold text-purple-950">Bank Transfer</div>
                    <div class="text-[10px] text-purple-800 font-medium">NEFT / IMPS / RTGS</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Settlement Flow Indicator -->
            <div class="p-3 rounded-xl bg-white border border-gray-200 flex items-center justify-between text-[10px] font-medium text-gray-700">
              <span class="font-bold text-brand-dark">Tenant Pays Any Mode</span>
              <svg class="w-3.5 h-3.5 text-emerald-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              <span class="font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded">100% Direct Bank Settlement</span>
              <svg class="w-3.5 h-3.5 text-emerald-500 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"/></svg>
              <span class="font-bold text-brand-teal">Instant WhatsApp Receipt</span>
            </div>
          </div>

          <!-- Flexibility Card 2: Universal Device Freedom -->
          <div class="p-6 sm:p-8 rounded-3xl bg-brand-surface border border-brand-border-light shadow-card hover-lift space-y-5 flex flex-col justify-between">
            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <div class="w-12 h-12 rounded-2xl bg-brand-teal/10 border border-brand-teal/20 text-brand-teal flex items-center justify-center shadow-sm">
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
                </div>
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-brand-gold/15 text-amber-900 text-[11px] font-bold border border-brand-gold/30">
                  Native Android + Web Portal
                </span>
              </div>

              <div>
                <h4 class="text-xl font-bold text-brand-dark" data-i18n="flex_device_title">Kisi Bhi Device Pe Chalao</h4>
                <p class="text-xs sm:text-sm text-gray-600 leading-relaxed mt-1" data-i18n="flex_device_desc">
                  Android phone pe native app chalao, ya laptop/desktop pe browser se poora hisaab dekho. iPhone users bhi seedha web portal se use kar sakte hain — bina kisi mehenge yearly app store fee ke.
                </p>
              </div>

              <!-- 4 Platforms -->
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 pt-1">
                <div class="p-3 rounded-xl bg-white border border-gray-200 flex items-start gap-2.5">
                  <div class="w-8 h-8 rounded-lg bg-brand-teal text-white flex items-center justify-center shrink-0 shadow-xs">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
                  </div>
                  <div>
                    <div class="text-xs font-bold text-brand-dark">Android App</div>
                    <div class="text-[10px] text-gray-500">Native APK • Offline Tolerant</div>
                  </div>
                </div>

                <div class="p-3 rounded-xl bg-white border border-gray-200 flex items-start gap-2.5">
                  <div class="w-8 h-8 rounded-lg bg-brand-gold text-brand-dark flex items-center justify-center shrink-0 shadow-xs">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
                  </div>
                  <div>
                    <div class="text-xs font-bold text-brand-dark">Desktop PC / Mac</div>
                    <div class="text-[10px] text-gray-500">Web Browser • Full CA Ledger</div>
                  </div>
                </div>

                <div class="p-3 rounded-xl bg-white border border-gray-200 flex items-start gap-2.5">
                  <div class="w-8 h-8 rounded-lg bg-gray-900 text-white flex items-center justify-center shrink-0 shadow-xs">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z"/></svg>
                  </div>
                  <div>
                    <div class="text-xs font-bold text-brand-dark">iPhone & iPad</div>
                    <div class="text-[10px] text-gray-500">Fast Web App • Zero Fee</div>
                  </div>
                </div>

                <div class="p-3 rounded-xl bg-white border border-gray-200 flex items-start gap-2.5">
                  <div class="w-8 h-8 rounded-lg bg-emerald-600 text-white flex items-center justify-center shrink-0 shadow-xs">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4"/></svg>
                  </div>
                  <div>
                    <div class="text-xs font-bold text-brand-dark">Google Cloud Sync</div>
                    <div class="text-[10px] text-gray-500">Real-time Multi-Device Sync</div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Sync Feature Tag -->
            <div class="p-3 rounded-xl bg-white border border-gray-200 flex items-center justify-between text-[10px] font-medium text-gray-700">
              <span class="font-bold text-brand-dark">Single Master Ledger</span>
              <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
              <span class="text-gray-600">Mobile + Web simultaneously updated in 1 second</span>
            </div>
          </div>
        </div>
      </div>
'''

# Find the end of the 10 feature cards grid in #features:
# Look for line with Feature 10 and then the closing </div> of the grid
end_grid_needle = '''            <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg bg-emerald-50 text-emerald-800">
              <svg class="w-3.5 h-3.5 text-emerald-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/></svg>
              <span>Reports & Statements</span>
            </span>
          </div>
        </div>
      </div>'''

assert end_grid_needle in content, "end_grid_needle not found in #features"

# Insert the addon right after the grid
content = content.replace(end_grid_needle, end_grid_needle + '\n' + features_flex_addon, 1)

# Remove standalone Section 5
content = content.replace(sec5_full_text, '', 1)
print("SUCCESS: Merged Section 5 into #features and eliminated standalone Section 5!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
