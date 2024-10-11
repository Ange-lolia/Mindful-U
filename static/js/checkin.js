// checkin.js

document.addEventListener('DOMContentLoaded', function () {
    const moodForm = document.getElementById('mood-form');
    const moodSelect = document.getElementById('mood-select');
    const responseMessage = document.getElementById('response-message');

    moodForm.addEventListener('submit', function (event) {
        event.preventDefault();  // Prevent the default form submission

        const selectedMood = moodSelect.value;

        fetch(`/mood_response/${selectedMood}`)
            .then(response => response.json())
            .then(data => {
                responseMessage.textContent = data.message;
            })
            .catch(error => {
                console.error('Error fetching mood response:', error);
                responseMessage.textContent = "Sorry, there was an error processing your mood.";
            });
    });
});
