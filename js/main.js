/* ===================================================
   VANLIFE — GLOBAL JS (calm UX, no scroll theatrics)
   =================================================== */

document.addEventListener('DOMContentLoaded', () => {

  /* ---- NAV SCROLL ---- */
  const nav = document.getElementById('nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 60);
    }, { passive: true });
  }

  /* ---- HAMBURGER / MOBILE MENU ---- */
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('open');
      mobileMenu.classList.toggle('open');
      document.body.style.overflow = mobileMenu.classList.contains('open') ? 'hidden' : '';
    });
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('open');
        mobileMenu.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  /* ---- ACTIVE NAV LINK ---- */
  const pathParts = window.location.pathname.split('/').filter(Boolean);
  const currentPage = pathParts[pathParts.length - 1] || 'index.html';
  const inSection = (name) => pathParts.includes(name);

  document.querySelectorAll('.nav-links a').forEach(a => {
    const href = a.getAttribute('href') || '';
    if (href.endsWith(currentPage)) {
      a.classList.add('active');
      return;
    }
    if (href.includes('guides/') && (inSection('guides') || currentPage === 'guides')) {
      a.classList.add('active');
      return;
    }
    if (href.includes('builds/') && inSection('builds')) {
      a.classList.add('active');
      return;
    }
    if (href.includes('blog/') && inSection('blog')) {
      a.classList.add('active');
    }
  });

  /* ---- FAQ ACCORDION ---- */
  document.querySelectorAll('.faq-q').forEach(btn => {
    btn.addEventListener('click', () => {
      const answer = btn.nextElementSibling;
      const isOpen = btn.classList.contains('open');
      document.querySelectorAll('.faq-q.open').forEach(q => {
        q.classList.remove('open');
        if (q.nextElementSibling) q.nextElementSibling.classList.remove('open');
      });
      if (!isOpen && answer) {
        btn.classList.add('open');
        answer.classList.add('open');
      }
    });
  });

  /* ---- SMOOTH ANCHOR SCROLL ---- */
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const hash = a.getAttribute('href');
      if (!hash || hash === '#') return;
      const target = document.querySelector(hash);
      if (!target) return;
      e.preventDefault();
      window.scrollTo({
        top: target.getBoundingClientRect().top + window.scrollY - 80,
        behavior: 'smooth'
      });
    });
  });

  /* ---- BUILD IMAGES ---- */
  document.querySelectorAll('.img-169 img').forEach(img => {
    const wrap = img.closest('.img-169');
    if (!wrap) return;
    const markLoaded = () => {
      if (img.naturalWidth > 0) wrap.classList.add('loaded');
    };
    if (img.complete) markLoaded();
    else img.addEventListener('load', markLoaded, { once: true });
  });

  /* ---- COOKIE CONSENT ---- */
  const banner = document.getElementById('cookie-banner');
  if (banner) {
    const key = 'vanlife_consent';
    if (!localStorage.getItem(key)) {
      banner.hidden = false;
    }
    banner.querySelectorAll('[data-consent]').forEach(btn => {
      btn.addEventListener('click', () => {
        localStorage.setItem(key, btn.getAttribute('data-consent'));
        banner.hidden = true;
      });
    });
  }

  /* ---- CONTACT FORM (Formspree) ---- */
  const form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const btn = form.querySelector('button[type="submit"]');
      if (btn) {
        btn.disabled = true;
        btn.textContent = 'Sending…';
      }
      try {
        const res = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } });
        if (res.ok) {
          const formView = document.getElementById('formView');
          const success = document.getElementById('formSuccess');
          if (formView) formView.style.display = 'none';
          if (success) success.style.display = 'block';
          form.reset();
        } else if (btn) {
          btn.disabled = false;
          btn.textContent = 'Send Message →';
          alert('Something went wrong. Please try again or email us directly.');
        }
      } catch (err) {
        if (btn) {
          btn.disabled = false;
          btn.textContent = 'Send Message →';
        }
        alert('Network error. Please check your connection and try again.');
      }
    });
  }

  /* ---- CHAR COUNT (contact) ---- */
  window.updateCount = function (el) {
    const counter = document.getElementById('charCount');
    if (counter && el) counter.textContent = String(el.value.length);
  };

});
