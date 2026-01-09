from flask import Flask, request, jsonify, render_template
import yt_dlp
import os

app = Flask(__name__)

# Only the affiliate tag
AFFILIATE_ID = os.environ.get("HEALTH_AFFILIATE_ID", "healthhackzon-21")

@app.route("/")
def index():
    # Amazon link with your affiliate tag
    affiliate_link = f"https://www.amazon.com/?tag={AFFILIATE_ID}"
    return render_template("index.html", affiliate_link=affiliate_link)

@app.route("/download", methods=["POST"])
def download():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    ydl_opts = {"quiet": True, "skip_download": True}

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get("url")
            title = info.get("title")
            if not video_url:
                raise Exception("Video URL not found")
    except Exception:
        return jsonify({
            "error": "Video not available. Make sure the link is public and valid."
        }), 400

    return jsonify({
        "title": title,
        "download_url": video_url
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
