 function generateContent() {
        var userInput = document.getElementById('userInput').value;

        // Make an AJAX request to Flask backend
        $.ajax({
            type: 'POST',
            url: '/index.html',
            data: {user_input: userInput},
            success: function(response) {
                // Parse the JSON response
                var responseData = JSON.parse(response);

                // Update the response text and media URL
                document.getElementById('caption').innerText = 'Caption: ' + responseData.text;
                document.getElementById('generated_media').innerText = 'Media URL: ' + responseData.url;

                // Show the response div
                document.getElementById('responseDiv').style.display = 'block';
            },
            error: function(error) {
                console.error('Error:', error);
            }
        });
    }
