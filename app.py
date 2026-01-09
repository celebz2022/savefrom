from flask import Flask, render_template, request, send_file
import requests
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download_video", methods=["POST"])
def download_video():
    video_url = request.form.get("url")
    if not video_url:
        return "No video URL provided", 400

    # Download the video to a temporary file
    try:
        r = requests.get(video_url, stream=True)
        filename = "video.mp4"
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    except Exception as e:
        return f"Error downloading video: {e}", 500

    # Send the file to user as attachment (download)
    response = send_file(filename, as_attachment=True)
    
    # Remove temporary file after sending
    if os.path.exists(filename):
        os.remove(filename)

    return response

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
