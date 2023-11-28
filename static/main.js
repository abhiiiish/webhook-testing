function generateContent() {
    var userInput = document.getElementById('userInput').value;

    // Make an AJAX request to Flask backend
    $.ajax({
        type: 'POST',
        url: 'https://socify-wofb.onrender.com/index',
        contentType: 'application/json',  // Set the Content-Type header
        data: JSON.stringify({ user_input: userInput }),  // Convert data to JSON string
        success: function (jsonResponse) {
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
