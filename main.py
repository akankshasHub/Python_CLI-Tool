import click
import requests
import os

# Set your Ollama API endpoint and key
OLLAMA_API_URL = "https://ollama.com/library/qwen2:0.5b"
OLLAMA_API_KEY = "ollama run qwen2:0.5b"  # Replace with your actual API key

def summarize_text(text):
    headers = {
        "Authorization": f"Bearer {OLLAMA_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "qwen2:0.5b",
        "text": text
    }
    response = requests.post(OLLAMA_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("summary", "No summary found")
    else:
        return f"Error: {response.status_code} - {response.text}"

@click.command()
@click.option('-t', '--text-file', type=click.Path(exists=True), help="Path to the text file.")
@click.argument('text', nargs=-1)
def main(text_file, text):
    if text_file:
        with open(text_file, 'r') as file:
            content = file.read()
    elif text:
        content = ' '.join(text)
    else:
        click.echo("Please provide either a text file or text input.")
        return
    
    summary = summarize_text(content)
    click.echo(f"Summary: {summary}")

if __name__ == '__main__':
    main()
