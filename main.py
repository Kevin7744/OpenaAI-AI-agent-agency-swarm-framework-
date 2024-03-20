from agency_swarm import set_openai_key
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.environ("OPENAI_API_KEY")

set_openai_key(openai_api_key)

