(() => {
  const nav = document.querySelector('.nav');
  const navLinks = document.querySelector('.nav-links');
  let menuButton = document.querySelector('.menu-btn');

  if (!menuButton && nav && navLinks) {
    menuButton = document.createElement('button');
    menuButton.className = 'menu-btn';
    menuButton.type = 'button';
    menuButton.setAttribute('aria-label', 'Menu');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.textContent = '☰';
    nav.appendChild(menuButton);
  }

  if (menuButton && navLinks) {
    const closeMenu = () => {
      navLinks.classList.remove('open');
      menuButton.setAttribute('aria-expanded', 'false');
      menuButton.textContent = '☰';
    };

    menuButton.addEventListener('click', () => {
      const open = navLinks.classList.toggle('open');
      menuButton.setAttribute('aria-expanded', String(open));
      menuButton.textContent = open ? '×' : '☰';
    });

    navLinks.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') closeMenu();
    });
  }

  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      (entries) => entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      }),
      { threshold: 0.12 }
    );
    document.querySelectorAll('.reveal').forEach((element) => observer.observe(element));
  } else {
    document.querySelectorAll('.reveal').forEach((element) => element.classList.add('visible'));
  }

  window.dataLayer = window.dataLayer || [];
  const cfg = window.TMO_CONFIG || {};

  if (cfg.gaMeasurementId && /^G-[A-Z0-9]+$/i.test(cfg.gaMeasurementId)) {
    const ga = document.createElement('script');
    ga.async = true;
    ga.src = `https://www.googletagmanager.com/gtag/js?id=${encodeURIComponent(cfg.gaMeasurementId)}`;
    document.head.appendChild(ga);
    window.gtag = function gtag() {
      window.dataLayer.push(arguments);
    };
    window.gtag('js', new Date());
    window.gtag('config', cfg.gaMeasurementId, { anonymize_ip: true });
  }

  function track(name, params = {}) {
    window.dataLayer.push({ event: name, ...params });
    if (window.gtag) window.gtag('event', name, params);
  }

  let whatsapp = document.querySelector('.floating-whatsapp, .floating-wa');

  if (whatsapp && whatsapp.classList.contains('floating-wa')) {
    whatsapp.classList.remove('floating-wa');
    whatsapp.classList.add('floating-whatsapp');
    whatsapp.dataset.track = 'whatsapp_floating';
    whatsapp.target = '_blank';
    whatsapp.rel = 'noopener';
    whatsapp.setAttribute('aria-label', 'WhatsApp');
    whatsapp.innerHTML = '<strong>WhatsApp</strong>';
  }

  if (!whatsapp) {
    whatsapp = document.createElement('a');
    whatsapp.className = 'floating-whatsapp';
    whatsapp.dataset.track = 'whatsapp_floating';
    whatsapp.href = 'https://wa.me/972502692223';
    whatsapp.target = '_blank';
    whatsapp.rel = 'noopener';
    whatsapp.setAttribute('aria-label', 'WhatsApp');
    whatsapp.innerHTML = '<strong>WhatsApp</strong>';
    document.body.appendChild(whatsapp);
  }

  document.querySelectorAll('[data-track]').forEach((element) => {
    element.addEventListener('click', () => track(element.dataset.track, { page_path: location.pathname }));
  });

  document.querySelectorAll('a[href^="tel:"]').forEach((element) => {
    if (!element.dataset.track) {
      element.addEventListener('click', () => track('phone_cta', { page_path: location.pathname }));
    }
  });

  document.querySelectorAll('a[href^="mailto:"]').forEach((element) => {
    if (!element.dataset.track) {
      element.addEventListener('click', () => track('email_cta', { page_path: location.pathname }));
    }
  });

  const messages = {
    he: {
      required: 'נא למלא את השדות הנדרשים ולאשר את העברת הפנייה.',
      opening: 'שלום, הגעתי דרך אתר Tomer Moshe & Co.',
      opened: 'WhatsApp נפתח עם הפנייה המוכנה.'
    },
    ru: {
      required: 'Заполните обязательные поля и подтвердите отправку обращения.',
      opening: 'Здравствуйте, я обращаюсь через сайт Tomer Moshe & Co.',
      opened: 'WhatsApp открыт с готовым обращением.'
    },
    en: {
      required: 'Please complete the required fields and confirm submission.',
      opening: 'Hello, I am contacting Tomer Moshe & Co. through the website.',
      opened: 'WhatsApp opened with your prepared enquiry.'
    }
  };

  document.querySelectorAll('[data-whatsapp-form]').forEach((form) => {
    const started = Date.now();

    form.addEventListener('submit', (event) => {
      event.preventDefault();

      const lang = form.dataset.lang || document.documentElement.lang || 'en';
      const copy = messages[lang] || messages.en;
      const status = form.querySelector('.form-status');
      const honeypot = form.elements.website;

      if ((honeypot && honeypot.value) || Date.now() - started < 1200) {
        if (status) status.textContent = '';
        return;
      }

      if (!form.reportValidity()) {
        if (status) status.textContent = copy.required;
        return;
      }

      const name = form.elements.fullName.value.trim();
      const phone = form.elements.phone.value.trim();
      const email = form.elements.email.value.trim();
      const message = form.elements.message.value.trim();

      const nameLabel = lang === 'he' ? 'שם' : lang === 'ru' ? 'Имя' : 'Name';
      const phoneLabel = lang === 'he' ? 'טלפון' : lang === 'ru' ? 'Телефон' : 'Phone';
      const lines = [copy.opening, '', `${nameLabel}: ${name}`, `${phoneLabel}: ${phone}`];

      if (email) lines.push(`Email: ${email}`);
      lines.push('', message);

      const url = `https://wa.me/972502692223?text=${encodeURIComponent(lines.join('\n'))}`;
      track('whatsapp_submit', { page_path: location.pathname, form_language: lang });
      if (status) status.textContent = copy.opened;
      window.open(url, '_blank', 'noopener');
    });
  });
})();
