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

  // Dropdown: on mobile, clicking the toggle expands the submenu in place.
  // On desktop, hover handles visibility via CSS; clicking navigates normally.
  const dropdowns = document.querySelectorAll('.nav-dropdown');

  dropdowns.forEach((dd) => {
    const toggle = dd.querySelector('.nav-dropdown-toggle');
    if (!toggle) return;

    toggle.addEventListener('click', (e) => {
      // Only intercept when the mobile menu is open
      if (nav && nav.classList.contains('open')) {
        e.preventDefault();
        const isOpen = dd.classList.contains('open');
        dropdowns.forEach((d) => d.classList.remove('open'));
        if (!isOpen) dd.classList.add('open');
      }
    });
  });

  // Close dropdowns when clicking outside (desktop)
  document.addEventListener('click', (e) => {
    if (!e.target.closest('.nav-dropdown')) {
      dropdowns.forEach((d) => d.classList.remove('open'));
    }
  });

  if (menu && nav) {
    // Close mobile menu on link click — skip the dropdown toggle itself
    menu.querySelectorAll('a').forEach((link) => {
      if (link.classList.contains('nav-dropdown-toggle')) return;
      link.addEventListener('click', () => {
        nav.classList.remove('open');
        dropdowns.forEach((d) => d.classList.remove('open'));
        if (menuBtn) {
          menuBtn.setAttribute('aria-expanded', 'false');
        }
      });
    });
  }
})();
