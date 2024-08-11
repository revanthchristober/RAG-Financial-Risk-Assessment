# src/generator.py

from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

class TextGenerator:
    def __init__(self, api_key: str):
        self.llm = OpenAI(api_key=api_key)
        self.prompt_template = PromptTemplate(
            input_variables=["data"],
            template="Analyze the following financial data: {data}",
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt_template)

    def generate_text(self, data: str) -> str:
        """Generates text based on the provided data."""
        try:
            response = self.chain.run(data=data)
            return response
        except Exception as e:
            print(f"Error generating text: {e}")
            return ""
