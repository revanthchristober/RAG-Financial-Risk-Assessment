# src/main.py

from retriever import DataRetriever
from generator import TextGenerator
from pipelines import RiskAssessmentPipeline
from config import Config

def main():
    # Load data
    retriever = DataRetriever(Config.DATA_PATH)
    data = retriever.load_data()

    # Initialize Text Generator
    generator = TextGenerator(api_key=Config.API_KEY)

    # Run the RAG pipeline
    pipeline = RiskAssessmentPipeline(retriever, generator)
    pipeline.run()

if __name__ == "__main__":
    main()
