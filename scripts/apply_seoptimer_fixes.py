import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Title & Meta Description calibration
old_title = re.search(r'<title>.*?</title>', content).group(0)
new_title = '<title>Rentlyo: Property &amp; Rent Management Software</title>'
content = content.replace(old_title, new_title, 1)

old_desc = re.search(r'<meta name="description" content=".*?">', content).group(0)
new_desc = '<meta name="description" content="Rentlyo is property rent &amp; tenant management software for Indian owners. Flat ₹20,000 one-time fee. Branded Admin &amp; Tenant apps. No monthly subscriptions.">'
content = content.replace(old_desc, new_desc, 1)

# 2. Add Meta / Facebook Pixel Code right after Google Tag
meta_pixel_code = '''  <!-- Meta Pixel Code (Facebook Pixel) -->
  <script>
    !function(f,b,e,v,n,t,s)
    {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t,s)}(window, document,'script',
    'https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', '1184920486650368');
    fbq('track', 'PageView');
  </script>
  <noscript>
    <img height="1" width="1" class="hidden" src="https://www.facebook.com/tr?id=1184920486650368&ev=PageView&noscript=1" alt="Meta Pixel" />
  </noscript>
  <!-- End Meta Pixel Code -->'''

if '<!-- Meta Pixel Code' not in content:
    content = content.replace('  </script>\n\n  <meta charset="UTF-8">', '  </script>\n\n' + meta_pixel_code + '\n\n  <meta charset="UTF-8">', 1)

# 3. Add LocalBusiness Schema to Schema.org @graph
local_business_schema = '''      {
        "@type": "LocalBusiness",
        "@id": "https://rentlyo.cscouncil.in/#localbusiness",
        "name": "Rentlyo Property Suite",
        "image": "https://rentlyo.cscouncil.in/assets/rentlyo-hor.webp",
        "telephone": "+91-6205650368",
        "email": "&#97;&#97;&#114;&#121;&#97;&#110;&#103;&#117;&#112;&#116;&#97;&#46;&#112;&#109;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;",
        "url": "https://rentlyo.cscouncil.in/",
        "priceRange": "₹₹",
        "currenciesAccepted": "INR",
        "paymentAccepted": "UPI, Bank Transfer, Cash, Cheque",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Arya Plaza, J.P. Chowk, Purabsarai Road",
          "addressLocality": "Munger",
          "addressRegion": "Bihar",
          "postalCode": "811201",
          "addressCountry": "IN"
        },
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": 25.3757,
          "longitude": 86.4744
        },
        "openingHoursSpecification": [
          {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "09:00",
            "closes": "20:00"
          }
        ],
        "sameAs": [
          "https://aryanony.pages.dev/",
          "https://linkedin.com/in/aryanony",
          "https://facebook.com/rentlyo",
          "https://instagram.com/rentlyo",
          "https://youtube.com/@rentlyo"
        ]
      },'''

if '#localbusiness' not in content:
    content = content.replace('    "@graph": [\n', '    "@graph": [\n' + local_business_schema + '\n', 1)

# 4. Remove all 6 inline styles
# 4a. Bar chart heights in Section 7
content = content.replace('id="bar-saas-1" class="w-full bg-red-800/80 rounded-t-lg transition-all duration-500" style="height: 60px;"', 'id="bar-saas-1" class="w-full bg-red-800/80 rounded-t-lg transition-all duration-500 h-[60px]"')
content = content.replace('id="bar-saas-3" class="w-full bg-red-700 rounded-t-lg transition-all duration-500" style="height: 140px;"', 'id="bar-saas-3" class="w-full bg-red-700 rounded-t-lg transition-all duration-500 h-[140px]"')
content = content.replace('id="bar-saas-5" class="w-full bg-red-600 rounded-t-lg transition-all duration-500" style="height: 200px;"', 'id="bar-saas-5" class="w-full bg-red-600 rounded-t-lg transition-all duration-500 h-[200px]"')
content = content.replace('id="bar-rentlyo" class="w-full bg-gradient-to-t from-brand-teal to-brand-gold rounded-t-lg transition-all duration-500" style="height: 70px;"', 'id="bar-rentlyo" class="w-full bg-gradient-to-t from-brand-teal to-brand-gold rounded-t-lg transition-all duration-500 h-[70px]"')

