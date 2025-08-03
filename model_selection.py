import requests

# Cache local AI models
AI_MODELS = None

def get_available_models():
    """
    Returns a list of available local AI models.
    """
    
    # Check if AI_MODELS is already cached
    global AI_MODELS
    if AI_MODELS is not None:
        return AI_MODELS
    
    try:
        response = requests.get("http://localhost:11434/api/tags")
        response.raise_for_status()
        models_data = response.json()
        AI_MODELS = [model['name'] for model in models_data.get('models', [])]
        return AI_MODELS
    except requests.RequestException as e:
        print(f"Error fetching models: {str(e)}")
        return None
 

def select_model():
    models = get_available_models()
    if not models:
        print("No AI models available for selection.")
        return None
    
    print("\nAvailable AI Models:")
    for i, model in enumerate(models):
        print(f"{i+1}. {model}")
        
    while True:
        try:
            choice = input("\nSelect an AI model by number (or type 'exit' to quit): ").strip()
            
            # Handle exit commands - default to the first model
            if choice.lower() in ['exit', 'quit', 'stop', 'bye']:
                print(f"\nDefaulting to the first AI model: {models[0]}")
                return models[0]
            
            if 1 <= int(choice) <= len(models):
                return models[int(choice) - 1]
            else:
                print(f"\n Please enter a number between 1 and {len(models)}.")
        except ValueError:
            print("\nInvalid input. Please enter a number corresponding to the model.")
            continue
            