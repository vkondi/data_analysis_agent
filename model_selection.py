
# Hardcoded AI models for the data analysis agent
AI_MODELS = ['llama3', 'deepseek-r1']

def select_model():
    if not AI_MODELS:
        print("No AI models available for selection.")
        return None
    
    print("\nAvailable AI Models:")
    for i, model in enumerate(AI_MODELS):
        print(f"{i+1}. {model}")
        
    while True:
        try:
            choice = input("\nSelect an AI model by number (or type 'exit' to quit): ").strip()
            
            # Handle exit commands - default to the first model
            if choice.lower() in ['exit', 'quit', 'stop', 'bye']:
                print(f"\nDefaulting to the first AI model: {AI_MODELS[0]}")
                return AI_MODELS[0]
            
            if 1 <= int(choice) <= len(AI_MODELS):
                return AI_MODELS[int(choice) - 1]
            else:
                print(f"\n Please enter a number between 1 and {len(AI_MODELS)}.")
        except ValueError:
            print("\nInvalid input. Please enter a number corresponding to the model.")
            continue
            