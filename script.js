// Minimal JS for menu + year; no framework needed
const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

const nav = document.getElementById('nav');
const menuBtn = document.getElementById('menuBtn');
const menu = document.getElementById('menu');
if (menuBtn && nav) {
  menuBtn.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    menuBtn.setAttribute('aria-expanded', String(open));
  });
}

// Enhance form inputs styles without extra CSS classes
for (const el of document.querySelectorAll('input, textarea')){
  el.style.width='100%';
  el.style.margin='8px 0 12px';
  el.style.padding='10px 12px';
  el.style.borderRadius='10px';
  el.style.border='1px solid rgba(148,163,184,.25)';
  el.style.background='rgba(2,6,23,.25)';
  el.style.color='inherit';
}