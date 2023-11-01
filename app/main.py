import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="BlockstakML API",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)

@app.get("/")
async def root():
    return {"message": "Successful Connection"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)