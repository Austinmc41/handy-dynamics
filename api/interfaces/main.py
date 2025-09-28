from fastapi import FastAPI

app = FastAPI()

@app.get('/bot_users')
async def get_bot_users():
    return ["User1", "User2"]
