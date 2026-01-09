from flask import Flask, request, jsonify, render_template
import yt_dlp
import os

app = Flask(__name__)

# Read Amazon affiliate ID from environment variable
AFFILIATE_ID = os.environ.get("HEALTH_AFFILIATE_ID", "healthhackzon-21")
AMAZON_PRODUCT_ID = os.environ.get("AMAZON_PRODUCT_ID", "B09XYZ123")  # Replace with your product

@app.route("/")
def index():
    # Generate affiliate link dynamically
    affiliate_link = f"https://www.amazon.com/dp/{AMAZON_PRODUCT_ID}?tag={AFFILIATE_ID}"
    return render_template("index.html", affiliate_link=affiliate_link)

@app.route("/download", methods=["POST"])
def download():
    url = request.json.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    ydl_opts = {"quiet": True, "skip_download": True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
        except Exception as e:
            return jsonify({"error": "Failed to fetch video. Make sure the link is public."}), 400

    return jsonify({
        "title": info.get("title"),
        "download_url": info.get("url")
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
