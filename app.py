from flask import Flask, request, jsonify, render_template
import yt_dlp
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # yt-dlp options: get direct video URL
    ydl_opts = {
        "quiet": True,
        "format": "mp4",
        "skip_download": True,
        "noplaylist": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            # Get the best video URL (mp4)
            video_url = info.get("url")
            title = info.get("title") or "video"
    except Exception as e:
        return jsonify({"error": "Video not available. Make sure the link is public and valid."}), 400

    return jsonify({
        "title": title,
        "download_url": video_url
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
