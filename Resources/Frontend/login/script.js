function login() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Here you can add your authentication logic
    // For simplicity, let's just check if username and password match "admin"
    if (username === 'admin' && password === 'admin') {
        alert('Login successful!');
        // Redirect to another page or perform further actions
    } else {
        alert('Invalid username or password. Please try again.');
    }
}
