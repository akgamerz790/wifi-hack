// Function to send credentials to the server (Flask)
function storeCredentials() {
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  const data = {
      username: username,
      password: password
  };

  fetch('/store_credentials', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
      alert('Credentials stored successfully!');
      console.log(data);
  })
  .catch((error) => {
      console.error('Error:', error);
  });
}
