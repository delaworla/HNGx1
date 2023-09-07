from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
import os

app = FastAPI()


@app.get("/get_info")
async def get_info(
    slack_name: str = Query(..., description="Slack name"),
    track: str = Query(..., description="Track"),
):
    # Get current day of the week in the 'UTC' timezone
    utc_timezone = timezone("UTC")
    current_day = datetime.now(utc_timezone).strftime("%A")

    # Get current UTC time with validation of +/-2
    utc_time = datetime.now(utc_timezone)
    utc_offset = utc_time.utcoffset().total_seconds() / 3600  # Convert to hours

    if abs(utc_offset) > 2:
        raise HTTPException(status_code=400, detail="Invalid UTC offset")

    # Get GitHub URLs from environment variables
    github_url_file = os.environ.get("GITHUB_URL_FILE", "Not available")
    github_url_source = os.environ.get("GITHUB_URL_SOURCE", "Not available")

    # Create the JSON response
    response_data = {
        "Slack name": slack_name,
        "Current day of the week": current_day,
        "Current UTC time": utc_time.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "Track": track,
        "GitHub URL of the file being run": github_url_file,
        "GitHub URL of the full source code": github_url_source,
    }

    return response_data
