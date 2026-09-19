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
    const hamburgerIcon = document.getElementById('hamburger-icon');
    const closeIcon = document.getElementById('close-icon');

    function openMobileMenu() {
      if (!mobileMenu || !mobileMenuBtn) return;
      mobileMenuBtn.setAttribute('aria-expanded', 'true');
      mobileMenu.classList.remove('hidden');
      if (hamburgerIcon) hamburgerIcon.classList.add('hidden');
      if (closeIcon) closeIcon.classList.remove('hidden');
    }

    function closeMobileMenu() {
      if (!mobileMenu || !mobileMenuBtn) return;
      mobileMenuBtn.setAttribute('aria-expanded', 'false');
      mobileMenu.classList.add('hidden');
      if (hamburgerIcon) hamburgerIcon.classList.remove('hidden');
      if (closeIcon) closeIcon.classList.add('hidden');
    }

    function toggleMobileMenu() {
      if (!mobileMenu) return;
      const isExpanded = mobileMenuBtn.getAttribute('aria-expanded') === 'true';
      if (isExpanded) {
        closeMobileMenu();
      } else {
        openMobileMenu();
      }
    }

    if (mobileMenuBtn && mobileMenu) {
      mobileMenuBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        toggleMobileMenu();
      });

      // Close menu when clicking any link inside it
      mobileMenu.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
          closeMobileMenu();
        });
      });

      // Close on click outside header and menu
      document.addEventListener('click', (e) => {
        const header = mobileMenuBtn.closest('header');
        if (header && !header.contains(e.target)) {
          closeMobileMenu();
        }
      });

      // Close on ESC key
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
          closeMobileMenu();
        }
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

    // Automatic APK Download tracking (supporting both demo_apk_download and apk_download)
    document.querySelectorAll('a[href*=".apk"], a[download]').forEach(anchor => {
      if (!anchor.hasAttribute('data-track-event')) {
        anchor.addEventListener('click', () => {
          const fileTarget = anchor.getAttribute('href');
          const fileLabel = anchor.textContent.trim() || 'APK Download';
          gtagEvent('demo_apk_download', { file: fileTarget, label: fileLabel });
          gtagEvent('apk_download', { file: fileTarget, label: fileLabel });
        });
      }
    });

    // Automatic Tel / Phone Call tracking (supporting both call_click and phone_call_click)
    document.querySelectorAll('a[href^="tel:"]').forEach(anchor => {
      anchor.addEventListener('click', () => {
        const phone = anchor.getAttribute('href');
        const label = anchor.textContent.trim() || 'Direct Phone';
        gtagEvent('call_click', { phone_number: phone, label: label });
        gtagEvent('phone_call_click', { phone_number: phone, label: label });
      });
    });

    // Automatic Outbound Link tracking
    document.querySelectorAll('a[href^="http"]:not([href*="rentlyo.cscouncil.in"]):not([href*="rentlyo.in"]):not([href*="aryaplaza.vercel.app"])').forEach(anchor => {
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
    initRoiCalculator();
    initExitIntentModal();

    // --------------------------------------------------------------------------
    // Rentlyo High-Performance Brand Loader Controller
    // --------------------------------------------------------------------------
    initRentlyoLoader();
  });

  // ROI / Time-Savings Calculator
  function initRoiCalculator() {
    const unitsSlider = document.getElementById('roi-units');
    const hoursSlider = document.getElementById('roi-hours');
    const rateSlider = document.getElementById('roi-rate');

    if (!unitsSlider || !hoursSlider || !rateSlider) return;

    const unitsVal = document.getElementById('roi-units-val');
    const hoursVal = document.getElementById('roi-hours-val');
    const rateVal = document.getElementById('roi-rate-val');

    const monthlyHoursDisplay = document.getElementById('roi-monthly-hours-saved');
    const annualSavingsDisplay = document.getElementById('roi-annual-savings');
    const paybackDisplay = document.getElementById('roi-payback-months');

    let roiLogTimer = null;

    function calculateRoi() {
      const units = parseInt(unitsSlider.value, 10);
      const weeklyHours = parseFloat(hoursSlider.value);
      const hourlyRate = parseInt(rateSlider.value, 10);

      if (unitsVal) unitsVal.textContent = units;
      if (hoursVal) hoursVal.textContent = weeklyHours + ' hrs/wk';
      if (rateVal) rateVal.textContent = '₹' + hourlyRate.toLocaleString('en-IN') + '/hr';

      // Rentlyo cuts ~80% of routine administration (meter reading, dues chasing, ledger reconciliation)
      const weeklySaved = weeklyHours * 0.8;
      const monthlyHoursSaved = Math.round(weeklySaved * 4.33);
      const annualHoursSaved = Math.round(weeklySaved * 52);
      const annualMoneySaved = Math.round(annualHoursSaved * hourlyRate);

      // Payback period for ₹20,000 one-time investment
      const monthlyMoneySaved = annualMoneySaved / 12;
      const paybackMonths = monthlyMoneySaved > 0 ? (20000 / monthlyMoneySaved).toFixed(1) : '—';

      if (monthlyHoursDisplay) monthlyHoursDisplay.textContent = `${monthlyHoursSaved} hrs/mo`;
      if (annualSavingsDisplay) annualSavingsDisplay.textContent = `₹${annualMoneySaved.toLocaleString('en-IN')}`;
      if (paybackDisplay) paybackDisplay.textContent = `${paybackMonths} mo`;

      clearTimeout(roiLogTimer);
      roiLogTimer = setTimeout(() => {
        gtagEvent('roi_calculator_used', {
          units: units,
          weekly_hours_spent: weeklyHours,
          hourly_rate: hourlyRate,
          annual_savings: annualMoneySaved,
          payback_months: paybackMonths
        });
      }, 1500);
    }

    unitsSlider.addEventListener('input', calculateRoi);
    hoursSlider.addEventListener('input', calculateRoi);
    rateSlider.addEventListener('input', calculateRoi);
    calculateRoi();
  }

  // Exit-Intent PDF Offer & Email Capture
  function initExitIntentModal() {
    // Only on desktop viewport, non-touch devices
    if (window.innerWidth < 1024 || 'ontouchstart' in window) return;

    const modal = document.getElementById('exit-intent-modal');
    if (!modal) return;

    const closeBtn = document.getElementById('exit-intent-close');
    const cancelBtn = document.getElementById('exit-intent-cancel');
    const form = document.getElementById('exit-intent-form');
    const successBox = document.getElementById('exit-intent-success');
    const emailInput = document.getElementById('exit-intent-email');

    // Check if dismissed this session
    try {
      if (sessionStorage.getItem('rentlyo_exit_dismissed') === 'true') {
        return;
      }
    } catch (e) {}

    let hasShown = false;

    function showModal() {
      if (hasShown) return;
      hasShown = true;
      modal.classList.remove('hidden');
      modal.classList.add('flex');
      gtagEvent('exit_intent_shown');
      if (emailInput) setTimeout(() => emailInput.focus(), 100);
    }

    function dismissModal() {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
      try {
        sessionStorage.setItem('rentlyo_exit_dismissed', 'true');
      } catch (e) {}
    }

    document.addEventListener('mouseleave', (e) => {
      if (e.clientY <= 15 && !hasShown) {
        showModal();
      }
    });

    if (closeBtn) closeBtn.addEventListener('click', dismissModal);
    if (cancelBtn) cancelBtn.addEventListener('click', dismissModal);

    modal.addEventListener('click', (e) => {
      if (e.target === modal) dismissModal();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        dismissModal();
      }
    });

    if (form) {
      form.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = emailInput ? emailInput.value.trim() : '';
        if (!email) return;

        try {
          localStorage.setItem('rentlyo_lead_email', email);
          sessionStorage.setItem('rentlyo_exit_dismissed', 'true');
        } catch (err) {}

        gtagEvent('lead_capture_submit', {
          email: email,
          source: 'exit_intent_blueprint'
        });

        // Show success state
        form.classList.add('hidden');
        if (successBox) successBox.classList.remove('hidden');

        setTimeout(() => {
          dismissModal();
        }, 3200);
      });
    }
  }

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

