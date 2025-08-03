import pandas as pd

from csv_files import list_csv_files
from data_analyzer import analyze_data
from data_loader import load_data

def main():
    # Select dataset
    file_path = list_csv_files()
    if not file_path:
        return
    
    # Load dataset
    df = load_data(file_path)
    if isinstance(df, str):
        print(df)
        return
    
    print("\nWelcome to the Data Analysis Agent!")
    print(f"\nDataset columns: ${list(df.columns)}")
    
    while True:
        query = input("\nEnter your query for data analysis(or type 'quit'/'exit'/'stop'/'bye' to exist): ").strip().lower()
        
        # Check for exit commands
        if(query.lower() in ['quit', 'exit', 'stop', 'bye']):
            print("\nExiting the Data Analysis Agent. Goodbye!")
            break
        
        # Analyze the query
        result, ollama_response = analyze_data(df, query)
        if isinstance(result, str) or ollama_response is None:
            print(result)
        else:
            print("Analysis Result:")
            print(result)

if __name__ == "__main__":
    main()