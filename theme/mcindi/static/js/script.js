(function () {
  const nav = document.getElementById('nav');
  const menu = document.getElementById('menu');
  const menuBtn = document.getElementById('menuBtn');
  const year = document.getElementById('year');

  if (year) {
    year.textContent = new Date().getFullYear().toString();
  }

  if (menuBtn && nav) {
    menuBtn.addEventListener('click', () => {
      const expanded = menuBtn.getAttribute('aria-expanded') === 'true';
      menuBtn.setAttribute('aria-expanded', String(!expanded));
      nav.classList.toggle('open');
    });
  }

  if (menu && nav) {
    menu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        nav.classList.remove('open');
        if (menuBtn) {
          menuBtn.setAttribute('aria-expanded', 'false');
        }
      });
    });
  }
})();
