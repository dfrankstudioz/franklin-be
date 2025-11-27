// Minimal static doc site renderer
// Expects markdown files to live in ./content/<filename>.md
// Pages array: title -> filename
const pages = [
  { title: "About", file: "about.md" },
  { title: "Getting Started", file: "getting-started.md" },
  { title: "Download", file: "download.md" },
  { title: "FAQ", file: "faq.md" },
  { title: "Support", file: "support.md" },
  { title: "License (EULA)", file: "licence.md" },
  { title: "Privacy Policy", file: "privacy-policy.md" },
  { title: "Refund Policy", file: "refund-policy.md" },
  { title: "Terms & Conditions", file: "terms-and-conditions.md" }
];

const navList = document.getElementById('nav-list');
const docEl = document.getElementById('doc');
const searchInput = document.getElementById('search');
const themeToggle = document.getElementById('toggle-theme');

function buildNav() {
  pages.forEach((p, idx) => {
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = `#${p.file}`;
    a.textContent = p.title;
    if (idx === 0) a.classList.add('active');
    li.appendChild(a);
    navList.appendChild(li);
  });
}

async function loadPage(filename) {
  try {
    const res = await fetch(`content/${filename}`);
    if (!res.ok) throw new Error('Not found');
    const text = await res.text();
    // Convert markdown -> HTML
    const rawHtml = marked.parse(text, {mangle:false, headerIds:true});
    // sanitize
    const clean = DOMPurify.sanitize(rawHtml);
    docEl.innerHTML = clean;
    // Update active nav
    document.querySelectorAll('.nav a').forEach(a => {
      a.classList.toggle('active', a.getAttribute('href') === `#${filename}`);
    });
    // blue link targets open in new tab if external
    docEl.querySelectorAll('a').forEach(a=>{
      try {
        if (a.hostname && a.hostname !== location.hostname) a.target = '_blank';
      } catch(e){}
    });
    // scroll to top
    docEl.scrollTop = 0;
  } catch (err) {
    docEl.innerHTML = `<h2>Page not found</h2><p>Could not load <code>${filename}</code>. Make sure the file exists in the <code>/content</code> folder and you're serving the site via HTTP (not file://).</p>`;
  }
}

function onHashChange() {
  const file = location.hash ? location.hash.substring(1) : pages[0].file;
  loadPage(file);
}

function wireEvents() {
  window.addEventListener('hashchange', onHashChange);
  searchInput.addEventListener('input', () => {
    // simple in-page search highlight (client-side)
    const term = searchInput.value.trim().toLowerCase();
    if (!term) {
      // remove highlights by reloading page
      onHashChange();
      return;
    }
    // plain text search on current doc
    const text = docEl.textContent.toLowerCase();
    if (!text.includes(term)) {
      // nothing found
      return;
    }
    // naive highlight: wrap occurrences in <mark>
    const inner = docEl.innerHTML;
    const re = new RegExp(term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
    const highlighted = inner.replace(re, match => `<mark style="background:linear-gradient(90deg,#fff1a8,#ffd27a);padding:0 2px;border-radius:3px;color:#072">` + match + `</mark>`);
    docEl.innerHTML = highlighted;
  });

  themeToggle.addEventListener('click', ()=> {
    const root = document.documentElement;
    if (root.classList.contains('light')) {
      root.classList.remove('light');
      themeToggle.textContent = '🌙';
      localStorage.removeItem('franklin-theme');
    } else {
      root.classList.add('light');
      themeToggle.textContent = '🌞';
      localStorage.setItem('franklin-theme','light');
    }
  });
}

function restoreTheme() {
  if (localStorage.getItem('franklin-theme') === 'light') {
    document.documentElement.classList.add('light');
    themeToggle.textContent = '🌞';
  }
}

function init() {
  buildNav();
  wireEvents();
  restoreTheme();
  // load initial page
  onHashChange();
}

init();