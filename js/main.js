$(document).ready(function() {
    // Load header and footer
    $("#header").load("components/header.html", function() {
        // Highlight current page in navigation
        $('a[href="' + window.location.pathname.split("/").pop() + '"]').addClass('active');
    });
    $("#footer").load("components/footer.html");
    $("#sidebar").load("components/sidebar.html", function() {
        // Initialize dropdowns
        $('.dropdown-toggle').dropdown();
    });

    // Sidebar toggle
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("sb-sidenav-toggled");
    });
});