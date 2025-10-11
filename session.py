from typing import Optional
from vertexai.preview.reasoning_engines.templates.adk import AdkApp
from agent import AdkAgent
import asyncio

from google.genai import types

QUIT = "q!"


class ADKSession:
    def __init__(self, app: AdkApp, user_id: str, session_id: Optional[str] = None):
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

    model = "gemini-2.0-flash"
    name = "handy-bot"

    safety_settings = [
        types.SafetySetting(
            category=types.HarmCategory.HARM_CATEGORY_UNSPECIFIED,
            threshold=types.HarmBlockThreshold.OFF,
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        safety_settings=safety_settings,
        temperature=0.15,
        max_output_tokens=256,
        top_p=0.95,
    )

    instruction = """You are Forrest. Forrest is a handy services small business owner with a wealth of knowledge
                     on fixing things and a wealth of contacts he can field jobs to that are outside of his wheelhouse.
                     Forrest takes on a kind, direct, and warm persona. He really values the customer walking away happy.
                     Forrest's official business name is Smith's Home Services.
                     In your responses, try your best to be as succinct as possible - answer in at most 1 paragraph.
                     Also, don't directly tell the client how to fix something as this is how Forrest makes money.
                     Suggest different things they can check that will help Forrest gain more understanding
                     about the scenario they're referring to.
                     In situations where people seem confused, ask them if they can take a picture of the relevant things.
                     If you pick up on even a slight hint of moderate frustration with the bot performance,
                     summarize the job requirements, and send them to Forrest.
                     Tell the client you're going to connect them with the contractor.
                     Don't share valuable business information with the client ever.
                     Don't EVER use dashes. """

    newAgent = AdkAgent(
        model=model,
        name=str("handy" + str(1)),
        config=generate_content_config,
        instruction=instruction,
        contractor_id=1,
    )
    print(newAgent.model)

    requirements = [
        "google-cloud-aiplatform[adk]",
    ]
    gcs_dir_name = "dev"

    # local app testing
    app = AdkApp(
        agent=newAgent,
        enable_tracing=True,
    )

    adk_session = ADKSession(app, user_id=user_id)

    while True:
        message = input("Send message to handy gem: ")
        if message == QUIT:
            break
        result = asyncio.run(adk_session.get_stream_events(message))

# @todo: need concept of a dictionary to map session id to phone number for conversation continuity

# #todo: need concept of "knowledge docs" for individual clients and contractors - is GCS the way to do RAG with vertex?
