# Google integrations

The site is ready for GA4 and Search Console.

- Set the GA4 Measurement ID (`G-...`) in `assets/config.js`.
- For Search Console HTML-tag verification, add the exact Google-provided `google-site-verification` meta tag to the root landing page/head before production cutover.
- Do not invent or reuse verification tokens from another account.

Tracked conversion events: `whatsapp_submit`, `whatsapp_cta`, `whatsapp_floating`, `phone_cta`, `email_cta`, `directions_cta`.
