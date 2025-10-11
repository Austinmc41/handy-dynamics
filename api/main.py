import uvicorn
from fastapi import FastAPI
from api.routers import bot_users, adk_sessions, contractors, agents, sign_up

app = FastAPI()


app.include_router(bot_users.router)
app.include_router(adk_sessions.router)
app.include_router(contractors.router)
app.include_router(agents.router)
app.include_router(sign_up.router)

@app.get("/")
def root():
    return {"message": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)