document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        const targetId = this.getAttribute('href');
        const targetSection = document.querySelector(targetId);

        const headerOffset = document.querySelector('header').offsetHeight; // Height of the header
        const elementPosition = targetSection.getBoundingClientRect().top;
        const scrollY = window.scrollY !== undefined ? window.scrollY : window.pageYOffset; // Fallback for older browsers
        const offsetPosition = elementPosition + scrollY - headerOffset; // Adjusting for header height

        window.scrollTo({
            top: offsetPosition,
            behavior: 'smooth'
        });
    });
});
