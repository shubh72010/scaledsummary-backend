from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route("/summary", methods=["POST"])
def get_summary():
    data = request.get_json()
    video_url = data.get("url", "")
    video_id = video_url.split("v=")[-1]
    
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry["text"] for entry in transcript])
        return jsonify({"transcript": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/", methods=["GET"])
def home():
    return "Backend is up and running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
