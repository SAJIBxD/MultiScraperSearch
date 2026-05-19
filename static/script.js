const q = document.getElementById('q');
const btn = document.getElementById('btn');
const results = document.getElementById('results');

btn.addEventListener('click', search);
q.addEventListener('keydown', e => e.key === 'Enter' && search());

async function search() {
  const kw = q.value.trim();
  if (!kw) return;
  results.innerHTML = '<div class="status">searching…</div>';
  try {
    const res = await fetch(`/search/${encodeURIComponent(kw)}`);
    const data = await res.json();
    results.innerHTML = '';
    if (!data.length) {
      results.innerHTML = '<div class="status">no results</div>';
      return;
    }
    data.forEach(sourceObj => {
      const name = Object.keys(sourceObj)[0];
      const items = sourceObj[name];
      const sec = document.createElement('div');
      sec.className = 'source';
      sec.innerHTML = `
        <div class="source-header">
          <span class="source-name">${name}</span>
          <div class="source-line"></div>
          <span class="count">${items.length}</span>
        </div>
        <div class="grid">${items.map(item => `
          <div class="card">
            <a href="${item.url}" target="_blank" rel="noopener">
              <div class="thumb-wrap"><img src="${item.thumbnail}" alt="" loading="lazy"></div>
              <div class="card-body"><div class="card-title">${item.title}</div></div>
            </a>
          </div>`).join('')}
        </div>`;
      results.appendChild(sec);
    });
  } catch {
    results.innerHTML = '<div class="status">error — is the server running?</div>';
  }
}
