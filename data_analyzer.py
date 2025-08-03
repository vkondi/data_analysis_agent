import pandas as pd

from ollama_client import query_ollama

# Analyze data based on interpreted query
def analyze_data(df, query):
    prompt = f"""
    System: You are a data analysis assistant. The dataset has columns: {list(df.columns)}.
    The user asked: "{query}"
    
    Suggest a pandas operation to answer the query. Return only the pandas command (e.g., df['Sales'].mean()).
    
    Note:
    1. Importantly, ensure the command is valid and can be executed on the DataFrame.
    2. Do not include any explanations or additional text, just the command.
    """
    
    ollama_response = query_ollama(prompt)
    print(f"Ollama's response: {ollama_response}")
    
    # Sanitize Ollama's response
    command = ollama_response.strip().split('\n')[0]  # Take the first line in case of multiple lines
    
    # Normalize column names
    df.columns = [col.strip() for col in df.columns]
    
    try:
        # Evaluate the response as a pandas command
        # Provide the DataFrame as a local variable
        local_vars = {'df': df, "pd": pd}
        result = eval(command, local_vars)
        return result, command
    except Exception as e:
        return f"Error analyzing data: {str(e)}", None