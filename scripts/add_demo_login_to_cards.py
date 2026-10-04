with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the two cards in #live-demo
old_demo_block = '''      <!-- Live Web Demos (Page 6 Links) -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Admin / Owner App Live Card -->
        <div class="p-8 rounded-3xl bg-brand-surface border-2 border-brand-gold/40 shadow-card hover-lift space-y-4">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-brand-teal uppercase tracking-wider" data-i18n="demo_admin_label">ADMIN / OWNER APP</span>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[11px] font-bold">
              <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
              Live Online
            </span>
          </div>
          <h3 class="text-xl sm:text-2xl font-extrabold text-brand-dark">Owner Management Portal</h3>
          <p class="text-sm text-gray-600 leading-relaxed" data-i18n="demo_admin_desc">
            Owner jo kuch bhi manage karta hai — dashboard, tenants, ledger, reports — sab yahan live hai.
          </p>
          <div class="pt-3 flex flex-wrap items-center gap-3">
            <a href="https://rentlyo-admin.vercel.app" target="_blank" rel="noopener noreferrer" class="btn-gold text-xs py-3 px-5 shadow-sm hover:shadow-glow flex items-center gap-1.5 font-bold">
              <span>Open Owner Admin Live</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            </a>
            <a href="downloads/rentlyo-admin.apk" download class="btn-secondary text-xs py-3 px-4 flex items-center gap-1 font-medium">
              <svg class="w-3.5 h-3.5 text-brand-teal" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
              <span>Download Admin APK (36.6 MB)</span>
            </a>
          </div>
          <div class="text-[11px] text-gray-500 font-mono">rentlyo-admin.vercel.app →</div>
        </div>

        <!-- Tenant Companion App Live Card -->
        <div class="p-8 rounded-3xl bg-brand-surface border-2 border-brand-teal/40 shadow-card hover-lift space-y-4">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-brand-gold uppercase tracking-wider" data-i18n="demo_tenant_label">RENTER / TENANT APP</span>
            <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[11px] font-bold">
              <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
              Live Online
            </span>
          </div>
          <h3 class="text-xl sm:text-2xl font-extrabold text-brand-dark">Tenant Self-Service App</h3>
          <p class="text-sm text-gray-600 leading-relaxed" data-i18n="demo_tenant_desc">
            Tenant jo apne phone pe dekhta hai — dues, history, deal summary — wahi yahan bhi hai.
          </p>
          <div class="pt-3 flex flex-wrap items-center gap-3">
            <a href="https://rentlyo.vercel.app" target="_blank" rel="noopener noreferrer" class="btn-primary text-xs py-3 px-5 shadow-sm hover:shadow-md flex items-center gap-1.5 font-bold">
              <span>Open Tenant App Live</span>
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            </a>
            <a href="downloads/rentlyo-tenant.apk" download class="btn-secondary text-xs py-3 px-4 flex items-center gap-1 font-medium">
              <svg class="w-3.5 h-3.5 text-brand-teal" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
              <span>Download Tenant APK (34.3 MB)</span>
            </a>
          </div>
          <div class="text-[11px] text-gray-500 font-mono">rentlyo.vercel.app →</div>
        </div>
      </div>'''

