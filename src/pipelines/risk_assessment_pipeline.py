# src/pipelines/risk_assessment_pipeline.py

from utils.data_processing import clean_data
from utils.logging_utils import setup_logging

class RiskAssessmentPipeline:
    def __init__(self, retriever, generator):
        self.retriever = retriever
        self.generator = generator
        self.logger = setup_logging()

    def run(self):
        """Runs the full risk assessment pipeline."""
        self.logger.info("Loading data...")
        data = self.retriever.load_data()

        self.logger.info("Cleaning data...")
        clean_data_df = clean_data(data)

        self.logger.info("Generating insights...")
        prompt = f"Analyze the following financial data: {clean_data_df.head().to_string()}"
        insights = self.generator.generate_text(prompt)

        self.logger.info("Generated Insights:")
        self.logger.info(insights)
