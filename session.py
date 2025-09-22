from google.adk.sessions import Session
from vertexai.preview.reasoning_engines.templates.adk import AdkApp
from agent import app
import asyncio

QUIT = "q!"

async def create_session(app: AdkApp, user_id: str):
    return await app.async_create_session(user_id=user_id)

async def get_session(app: AdkApp, user_id: str, session_id: str):
    await app.async_get_session(user_id=user_id, session_id=session_id)

async def list_sessions(app: AdkApp, user_id: str):
    await app.async_list_sessions(user_id=user_id)


async def get_stream_events(session: Session, message: str):
    """
    Calls an asynchronous streaming function and collects events.

    The 'async for' loop pauses and resumes execution for each event,
    allowing other tasks to run concurrently.
    """
    events = []
    print("Collecting events...")
    async for event in app.async_stream_query(
            user_id="12345",
            session_id=session.id,
            message=message,
    ):
        print(f"Received event: {event}")
        events.append(event)

    print("\nAll events collected.")
    return events


session = asyncio.run(create_session(app,"12345"))


while True:
    message = input("Send message to handy gem: ")

    if message == QUIT:
        break

    result = asyncio.run(get_stream_events(session, message))

# @todo: need concept of a dictionary to map session id to phone number for conversation continuity