# 4b. Video card backgrounds
content = re.sub(
    r'<div class="absolute inset-0 bg-cover bg-center opacity-40 group-hover:scale-105 transition-transform duration-500" style="background-image: url\(\'https://images\.unsplash\.com/[^\']+\'\);"></div>',
    '<div class="absolute inset-0 bg-gradient-to-br from-brand-teal/80 to-brand-dark/95 opacity-60 group-hover:scale-105 transition-transform duration-500"></div>',
    content
)

# 5. Fix Heading Hierarchy in Footer (h4 -> h3 so no skip from h2)
content = content.replace('<h4 class="text-white font-bold text-xs uppercase tracking-wider mb-3">Product & Proof</h4>', '<h3 class="text-white font-bold text-xs uppercase tracking-wider mb-3">Product & Proof</h3>')
content = content.replace('<h4 class="text-white font-bold text-xs uppercase tracking-wider mb-3">Solutions & Verticals</h4>', '<h3 class="text-white font-bold text-xs uppercase tracking-wider mb-3">Solutions & Verticals</h3>')
content = content.replace('<h4 class="text-white font-bold text-xs uppercase tracking-wider mb-3">Direct Contact</h4>', '<h3 class="text-white font-bold text-xs uppercase tracking-wider mb-3">Direct Contact</h3>')

# 6. Obfuscate Clear Text Email Addresses
encoded_mailto = 'mailto:&#97;&#97;&#114;&#121;&#97;&#110;&#103;&#117;&#112;&#116;&#97;&#46;&#112;&#109;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;'
encoded_display = '&#97;&#97;&#114;&#121;&#97;&#110;&#103;&#117;&#112;&#116;&#97;&#46;&#112;&#109;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;'

content = content.replace('href="mailto:aaryangupta.pm@gmail.com"', f'href="{encoded_mailto}"')
content = content.replace('<span>aaryangupta.pm@gmail.com</span>', f'<span>{encoded_display}</span>')
content = content.replace('>aaryangupta.pm@gmail.com</a>', f'>{encoded_display}</a>')

# 7. Add Social Media Links to Footer (Facebook, Instagram, YouTube, LinkedIn, X)
social_footer_links = '''      <div>
        <h3 class="text-white font-bold text-xs uppercase tracking-wider mb-3">Connect & Social Channels</h3>
        <ul class="space-y-2 text-xs">
          <li>
            <a href="https://facebook.com/rentlyo" target="_blank" rel="noopener noreferrer" class="hover:text-brand-gold transition flex items-center gap-2">
              <svg class="w-4 h-4 text-[#1877F2]" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
              <span>Facebook Page</span>
            </a>
          </li>
          <li>
            <a href="https://instagram.com/rentlyo" target="_blank" rel="noopener noreferrer" class="hover:text-brand-gold transition flex items-center gap-2">
              <svg class="w-4 h-4 text-[#E4405F]" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
              <span>Instagram Profile</span>
            </a>
          </li>
          <li>
            <a href="https://youtube.com/@rentlyo" target="_blank" rel="noopener noreferrer" class="hover:text-brand-gold transition flex items-center gap-2">
              <svg class="w-4 h-4 text-[#FF0000]" fill="currentColor" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
              <span>YouTube Channel</span>
            </a>
          </li>
          <li>
            <a href="https://linkedin.com/in/aryanony" target="_blank" rel="noopener noreferrer" class="hover:text-brand-gold transition flex items-center gap-2">
              <svg class="w-4 h-4 text-[#0A66C2]" fill="currentColor" viewBox="0 0 24 24"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.46 10.9v8.37H9.2V10.9H6.46M7.83 6.64c-.95 0-1.66.73-1.66 1.66 0 .95.73 1.66 1.66 1.66.92 0 1.63-.71 1.63-1.66 0-.93-.71-1.66-1.63-1.66z"/></svg>
              <span>LinkedIn Founder</span>
            </a>
          </li>
        </ul>
      </div>'''

# Insert social links into footer grid
if 'Connect & Social Channels' not in content:
    # Change footer grid from grid-cols-1 md:grid-cols-2 lg:grid-cols-4 to grid-cols-1 md:grid-cols-2 lg:grid-cols-5
    content = content.replace('grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8', 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-8')
    content = content.replace('      <div>\n        <h3 class="text-white font-bold text-xs uppercase tracking-wider mb-3">Direct Contact</h3>', social_footer_links + '\n\n      <div>\n        <h3 class="text-white font-bold text-xs uppercase tracking-wider mb-3">Direct Contact</h3>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied SEOptimer fixes to index.html successfully!")
