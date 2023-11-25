function generateContent() {
    var userInput = document.getElementById('userInput').value;

    // Make an AJAX request to Flask backend
    $.ajax({
        type: 'POST',
        url: 'https://socify-wofb.onrender.com/webhook',
        data: { user_input: userInput },
        success: function (response) {
            // Update the response text
            document.getElementById('responseText').innerText = response;
            // Show the response div
            document.getElementById('responseDiv').style.display = 'block';
        },
        error: function (error) {
            console.error('Error:', error);
        }
    });
}

const webhook = "https://socify-wofb.onrender.com/webhook";

function fetchWebhook() {
    fetch(webhook, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
    })
        .then(response => {
            if (response.status === 200) {
                return response.json();
            } else {
                throw new Error('Failed to fetch data');
            }
        })
        .then(data => {
            // Update the webpage with the fetched data
            updateWebPage(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


