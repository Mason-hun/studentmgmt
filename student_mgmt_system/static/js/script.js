// script.js

// Collapse navbar automatically after clicking a link (mobile UX improvement)
document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll(".nav-link");
    const navbarCollapse = document.getElementById("navbarNav");

    navLinks.forEach(link => {
        link.addEventListener("click", () => {
            if (navbarCollapse.classList.contains("show")) {
                new bootstrap.Collapse(navbarCollapse).toggle();
            }
        });
    });
});

// Example: Responsive alert when window resizes
window.addEventListener("resize", function () {
    if (window.innerWidth < 768) {
        console.log("Mobile view active");
    } else {
        console.log("Desktop view active");
    }
});