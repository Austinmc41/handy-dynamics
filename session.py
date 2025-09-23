from typing import Optional
from vertexai.preview.reasoning_engines.templates.adk import AdkApp
from agent import app
import asyncio

QUIT = "q!"

class ADKSession:
    def __init__(self, app: AdkApp, user_id: str, session_id: Optional[str]= None):
        self.app = app
        self.user_id = user_id
        if session_id:
            self.session_id = session_id
        else:
            session = asyncio.run(self.create_session(app, self.user_id))
            self.session_id = session.id

    async def create_session(self, app: AdkApp, user_id: str):
        return await app.async_create_session(user_id=user_id)

    async def get_session(self, app: AdkApp, user_id: str, session_id: str):
        await app.async_get_session(user_id=user_id, session_id=session_id)

    async def list_sessions(self, app: AdkApp, user_id: str):
        await app.async_list_sessions(user_id=user_id)

    async def get_stream_events(self, message: str):
        """
        Calls an asynchronous streaming function and collects events.

        The 'async for' loop pauses and resumes execution for each event,
        allowing other tasks to run concurrently.
        """
        events = []
        print("Collecting events...")
        async for event in app.async_stream_query(
                user_id=self.user_id,
                session_id=self.session_id,
                message=message,
        ):
            print(f"Received event: {event}")
            events.append(event)

        print("\nAll events collected.")
        return events

if __name__ == "__main__":
    user_id = "12345"
    adk_session = ADKSession(app, user_id=user_id)

    while True:
        message = input("Send message to handy gem: ")
        if message == QUIT:
            break
        result = asyncio.run(adk_session.get_stream_events(message))

# @todo: need concept of a dictionary to map session id to phone number for conversation continuity

# #todo: need concept of "knowledge docs" for individual clients and contractors - is GCS the way to do RAG with vertex?




