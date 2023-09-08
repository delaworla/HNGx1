from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
from pytz import timezone
import response

app = FastAPI()

utc_timezone = timezone("UTC")
current_day = datetime.now(utc_timezone).strftime("%A")

       
utc_time = datetime.now(utc_timezone)
utc_offset_minutes = (
            utc_time.utcoffset().total_seconds() / 60
        )  

if abs(utc_offset_minutes) > 2:
    raise HTTPException(status_code=400, detail="Invalid UTC offset")



@app.get("/")
async def get_info():
    
    
    response_data = {
            "Slack name": slack_name,
            "Current day of the week": current_day,
            "Current UTC time": utc_time.strftime("%Y-%m-%d %H:%M:%S %Z"),
            "Track": track,
            "GitHub URL of the file being run": f"https://github.com/delaworla/backend_track/main.py",
            "GitHub URL of the full source code": f"https://github.com/delaworla/backend_track",
            "Status code": print(response.status_code)
        }
    return response_data