new_demo_block = '''      <!-- Live Web Demos (Page 6 Links) -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <!-- Admin / Owner App Live Card -->
        <div class="p-5 sm:p-6 lg:p-8 rounded-3xl bg-brand-surface border-2 border-brand-gold/40 shadow-card hover-lift space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-brand-teal uppercase tracking-wider" data-i18n="demo_admin_label">ADMIN / OWNER APP</span>
              <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[11px] font-bold">
                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                Live Online
              </span>
            </div>
            <h3 class="text-xl sm:text-2xl font-extrabold text-brand-dark">Owner Management Portal</h3>
            <p class="text-sm text-gray-600 leading-relaxed" data-i18n="demo_admin_desc">
              Owner jo kuch bhi manage karta hai — dashboard, tenants, ledger, reports — sab yahan live hai.
            </p>

            <!-- Demo Login Credentials Box (Matching Screenshot 2) -->
            <div class="p-3.5 bg-white rounded-2xl border border-gray-200 text-xs space-y-2 shadow-sm">
              <div class="font-bold text-gray-900 text-xs flex justify-between items-center">
                <span>Demo Login Credentials:</span>
                <span class="text-[10px] text-emerald-600 font-bold bg-emerald-50 px-2 py-0.5 rounded border border-emerald-200/60">Active</span>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-gray-500 font-medium">Mobile Number:</span>
                <div class="flex items-center gap-1.5">
                  <code class="font-bold font-mono text-brand-teal text-xs">9308489230</code>
                  <button type="button" onclick="navigator.clipboard.writeText('9308489230'); this.innerText='Copied!'; setTimeout(() => this.innerText='Copy', 2000);" class="px-1.5 py-0.5 text-[9px] bg-gray-100 hover:bg-brand-gold hover:text-brand-dark rounded font-semibold transition">Copy</button>
                </div>
              </div>
              <div class="flex justify-between items-center">
                <span class="text-gray-500 font-medium">Password:</span>
                <div class="flex items-center gap-1.5">
                  <code class="font-bold font-mono text-brand-teal text-xs">Rentlyo123</code>
                  <button type="button" onclick="navigator.clipboard.writeText('Rentlyo123'); this.innerText='Copied!'; setTimeout(() => this.innerText='Copy', 2000);" class="px-1.5 py-0.5 text-[9px] bg-gray-100 hover:bg-brand-gold hover:text-brand-dark rounded font-semibold transition">Copy</button>
                </div>
              </div>
              <div class="text-[10px] text-gray-400 pt-0.5 border-t border-gray-100 flex items-center justify-between">
                <span>PIN (if prompted): <code class="bg-gray-100 px-1 py-0.5 rounded text-gray-700 font-mono">123456</code></span>
                <span class="text-gray-400">Sample: Arya Plaza</span>
              </div>
            </div>
          </div>

          <div class="space-y-3 pt-2">
            <div class="flex flex-wrap items-center gap-3">
              <a href="https://rentlyo-admin.vercel.app" target="_blank" rel="noopener noreferrer" class="btn-gold text-xs py-3 px-5 shadow-sm hover:shadow-glow flex items-center gap-1.5 font-bold flex-1 sm:flex-initial justify-center">
                <span>Open Owner Admin Live</span>
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
              </a>
              <a href="downloads/rentlyo-admin.apk" download class="btn-secondary text-xs py-3 px-4 flex items-center gap-1 font-medium flex-1 sm:flex-initial justify-center">
                <svg class="w-3.5 h-3.5 text-brand-teal" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                <span>Download Admin APK (36.6 MB)</span>
              </a>
            </div>
            <div class="text-[11px] text-gray-500 font-mono">rentlyo-admin.vercel.app →</div>
          </div>
        </div>

        <!-- Tenant Companion App Live Card -->
        <div class="p-5 sm:p-6 lg:p-8 rounded-3xl bg-brand-surface border-2 border-brand-teal/40 shadow-card hover-lift space-y-4 flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-brand-gold uppercase tracking-wider" data-i18n="demo_tenant_label">RENTER / TENANT APP</span>
              <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 text-[11px] font-bold">
                <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                Live Online
              </span>
            </div>
            <h3 class="text-xl sm:text-2xl font-extrabold text-brand-dark">Tenant Self-Service App</h3>
            <p class="text-sm text-gray-600 leading-relaxed" data-i18n="demo_tenant_desc">
              Tenant jo apne phone pe dekhta hai — dues, history, deal summary — wahi yahan bhi hai.
            </p>

            <!-- Tenant Access Box (Matching Screenshot 2) -->
            <div class="p-3.5 bg-white rounded-2xl border border-gray-200 text-xs space-y-2 shadow-sm">
              <div class="font-bold text-gray-900 text-xs flex justify-between items-center">
                <span>Tenant Access:</span>
                <span class="text-[10px] text-brand-teal font-bold bg-teal-50 px-2 py-0.5 rounded border border-teal-200/60">Live Sandbox</span>
              </div>
              <p class="text-gray-600 text-[11px] leading-relaxed">
                Log in with credentials generated directly from the Owner Admin Console, or explore pre-loaded demo units for Arya Plaza.
              </p>
              <div class="text-[10px] text-gray-500 pt-1 border-t border-gray-100 flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>
                <span>Instant WhatsApp rent receipts & UPI 0% gateway testable live.</span>
              </div>
            </div>
          </div>

          <div class="space-y-3 pt-2">
            <div class="flex flex-wrap items-center gap-3">
              <a href="https://rentlyo.vercel.app" target="_blank" rel="noopener noreferrer" class="btn-primary text-xs py-3 px-5 shadow-sm hover:shadow-md flex items-center gap-1.5 font-bold flex-1 sm:flex-initial justify-center">
                <span>Open Tenant App Live</span>
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
              </a>
              <a href="downloads/rentlyo-tenant.apk" download class="btn-secondary text-xs py-3 px-4 flex items-center gap-1 font-medium flex-1 sm:flex-initial justify-center">
                <svg class="w-3.5 h-3.5 text-brand-teal" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                <span>Download Tenant APK (34.3 MB)</span>
              </a>
            </div>
            <div class="text-[11px] text-gray-500 font-mono">rentlyo.vercel.app →</div>
          </div>
        </div>
      </div>'''

