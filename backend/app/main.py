from fastapi import FastAPI

app = FastAPI(title="Device Validation Platform API")

@app.get("/")
def read_root():
    return {"message": "Hello, Device Validation Platform!"}
