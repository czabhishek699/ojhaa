document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // In a real application, you would perform authentication here
    // For simplicity, we're just checking if the username and password match the stored data
    if (username === 'czabhishek' && password === '82025840') {
        window.location.href = 'home.html'; // Redirect to home.html on successful login
    } else {
        // Display the error message
        const errorMessage = document.createElement('div');
        errorMessage.textContent = 'Your credentials are incorrect. Please retry.';
        errorMessage.id = 'error-message';
        errorMessage.className = 'error-message';

        // Remove any existing error messages
        const existingErrorMessage = document.getElementById('error-message');
        if (existingErrorMessage) {
            existingErrorMessage.remove();
        }

        // Append the new error message to the login container
        const loginContainer = document.querySelector('.login-container');
        loginContainer.appendChild(errorMessage);
    }
});
