from agency_swarm import set_openai_key
import os
from dotenv import load_dotenv

from Tools.tool_browsing import BrowsingTool
from Tools.tool_langchain import LangchainTool

from agency_swarm import Agent
from agency_swarm import Agency


load_dotenv()

openai_api_key = os.environ("OPENAI_API_KEY")

set_openai_key(openai_api_key)
  

ceo = Agent(name="CEO",
            description="Responsible for client communication, task planning and management.",
            instructions="You must converse with other agents to ensure complete task execution.", # can be a file like ./instructions.md
            files_folder="./files", # files to be uploaded to OpenAI
            schemas_folder="./schemas", # OpenAPI schemas to be converted into tools
            tools=[BrowsingTool, LangchainTool])

# Agency communication flows
agency = Agency([
    ceo,  # CEO will be the entry point for communication with the user
    [ceo, dev],  # CEO can initiate communication with Developer
    [ceo, va],   # CEO can initiate communication with Virtual Assistant
    [dev, va]    # Developer can initiate communication with Virtual Assistant
], shared_instructions='agency_manifesto.md') # shared instructions for all agents