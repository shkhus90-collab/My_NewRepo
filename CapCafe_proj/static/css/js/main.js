// static/js/main.js

document.addEventListener("DOMContentLoaded", function () {
    console.log("CapCafe JS Initialized Successfully.");

    // Auto-dismiss alert notifications after 4 seconds if present
    setTimeout(function () {
        let alerts = document.querySelectorAll('.alert');
        alerts.forEach(function (alert) {
            let bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 4000);

    // Optional: Add active class to current navbar link dynamically
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentLocation) {
            link.classList.add('active', 'fw-bold', 'text-warning');
        }
    });
});