from fastapi import FastAPI

app = FastAPI(
    title="CloudSense AI",
    description="AI-Powered Multi-Cloud Intelligence Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to CloudSense AI 🚀",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }