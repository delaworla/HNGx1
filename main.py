from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
from pytz import timezone


app = FastAPI()




@app.get("/api")
async def api(slack_name: str, track: str):
    
    
    response_data = {
            "Slack name": slack_name,
            "Current day of the week": current_day,
            "Current UTC time": utc_time.strftime("%Y-%m-%dT%H:%M:%S %Z"),
            "Track": track,
            "GitHub URL of the file being run": f"https://github.com/delaworla/backend_track/main.py",
            "GitHub URL of the full source code": f"https://github.com/delaworla/backend_track",
            "status_code": status_code,
        }
    return response_data
