from csv_files import list_csv_files
from data_analyzer import analyze_data
from data_loader import load_data
from model_selection import select_model

# Handle dataset selection and loading
def select_dataset():
    file_path = list_csv_files()
    if not file_path:
        return None, None
    
    # Load dataset
    df = load_data(file_path)
    if isinstance(df, str):
        print(df)
        return file_path, None
    
    return file_path, df
    
def main():
    # Select AI model
    selected_model = select_model()
    if not selected_model:
        return
    
    # Select dataset
    file_path, df = select_dataset()
    if not file_path or df is None:
        return
    
    print("\nWelcome to the Data Analysis Agent!")
    print(f"\nUsing AI Model: {selected_model}")
    print(f"\nDataset columns: ${list(df.columns)}")
    
    while True:
        print("\nMain Menu:")
        print("1. Select AI Model")
        print("2. Select Dataset")
        print("3. Analyze Data")
        print("4. Exit")
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            selected_model = select_model()
            if not selected_model:
                return
        elif choice == '2':
            # Select dataset
            file_path, df = select_dataset()
            if not file_path or df is None:
                return
        elif choice == '3':
            while True:
                query = input("\nEnter your query for data analysis(or type 'quit'/'exit'/'stop'/'bye' to exist): ").strip().lower()
            
                # Check for exit commands
                if(query.lower() in ['quit', 'exit', 'stop', 'bye']):
                    print("\nExiting the Data Analysis Agent. Goodbye!")
                    break
            
                # Analyze the query
                result, ollama_response = analyze_data(df, query, selected_model)
                if isinstance(result, str) or ollama_response is None:
                    print(result)
                else:
                    print("Analysis Result:")
                    print(result)
        elif choice == '4':
            print("\nExiting the Data Analysis Agent. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option (1-4).")


if __name__ == "__main__":
    main()