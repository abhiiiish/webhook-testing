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

function fetchWebhookWithXHR() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', webhook, true);

    xhr.onload = function () {
        if (xhr.status === 200) {
            try {
                var data = JSON.parse(xhr.responseText);
                updateWebPage(data);
            } catch (error) {
                console.error('Error parsing JSON:', error);
            }
        } else {
            console.error('Request failed with status:', xhr.status);
        }
    };

    xhr.onerror = function () {
        console.error('Network error occurred');
    };

    xhr.send();
}

function updateWebPage(data) {
    // Assuming you have an element with id 'webhookData' to display the data
    const webhookDataElement = document.getElementById('webhookData');

    // Update the content of the element with the fetched data
    webhookDataElement.innerText = JSON.stringify(data, null, 2);
}



