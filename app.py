from flask import Flask, request, jsonify, render_template, send_file
import yt_dlp
import os
import uuid

app = Flask(__name__)

# Ensure downloads folder exists
os.makedirs("downloads", exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download", methods=["POST"])
def download():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    # Generate a unique filename
    filename = f"{uuid.uuid4()}.mp4"
    filepath = os.path.join("downloads", filename)

    # yt-dlp options
    ydl_opts = {
        "format": "mp4",
        "quiet": True,
        "outtmpl": filepath,
        "noplaylist": True,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        return jsonify({"error": f"Video not available: {str(e)}"}), 400

    return jsonify({
        "download_url": f"/get_video/{filename}"
    })

@app.route("/get_video/<filename>")
def get_video(filename):
    filepath = os.path.join("downloads", filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
