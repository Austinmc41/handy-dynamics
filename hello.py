import vertexai
from vertexai import agent_engines # For the prebuilt templates
from google.adk.agents import Agent
from vertexai.agent_engines import AdkApp
from google.genai import types

model = "gemini-2.0-flash"

# setting up the environment
vertexai.init(  # For service interactions via client.agent_engines
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
   name='currency_exchange_agent',                   # Required. change by use case
   generate_content_config=generate_content_config,  # Optional.
)
app = AdkApp(agent=agent)

# for deployment
requirements = [
    "google-cloud-aiplatform[adk]",
]
gcs_dir_name = "dev"

remote_agent = vertexai.agent_engines.create(
    agent,
    min_instances=1,
    max_instances = 1,
    resource_limits= {"cpu": "4", "memory": "8Gi"},
    container_concurrency= 1,
    requirements=requirements,
    gcs_dir_name=gcs_dir_name,
)







