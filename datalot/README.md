# SummitLeads vs Datalot / Centerfield Insurance Services

Full battle card (HTML, screenshots embedded) was generated in a Claude.ai chat session on 2026-08-23 and delivered directly to Ariel as a self-contained file — not committed here as a large binary blob to keep this repo lightweight.

Key findings, for reference:
- Datalot rebranded to Centerfield Insurance Services; national insurance demand-gen + carrier distribution, since 2009
- Two-tier architecture: static S3/CloudFront marketing shell + custom PHP lead-intake engine (/consumer/*.php: js.php, init.php, ajax.php, pixels.php, provision_number.php, templates/resume_form.html)
- Headline finding: live TrustedForm TCPA consent certification (api.trustedform.com) — SummitLeads currently only self-attests consent (timestamp+IP), this is the real gap to close before any B2B expansion
- Real defect found: /company.html and /contact-us.html both redirect through to real 404s on centerfield.com (verified full redirect chain)
- Similarweb traffic pull BLOCKED this session — cc-runner-ghonly.yml disabled pending OAuth refresh (see infra notes); apify_api_token confirmed live in vault for this exact purpose, ready once unblocked
- Full martech/adtech stack captured via live Playwright network trace: GTM, multi-property GA4, Google Ads, LinkedIn Ads, ZoomInfo, Rubicon/TTD, Clickagy, VWO, Olark

Honesty Protocol: this card explicitly does NOT claim SummitLeads competes head-to-head with Datalot/Centerfield today — different scale/category. Value is the build reference, especially TCPA tooling.
