from flask import Flask, request, jsonify, render_template
import yt_dlp
import os

app = Flask(__name__)

# Serve the main page
@app.route("/")
def index():
    return render_template("index.html")

# API endpoint to get Instagram video URL
@app.route("/download", methods=["POST"])
def download():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # yt-dlp options: skip download, just extract info
    ydl_opts = {"quiet": True, "skip_download": True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
    except Exception as e:
        return jsonify({"error": "Video not available. Make sure the link is public and valid."}), 400

    return jsonify({
        "title": info.get("title"),
        "download_url": info.get("url")
    })

# Run the app using the PORT provided by Render (or default 5000 locally)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
