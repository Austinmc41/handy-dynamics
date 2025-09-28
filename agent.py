import vertexai
from google.adk.agents import Agent
from vertexai.agent_engines import AdkApp
from google.genai import types


model = "gemini-2.0-flash"

# setting up the environment
vertexai.init(  # For services interactions via client.agent_engines
    project="handy-bot",
    location="us-east4",
    staging_bucket="gs://handy-agent-store"
)

# Develop an Agent Development Kit agent
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


agent = Agent(
   model=model,                                      # Required.
   name='handy_agent',# Required. change by use case
   generate_content_config=generate_content_config,  # Optional.
   instruction='''You are Forrest. Forrest is a handy services small business owner with a wealth of knowledge 
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
                  Don't EVER use dashes. ''',
)

# local app
app = AdkApp(agent=agent,
             enable_tracing=True,)

# for deployment
requirements = [
    "google-cloud-aiplatform[adk]",
]
gcs_dir_name = "dev"

# deployed agent engine
# remote_agent = vertexai.agent_engines.create(
#     agent,
#     min_instances=1,
#     max_instances = 1,
#     resource_limits= {"cpu": "4", "memory": "8Gi"},
#     container_concurrency= 1,
#     requirements=requirements,
#     gcs_dir_name=gcs_dir_name,
# )






