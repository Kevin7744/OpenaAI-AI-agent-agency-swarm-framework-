from agency_swarm import set_openai_key
import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.environ("OPENAI_API_KEY")

set_openai_key(openai_api_key)


#  Define your custom tools with Instructor:

from agency_swarm.tools import BaseTool
from pydantic import Field

class BrowsingTool(BaseTool):
    """
    A brief description of what the custom tool does. 
    The docstring should clearly explain the tool's purpose and functionality.
    """

    # Define the fields with descriptions using Pydantic Field
    example_field: str = Field(
        ..., description="Description of the example field, explaining its purpose and usage."
    )

    # Additional fields as required
    # ...

    def run(self):
        """
        The implementation of the run method, where the tool's main functionality is executed.
        This method should utilize the fields defined above to perform its task.
        Doc string description is not required for this method.
        """

        # Your custom tool logic goes here
        do_something(self.example_field)

        # Return the result of the tool's operation
        return "Result of MyCustomTool operation"
    
