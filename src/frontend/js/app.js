// Web Dashboard bootstrap: checks that the Backend API is reachable.
// Page modules (history.js, compare.js, whatif.js, replay.js) are added in their increments.
fetch('/api/health')
  .then((r) => r.json())
  .then((h) => { document.getElementById('status').textContent = `API: ${h.status} | model loaded: ${h.model_loaded}`; })
  .catch(() => { document.getElementById('status').textContent = 'API not reachable'; });
