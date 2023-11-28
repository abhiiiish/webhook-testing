function generateContent() {
    var userInput = document.getElementById('userInput').value;

    // Make an AJAX request to Flask backend
    $.ajax({
        type: 'POST',
        url: 'https://socify-wofb.onrender.com/index.html',  // Updated URL
        data: { user_input: userInput },
        success: function (response) {
            // Parse the JSON response
            var jsonResponse = JSON.parse(response);

            // Update the response text
            document.getElementById('responseText').innerText = jsonResponse.text;
            // Show the response div
            document.getElementById('responseDiv').style.display = 'block';
        },
        error: function (error) {
            console.error('Error:', error);
        }
    });
}
