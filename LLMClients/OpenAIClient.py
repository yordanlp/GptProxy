from langchain_openai import ChatOpenAI
import openai
from Models.LLMResponse import LLMResponse
from .BaseLLMClient import BaseLLMClient

class OpenAIClient(BaseLLMClient):

    def __init__(self, openai_api_key, model_name):
        super().__init__() 
        self.client = ChatOpenAI(openai_api_key=openai_api_key, model_name=model_name)

    def query(self, prompt_text) -> LLMResponse:
        try:
            response = self.client.invoke(prompt_text)
        except openai.APIError as error:
            return LLMResponse("", error.status_code, [error.body])

        return LLMResponse(response.content)
