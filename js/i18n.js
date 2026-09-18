/**
 * Rentlyo Bilingual Translation Engine (English / हिन्दी)
 * Founder: Aaryan Gupta (+91 62056 50368 | aaryangupta.pm@gmail.com)
 */

(function () {
  'use strict';

  const translations = {
    en: {
      // Nav & Common
      "nav_features": "Features",
      "nav_pricing": "Pricing",
      "nav_calculator": "ROI Calculator",
      "nav_demo": "Demo APK",
      "nav_proof": "Live Proof",
      "nav_founder": "Founder",
      "nav_faq": "FAQ",
      "nav_contact": "Contact",
      "cta_download_demo": "Download Demo APK",
      "cta_whatsapp": "Chat on WhatsApp",
      "cta_see_pricing": "See Pricing",
      "cta_talk_to_dev": "Speak with Founder",

      // Hero
      "hero_badge": "One-Time Purchase • Lifetime Ownership • Zero Subscriptions",
      "hero_headline": "Run your rent on software you own — not a subscription you rent.",
      "hero_subline": "A complete, white-label Android property management platform for owners with 5–50 units. One-time ₹20,000. No monthly fee. No per-tenant fee. Zero server bills.",
      "trust_price": "One-time ₹20,000",
      "trust_no_monthly": "No monthly fee ever",
      "trust_no_server": "Runs on free Firebase tier",
      "trust_live_proof": "Live at Arya Plaza, Munger",

      // Problem
      "problem_eyebrow": "The Real Problem",
      "problem_title": "Why paper registers and monthly SaaS both fail property owners",
      "prob_disputes_title": "Rent & Due Disputes",
      "prob_disputes_desc": "Tenants forget cash payments or misunderstand partial carryovers. Paper registers lack proof, leading to endless arguments.",
      "prob_deposit_title": "Deposit & Advance Confusion",
      "prob_deposit_desc": "Advance top-ups and deductions get mixed into normal rent, causing tense move-out calculations.",
      "prob_saas_title": "The Subscription Trap",
      "prob_saas_desc": "Most apps charge ₹1,500–₹3,000 every single month or per flat. Over 3 years you pay ₹70,000+ for software you never own.",
      "prob_opaque_title": "Zero Tenant Self-Service",
      "prob_opaque_desc": "Tenants repeatedly call to ask 'Kitna baaki hai?' (How much is left?). Neither party has a shared live statement.",

      // How It Works
      "how_eyebrow": "Simple 4-Step Flow",
      "how_title": "How Rentlyo streamlines your rental operations",
      "how_step1_title": "Add Unit & Lease Terms",
      "how_step1_desc": "Set unit name, monthly rent, advance deposit, electricity meter rates, and optional step-up escalation tiers in the Admin Console.",
      "how_step2_title": "Tenant Logs In Privately",
      "how_step2_desc": "Tenant installs their branded Rentlyo app and unlocks with their phone and 6-digit PIN. No complex registration required.",
      "how_step3_title": "Rent Calculates Automatically",
      "how_step3_desc": "The shared rent engine computes dues, advance consumption, utility sub-meters, and overdue carryovers identically in both apps.",
      "how_step4_title": "Instant Confirmation & Ledger",
      "how_step4_desc": "Tenant reports payment with one-tap UPI handoff and WhatsApp receipt. Admin confirms in one tap; ledger balances instantly.",

      // Two Apps
      "apps_eyebrow": "Synchronized Ecosystem",
      "apps_title": "Two focused apps. One shared financial ledger.",
      "tenant_app_label": "Tenant Companion App",
      "admin_app_label": "Owner & Manager Console",

      // Calculator
      "calc_eyebrow": "The Unbeatable Math",
      "calc_title": "Calculate how much you save with one-time ownership",
      "calc_desc": "Compare typical SaaS rental software subscriptions against Rentlyo's flat ₹20,000 lifetime cost.",
      "calc_unit_label": "Number of rental units / shops:",
      "calc_rate_label": "Monthly SaaS subscription quoted:",
      "calc_rate_type_flat": "Flat per month (₹)",
      "calc_rate_type_per_unit": "Per unit / month (₹)",
      "calc_saas_label": "Typical Subscription Cost",
      "calc_rentlyo_label": "Rentlyo One-Time Ownership",
      "calc_1yr": "1 Year",
      "calc_3yr": "3 Years",
      "calc_5yr": "5 Years",
      "calc_rentlyo_flat_text": "₹20,000 (Once and for all)",

      // Founder Guarantee
      "founder_eyebrow": "Built by Aaryan Gupta",
      "founder_title": "Direct Founder Accountability & Guarantee",
      "founder_desc": "You are dealing directly with the software engineer who designed and built Rentlyo. Every deployment is personally configured, tested, and handed over with complete source transparency.",

      // Pricing
      "pricing_eyebrow": "Transparent Pricing",
      "pricing_title": "₹20,000 once. Yours for life.",
      "pricing_desc": "No recurring monthly fees. No per-tenant tax. No renewal invoices.",
      "pricing_badge": "Complete White-Label Suite",
      "pricing_what_included": "Everything Included in Your Deployment:",
      "pricing_feat_1": "Both Release APKs (Branded Tenant Companion + Owner Admin Console)",
      "pricing_feat_2": "Full automated white-label deployment configured with your brand & logo",
      "pricing_feat_3": "Firebase cloud configuration (Firestore, Auth, Cloud Messaging)",
      "pricing_feat_4": "Rent calculation engine with advance consumption and utility sub-meters",
      "pricing_feat_5": "One-tap UPI payment handoff + WhatsApp receipt generation",
      "pricing_feat_6": "Digital gate passes, visitor pre-approvals, and maintenance ticketing",
      "pricing_feat_7": "PDF statements, CSV and Excel-compatible exports",
      "pricing_never_charged": "What you will NEVER be charged for:",
      "pricing_never_1": "No monthly or yearly subscription fees",
      "pricing_never_2": "No per-flat, per-room, or per-tenant charges",
      "pricing_never_3": "No cloud server hosting costs (runs on Firebase free tier)",
      "pricing_never_4": "No renewal fees or feature-lock fees",
      "pricing_req_title": "What you need to provide:",
      "pricing_req_text": "An Android phone (for owner & tenants) and a free Google Firebase account (we set this up with you).",
      "pricing_custom_quote": "Managing multiple properties or 50+ units? Contact for a tailored deployment quote.",

      // FAQ
      "faq_eyebrow": "Clear Answers",
      "faq_title": "Frequently Asked Questions",
      "faq_q1": "What happens if you stop supporting the software?",
      "faq_a1": "You retain your installed applications and full control over your Firebase database. Because Rentlyo operates directly on your own Firebase instance and does not route through any intermediary subscription server, your software and rent data will continue to run indefinitely.",
      "faq_q2": "Are there really no monthly server or database bills?",
      "faq_a2": "Yes, zero monthly server bills. Rentlyo is architected entirely on Google Firebase's generous free tier (Spark Plan), which includes 50,000 reads and 20,000 writes every day. For properties with 5 to 50 units, normal daily rent management uses less than 10% of this free quota.",
      "faq_q3": "Do I need technical or coding knowledge to use this?",
      "faq_a3": "No technical knowledge is required. We deliver pre-compiled, branded Android APKs configured with your property name, logo, and payment UPI. You and your tenants simply install the app like any standard Android app and log in with your phone number and 6-digit PIN.",
      "faq_q4": "Can I manage multiple properties?",
      "faq_a4": "Yes. Rentlyo Admin includes built-in multi-property context switching. You can switch between residential apartments, commercial shopping complexes, and PG hostels within the same admin interface without logging out.",
      "faq_q5": "Is my property and tenant financial data safe?",
      "faq_a5": "Yes, your data is protected by Google Firebase infrastructure and battle-tested Firestore security rules. Tenants can only read and modify their own specific lease deal, while owners have protected administrative access enforced by cryptographic role checks.",

      // Final CTA
      "final_cta_title": "Ready to own your property management software?",
      "final_cta_desc": "Download the demo APK, test all features on your phone, or book a live 10-minute walkthrough call with Aaryan before deciding."
    },

    hi: {
      // Nav & Common
      "nav_features": "विशेषताएं",
      "nav_pricing": "कीमत",
      "nav_calculator": "कैलकुलेटर",
      "nav_demo": "डेमो APK",
      "nav_proof": "लाइव सबूत",
      "nav_founder": "निर्माता (Founder)",
      "nav_faq": "सवाल-जवाब",
      "nav_contact": "संपर्क",
      "cta_download_demo": "डेमो APK डाउनलोड करें",
      "cta_whatsapp": "व्हाट्सएप पर बात करें",
      "cta_see_pricing": "कीमत देखें",
      "cta_talk_to_dev": "आर्यन से बात करें",

      // Hero
      "hero_badge": "एकमुश्त भुगतान • लाइफटाइम मालिकाना हक • शून्य सब्सक्रिप्शन",
      "hero_headline": "किराया उस सॉफ्टवेयर पर चलाएं जिसके आप मालिक हैं — हर महीने किराए पर नहीं।",
      "hero_subline": "5 से 50 फ्लैट या दुकान वाले मकान मालिकों के लिए संपूर्ण व्हाइट-लेबल एंड्रॉइड प्रॉपर्टी मैनेजमेंट प्लेटफॉर्म। केवल ₹20,000 एक बार। कोई मासिक शुल्क नहीं। शून्य सर्वर बिल।",
      "trust_price": "एकमुश्त ₹20,000 मात्र",
      "trust_no_monthly": "कोई मासिक किराया नहीं",
      "trust_no_server": "फ्री फायरबेस पर चलता है",
      "trust_live_proof": "आर्या प्लाजा, मुंगेर में लाइव",

      // Problem
      "problem_eyebrow": "असली समस्या",
      "problem_title": "कागजी रजिस्टर और मासिक सब्सक्रिप्शन दोनों मालिकों के लिए नुकसानदेह क्यों हैं",
      "prob_disputes_title": "किराया और बकाए पर विवाद",
      "prob_disputes_desc": "किराएदार नकद भुगतान भूल जाते हैं या पिछले बकाए पर बहस करते हैं। कागजी रजिस्टर में कोई ठोस सबूत नहीं होता।",
      "prob_deposit_title": "एडवांस और सिक्योरिटी में उलझन",
      "prob_deposit_desc": "एडवांस जमा और कटौतियां सामान्य किराए में मिल जाती हैं, जिससे कमरा खाली करते समय तनाव और विवाद होता है।",
      "prob_saas_title": "मासिक सब्सक्रिप्शन का जाल",
      "prob_saas_desc": "अन्य ऐप्स हर महीने ₹1,500–₹3,000 मांगते हैं। 3 साल में आप ₹70,000 से अधिक दे देते हैं, फिर भी सॉफ्टवेयर आपका नहीं होता।",
      "prob_opaque_title": "किराएदारों के बार-बार फोन",
      "prob_opaque_desc": "किराएदार बार-बार फोन करके पूछते हैं 'कितना बकाया है?'। दोनों पक्षों के पास कोई साझा लाइव खाता-बही नहीं होती।",

      // How It Works
      "how_eyebrow": "आसान 4 चरण",
      "how_title": "रेंटलीयो आपके किराए के काम को कैसे आसान बनाता है",
      "how_step1_title": "यूनिट और शर्तें दर्ज करें",
      "how_step1_desc": "एडमिन ऐप में दुकान/फ्लैट का नाम, मासिक किराया, सिक्योरिटी डिपॉजिट, बिजली सब-मीटर दर और किराया वृद्धि दर सेट करें।",
      "how_step2_title": "किराएदार ऐप में लॉग इन करें",
      "how_step2_desc": "किराएदार अपने नाम का ऐप डाउनलोड करते हैं और अपने फोन नंबर व 6-अंकों के सुरक्षित पिन से आसानी से लॉग इन करते हैं।",
      "how_step3_title": "किराया अपने आप कैलकुलेट होता है",
      "how_step3_desc": "रेंटलीयो का सटीक इंजन बकाया, एडवांस एडजस्टमेंट और बिजली बिल दोनों ऐप्स में रीयल-टाइम में एक समान दिखाता है।",
      "how_step4_title": "यूपीआई से भुगतान और तुरंत रसीद",
      "how_step4_desc": "किराएदार 1-क्लिक यूपीआई से भुगतान करके व्हाट्सएप रसीद भेजते हैं। एडमिन 1-टैप में पुष्टि करता है; खाता तुरंत अपडेट होता है।",

      // Two Apps
      "apps_eyebrow": "एक साथ जुड़े 2 ऐप",
      "apps_title": "दो समर्पित ऐप्स। एक साझा खाता-बही।",
      "tenant_app_label": "किराएदार ऐप (Tenant App)",
      "admin_app_label": "मालिक कंसोल (Admin Console)",

      // Calculator
      "calc_eyebrow": "सीधा गणित",
      "calc_title": "कैलकुलेट करें कि एकमुश्त खरीद से आपकी कितनी बचत होगी",
      "calc_desc": "अन्य सॉफ्टवेयर के मासिक सब्सक्रिप्शन की तुलना रेंटलीयो के ₹20,000 लाइफटाइम खर्च से करें।",
      "calc_unit_label": "फ्लैटों / दुकानों की संख्या:",
      "calc_rate_label": "मासिक सब्सक्रिप्शन जो अन्य ऐप्स मांगते हैं:",
      "calc_rate_type_flat": "फ्लैट प्रति माह (₹)",
      "calc_rate_type_per_unit": "प्रति यूनिट / माह (₹)",
      "calc_saas_label": "अन्य ऐप्स का सब्सक्रिप्शन खर्च",
      "calc_rentlyo_label": "रेंटलीयो एकमुश्त मालिकाना हक",
      "calc_1yr": "1 वर्ष",
      "calc_3yr": "3 वर्ष",
      "calc_5yr": "5 वर्ष",
      "calc_rentlyo_flat_text": "₹20,000 (हमेशा के लिए एक बार)",

      // Founder Guarantee
      "founder_eyebrow": "आर्यन गुप्ता द्वारा निर्मित",
      "founder_title": "सीधी संस्थापक जवाबदेही और गारंटी",
      "founder_desc": "आप सीधे उस सॉफ्टवेयर इंजीनियर से जुड़ते हैं जिसने रेंटलीयो बनाया है। हर ऐप सेटअप व्यक्तिगत रूप से कॉन्फ़िगर और परखा जाता है।",

      // Pricing
      "pricing_eyebrow": "स्पष्ट और पारदर्शी कीमत",
      "pricing_title": "₹20,000 केवल एक बार। जीवन भर आपका।",
      "pricing_desc": "कोई मासिक शुल्क नहीं। कोई प्रति-किराएदार टैक्स नहीं। कोई रिन्यूअल इनवॉइस नहीं।",
      "pricing_badge": "पूरा व्हाइट-लेबल सुइट",
      "pricing_what_included": "आपको क्या-क्या मिलेगा:",
      "pricing_feat_1": "दोनों तैयार APK (किराएदार ऐप + मालिक एडमिन कंसोल आपके ब्रांड नाम व लोगो के साथ)",
      "pricing_feat_2": "पूर्ण स्वचालित व्हाइट-लेबल सेटअप (नाम, रंग, आइकन और स्प्लैश स्क्रीन)",
      "pricing_feat_3": "गूगल फायरबेस क्लाउड डेटाबेस और ऑथेंटिकेशन सेटअप",
      "pricing_feat_4": "स्वचालित रेंट इंजन (एडवांस समायोजन और बिजली सब-मीटर बिलिंग सहित)",
      "pricing_feat_5": "वन-टैप UPI पेमेंट और व्हाट्सएप रसीद शेयरिंग",
      "pricing_feat_6": "डिजिटल गेट पास, विजिटर अप्रूवल और शिकायत निवारण सिस्टम",
      "pricing_feat_7": "PDF लेजर स्टेटमेंट, CSV और एक्सेल रिपोर्ट डाउनलोड",
      "pricing_never_charged": "आपसे कभी क्या नहीं लिया जाएगा:",
      "pricing_never_1": "कोई मासिक या वार्षिक रिन्यूअल फीस नहीं",
      "pricing_never_2": "प्रति-फ्लैट या प्रति-किराएदार कोई अतिरिक्त शुल्क नहीं",
      "pricing_never_3": "कोई सर्वर बिल नहीं (फायरबेस के 100% फ्री टियर पर चलता है)",
      "pricing_never_4": "कोई हिडन चार्ज या फीचर लॉक नहीं",
      "pricing_req_title": "आपको क्या चाहिए:",
      "pricing_req_text": "मालिक और किराएदार के पास एक एंड्रॉइड स्मार्टफोन और एक फ्री गूगल फायरबेस खाता (जो हम खुद सेटअप कराते हैं)।",
      "pricing_custom_quote": "50+ यूनिट या कई प्रॉपर्टीज का प्रबंधन कर रहे हैं? विशेष कोटेशन के लिए संपर्क करें।",

      // FAQ
      "faq_eyebrow": "सीधे उत्तर",
      "faq_title": "अक्सर पूछे जाने वाले सवाल",
      "faq_q1": "अगर आप भविष्य में सपोर्ट बंद कर दें तो क्या होगा?",
      "faq_a1": "आपका ऐप और डेटा हमेशा चलता रहेगा क्योंकि यह सीधे आपके खुद के गूगल फायरबेस पर काम करता है, किसी तीसरे पक्ष के सर्वर पर नहीं। आपके ऐप्स स्वतंत्र हैं और कभी बंद नहीं होंगे।",
      "faq_q2": "क्या सच में कोई मासिक सर्वर या डेटाबेस बिल नहीं आता?",
      "faq_a2": "हाँ, बिल्कुल शून्य सर्वर बिल। रेंटलीयो को गूगल फायरबेस के फ्री प्लान (स्पार्क प्लान) पर चलाया जाता है जिसमें प्रतिदिन 50,000 रीड और 20,000 राइट मिलते हैं। 5 से 50 यूनिट की संपत्ति इसका 10% भी इस्तेमाल नहीं कर पाती।",
      "faq_q3": "क्या इसे चलाने के लिए तकनीकी ज्ञान या कोडिंग की जरूरत है?",
      "faq_a3": "बिल्कुल नहीं। हम आपको आपके नाम और लोगो के साथ तैयार मोबाइल ऐप (APK) बनाकर देते हैं। आप और आपके किराएदार इसे किसी भी सामान्य ऐप की तरह आसानी से इस्तेमाल कर सकते हैं।",
      "faq_q4": "क्या मैं एक से अधिक प्रॉपर्टी मैनेज कर सकता हूँ?",
      "faq_a4": "हाँ। रेंटलीयो एडमिन में मल्टी-प्रॉपर्टी स्विचिंग की सुविधा है। आप एक ही ऐप से आवासीय फ्लैट, शॉपिंग कॉम्प्लेक्स और पीजी हॉस्टल को अलग-अलग मैनेज कर सकते हैं।",
      "faq_q5": "क्या मेरा और किराएदार का डेटा पूरी तरह सुरक्षित है?",
      "faq_a5": "हाँ, आपका डेटा गूगल के सुरक्षित क्लाउड और फायरस्टोर रूल्स से सुरक्षित है। किराएदार केवल अपना ही खाता देख सकते हैं, जबकि मालिक के पास 6-अंकों के पिन से सुरक्षित एडमिन अधिकार होते हैं।",

      // Final CTA
      "final_cta_title": "क्या आप अपने प्रॉपर्टी सॉफ्टवेयर के मालिक बनने के लिए तैयार हैं?",
      "final_cta_desc": "डेमो APK डाउनलोड करें, अपने फोन पर चलाकर देखें, या निर्णय लेने से पहले 10 मिनट का लाइव वॉकथ्रू कॉल बुक करें।"
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
        el.textContent = dict[key];
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
