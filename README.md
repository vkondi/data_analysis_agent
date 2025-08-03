# Data Analysis Agent

A Python-based interactive data analysis tool that leverages local AI models (via Ollama) to perform intelligent data analysis on CSV files. This application allows users to ask natural language queries about their data and receive automated pandas-based analysis results.

## Features

- **Interactive Data Analysis**: Ask questions about your data in natural language
- **Local AI Integration**: Uses Ollama for local AI model inference
- **CSV File Support**: Automatically detects and loads CSV files from the `data/` directory
- **Multiple AI Models**: Choose from available local AI models
- **Pandas Integration**: Generates and executes pandas commands for data analysis
- **User-Friendly Interface**: Simple menu-driven interface for easy navigation

## Prerequisites

Before running this application, you need to have:

1. **Python 3.7+** installed on your system
2. **Ollama** installed and running locally
   - Download from: https://ollama.ai/
   - Install and start the Ollama service
3. **At least one AI model** pulled in Ollama (e.g., `llama2`, `codellama`, `mistral`)

## Installation

1. **Clone or download** this repository to your local machine

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare your data**:
   - Create a `data/` folder in the project directory
   - Place your CSV files in the `data/` folder
   - The application will automatically detect available CSV files

4. **Start Ollama** (if not already running):
   ```bash
   ollama serve
   ```

5. **Pull an AI model** (if you haven't already):
   ```bash
   ollama pull llama2
   # or any other model like:
   # ollama pull codellama
   # ollama pull mistral
   ```

## Usage

1. **Start the application**:
   ```bash
   python main.py
   ```

2. **Select an AI Model**: Choose from available local models

3. **Select a Dataset**: Pick a CSV file from the `data/` directory

4. **Analyze Data**: Ask questions about your data in natural language

### Example Queries

- "What is the average sales?"
- "Show me the top 5 highest values in the salary column"
- "Count the number of rows"
- "What is the correlation between age and salary?"
- "Group by department and show the mean salary"

## Project Structure

```
data_analysis_agent/
├── main.py              # Main application entry point
├── data_analyzer.py     # Core data analysis logic
├── model_selection.py   # AI model selection interface
├── ollama_client.py     # Ollama API integration
├── csv_files.py         # CSV file management
├── data_loader.py       # Data loading utilities
├── requirements.txt     # Python dependencies
├── data/               # Directory for CSV files
│   ├── sales_data.csv
│   ├── emp_data.csv
│   └── ...
└── README.md           # This file
```

## How It Works

1. **Model Selection**: The application connects to Ollama's API to discover available local AI models
2. **Data Loading**: CSV files are automatically detected and loaded using pandas
3. **Query Processing**: Natural language queries are sent to the selected AI model
4. **Code Generation**: The AI model generates appropriate pandas commands
5. **Execution**: The generated pandas code is executed on the dataset
6. **Results**: Analysis results are displayed to the user

## Supported Data Formats

- **CSV files** only (placed in the `data/` directory)
- Files should have headers (column names)
- Standard CSV format with comma separators

## Troubleshooting

### Common Issues

1. **"No AI models available"**
   - Ensure Ollama is running: `ollama serve`
   - Pull at least one model: `ollama pull llama2`

2. **"No CSV files found"**
   - Create a `data/` folder in the project directory
   - Place your CSV files in the `data/` folder

3. **Connection errors**
   - Verify Ollama is running on `http://localhost:11434`
   - Check if the Ollama service is accessible

4. **Analysis errors**
   - Ensure your CSV files have proper headers
   - Check that column names in queries match your data
   - Verify data types are appropriate for the analysis

## Dependencies

- `pandas==2.3.1` - Data manipulation and analysis
- `requests==2.32.4` - HTTP requests for Ollama API

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this data analysis agent.

---

**Note**: This application requires Ollama to be running locally with at least one AI model installed. Make sure you have sufficient system resources for running local AI models.