# RAG-based Financial Risk Assessment Tool

## Overview

The RAG-based Financial Risk Assessment Tool is designed to leverage Retrieval-Augmented Generation (RAG) techniques to assess financial risk using advanced AI models. This project aims to provide insights into financial data and assist in risk assessment through an automated pipeline.

## Project Structure

- **`src/`**: Contains the main source code files.
  - **`__init__.py`**: Initialization file for the `src` module.
  - **`retriever.py`**: Implements data retrieval using a retriever model.
  - **`generator.py`**: Implements text generation using a generator model.
  - **`main.py`**: Main script to run the RAG pipeline.
  - **`config.py`**: Configuration settings for the project.
  - **`utils/`**: Utility functions and helpers.
    - **`data_processing.py`**: Data processing and cleaning functions.
    - **`model_utils.py`**: Helper functions for model operations.
    - **`logging_utils.py`**: Logging functions for debugging.
  - **`tests/`**: Contains unit and integration tests.
    - **`test_retriever.py`**: Unit tests for the retriever module.
    - **`test_generator.py`**: Unit tests for the generator module.
    - **`test_main.py`**: Tests for the main pipeline.
  - **`pipelines/`**: Custom pipelines for complex workflows.
    - **`risk_assessment_pipeline.py`**: Pipeline specific to financial risk assessment.

- **`data/`**: Data storage and management.
  - **`raw/`**: Raw datasets.
  - **`processed/`**: Processed data ready for analysis.

- **`config/`**: Configuration files.
  - **`default_config.yaml`**: General configuration for the project.
  - **`logging_config.yaml`**: Logging configuration.
  - **`pipeline_config.yaml`**: Pipeline-specific configurations.

- **`logs/`**: Logs related to the project.

- **`notebooks/`**: Jupyter Notebooks for experimentation and analysis.
  - **`RAG_pipeline_demo.ipynb`**: Demonstration of the RAG pipeline.
  - **`EDA.ipynb`**: Exploratory Data Analysis (EDA) notebook.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd RAG-Financial-Risk-Assessment
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables (if needed):

   ```bash
   export OPENAI_API_KEY=<your_openai_api_key>
   ```

## Usage

1. **Run the RAG Pipeline**:

   ```bash
   python src/main.py
   ```

   This will execute the RAG pipeline for financial risk assessment.

2. **Demo Notebook**:

   Open and run `notebooks/RAG_pipeline_demo.ipynb` in a Jupyter Notebook environment to see a demonstration of the RAG pipeline.

3. **Exploratory Data Analysis (EDA)**:

   Explore the dataset and perform EDA using `notebooks/EDA.ipynb`.

## Configuration

The configuration files are located in the `config/` directory:
- **`default_config.yaml`**: General settings and model configurations.
- **`logging_config.yaml`**: Settings for logging and debugging.
- **`pipeline_config.yaml`**: Specific configurations for the RAG pipeline.

## Testing

To run the unit and integration tests, use:

```bash
pytest src/tests/
```

## Contribution

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact [revanthchrixtopher@outlook.com](mailto:revanthchrixtopher@outlook.com).