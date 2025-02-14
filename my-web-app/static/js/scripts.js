// This file contains JavaScript code for client-side interactivity, such as handling form submissions and updating the UI dynamically. 

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('math-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `Result: ${data.result}`;
        })
        .catch((error) => {
            console.error('Error:', error);
            resultDiv.innerHTML = 'An error occurred. Please try again.';
        });
    });
});