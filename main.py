from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
from pytz import timezone
import os

app = FastAPI()

@app.get("/api")
def api(slack_name: str, track: str):
    # Get the current day of the week.
    current_day = datetime.datetime.now().weekday()

    # Get the current UTC time.
    current_utc_time = datetime.datetime.utcnow()

    # Get the GitHub URL of the file being run.
    file_url = "https://github.com/delaworla/backend_track/main.py"

    # Get the GitHub URL of the full source code.
    repo_url = "https://github.com/delaworla/backend_track"

    # Create the response payload.
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "current_utc_time": current_utc_time,
        "track": track,
        "file_url": file_url,
        "repo_url": repo_url,
    }

    return response
