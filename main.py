from flask import Flask, request, jsonify
import datetime
import pytz
import os

app = Flask(__name__)


@app.route("/get_info", methods=["GET"])
def get_info():
    # Get query parameters
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    # Get current day of the week
    current_day = datetime.datetime.now().strftime("%A")

    # Get current UTC time with validation of +/-2
    utc_time = datetime.datetime.now(pytz.utc)
    utc_offset = utc_time.utcoffset().total_seconds() / 3600  # Convert to hours

    if abs(utc_offset) <= 2:
        utc_time_str = utc_time.strftime("%Y-%m-%d %H:%M:%S %Z")
    else:
        return jsonify({"error": "Invalid UTC offset"}), 400

    # Get GitHub URLs
    github_url_file = os.environ.get("GITHUB_URL_FILE", "Not available")
    github_url_source = os.environ.get("GITHUB_URL_SOURCE", "Not available")

    # Create the JSON response
    response_data = {
        "Slack name": slack_name,
        "Current day of the week": current_day,
        "Current UTC time": utc_time_str,
        "Track": track,
        "GitHub URL of the file being run": github_url_file,
        "GitHub URL of the full source code": github_url_source,
    }

    return jsonify(response_data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
