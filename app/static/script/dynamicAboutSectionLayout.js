/* Keep the education and contact boxes at the top of the about section for smaller screens */

function moveBoxes() {
    const contactBox = document.getElementById('contact-box');
    const educationBox = document.getElementById('education-box');
    const leftColumn = document.getElementById('about-left-column');
    const rightColumn = document.getElementById('about-right-column');

    if (window.innerWidth < 800) {
        // Move boxes to the top of the right column on smaller screens
        rightColumn.insertBefore(educationBox, rightColumn.firstChild);
        rightColumn.insertBefore(contactBox, rightColumn.firstChild);
    } else {
        // Move boxes back to the top of the left column if not already present
        if (!(leftColumn.contains(educationBox) && leftColumn.contains(contactBox))) {
            leftColumn.insertBefore(educationBox, leftColumn.firstChild);
            leftColumn.insertBefore(contactBox, leftColumn.firstChild);
        }
    }
}

// Initial check when page loads
moveBoxes();

// Add event listener for window resize
window.addEventListener('resize', moveBoxes);
