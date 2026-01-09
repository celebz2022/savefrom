<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Instagram & Social Media Downloader</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <div class="container">
        <h2>Instagram & Social Media Downloader</h2>
        <form id="download-form" method="POST" action="/download_video" target="_blank">
            <input type="text" name="url" placeholder="Paste video URL here" required>
            <button type="submit" onclick="openAffiliate()">Download</button>
        </form>
        <footer>Powered by your affiliate link</footer>
    </div>

    <script>
    function openAffiliate() {
        // Open Amazon affiliate link in new tab
        window.open("https://www.amazon.ae/dp/B07DX89ZHN?tag=healthhackzon-21", "_blank");
    }
    </script>
</body>
</html>
