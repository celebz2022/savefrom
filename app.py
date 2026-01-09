from flask import Flask, request, jsonify, send_from_directory
import yt_dlp
import os

app = Flask(__name__)

# Serve the frontend
@app.route("/")
def index():
    return send_from_directory('.', 'index.html')  # '.' is your project folder

# API endpoint to get Instagram video URL
@app.route("/download", methods=["POST"])
def download():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # yt-dlp options: don't download, just extract info
    ydl_opts = {"quiet": True, "skip_download": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return jsonify({
        "title": info.get("title"),
        "download_url": info.get("url")
    })

# Run the app using the PORT provided by Render (or default 5000 locally)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
