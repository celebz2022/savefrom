from flask import Flask, request, jsonify, render_template
import yt_dlp
import os

app = Flask(__name__)

# Serve frontend
@app.route("/")
def index():
    return render_template("index.html")

# API endpoint to get Instagram video URL
@app.route("/download", methods=["POST"])
def download():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        # Optional: Login if needed (for private posts)
        # "username": os.environ.get("INSTA_USER"),
        # "password": os.environ.get("INSTA_PASS")
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
        except Exception as e:
            return jsonify({"error": f"Video not available. {str(e)}"}), 400

    return jsonify({
        "title": info.get("title"),
        "download_url": info.get("url")
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