assert old_demo_block in content, "old_demo_block not found in index.html"
content = content.replace(old_demo_block, new_demo_block, 1)

# Also update the banner below it to personal guided walkthrough
old_banner = '''      <!-- Login Kaise Milega? (Page 6 Direct WhatsApp Callout with bespoke Lock Vector) -->
      <div class="p-8 rounded-3xl bg-amber-50/70 border-2 border-amber-300 shadow-sm flex flex-col md:flex-row items-center justify-between gap-6">
        <div class="space-y-2 text-center md:text-left">
          <div class="inline-flex items-center gap-2 text-amber-900 font-extrabold text-sm uppercase tracking-wider">
            <svg class="w-5 h-5 text-amber-700 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
            <span data-i18n="demo_login_title">Login kaise milega?</span>
          </div>
          <p class="text-sm text-gray-700 leading-relaxed max-w-2xl" data-i18n="demo_login_desc">
            Live login details surakshit rakhne ke liye yahan print nahi kiye — ek WhatsApp message bhejo, turant mil jayenge. Isse aapko hi sabse pehle, personally live demo dikhaya jaa sakta hai.
          </p>
        </div>
        <div class="flex flex-col sm:flex-row gap-3 shrink-0">
          <a href="https://wa.me/916205650368?text=Hello%20Aaryan,%20please%20send%20me%20demo%20login%20details%20for%20Rentlyo." target="_blank" rel="noopener noreferrer" class="btn-gold text-sm py-3 px-6 shadow-glow font-bold flex items-center justify-center gap-2" data-track-event="whatsapp_click" data-track-label="Demo Login Request">
            <svg class="w-4 h-4 fill-current shrink-0" viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0012.04 2zm.01 1.67c2.2 0 4.26.86 5.82 2.41a8.174 8.174 0 012.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.42 0-2.82-.37-4.06-1.07l-.29-.17-3.02.79.81-2.94-.19-.3a8.212 8.212 0 01-1.26-4.36c0-4.54 3.7-8.24 8.24-8.24z"/></svg>
            <span data-i18n="cta_request_login_whatsapp">WhatsApp pe Login Maango (+91 62056 50368)</span>
          </a>
        </div>
      </div>'''

new_banner = '''      <!-- Personal Guided Walkthrough Callout -->
      <div class="p-6 sm:p-8 rounded-3xl bg-amber-50/70 border-2 border-amber-300 shadow-sm flex flex-col md:flex-row items-center justify-between gap-6 hover-lift">
        <div class="space-y-2 text-center md:text-left">
          <div class="inline-flex items-center gap-2 text-amber-900 font-extrabold text-sm uppercase tracking-wider">
            <svg class="w-5 h-5 text-amber-700 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
            <span data-i18n="demo_login_title">Personal 1-on-1 Guided Walkthrough Chahiye?</span>
          </div>
          <p class="text-sm text-gray-700 leading-relaxed max-w-2xl" data-i18n="demo_login_desc">
            Apni property, complex ya PG ke hisaab se customized demo ya 1-on-1 walkthrough chahiye? Ek WhatsApp message bhejiye — founder Aaryan Gupta aapko 15 minute me live setup dikhayenge.
          </p>
        </div>
        <div class="flex flex-col sm:flex-row gap-3 shrink-0 w-full sm:w-auto">
          <a href="https://wa.me/916205650368?text=Hello%20Aaryan,%20can%20you%20give%20me%20a%20personal%20live%20walkthrough%20of%20Rentlyo%20for%20my%20property?" target="_blank" rel="noopener noreferrer" class="btn-gold text-sm py-3 px-6 shadow-glow font-bold flex items-center justify-center gap-2 w-full sm:w-auto" data-track-event="whatsapp_click" data-track-label="Demo Walkthrough Request">
            <svg class="w-4 h-4 fill-current shrink-0" viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0012.04 2zm.01 1.67c2.2 0 4.26.86 5.82 2.41a8.174 8.174 0 012.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.42 0-2.82-.37-4.06-1.07l-.29-.17-3.02.79.81-2.94-.19-.3a8.212 8.212 0 01-1.26-4.36c0-4.54 3.7-8.24 8.24-8.24z"/></svg>
            <span data-i18n="cta_request_login_whatsapp">WhatsApp pe Guided Walkthrough Maango (+91 62056 50368)</span>
          </a>
        </div>
      </div>'''

assert old_banner in content, "old_banner not found in index.html"
content = content.replace(old_banner, new_banner, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html updated successfully!")
