from flask import Flask, request, send_file, render_template
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/download")
def download():
    url = request.args.get("url")
    if not url:
        return "No URL provided", 400

    opts = {
        "outtmpl": os.path.join(DOWNLOAD_FOLDER, "%(title)s.%(ext)s"),
        "quiet": True,
        "format": "mp4",
    }

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        return send_file(
            filename,
            as_attachment=True,
            download_name=os.path.basename(filename),
            mimetype="video/mp4"
        )
    except Exception as e:
        return f"Error downloading video: {str(e)}", 500

if __name__ == "__main__":
    app.run(debug=True)
