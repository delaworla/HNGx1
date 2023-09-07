from fastapi import FastAPI, HTTPException, Query
from datetime import datetime
from pytz import timezone

app = FastAPI()


@app.get("/api")
async def get_info(
    slack_name: str = Query(..., description="Slack name"),
    track: str = Query(..., description="Track"),
):
    try:
        # Get current day of the week in the 'UTC' timezone
        utc_timezone = timezone("UTC")
        current_day = datetime.now(utc_timezone).strftime("%A")

        # Get current UTC time with validation of +/-2 minutes
        utc_time = datetime.now(utc_timezone)
        utc_offset_minutes = (
            utc_time.utcoffset().total_seconds() / 60
        )  # Convert to minutes

        if abs(utc_offset_minutes) > 2:
            raise HTTPException(status_code=400, detail="Invalid UTC offset")

        # Create the JSON response
        response_data = {
            "Slack name": slack_name,
            "Current day of the week": current_day,
            "Current UTC time": utc_time.strftime("%Y-%m-%d %H:%M:%S %Z"),
            "Track": track,
            "GitHub URL of the file being run": f"https://github.com/delaworla/backend_track/main.py",
            "GitHub URL of the full source code": f"https://github.com/delaworla/backend_track",
        }

        return response_data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=80)
