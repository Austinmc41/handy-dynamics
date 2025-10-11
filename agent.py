import vertexai
from google.adk.agents import LlmAgent
from google.genai.types import GenerateContentConfig
from pydantic import ConfigDict
from vertexai.agent_engines import AdkApp
from google.genai import types
import argparse


class AdkAgent(LlmAgent):
    contractor_id: int
    config: GenerateContentConfig
    model_config = ConfigDict(extra="allow")


if __name__ == "__main__":

    model = "gemini-2.0-flash"

    # setting up the environment
    vertexai.init(  # For services interactions via client.agent_engines
        project="handy-bot",
        location="us-east4",
        staging_bucket="gs://handy-agent-store",
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

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name")
    parser.add_argument("-i", "--instruction")
    args = parser.parse_args()
    name = args.name
    instruction = args.instruction

    newAgent = AdkAgent(
        model=model,
        name=name,
        config=generate_content_config,
        instruction=instruction,
        contractor_id=1,
    )

    requirements = [
        "google-cloud-aiplatform[adk]",
    ]
    gcs_dir_name = "dev"

    # local app testing
    # app = AdkApp(agent=newAgent,
    #              enable_tracing=True,)

    # deployed agent engine
    remote_agent = vertexai.agent_engines.create(
        newAgent,
        min_instances=1,
        max_instances=1,
        resource_limits={"cpu": "4", "memory": "8Gi"},
        container_concurrency=1,
        requirements=requirements,
        gcs_dir_name=gcs_dir_name,
    )
