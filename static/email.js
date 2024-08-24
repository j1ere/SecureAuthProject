document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('signupForm').addEventListener('submit', function(event) {
        var emailInput = document.getElementById('email').value;
        var errorMessage = document.getElementById('error-message');

        // Regular expression to match name@gmail.com format
        var gmailPattern = /^[a-zA-Z0-9._%+-]+@gmail\.com$/;

        if (!gmailPattern.test(emailInput)) {
            event.preventDefault();  // Prevent form submission
            errorMessage.style.display = 'block';  // Show the error message
        } else {
            errorMessage.style.display = 'none';  // Hide the error message if valid
        }
    });
});

