/**
 * Rentlyo Core Web Client Scripts
 * Handles navigation, sticky mobile CTA, screenshot carousel, FAQ accordion, and analytics events.
 */

(function () {
  'use strict';

  // Analytics Helper
  window.dataLayer = window.dataLayer || [];
  function gtagEvent(eventName, params = {}) {
    window.dataLayer.push({
      event: eventName,
      ...params,
      timestamp: new Date().toISOString()
    });
  }
  window.gtagEvent = gtagEvent;

  // Throttled calculator event
  let calcTimer = null;
  window.logCalculatorUsed = function (units, monthlyCost, savings) {
    clearTimeout(calcTimer);
    calcTimer = setTimeout(() => {
      gtagEvent('calculator_used', {
        units: units,
        monthly_cost: monthlyCost,
        estimated_3yr_savings: savings
      });
    }, 1500);
  };

  document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    if (mobileMenuBtn && mobileMenu) {
      mobileMenuBtn.addEventListener('click', () => {
        const isExpanded = mobileMenuBtn.getAttribute('aria-expanded') === 'true';
        mobileMenuBtn.setAttribute('aria-expanded', !isExpanded);
        mobileMenu.classList.toggle('hidden');
      });

      mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
          mobileMenu.classList.add('hidden');
          mobileMenuBtn.setAttribute('aria-expanded', 'false');
        });
      });
    }

    // 2. Sticky Mobile Bottom Bar
    const heroSection = document.getElementById('hero');
    const stickyBottomBar = document.getElementById('sticky-mobile-bar');
    if (stickyBottomBar && heroSection) {
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach(entry => {
            if (entry.isIntersecting) {
              stickyBottomBar.classList.add('translate-y-full');
              stickyBottomBar.classList.remove('translate-y-0');
            } else {
              stickyBottomBar.classList.remove('translate-y-full');
              stickyBottomBar.classList.add('translate-y-0');
            }
          });
        },
        { rootMargin: '-80px 0px 0px 0px' }
      );
      observer.observe(heroSection);
    }

    // 3. Screenshot Carousel
    const carouselTrack = document.getElementById('carousel-track');
    const prevBtn = document.getElementById('carousel-prev');
    const nextBtn = document.getElementById('carousel-next');
    const dotsContainer = document.getElementById('carousel-dots');

    if (carouselTrack) {
      const slides = carouselTrack.querySelectorAll('.carousel-slide');
      let currentIndex = 0;
      let autoPlayInterval = null;

      // Render Dots
      if (dotsContainer && slides.length > 1) {
        dotsContainer.innerHTML = '';
        slides.forEach((_, idx) => {
          const dot = document.createElement('button');
          dot.className = `w-2.5 h-2.5 rounded-full transition-all duration-300 ${
            idx === 0 ? 'bg-brand-gold w-6' : 'bg-gray-300 hover:bg-gray-400'
          }`;
          dot.setAttribute('aria-label', `Go to screenshot slide ${idx + 1}`);
          dot.addEventListener('click', () => {
            goToSlide(idx);
            resetAutoplay();
          });
          dotsContainer.appendChild(dot);
        });
      }

      function updateDots() {
        if (!dotsContainer) return;
        const dots = dotsContainer.querySelectorAll('button');
        dots.forEach((dot, idx) => {
          if (idx === currentIndex) {
            dot.className = 'w-6 h-2.5 rounded-full transition-all duration-300 bg-brand-gold';
          } else {
            dot.className = 'w-2.5 h-2.5 rounded-full transition-all duration-300 bg-gray-300 hover:bg-gray-400';
          }
        });
      }

      function goToSlide(index) {
        if (index < 0) {
          currentIndex = slides.length - 1;
        } else if (index >= slides.length) {
          currentIndex = 0;
        } else {
          currentIndex = index;
        }

        const offsetPercent = currentIndex * 100;
        carouselTrack.style.transform = `translateX(-${offsetPercent}%)`;
        updateDots();

        gtagEvent('screenshot_carousel_interact', { slide_index: currentIndex });
      }

      if (prevBtn) {
        prevBtn.addEventListener('click', () => {
          goToSlide(currentIndex - 1);
          resetAutoplay();
        });
      }

      if (nextBtn) {
        nextBtn.addEventListener('click', () => {
          goToSlide(currentIndex + 1);
          resetAutoplay();
        });
      }

      // Touch / Swipe support
      let touchStartX = 0;
      let touchEndX = 0;

      carouselTrack.addEventListener('touchstart', (e) => {
        touchStartX = e.changedTouches[0].screenX;
      }, { passive: true });

      carouselTrack.addEventListener('touchend', (e) => {
        touchEndX = e.changedTouches[0].screenX;
        const diff = touchStartX - touchEndX;
        if (Math.abs(diff) > 40) {
          if (diff > 0) {
            goToSlide(currentIndex + 1);
          } else {
            goToSlide(currentIndex - 1);
          }
          resetAutoplay();
        }
      }, { passive: true });

      // Auto-advance
      function startAutoplay() {
        if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
          autoPlayInterval = setInterval(() => {
            goToSlide(currentIndex + 1);
          }, 4500);
        }
      }

      function resetAutoplay() {
        if (autoPlayInterval) {
          clearInterval(autoPlayInterval);
          startAutoplay();
        }
      }

      startAutoplay();
      carouselTrack.parentElement.addEventListener('mouseenter', () => clearInterval(autoPlayInterval));
      carouselTrack.parentElement.addEventListener('mouseleave', startAutoplay);
    }

    // 4. FAQ Accordion
    document.querySelectorAll('.faq-toggle').forEach(button => {
      button.addEventListener('click', () => {
        const isExpanded = button.getAttribute('aria-expanded') === 'true';
        const content = button.nextElementSibling;
        const icon = button.querySelector('.faq-icon');

        // Close other FAQs
        document.querySelectorAll('.faq-toggle').forEach(otherBtn => {
          if (otherBtn !== button) {
            otherBtn.setAttribute('aria-expanded', 'false');
            if (otherBtn.nextElementSibling) {
              otherBtn.nextElementSibling.classList.add('hidden');
            }
            const otherIcon = otherBtn.querySelector('.faq-icon');
            if (otherIcon) {
              otherIcon.style.transform = 'rotate(0deg)';
            }
          }
        });

        // Toggle current
        button.setAttribute('aria-expanded', !isExpanded);
        if (content) {
          content.classList.toggle('hidden');
        }
        if (icon) {
          icon.style.transform = isExpanded ? 'rotate(0deg)' : 'rotate(180deg)';
        }

        if (!isExpanded) {
          const qText = button.querySelector('span')?.textContent || 'FAQ Item';
          gtagEvent('faq_expand', { question: qText });
        }
      });
    });

    // 5. Analytics Link Clicks & Automatic Conversion Tracking
    document.querySelectorAll('a[data-track-event]').forEach(anchor => {
      anchor.addEventListener('click', () => {
        const eventName = anchor.getAttribute('data-track-event');
        const targetLabel = anchor.getAttribute('data-track-label') || anchor.textContent.trim();
        gtagEvent(eventName, { label: targetLabel });
      });
    });

    // Automatic WhatsApp conversion tracking
    document.querySelectorAll('a[href*="wa.me"]').forEach(anchor => {
      if (!anchor.hasAttribute('data-track-event')) {
        anchor.addEventListener('click', () => {
          gtagEvent('whatsapp_click', {
            url: anchor.href,
            label: anchor.textContent.trim() || 'WhatsApp CTA'
          });
        });
      }
    });

    // Automatic APK Download tracking
    document.querySelectorAll('a[href*=".apk"], a[download]').forEach(anchor => {
      if (!anchor.hasAttribute('data-track-event')) {
        anchor.addEventListener('click', () => {
          gtagEvent('apk_download', {
            file: anchor.getAttribute('href'),
            label: anchor.textContent.trim() || 'APK Download'
          });
        });
      }
    });

    // Automatic Tel / Phone Call tracking
    document.querySelectorAll('a[href^="tel:"]').forEach(anchor => {
      anchor.addEventListener('click', () => {
        gtagEvent('phone_call_click', {
          phone_number: anchor.getAttribute('href'),
          label: anchor.textContent.trim() || 'Direct Phone'
        });
      });
    });

    // Automatic Outbound Link tracking
    document.querySelectorAll('a[href^="http"]:not([href*="rentlyo.cscouncil.in"])').forEach(anchor => {
      if (!anchor.href.includes('wa.me') && !anchor.href.includes('localhost')) {
        anchor.addEventListener('click', () => {
          gtagEvent('outbound_click', {
            destination: anchor.href,
            label: anchor.textContent.trim()
          });
        });
      }
    });

    // --------------------------------------------------------------------------
    // Modern Luxury Micro-Interactions & Scroll Effects
    // --------------------------------------------------------------------------
    initScrollReveal();
    initHeaderScroll();
    initCopyMicroInteractions();
    initSmoothCounterAnimation();

    // --------------------------------------------------------------------------
    // Rentlyo High-Performance Brand Loader Controller
    // --------------------------------------------------------------------------
    initRentlyoLoader();
  });

  // 1. Scroll-Triggered Reveal with Zero Lag
  function initScrollReveal() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      document.querySelectorAll('.reveal-init, .reveal-scale-init').forEach(el => el.classList.add('revealed'));
      return;
    }

    const candidateSelectors = [
      '#hero h1',
      '#hero p',
      '#hero .flex-col.sm\\:flex-row',
      '#live-proof .glass-card',
      '#problems .p-6',
      '#features .glass-card',
      '#architecture .bg-brand-dark',
      '#calculator .glass-card',
      '#pricing .glass-card',
      '#founder .glass-card',
      '#faq .glass-card',
      '.hover-lift'
    ];

    candidateSelectors.forEach(sel => {
      document.querySelectorAll(sel).forEach((el, index) => {
        if (!el.classList.contains('reveal-init') && !el.classList.contains('reveal-scale-init')) {
          el.classList.add('reveal-init');
          const delayClass = `delay-${((index % 4) + 1) * 100}`;
          el.classList.add(delayClass);
        }
      });
    });

    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '0px 0px -40px 0px',
      threshold: 0.08
    });

    document.querySelectorAll('.reveal-init, .reveal-scale-init').forEach(el => {
      revealObserver.observe(el);
    });
  }

  // 2. High-Performance Magic Header: Auto-Hide & Auto-Show on Scroll
  function initHeaderScroll() {
    const header = document.querySelector('header');
    if (!header) return;

    header.classList.add('magic-header');

    let lastScrollY = Math.max(0, window.scrollY || 0);
    let ticking = false;
    const scrollThreshold = 8;  // delta buffer to prevent jitter
    const topTolerance = 75;    // always reveal when within 75px of page top

    function handleScroll() {
      const currentScrollY = Math.max(0, window.scrollY || 0);
      const mobileMenu = document.getElementById('mobile-menu');
      const isMobileMenuOpen = mobileMenu && !mobileMenu.classList.contains('hidden');

      // 1. Elevation backdrop when scrolled > 15px
      if (currentScrollY > 15) {
        header.classList.add('header-scrolled');
      } else {
        header.classList.remove('header-scrolled');
      }

      // 2. Auto-hide & Auto-reveal (Magic Header logic)
      if (isMobileMenuOpen || currentScrollY <= topTolerance) {
        // Keep visible at top or when mobile menu drawer is open
        header.classList.remove('header-hidden');
        header.classList.add('header-visible');
        lastScrollY = currentScrollY;
        ticking = false;
        return;
      }

      const delta = currentScrollY - lastScrollY;

      if (Math.abs(delta) >= scrollThreshold) {
        if (delta > 0) {
          // Scrolling Down -> Auto-Hide smoothly
          header.classList.add('header-hidden');
          header.classList.remove('header-visible');
        } else {
          // Scrolling Up -> Auto-Show immediately
          header.classList.remove('header-hidden');
          header.classList.add('header-visible');
        }
        lastScrollY = currentScrollY;
      }

      ticking = false;
    }

    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(handleScroll);
        ticking = true;
      }
    }, { passive: true });

    // Accessibility: Auto-reveal header if user navigates into it using Tab key
    header.addEventListener('focusin', () => {
      header.classList.remove('header-hidden');
      header.classList.add('header-visible');
    });
  }

  // 3. Copy Micro-Interactions
  function initCopyMicroInteractions() {
    document.querySelectorAll('[data-copy-text], button[onclick*="clipboard"]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        let textToCopy = btn.getAttribute('data-copy-text');
        if (!textToCopy) {
          const match = btn.getAttribute('onclick')?.match(/writeText\('([^']+)'\)/);
          if (match) textToCopy = match[1];
        }
        if (!textToCopy) return;

        btn.style.transition = 'all 0.25s cubic-bezier(0.16, 1, 0.3, 1)';
        btn.style.transform = 'scale(0.92)';
        setTimeout(() => {
          btn.style.transform = 'scale(1.06)';
        }, 80);
        setTimeout(() => {
          btn.style.transform = 'scale(1)';
        }, 220);
      });
    });
  }

  // 4. Smooth Counter Ease-Up Animation
  function initSmoothCounterAnimation() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    const counterElements = document.querySelectorAll('[data-counter-target]');
    if (!counterElements.length) return;

    const counterObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseFloat(el.getAttribute('data-counter-target'));
          const prefix = el.getAttribute('data-counter-prefix') || '';
          const suffix = el.getAttribute('data-counter-suffix') || '';
          const duration = parseInt(el.getAttribute('data-counter-duration') || '900', 10);
          const startTime = performance.now();

          function updateCounter(now) {
            const elapsed = now - startTime;
            const progress = Math.min(1, elapsed / duration);
            const easeOut = 1 - Math.pow(1 - progress, 3);
            const current = Math.round(target * easeOut * 10) / 10;

            el.textContent = `${prefix}${Number.isInteger(target) ? Math.round(current).toLocaleString('en-IN') : current.toFixed(1)}${suffix}`;

            if (progress < 1) {
              requestAnimationFrame(updateCounter);
            }
          }

          requestAnimationFrame(updateCounter);
          observer.unobserve(el);
        }
      });
    }, { threshold: 0.2 });

    counterElements.forEach(el => counterObserver.observe(el));
  }

  function initRentlyoLoader() {
    const loader = document.getElementById('rentlyo-loader');
    if (!loader) return;

    const fill = document.getElementById('rentlyo-loader-fill');
    const percent = document.getElementById('rentlyo-loader-percent');
    const statusText = document.getElementById('rentlyo-loader-status');

    let currentProgress = 0;
    let isDismissed = false;

    function setProgress(val, message) {
      if (isDismissed) return;
      currentProgress = Math.max(currentProgress, Math.min(100, val));
      if (fill) fill.style.width = currentProgress + '%';
      if (percent) percent.textContent = Math.round(currentProgress) + '%';
      if (statusText && message) {
        statusText.textContent = message;
      }
    }

    function dismissLoader() {
      if (isDismissed) return;
      isDismissed = true;
      setProgress(100, 'Property OS Ready');

      setTimeout(() => {
        loader.classList.add('loaded');
        loader.setAttribute('aria-hidden', 'true');
        try {
          sessionStorage.setItem('rentlyo_visited', 'true');
        } catch (e) {}

        setTimeout(() => {
          loader.style.display = 'none';
        }, 400);
      }, 140);
    }

    // Allow instant tap/click to dismiss for power users
    loader.addEventListener('click', dismissLoader);

    // Check repeat visit in current browser session
    const isRepeat = (function() {
      try {
        return sessionStorage.getItem('rentlyo_visited') === 'true';
      } catch (e) {
        return false;
      }
    })();

    if (isRepeat) {
      // Snappy micro-transition on repeat navigation (~150ms)
      setProgress(45, 'Resuming Property OS...');
      setTimeout(() => setProgress(88, 'Synchronizing Ledger...'), 40);
      setTimeout(dismissLoader, 130);
    } else {
      // First visit: authoritative, smooth high-tech progression
      setProgress(25, 'Initializing Property OS...');

      setTimeout(() => {
        setProgress(58, 'Verifying Local Ledger & Sync...');
      }, 80);

      setTimeout(() => {
        setProgress(88, 'Securing Offline Architecture...');
      }, 180);

      if (document.readyState === 'complete') {
        setTimeout(dismissLoader, 280);
      } else {
        window.addEventListener('load', () => {
          setTimeout(dismissLoader, 160);
        });
      }

      // Hard safety timeout fallback (max 700ms)
      setTimeout(dismissLoader, 700);
    }
  }

  // Pre-initialize loader immediately if DOM is already interactive
  if (document.readyState === 'interactive' || document.readyState === 'complete') {
    initRentlyoLoader();
  }
})();

