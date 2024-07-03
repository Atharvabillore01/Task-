// Example AJAX request for login
$('#login-form').submit(function(event) {
    event.preventDefault();
    
    var formData = {
        email: $('#email').val(),
        password: $('#password').val()
    };

    $.ajax({
        type: 'POST',
        url: '/api/login',  // Use the appropriate endpoint
        data: JSON.stringify(formData),
        contentType: 'application/json',
        success: function(response) {
            if (response.valid) {
                window.location.href = '/';  // Redirect to home page on successful login
            } else {
                $('#error-message').text('Invalid email or password. Please try again.');  // Display error message
            }
        },
        error: function(xhr, status, error) {
            console.error('Error:', error);  // Log any AJAX errors for debugging
            $('#error-message').text('An error occurred. Please try again later.');  // Display generic error message
        }
    });
});
