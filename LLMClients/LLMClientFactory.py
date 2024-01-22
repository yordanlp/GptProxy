import os
from .BaseLLMClient import BaseLLMClient
from .OpenAIClient import OpenAIClient


class LLMClientFactory():

    @staticmethod
    def CreateClient( client_key, config = {} ) -> BaseLLMClient:
        
        if client_key == "OPEN_AI":
            api_key = os.getenv("OPENAI_API_KEY")
            return OpenAIClient(api_key, config['model_name'])
        
        ## Here you could add implementation to create another LLM Clients like custom made or from another provider