$('#loginForm').on('submit', function(e) {
    e.preventDefault();

    var username = $('#username').val();
    var password = $('#password').val();

    $.ajax({
        url: '/api/login',  // Change this to your server's login endpoint
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            username: username,
            password: password
        }),
        success: function(response) {
            if (response.valid) {
                $('#loginMessage').text('Login successful!').css('color', 'green');
                // Optionally redirect to another page
                // window.location.href = 'index.html';
            } else {
                $('#loginMessage').text('Invalid username or password.').css('color', 'red');
            }
        },
        error: function() {
            $('#loginMessage').text('An error occurred. Please try again.').css('color', 'red');
        }
    });
});