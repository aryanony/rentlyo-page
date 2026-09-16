/**
 * Rentlyo Interactive Cost & ROI Calculator (Advanced Engine)
 * Verified math: Rentlyo flat ₹20,000 one-time vs recurring SaaS subscriptions.
 */

(function () {
  'use strict';

  const RENTLYO_FLAT_PRICE = 20000;

  // DOM Elements
  const unitSlider = document.getElementById('calc-units');
  const unitDisplay = document.getElementById('calc-units-display');
  const rateInput = document.getElementById('calc-rate');
  const pricingType = document.getElementById('calc-pricing-type'); // 'flat' or 'per-unit'
  
  const cost1yrElem = document.getElementById('calc-saas-1yr');
  const cost3yrElem = document.getElementById('calc-saas-3yr');
  const cost5yrElem = document.getElementById('calc-saas-5yr');
  
  const savings3yrElem = document.getElementById('calc-savings-3yr');
  const breakevenElem = document.getElementById('calc-breakeven');
  
  // Bar chart elements
  const barRentlyo = document.getElementById('bar-rentlyo');
  const barSaas1 = document.getElementById('bar-saas-1');
  const barSaas3 = document.getElementById('bar-saas-3');
  const barSaas5 = document.getElementById('bar-saas-5');

  if (!unitSlider || !rateInput) return;

  function formatINR(val) {
    return '₹' + Math.round(val).toLocaleString('en-IN');
  }

  function calculate() {
    const units = parseInt(unitSlider.value, 10) || 15;
    const rate = parseFloat(rateInput.value) || 1499;
    const isPerUnit = pricingType ? pricingType.value === 'per-unit' : false;

    if (unitDisplay) {
      unitDisplay.textContent = units;
    }

    const monthlyCost = isPerUnit ? rate * units : rate;
    const saas1Yr = monthlyCost * 12;
    const saas3Yr = monthlyCost * 36;
    const saas5Yr = monthlyCost * 60;

    const savings3Yr = saas3Yr - RENTLYO_FLAT_PRICE;
    const breakevenMonths = monthlyCost > 0 ? Math.ceil(RENTLYO_FLAT_PRICE / monthlyCost) : 12;

    if (cost1yrElem) cost1yrElem.textContent = formatINR(saas1Yr);
    if (cost3yrElem) cost3yrElem.textContent = formatINR(saas3Yr);
    if (cost5yrElem) cost5yrElem.textContent = formatINR(saas5Yr);

    if (savings3yrElem) {
      if (savings3Yr > 0) {
        savings3yrElem.textContent = `Save ${formatINR(savings3Yr)}`;
      } else {
        savings3yrElem.textContent = `Breakeven in ~${breakevenMonths} mos`;
      }
    }

    if (breakevenElem) {
      breakevenElem.textContent = `Breakeven reached in Month ${breakevenMonths}. After that, 100% of collected rent is yours.`;
    }

    // Chart heights scaling (max height ~200px)
    const maxReference = Math.max(saas5Yr, 50000);
    const maxHeightPx = 200;

    const rentlyoHeight = Math.max(28, Math.min(maxHeightPx, (RENTLYO_FLAT_PRICE / maxReference) * maxHeightPx));
    const saas1Height = Math.max(24, Math.min(maxHeightPx, (saas1Yr / maxReference) * maxHeightPx));
    const saas3Height = Math.max(36, Math.min(maxHeightPx, (saas3Yr / maxReference) * maxHeightPx));
    const saas5Height = Math.max(48, Math.min(maxHeightPx, (saas5Yr / maxReference) * maxHeightPx));

    if (barRentlyo) barRentlyo.style.height = `${rentlyoHeight}px`;
    if (barSaas1) barSaas1.style.height = `${saas1Height}px`;
    if (barSaas3) barSaas3.style.height = `${saas3Height}px`;
    if (barSaas5) barSaas5.style.height = `${saas5Height}px`;

    // Push analytics event (throttled)
    if (window.dataLayer && typeof window.logCalculatorUsed === 'function') {
      window.logCalculatorUsed(units, monthlyCost, savings3Yr);
    }
  }

  // Preset buttons
  document.querySelectorAll('[data-calc-preset]').forEach(btn => {
    btn.addEventListener('click', () => {
      const pVal = parseInt(btn.getAttribute('data-calc-preset'), 10);
      if (pVal) {
        unitSlider.value = pVal;
        calculate();
      }
    });
  });

  // Event Listeners
  unitSlider.addEventListener('input', calculate);
  rateInput.addEventListener('input', calculate);
  if (pricingType) {
    pricingType.addEventListener('change', calculate);
  }

  calculate();
  window.recalculateCosts = calculate;
})();
