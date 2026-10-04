/**
 * Rentlyo Bilingual Translation Engine (English / हिन्दी)
 * Fully aligned with Rentlyo-Brochure.pdf (10 Pages)
 * Founder: Aaryan Gupta (+91 62056 50368 | aaryangupta.pm@gmail.com)
 */

(function () {
  'use strict';

  const translations = {
    en: {
      // Nav & Common CTAs
      "header_nav_features": "Features",
      "header_nav_solutions": "Solutions",
      "header_nav_proof": "Case Study",
      "header_nav_pricing": "Pricing",
      "header_nav_calculator": "Calculator",
      "header_nav_explore": "Explore",
      "header_cta_brochure": "Brochure PDF",
      "header_cta_demo": "Demo APK",
      "header_cta_whatsapp": "WhatsApp",
      "nav_features": "Features",
      "nav_pricing": "Pricing",
      "nav_calculator": "ROI Calculator",
      "nav_demo": "Demo",
      "nav_proof": "Case Study",
      "nav_faq": "FAQ",
      "nav_contact": "Contact",
      "cta_download_demo": "Download Demo APK",
      "cta_download_brochure": "Download Brochure (PDF)",
      "cta_download_brochure_short": "Brochure PDF",
      "cta_whatsapp": "Chat on WhatsApp",
      "cta_see_pricing": "See Launch Pricing",
      "cta_talk_to_dev": "Speak with Founder",
      "top_announcement": "Live verified deployment: Arya Plaza, Munger",
      "top_visit_portal": "Visit live portal →",

      // Hero (Page 1 of Brochure)
      "hero_badge": "One-Time Payment • Lifetime Ownership • Zero Subscriptions",
      "hero_headline": "Don't rent your software. Buy it — forever.",
      "hero_subline": "Two apps. One live ledger. Your rent, security deposits, and utility bills run on autopilot.",
      "hero_feat_onetime": "One-Time Payment",
      "hero_feat_website": "Free Property Website Included",
      "hero_feat_google": "Free Google Business Listing",
      "trust_price": "Launch Price: ₹20,000",
      "trust_no_monthly": "Zero monthly fees",
      "trust_no_server": "Free Firebase Cloud Hosting",
      "trust_live_proof": "Live at Arya Plaza, Munger ↗",
      "hero_brochure_desc": "Official 10-page brochure with feature checklist, transparent pricing, and deployment details.",

      // Page 2: Roz Ki Problem (Daily Pain Points)
      "problem_eyebrow": "DAILY RENTAL PROBLEMS",
      "problem_title": "Running rent on paper registers has become unbearable.",
      "problem_subtitle": "Shops, flats, rooms, or warehouses — whatever you rent out, you face these 4 daily headaches every single month.",
      "problem_stat_num": "2–3 Days",
      "problem_stat_label": "Time spent every single month by a 10–15 unit landlord just chasing rent and following up — month after month, forever.",
      "prob_1_title": "\"I already paid!\"",
      "prob_1_desc": "Nobody has written proof. Two conflicting memories, and an inevitable monthly argument with tenants.",
      "prob_2_title": "Deposit & Advance Confusion",
      "prob_2_desc": "How much advance deposit is left? Nobody knows for sure. Every month requires manual recalculation and tension on move-out.",
      "prob_3_title": "Exhausted Filling Registers",
      "prob_3_desc": "Every rent collection, partial payment, and meter reading — hand-written, re-calculated, and checked repeatedly.",
      "prob_4_title": "Chasing Rent Every Month",
      "prob_4_desc": "Call them. They promise 'tomorrow'. Call again. Neither side has the true live ledger status.",

      // Page 3: The Solution (4 Steps & Live Flow)
      "how_eyebrow": "THE AUTOMATED SOLUTION",
      "how_title": "Two apps. One live ledger. 4 steps — then it runs itself.",
      "how_subtitle": "A fully connected ecosystem that handles every rupee automatically.",
      "arch_owner_label": "Owner App",
      "arch_owner_sub": "Set deal. Confirm payment.",
      "arch_ledger_label": "Live Ledger",
      "arch_ledger_sub": "Every rupee. In one place.",
      "arch_tenant_label": "Tenant App",
      "arch_tenant_sub": "See dues. Report payment.",
      "how_step1_title": "1. Add Tenant & Lease Terms",
      "how_step1_desc": "Unit, rent, deposit, future increase — configured once. Existing tenants can also be onboarded with their complete past history.",
      "how_step2_title": "2. Tenant Receives App",
      "how_step2_desc": "They install the app, set their private 6-digit PIN, and view only their specific lease and payment status.",
      "how_step3_title": "3. Rent Calculates Automatically",
      "how_step3_desc": "Exact amount shows every month — advance deposits adjusted and scheduled escalations applied. You do zero manual math.",
      "how_step4_title": "4. They Pay, You Confirm",
      "how_step4_desc": "Whichever payment mode they choose, tenant reports payment. You approve in one tap. Instant WhatsApp receipt generated.",

      // Page 4: Sab Kuch Shamil Hai (Comprehensive Feature Suite)
      "features_eyebrow": "EVERYTHING IS INCLUDED",
      "features_title": "Whatever a real property needs, everything is built right in.",
      "features_subtitle": "No locked add-ons, no expensive plugins. Designed for real ground realities.",
      "feat_1_title": "Live Dashboard",
      "feat_1_desc": "Real-time visibility over collected rent, outstanding dues, and vacant units across all your buildings.",
      "feat_2_title": "Automated Deposit Tracking",
      "feat_2_desc": "Advance security deposits track and adjust automatically with zero math confusion.",
      "feat_3_title": "Pre-Scheduled Rent Escalations",
      "feat_3_desc": "Set future step-up rent increase dates and percentages right now; they apply automatically on schedule.",
      "feat_4_title": "Commercial + Residential Together",
      "feat_4_desc": "Manage shopping plazas, market complexes, residential flats, and rooms simultaneously.",
      "feat_5_title": "Multi-Unit Tenancy (1 Deal)",
      "feat_5_desc": "Rent multiple physical units (e.g. 2 shops or 1 shop + godown) under a single consolidated tenant deal.",
      "feat_6_title": "Electricity & Water Sub-Meters",
      "feat_6_desc": "Generate custom utility bills with past/current readings and tailored tariff rates per unit.",
      "feat_7_title": "Maintenance, Notices & Gate Passes",
      "feat_7_desc": "Categorized repair workflows, official broadcast notices, and digital entry/exit gate passes.",
      "feat_8_title": "Visitor Logs & PG Mess Menu",
      "feat_8_desc": "Digital visitor entry logging and a weekly 4-meal PG/hostel mess menu published directly to occupants.",
      "feat_9_title": "PDF, Excel & CSV Reports",
      "feat_9_desc": "Complete financial statements, tax ledgers, and tenant summaries downloadable in one tap.",
      "feat_10_title": "6-Digit PIN & Bilingual Toggle",
      "feat_10_desc": "Bank-grade PIN security on every device, with complete interface localization in both English and Hindi.",

      // Page 5: Koi Rok-Tok Nahi (Flexible Payments & Devices)
      "flex_eyebrow": "ZERO RESTRICTIONS",
      "flex_title": "Pay however you want. Run on any device.",
      "flex_pay_title": "Accept Any Payment Mode",
      "flex_pay_desc": "UPI, Cash, Cheque, or Bank Transfer — whichever method your tenant prefers, the app records it cleanly. You are never restricted to a single payment gateway.",
      "flex_pay_badges": "UPI • Cash • Cheque • Bank Transfer",
      "flex_device_title": "Works Across All Devices",
      "flex_device_desc": "Run on native Android app or directly via web browser on your computer/laptop. Desktop version included. iPhone users can use the complete web portal — zero need for costly yearly App Store fees.",
      "flex_device_badges": "Android • Web Browser • Desktop PC • iPhone (via Web)",
      "flex_barrier_title": "0 Barriers • 0 Gateway Commission",
      "flex_barrier_desc": "Zero payment gateway transaction deductions, zero single-device lock-in. The way you already operate, just digitized effortlessly.",

      // Page 6: Khud Dekho, Vishwas Karo (Live Demo Verifiable)
      "demo_eyebrow": "SEE IT LIVE, BELIEVE IT",
      "demo_title": "Live demo — open and test yourself right now.",
      "demo_subtitle": "This is not a static mockup. The links below open genuine, working applications running live in the cloud.",
      "demo_admin_label": "ADMIN / OWNER APP",
      "demo_admin_url": "rentlyo-admin.vercel.app →",
      "demo_admin_desc": "Everything the property owner manages — dashboard, tenants, financial ledger, and reports — is live here.",
      "demo_tenant_label": "RENTER / TENANT APP",
      "demo_tenant_url": "rentlyo.vercel.app →",
      "demo_tenant_desc": "What tenants see on their phone — outstanding dues, payment history, and deal summary — is live here.",
      "demo_login_title": "Want a 1-on-1 Personal Live Walkthrough?",
      "demo_login_desc": "Need a personalized demo with data configured for your specific property, commercial complex, or PG? Message founder Aaryan Gupta on WhatsApp for a fast 15-minute live walkthrough.",
      "cta_request_login_whatsapp": "Book 1-on-1 Walkthrough on WhatsApp (+91 62056 50368)",
      "demo_landing_note": "You can also explore our official landing page at rentlyo.cscouncil.in",

      // Page 7: Demo Nahi — Asli Hai (Arya Plaza Real Case Study)
      "proof_eyebrow": "NOT A DEMO — IT'S REAL",
      "proof_title": "Already running in production on a real commercial property.",
      "proof_desc": "Rentlyo wasn't built in a sanitized tech office. It was forged inside an active commercial marketplace, solving daily ground-reality problems.",
      "proof_property_name": "Arya Plaza",
      "proof_property_address": "J.P. Chowk, Purabsarai Road, Munger, Bihar",
      "proof_units_num": "7",
      "proof_units_label": "Commercial Units",
      "proof_ledger_num": "100%",
      "proof_ledger_label": "Digital Ledger",
      "proof_property_summary": "Shops, tenants, deposits, rent escalations, utility sub-meters — everything operates on this exact software every day.",
      "proof_quote": "\"Every feature exists because an actual tenant in a real shop brought a real-life problem that paper registers couldn't solve.\"",
      "proof_pillar_1": "Built by a working software engineer",
      "proof_pillar_2": "Who is himself a commercial property owner",
      "proof_pillar_3": "Battle-tested daily on ground, not in a lab",
      "proof_pillar_4": "See it live in action before paying a single rupee",

      // Page 8: Apna Plan Chuno (All 4 Pricing Plans)
      "pricing_eyebrow": "CHOOSE YOUR PLAN",
      "pricing_title": "Launch pricing. Lock it in right now.",
      "pricing_subtitle": "Introductory prices for early customers. Standard prices shown alongside — these rates will not stay forever.",
      "plan_popular_badge": "MOST POPULAR",
      "plan_portfolio_badge": "BEST FOR LARGE PORTFOLIOS",
      "plan_complete_title": "COMPLETE PACKAGE",
      "plan_complete_std": "Standard ₹35,000",
      "plan_complete_price": "₹20,000",
      "plan_complete_billing": "ONE-TIME · LAUNCH PRICE",
      "plan_complete_f1": "1 property, fully branded app with your name & logo",
      "plan_complete_f2": "Free dedicated website for your property",
      "plan_complete_f3": "Free professional Google Business Profile listing",
      "plan_complete_f4": "3 months active dedicated founder support",
      "plan_complete_f5": "Critical issues — always free fixes for life",

      "plan_multi_title": "MULTI-PROPERTY",
      "plan_multi_std": "Standard ₹50,000",
      "plan_multi_price": "₹35,000",
      "plan_multi_billing": "ONE-TIME · LAUNCH PRICE",
      "plan_multi_f1": "Multiple properties managed inside 1 single app",
      "plan_multi_f2": "Free property website + Google Business listing",
      "plan_multi_f3": "6 months active dedicated founder support",
      "plan_multi_f4": "Critical issues — always free fixes for life",
      "plan_multi_f5": "Best choice for expanding commercial & residential portfolios",

      "plan_software_title": "SOFTWARE ONLY",
      "plan_software_price": "₹19,999",
      "plan_software_billing": "ONE-TIME PAYMENT",
      "plan_software_desc": "1 property, app only — website/Google listing not included. 3 months support + lifetime critical fixes. For owners who only require the mobile apps.",

      "plan_care_title": "MANAGED YEARLY CARE",
      "plan_care_price": "₹10,000/yr",
      "plan_care_billing": "ANNUAL PEACE OF MIND",
      "plan_care_desc": "Multi-property + website + Google listing. Lifetime support, maintenance, and every software upgrade. For owners who want complete, worry-free management.",

      // Page 9: Konfusion Nahi — Sab Saaf & Cloud Hosting Free
      "inc_eyebrow": "NO CONFUSION — 100% TRANSPARENT",
      "inc_title": "Included with Every Single Plan:",
      "inc_f1": "Two apps — Owner Console + Tenant Companion in your brand",
      "inc_f2": "Your logo, property name, and theme colors everywhere",
      "inc_f3": "Your own private, isolated Google Firebase database",
      "inc_f4": "Unlimited tenants — zero per-unit fees",
      "inc_f5": "Every payment method tracked (Cash, UPI, Cheque, Transfer)",
      "inc_f6": "Complete 100% white-glove setup handled by founder",
      "inc_f7": "Personalized 1-on-1 walkthrough and handover call",
      "inc_f8": "Assistance publishing to Play Store / App Store",

      "cloud_title": "With Rentlyo, Cloud Hosting is Also 100% FREE",
      "cloud_desc": "Rentlyo includes cloud database hosting — no separate server, database, or cloud company bills needed. And this does not expire: there is no '3 years free, then paid' gimmick. As long as your portfolio is within the sizes below, it stays free forever.",
      "cloud_r1_num": "150+",
      "cloud_r1_label": "Renters",
      "cloud_r1_sub": "On 1 Property — Completely FREE Forever",
      "cloud_r2_num": "400+",
      "cloud_r2_label": "Renters",
      "cloud_r2_sub": "Across Multi-Property Portfolio — Completely FREE",
      "cloud_scale_desc": "Growing even larger? Zero worries — extra cloud costs are tiny and predictable, typically under ₹100–₹200 per month — far lower than any subscription SaaS software.",

      // Page 10: Shuru Karo Aaj Hi & Objection Handlers
      "final_eyebrow": "START TODAY",
      "final_title": "Your next rent cycle can run itself on autopilot.",
      "final_subtitle": "Common questions before getting started:",
      "obj_1_q": "\"I'm not a technical person, will I be able to run this?\"",
      "obj_1_a": "Yes! Everything is pre-configured and handed over ready to use. If you know how to use WhatsApp, you can easily run Rentlyo.",
      "obj_2_q": "\"Is our financial and tenant data safe?\"",
      "obj_2_a": "Your data resides strictly in your own private cloud account — not with us. 6-digit PIN protected, and each tenant only ever sees their own lease.",
      "obj_3_q": "\"What happens after the support period ends?\"",
      "obj_3_a": "Critical issues are always fixed free for life on every plan. For regular new features and continuous updates, Managed Yearly Care is available.",
      "contact_phone_label": "CALL / WHATSAPP",
      "contact_phone_val": "+91 62056 50368",
      "contact_web_label": "WEBSITE",
      "contact_web_val": "rentlyo.cscouncil.in",
      "contact_demo_label": "LIVE DEMO LOCATION",
      "contact_demo_val": "Arya Plaza, J.P. Chowk, Munger, Bihar",
      "brand_motto": "RENTLYO · SIMPLIFY EVERY RENTAL",

      // Brochure Banner & Download Cards
      "brochure_banner_title": "Download the Complete Rentlyo Brochure",
      "brochure_banner_desc": "Get the official 10-page PDF containing all system workflows, feature checklists, transparent pricing, and deployment details.",
      "brochure_download_cta": "Download Official Brochure (PDF • 2.68 MB)"
    },

    hi: {
      // Nav & Common CTAs
      "header_nav_features": "फीचर्स",
      "header_nav_solutions": "सॉल्यूशंस",
      "header_nav_proof": "केस स्टडी",
      "header_nav_pricing": "कीमत",
      "header_nav_calculator": "कैलकुलेटर",
      "header_nav_explore": "और देखें",
      "header_cta_brochure": "ब्रोशर PDF",
      "header_cta_demo": "डेमो APK",
      "header_cta_whatsapp": "व्हाट्सएप",
      "nav_features": "विशेषताएं",
      "nav_pricing": "कीमत",
      "nav_calculator": "कैलकुलेटर",
      "nav_demo": "डेमो",
      "nav_proof": "केस स्टडी",
      "nav_faq": "सवाल-जवाब",
      "nav_contact": "संपर्क",
      "cta_download_demo": "डेमो APK डाउनलोड करें",
      "cta_download_brochure": "ब्रोशर डाउनलोड करें (PDF)",
      "cta_download_brochure_short": "ब्रोशर PDF",
      "cta_whatsapp": "व्हाट्सएप पर बात करें",
      "cta_see_pricing": "लॉन्च कीमत देखें",
      "cta_talk_to_dev": "आर्यन से बात करें",
      "top_announcement": "लाइव सत्यापित डिप्लॉयमेंट: आर्या प्लाजा, मुंगेर",
      "top_visit_portal": "लाइव पोर्टल देखें →",

      // Hero (Page 1 of Brochure)
      "hero_badge": "एकमुश्त भुगतान • लाइफटाइम मालिकाना हक • शून्य सब्सक्रिप्शन",
      "hero_headline": "Software rent pe mat lo. Khareed lo — hamesha ke liye.",
      "hero_subline": "Do apps. Ek hi live hisaab-kitab. Aapka kiraya, deposit, bill — sab kuch khud-ba-khud sambhlega.",
      "hero_feat_onetime": "Ek baar ka payment",
      "hero_feat_website": "Free website shamil",
      "hero_feat_google": "Free Google listing",
      "trust_price": "लॉन्च कीमत: केवल ₹20,000",
      "trust_no_monthly": "कोई मासिक किराया नहीं",
      "trust_no_server": "फ्री फायरबेस क्लाउड होस्टिंग",
      "trust_live_proof": "आर्या प्लाजा, मुंगेर में लाइव ↗",
      "hero_brochure_desc": "ऑफिशियल 10-पेज का ब्रोशर जिसमें सभी फीचर्स, पारदर्शी कीमतें और डिप्लॉयमेंट विवरण शामिल हैं।",

      // Page 2: Roz Ki Problem (Daily Pain Points)
      "problem_eyebrow": "ROZ KI PROBLEM",
      "problem_title": "Register pe kiraya chalana, ab bahut mushkil ho gaya hai.",
      "problem_subtitle": "Shop ho, flat ho, room ho ya godown — jo bhi kiraye pe dete ho, ye 4 problem aapko bhi roz face karni padti hai.",
      "problem_stat_num": "2–3 din",
      "problem_stat_label": "10-15 unit wale owner ka itna time jaata hai sirf kiraya follow-up me — har mahine, hamesha.",
      "prob_1_title": "\"Maine to de diya tha\"",
      "prob_1_desc": "Kisi ke paas likha hua proof nahi. Do alag yaadein, aur mahine me ek baar jhagda.",
      "prob_2_title": "Deposit ka hisaab gadbad",
      "prob_2_desc": "Kitna advance bacha hai — koi pakka nahi bata sakta. Har baar hath se jodna padta hai aur khali karte samay vivaad hota hai.",
      "prob_3_title": "Register bharte-bharte thak gaye",
      "prob_3_desc": "Har kiraya, har part-payment, har reading — hath se likho, phir se check karo.",
      "prob_4_title": "Har mahine peeche bhaagna",
      "prob_4_desc": "Call karo. Wo bolein \"kal de denge.\" Phir call karo. Kisi ko sahi status pata hi nahi.",

      // Page 3: The Solution (4 Steps & Live Flow)
      "how_eyebrow": "S O L U T I O N",
      "how_title": "Do apps. Ek live hisaab. 4 step — phir khud chalta hai.",
      "how_subtitle": "Ek poora ecosystem jo har rupaye ka hisaab khud rakhta hai.",
      "arch_owner_label": "Owner App",
      "arch_owner_sub": "Deal set karo. Payment confirm karo.",
      "arch_ledger_label": "Live Hisaab",
      "arch_ledger_sub": "Har rupaya. Ek hi jagah.",
      "arch_tenant_label": "Tenant App",
      "arch_tenant_sub": "Kitna due hai, dekho. Payment report karo.",
      "how_step1_title": "1. Tenant add karo",
      "how_step1_desc": "Unit, rent, deposit, future increase — ek baar me. Purane tenant bhi, poori history ke saath.",
      "how_step2_title": "2. Tenant ko app milta hai",
      "how_step2_desc": "Wo app kholke 6-digit PIN set karte hain, aur sirf apna hi lease dekhte hain.",
      "how_step3_title": "3. Rent khud calculate hota hai",
      "how_step3_desc": "Har mahine sahi amount dikhta hai — deposit adjust, increase apply. Aapko kuch nahi karna.",
      "how_step4_title": "4. Wo pay karein, aap confirm karo",
      "how_step4_desc": "Jo bhi tarika ho, tenant pay karke report kare. Aap tap karke approve karo. WhatsApp pe receipt.",

      // Page 4: Sab Kuch Shamil Hai (Comprehensive Feature Suite)
      "features_eyebrow": "SAB KUCH SHAMIL HAI",
      "features_title": "Jo bhi ek real property ko chahiye, sab yahan hai.",
      "features_subtitle": "Koi locked feature nahi, koi mehanga plugin nahi. Zameeni zaroorato ke liye tayyar.",
      "feat_1_title": "Live Dashboard",
      "feat_1_desc": "Due amount, collection status aur khaali units ka live status ek nazar me.",
      "feat_2_title": "Deposit Tracking",
      "feat_2_desc": "Security deposit aur advance khud-ba-khud adjust hota hai — hisaab me zero gadbad.",
      "feat_3_title": "Future Rent Increase",
      "feat_3_desc": "Aane wale saalon ki kiraya vriddhi abhi se set karo; date aate hi khud apply ho jayegi.",
      "feat_4_title": "Commercial + Residential Ek Saath",
      "feat_4_desc": "Dukanein, commercial market complexes, residential flats aur rooms sab ek hi app se manage karein.",
      "feat_5_title": "Ek Lease, Kai Units (Multi-Unit)",
      "feat_5_desc": "Ek hi tenant deal me kai physical units (jaise 2 dukaan ya 1 dukaan + 1 godown) ko jodein.",
      "feat_6_title": "Bijli-Paani Sub-Meter Bill",
      "feat_6_desc": "Previous aur current reading daalkar customized unit tariff ke sath automatic bill banayein.",
      "feat_7_title": "Maintenance, Notice & Gate Pass",
      "feat_7_desc": "Shikayat nivaran workflow, digital notices aur outpass/visitor gate pass ka suvidhajanak prabandh.",
      "feat_8_title": "Visitor Log & PG Mess Menu",
      "feat_8_desc": "Digital aagantuk log aur PG/hostel ka 4-meal weekly bhojan menu seedhe app me publish karein.",
      "feat_9_title": "PDF, Excel & CSV Reports",
      "feat_9_desc": "Full ledger financial statement aur audit reports ek tap me PDF, Excel aur CSV me download karein.",
      "feat_10_title": "6-Digit PIN Lock (English & Hindi)",
      "feat_10_desc": "Har user ke liye 6-digit PIN lock security aur 100% English aur Hindi bhasha toggle.",

      // Page 5: Koi Rok-Tok Nahi (Flexible Payments & Devices)
      "flex_eyebrow": "KOI ROK-TOK NAHI",
      "flex_title": "Jaise chaho pay karo. Jis bhi device pe chalao.",
      "flex_pay_title": "Kaise Bhi Pay Karo",
      "flex_pay_desc": "UPI ho, cash ho, cheque ho, bank transfer ho — tenant jo bhi tarika use kare, app sab record kar leta hai. Kisi ek hi payment method pe atke nahi rehna.",
      "flex_pay_badges": "UPI • Cash • Cheque • Bank Transfer",
      "flex_device_title": "Kisi Bhi Device Pe",
      "flex_device_desc": "Android app pe chalao, ya seedha web browser se (computer/laptop). Desktop version bhi milta hai. iPhone wale bhi web version se poora use kar sakte hain — App Store ki yearly fees ki zaroorat hi nahi.",
      "flex_device_badges": "Android • Web Browser • Desktop PC • iPhone (via Web)",
      "flex_barrier_title": "0 Barrier • 0 Payment Gateway Cut",
      "flex_barrier_desc": "Koi payment gateway fees nahi, koi ek device tak limited nahi. Jaise aap already kaam karte ho, bas wahi digital ho jaata hai.",

      // Page 6: Khud Dekho, Vishwas Karo (Live Demo Verifiable)
      "demo_eyebrow": "KHUD DEKHO, VISHWAS KARO",
      "demo_title": "Live demo — abhi khol ke khud check karo.",
      "demo_subtitle": "Ye koi mockup nahi hai. Neeche diye gaye links pe seedha asli, chalta hua app hai.",
      "demo_admin_label": "ADMIN / OWNER APP",
      "demo_admin_url": "rentlyo-admin.vercel.app →",
      "demo_admin_desc": "Owner jo kuch bhi manage karta hai — dashboard, tenants, ledger, reports — sab yahan live hai.",
      "demo_tenant_label": "RENTER / TENANT APP",
      "demo_tenant_url": "rentlyo.vercel.app →",
      "demo_tenant_desc": "Tenant jo apne phone pe dekhta hai — dues, history, deal summary — wahi yahan bhi hai.",
      "demo_login_title": "Personal 1-on-1 Guided Walkthrough Chahiye?",
      "demo_login_desc": "Apni property, complex ya PG ke hisaab se customized demo ya 1-on-1 walkthrough chahiye? Ek WhatsApp message bhejiye — founder Aaryan Gupta aapko 15 minute me live setup dikhayenge.",
      "cta_request_login_whatsapp": "WhatsApp pe Guided Walkthrough Maango (+91 62056 50368)",
      "demo_landing_note": "Aap product landing page bhi dekh sakte hain: rentlyo.cscouncil.in",

      // Page 7: Demo Nahi — Asli Hai (Arya Plaza Real Case Study)
      "proof_eyebrow": "DEMO NAHI — ASLI HAI",
      "proof_title": "Pehle se ek real property pe chal raha hai.",
      "proof_desc": "Rentlyo office me nahi, ek asli commercial market ke andar banaya gaya — roz ki real problems solve karte hue.",
      "proof_property_name": "Arya Plaza",
      "proof_property_address": "J.P. Chowk, Purabsarai Road, Munger, Bihar",
      "proof_units_num": "7",
      "proof_units_label": "Commercial Units",
      "proof_ledger_num": "100%",
      "proof_ledger_label": "Digital Hisaab",
      "proof_property_summary": "Shops, tenants, deposit, rent increase, utility bill — sab is exact software pe, roz chalta hai.",
      "proof_quote": "\"Har feature isliye bana kyunki ek real tenant, ek real dukaan me, ek aisi problem laaya jo register se solve nahi hoti thi.\"",
      "proof_pillar_1": "Ek working software engineer ne banaya",
      "proof_pillar_2": "Jo khud bhi property owner hai",
      "proof_pillar_3": "Roz test hota hai, sirf lab me nahi",
      "proof_pillar_4": "Pay karne se pehle khud chalta dekho",

      // Page 8: Apna Plan Chuno (All 4 Pricing Plans)
      "pricing_eyebrow": "APNA PLAN CHUNO",
      "pricing_title": "Launch pricing. Abhi lock karo.",
      "pricing_subtitle": "Early customers ke liye shuruaati price. Standard price saath me dikhaya hai — ye rate hamesha nahi rahega.",
      "plan_popular_badge": "SABSE PASANDEEDA",
      "plan_portfolio_badge": "BADE PORTFOLIO KE LIYE BEST",
      "plan_complete_title": "COMPLETE PACKAGE",
      "plan_complete_std": "Standard ₹35,000",
      "plan_complete_price": "₹20,000",
      "plan_complete_billing": "EK BAAR · LAUNCH PRICE",
      "plan_complete_f1": "1 property, aapke naam/brand ke saath app",
      "plan_complete_f2": "Free website aapki property ke liye",
      "plan_complete_f3": "Free professional Google listing",
      "plan_complete_f4": "3 mahine active support",
      "plan_complete_f5": "Critical issue — hamesha free fix",

      "plan_multi_title": "MULTI-PROPERTY",
      "plan_multi_std": "Standard ₹50,000",
      "plan_multi_price": "₹35,000",
      "plan_multi_billing": "EK BAAR · LAUNCH PRICE",
      "plan_multi_f1": "Kai properties, ek hi app",
      "plan_multi_f2": "Free website + Google listing",
      "plan_multi_f3": "6 mahine active support",
      "plan_multi_f4": "Critical issue — hamesha free fix",
      "plan_multi_f5": "Bade portfolio ke liye sabse behtar vikalp",

      "plan_software_title": "SOFTWARE ONLY",
      "plan_software_price": "₹19,999",
      "plan_software_billing": "EK BAAR",
      "plan_software_desc": "1 property, sirf app — website/Google listing nahi. 3 mahine support + lifetime critical-fix. Jo sirf app chahte hain.",

      "plan_care_title": "MANAGED YEARLY CARE",
      "plan_care_price": "₹10,000/yr",
      "plan_care_billing": "HAR SAAL · TENSION-FREE",
      "plan_care_desc": "Multi-property + website + Google listing. Lifetime support, maintenance, har update. Jo tension-free rehna chahte hain.",

      // Page 9: Konfusion Nahi — Sab Saaf & Cloud Hosting Free
      "inc_eyebrow": "KONFUSION NAHI — SAB SAAF",
      "inc_title": "Har plan me ye sab milta hai:",
      "inc_f1": "Do apps — Owner + Tenant, aapke brand me",
      "inc_f2": "Aapka logo, naam, colours — har jagah",
      "inc_f3": "Aapka apna private database",
      "inc_f4": "Unlimited tenants — koi prati-flat fees nahi",
      "inc_f5": "Har payment method track hoti hai (Cash, UPI, Cheque, Transfer)",
      "inc_f6": "Poora setup humari taraf se",
      "inc_f7": "Training aur handover call",
      "inc_f8": "Play Store/App Store pe bhi publish karne me madad",

      "cloud_title": "Rentlyo Ke Saath, Cloud Hosting Bhi FREE Hai",
      "cloud_desc": "Rentlyo me cloud hosting shamil hai — kisi alag server, database ya hosting company ki zaroorat nahi. Aur ye time ke saath khatam nahi hoti — \"3 saal free, fir band\" jaisi koi cheez nahi hai. Jab tak aapka portfolio neeche diye size ke andar hai, hamesha ke liye free rehta hai.",
      "cloud_r1_num": "150+",
      "cloud_r1_label": "Renters",
      "cloud_r1_sub": "Ek property pe — bilkul FREE",
      "cloud_r2_num": "400+",
      "cloud_r2_label": "Renters",
      "cloud_r2_sub": "Multi-property portfolio me — bilkul FREE",
      "cloud_scale_desc": "Isse bhi bada ho jao? Koi tension nahi — tab bhi extra cost chhota aur predictable hota hai, aksar ₹100-200 per mahina se kam — kisi bhi subscription software se kahi kam.",

      // Page 10: Shuru Karo Aaj Hi & Objection Handlers
      "final_eyebrow": "SHURU KARO AAJ HI",
      "final_title": "Aapka agla rent cycle khud chal sakta hai.",
      "final_subtitle": "Shuru karne se pehle aam sawal:",
      "obj_1_q": "\"Main technical nahi hoon, phir bhi chalega?\"",
      "obj_1_a": "Haan. Sab kuch set-up karke diya jaata hai. WhatsApp chala lete ho? Ye bhi chala loge.",
      "obj_2_q": "\"Data safe hai?\"",
      "obj_2_a": "Aapke apne account me rehta hai — hamare paas nahi. PIN-locked, har tenant sirf apna hi lease dekhta hai.",
      "obj_3_q": "\"Support khatam hone ke baad?\"",
      "obj_3_a": "Critical issues hamesha free fix hote hain, har plan me. Regular updates ke liye Managed Yearly Care best hai.",
      "contact_phone_label": "CALL / WHATSAPP",
      "contact_phone_val": "+91 62056 50368",
      "contact_web_label": "WEBSITE",
      "contact_web_val": "rentlyo.cscouncil.in",
      "contact_demo_label": "LIVE DEMO LOCATION",
      "contact_demo_val": "आर्या प्लाजा, जे.पी. चौक, मुंगेर, बिहार",
      "brand_motto": "RENTLYO · SIMPLIFY EVERY RENTAL",

      // Brochure Banner & Download Cards
      "brochure_banner_title": "संपूर्ण रेंटलीयो ब्रोशर (PDF) डाउनलोड करें",
      "brochure_banner_desc": "ऑफिशियल 10-पेज का PDF डाउनलोड करें जिसमें सभी सिस्टम वर्कफ़्लो, फीचर्स, पारदर्शी मूल्य निर्धारण और डिप्लॉयमेंट विवरण शामिल हैं।",
      "brochure_download_cta": "ऑफिशियल ब्रोशर डाउनलोड करें (PDF • 2.68 MB)"
    }
  };

  let currentLang = localStorage.getItem('rentlyo_lang') || 'en';

  function applyLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('rentlyo_lang', lang);
    document.documentElement.lang = lang;

    const dict = translations[lang] || translations.en;

    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (dict[key]) {
        if (dict[key].includes('<') && dict[key].includes('>')) {
          el.innerHTML = dict[key];
        } else {
          el.textContent = dict[key];
        }
      }
    });

    document.querySelectorAll('.lang-btn').forEach(btn => {
      if (btn.getAttribute('data-lang') === lang) {
        btn.classList.add('bg-brand-teal', 'text-white');
        btn.classList.remove('text-gray-300', 'hover:text-white');
      } else {
        btn.classList.remove('bg-brand-teal', 'text-white');
        btn.classList.add('text-gray-300', 'hover:text-white');
      }
    });

    if (typeof window.recalculateCosts === 'function') {
      window.recalculateCosts();
    }

    if (typeof window.gtagEvent === 'function') {
      window.gtagEvent('language_switch', { language: lang });
    }
  }

  window.setLanguage = applyLanguage;

  document.addEventListener('DOMContentLoaded', () => {
    applyLanguage(currentLang);

    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const lang = btn.getAttribute('data-lang');
        if (lang) {
          applyLanguage(lang);
        }
      });
    });
  });
})();
