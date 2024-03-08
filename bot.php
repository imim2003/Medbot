
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MedBot</title>
</head>
<body>
    <h1>Medical Chatbot</h1>

    <!-- Embed Streamlit interface using an iframe -->
    <iframe src="http://localhost:8501" width="800" height="600"></iframe>

    <script>
        // Example: Send message to Streamlit chatbot
        function sendMessage(message) {
            // Replace 'iframe_id' with the actual ID of your iframe
            var iframe = document.getElementById('iframe_id');
            iframe.contentWindow.postMessage({ type: 'message', text: message }, '*');
        }

        // Example: Receive response from Streamlit chatbot
        window.addEventListener('message', function(event) {
            if (event.origin !== 'http://localhost:8501/') return; // Ensure message is from Streamlit
            if (event.data.type === 'response') {
                var response = event.data.text;
                // Display response to the user
                console.log('Response from chatbot:', response);
            }
        });
    </script>
</body>
</html>
