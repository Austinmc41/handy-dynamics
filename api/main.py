import uvicorn
from fastapi import FastAPI
from api.routers import bot_users, adk_sessions

app = FastAPI()


app.include_router(bot_users.router)
app.include_router(adk_sessions.router)

@app.get("/")
def root():
    return {"message": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)