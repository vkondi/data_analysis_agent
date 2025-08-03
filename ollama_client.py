import requests
import json

# Ollama API endpoint (default local endpoint)
OLLAMA_API = "http://localhost:11434/api/generate"

# Query Ollama to interpret the user's query
def query_ollama(prompt, selected_model):
    payload = {
        "model": selected_model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_API, json=payload)
        response.raise_for_status()
        return json.loads(response.text)['response']
    except Exception as e:
        return f"Error querying Ollama API: {str(e)}"