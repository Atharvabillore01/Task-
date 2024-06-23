$(document).ready(function() {
    // Login form submission
    $("#loginForm").submit(function(e) {
        e.preventDefault();
        $.ajax({
            url: "https://api.example.com/login", // Replace with your API endpoint
            method: "POST",
            data: {
                username: $("#username").val(),
                password: $("#password").val()
            },
            success: function(response) {
                alert("Login successful!");
                // Redirect to profile page or handle the response
            },
            error: function(xhr, status, error) {
                alert("Login failed. Please try again.");
            }
        });
    });

    // Search functionality (add this to search.html)
    $("#searchForm").submit(function(e) {
        e.preventDefault();
        $.ajax({
            url: "https://api.example.com/search", // Replace with your API endpoint
            method: "GET",
            data: {
                query: $("#searchQuery").val()
            },
            success: function(response) {
                // Display search results
                $("#searchResults").html(response);
            },
            error: function(xhr, status, error) {
                alert("Search failed. Please try again.");
            }
        });
    });
});