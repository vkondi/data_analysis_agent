import os
import glob

def list_csv_files():
    # Check if data folder exists
    data_folder = "data"
    if not os.path.exists(data_folder):
        print("Data folder does not exist. Please create a 'data' folder and place your CSV files there.")
        return None
    
    # Retrieve all CSV files in the data folder
    csv_files = glob.glob(os.path.join(data_folder, "*.csv"))
    
    if not csv_files:
        print("No CSV files found in the data folder. Add some CSV files to proceed.")
        return None
    
    # List the CSV files
    print("Available CSV files:")
    for i, file in enumerate(csv_files):
        print(f"{i +1}. {os.path.basename(file)}")
        
    # Get user input for file selection
    while True:
        try:
            choice = input("\nSelect a file to analyze by number (or type 'exit' to quit):").strip()
            if choice.lower() in ['exit','quit', 'stop', 'bye']:
                print("\nExiting the data analysis agent. Goodbye!\n")
                return None
            
            if 1 <= int(choice) <= len(csv_files):
                return csv_files[int(choice) - 1]
            else:
                print(f"\nPlease enter a number between 1 and {len(csv_files)}.")
        except ValueError:
            print("\nInvalid input. Please enter a number corresponding to the file.")
            continue