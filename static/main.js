function generateContent() {
    var userInput = document.getElementById('userInput').value;

    // Make an AJAX request to Flask backend
    $.ajax({
        type: 'POST',
        url: '/index',
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
