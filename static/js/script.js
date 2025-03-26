// Show scary popups randomly
function showPopup() {
    const popup = document.getElementById('popup');
    popup.style.display = 'block';
    setTimeout(() => {
        popup.style.display = 'none';
    }, 3000); // Popup disappears after 3 seconds
}

// Randomly trigger popups
setInterval(() => {
    if (Math.random() < 0.5) { // 30% chance to show popup
        showPopup();
    }
}, 5000);

// Close popup manually
function closePopup() {
    const popup = document.getElementById('popup');
    popup.style.display = 'none';
}

// Add glitch effect to body
setInterval(() => {
    document.body.style.animation = 'glitch 0.5s infinite';
    setTimeout(() => {
        document.body.style.animation = 'none';
    }, 500);
}, 3000);
