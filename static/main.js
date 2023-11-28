User
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



function fetchProfiles() {
    // Make an AJAX request to fetch profiles from the backend
    $.ajax({
        type: 'POST',
        url: '/db',
        success: function (data) {
            // Clear existing table rows
            var tableBody = document.getElementById('profilesTableBody');
            tableBody.innerHTML = '';

            // Iterate through profiles and add rows to the table
            data.profiles.forEach(function (profile) {
                var row = tableBody.insertRow(-1);
                var cellId = row.insertCell(0);
                var cellBrandId = row.insertCell(1);
                var cellPostId = row.insertCell(2);
                var cellCaption = row.insertCell(3);
                var cellStatus = row.insertCell(4);
                var cellMediaUrl = row.insertCell(5);
                var cellMediaType = row.insertCell(6);

                // Populate cells with profile data
                cellId.innerHTML = profile.id;
                cellBrandId.innerHTML = profile.brand_id;
                cellPostId.innerHTML = profile.post_id;
                cellCaption.innerHTML = profile.caption;
                cellStatus.innerHTML = profile.status;
                cellMediaUrl.innerHTML = profile.media_url;
                cellMediaType.innerHTML = profile.media_type;
            });
        },
        error: function (error) {
            console.error('Error fetching profiles:', error);
        }
    });
}



