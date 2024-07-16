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

        // Handle dropdown close on click outside
        $(document).on('click', function(e) {
            if (!$(e.target).closest('.dropdown-toggle').length) {
                $('.dropdown-menu').removeClass('show');
            }
        });
    });

    // Sidebar toggle
    $(document).ready(function() {
        // Handle click event on dropdown toggles
        $('.dropdown-toggle').click(function(e) {
            e.preventDefault(); // Prevent default action of anchor tag
    
            var $parentDropdown = $(this).parent('.dropdown'); // Get parent dropdown element
            var $dropdownMenu = $parentDropdown.find('.dropdown-menu'); // Get dropdown menu
    
            // Toggle the dropdown menu visibility
            $dropdownMenu.toggleClass('show');
    
            // Close other dropdowns
            $('.dropdown-menu').not($dropdownMenu).removeClass('show');
        });
    
        // Close dropdowns when clicking outside
        $(document).click(function(e) {
            if (!$(e.target).closest('.dropdown').length) {
                $('.dropdown-menu').removeClass('show');
            }
        });
    });

    // Set max date for date of birth input
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

function filterUsers() {
    var input, filter, cards, cardContainer, title, txtValue, i;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    cardContainer = document.getElementById("users-list");
    cards = cardContainer.getElementsByClassName("user-card");

    for (i = 0; i < cards.length; i++) {
        title = cards[i].getElementsByClassName("card-title")[0];
        txtValue = title.textContent || title.innerText;
        
        if (txtValue.toUpperCase().startsWith(filter)) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}

function filterStudents() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    table = document.getElementById("students-table");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 1; i < tr.length; i++) {
        tds = tr[i].getElementsByTagName("td");
        var found = false;
        for (var j = 0; j < tds.length; j++) {
            td = tds[j];
            if (td) {
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().startsWith(filter)) {
                    found = true;
                    break; // Exit loop if a match is found
                }
            }
        }
        if (found) {
            tr[i].style.display = "";
        } else {
            tr[i].style.display = "none";
        }
    }
}

$(document).ready(function() {
    // Show/hide steps based on button clicks
    $('.next-btn').click(function() {
        $('#step1').hide();
        $('#step2').show();
    });

    // Validate form inputs (example)
    $('#signupForm').submit(function(event) {
        var password = $('#password').val();
        var confirm_password = $('#confirm_password').val();

        if (password !== confirm_password) {
            alert("Passwords do not match.");
            event.preventDefault(); // Prevent form submission
        }
    });
});

// signup

$(document).ready(function() {
    let currentStep = 1;
    const totalSteps = 6;

    function updateStep(step) {
        $('.signup-step').removeClass('active animate__animated animate__fadeIn');
        $(`#step-${step}`).addClass('active animate__animated animate__fadeIn');
        $('#step-counter').text(step);
        updateButtons();
        updateProgressBar();
    }

    function updateButtons() {
        $('#prev-btn').prop('disabled', currentStep === 1);
        if (currentStep === totalSteps) {
            $('#next-btn').addClass('d-none');
            $('#submit-btn').removeClass('d-none');
        } else {
            $('#next-btn').removeClass('d-none');
            $('#submit-btn').addClass('d-none');
        }
    }

    function updateProgressBar() {
        const progress = (currentStep / totalSteps) * 100;
        $('.progress-bar').css('width', `${progress}%`).attr('aria-valuenow', progress);
    }

    $('#next-btn').click(function() {
        if (currentStep < totalSteps) {
            currentStep++;
            updateStep(currentStep);
        }
    });

    $('#prev-btn').click(function() {
        if (currentStep > 1) {
            currentStep--;
            updateStep(currentStep);
        }
    });


    $('#signup-form').submit(function(e) {
        e.preventDefault(); // Prevent default form submission
        if (validateStep(currentStep)) {
            // AJAX submission or any other processing here
            alert('Form submitted successfully!');
            // You can redirect or perform any necessary actions after successful submission
        }
    });
    updateStep(currentStep);
});
