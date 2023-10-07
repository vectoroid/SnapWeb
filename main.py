"""
WebSnap

Snapshots of any web-based image, page section, or entire webpage: anything which can be displayed on a single screen.
"""

import deta

from fastapi import FastAPI


# initialize App
app_title = "WebSnap"
app_version = "0.1"
app_description = "Snapshots of any web-based image, page section, or entire webpage: anything which can be displayed on a single screen."

app = FastAPI(title=app_title, description=app_description)


# App Routes
@app.get("/")
async def root():
    return {"message": "Hello World"}