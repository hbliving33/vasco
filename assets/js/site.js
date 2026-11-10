// Mobile menu
document.querySelectorAll('.menu-btn').forEach(b => b.addEventListener('click', () => {
  document.querySelector('nav.main').classList.toggle('open');
}));

// Portfolio filters + lightbox
const filters = document.querySelectorAll('.filters button');
filters.forEach(btn => btn.addEventListener('click', () => {
  filters.forEach(b => b.classList.remove('on')); btn.classList.add('on');
  const f = btn.dataset.f;
  document.querySelectorAll('.gallery figure').forEach(fig => {
    fig.style.display = (f === 'all' || fig.dataset.cat === f) ? '' : 'none';
  });
}));
const lb = document.querySelector('.lightbox');
if (lb) {
  const img = lb.querySelector('img');
  document.querySelectorAll('.gallery figure').forEach(fig => fig.addEventListener('click', () => {
    const src = fig.querySelector('img');
    img.src = src.src; img.alt = src.alt; lb.classList.add('open');
  }));
  lb.addEventListener('click', e => { if (e.target !== img) lb.classList.remove('open'); });
  document.addEventListener('keydown', e => { if (e.key === 'Escape') lb.classList.remove('open'); });
}

// Sortable tables: click any column heading to sort / reverse
document.querySelectorAll('table.data').forEach(table => {
  table.querySelectorAll('th').forEach((th, i) => th.addEventListener('click', () => {
    const asc = !th.classList.contains('asc');
    table.querySelectorAll('th').forEach(h => h.classList.remove('asc', 'desc'));
    th.classList.add(asc ? 'asc' : 'desc');
    const body = table.tBodies[0];
    [...body.rows].sort((a, b) => {
      const x = a.cells[i].dataset.sort || a.cells[i].innerText.trim(), y = b.cells[i].dataset.sort || b.cells[i].innerText.trim();
      return (asc ? 1 : -1) * x.localeCompare(y, undefined, { numeric: true });
    }).forEach(r => body.appendChild(r));
  }));
});

// Estimate form — delivery endpoint not connected yet
document.querySelectorAll('form.estimate').forEach(form => form.addEventListener('submit', e => {
  e.preventDefault();
  const endpoint = form.dataset.endpoint;
  const msg = form.parentElement.querySelector('.form-msg');
  if (!endpoint) {
    msg.textContent = 'Thanks!  Online requests are being set up — please call us at (714) 968-8845 and we will schedule your free estimate.';
    msg.style.display = 'block'; return;
  }
  fetch(endpoint, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
    .then(r => { msg.textContent = r.ok ? 'Thanks!  We received your request and will contact you shortly.' : 'Something went wrong.  Please call (714) 968-8845.'; msg.style.display = 'block'; if (r.ok) form.reset(); })
    .catch(() => { msg.textContent = 'Something went wrong.  Please call (714) 968-8845.'; msg.style.display = 'block'; });
}));

document.querySelectorAll('.year').forEach(el => el.textContent = new Date().getFullYear());

// Solar Education: solar panel tiles open their topic in a pop-up
(function () {
  const dialogs = document.querySelectorAll('dialog.edu');
  if (!dialogs.length) return;
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let lastTile = null;
  function openTopic(id, tile) {
    const d = document.getElementById(id);
    if (!d || d.open) return;
    lastTile = tile || document.querySelector('.spanel[data-open="' + id + '"]');
    d.showModal();
    d.querySelector('.edu-body').scrollTop = 0; d.scrollTop = 0;
    history.replaceState(null, '', '#' + id);
  }
  document.querySelectorAll('.spanel').forEach(tile => tile.addEventListener('click', () => {
    if (reduce) return openTopic(tile.dataset.open, tile);
    tile.classList.add('zap');
    setTimeout(() => { tile.classList.remove('zap'); openTopic(tile.dataset.open, tile); }, 260);
  }));
  dialogs.forEach(d => {
    d.querySelector('.edu-x').addEventListener('click', () => d.close());
    d.addEventListener('click', e => { if (e.target === d) d.close(); });   // click outside the panel
    d.addEventListener('close', () => {
      history.replaceState(null, '', location.pathname + location.search);
      if (lastTile) lastTile.focus({ preventScroll: true });
    });
  });
  const openFromHash = () => { const id = location.hash.slice(1); if (id && document.getElementById(id) && document.getElementById(id).matches('dialog.edu')) openTopic(id); };
  window.addEventListener('hashchange', openFromHash);
  openFromHash();
})();
