# DNS & Email Security Configuration (SPF, DMARC, DKIM)

To resolve the **"Without an SPF record, spammers can easily spoof emails"** warning from SEOSiteCheckup, add the following TXT DNS records to your domain DNS management zone (Cloudflare, cPanel, Namecheap, or GoDaddy):

---

### 1. SPF Record (Sender Policy Framework)
- **Record Type:** `TXT`
- **Host / Name:** `@` (or `rentlyo.cscouncil.in` / `cscouncil.in`)
- **TTL:** `Auto` or `3600`
- **Value / Content:**
  ```text
  v=spf1 include:_spf.google.com ~all
  ```
  *(If using your hosting server's default mail agent, use: `v=spf1 +a +mx ~all`)*

---

### 2. DMARC Record (Domain-based Message Authentication)
- **Record Type:** `TXT`
- **Host / Name:** `_dmarc`
- **TTL:** `Auto` or `3600`
- **Value / Content:**
  ```text
  v=DMARC1; p=quarantine; rua=mailto:aaryangupta.pm@gmail.com; pct=100
  ```

---

### 3. Verification
After adding the TXT record, verify it using:
```bash
nslookup -type=TXT rentlyo.cscouncil.in
```
or visit [mxtoolbox.com/spf.aspx](https://mxtoolbox.com/spf.aspx) to confirm the SPF record is active.
