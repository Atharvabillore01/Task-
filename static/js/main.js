$(document).ready(function() {
    // Load header, footer, and sidebar
    $("#header").load("{{ url_for('static', filename='components/header.html') }}", function() {
        // Highlight current page in navigation
        $('a[href="' + window.location.pathname.split("/").pop() + '"]').addClass('active');
    });
    $("#footer").load("{{ url_for('static', filename='components/footer.html') }}");
    $("#sidebar").load("{{ url_for('static', filename='components/sidebar.html') }}", function() {
        // Initialize dropdowns
        $('.dropdown-toggle').dropdown();
    });

    // Sidebar toggle
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("sb-sidenav-toggled");
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var today = new Date().toISOString().split('T')[0];
    var dobInput = document.getElementById('dob');
    if (dobInput) {
        dobInput.setAttribute('max', today);
    }
});

function deleteProfile(profileId) {
    if (confirm('Are you sure you want to delete this profile?')) {
        fetch(`/delete/${profileId}`, {
            method: 'DELETE'
        })
        .then(response => {
            if (response.ok) {
                window.location.reload();
            } else {
                alert('Failed to delete profile.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to delete profile.');
        });
    }
}
