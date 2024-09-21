from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
HF_TOKEN = "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"
REPO_ID = "mistralai/Mistral-7B-Instruct-v0.2"

# Function to read text from a .txt file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Function to save summary to a .txt file
def save_summary_to_file(summary, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(summary)
    logger.info(f"Summary saved to {output_file}")

def count_words(text):
    words = text.split()  # Split the text into words
    return len(words)
# Function to generate summary
def generate_summary(text):
    # Login to Hugging Face
    logger.info("Logging in to Hugging Face...")
    login(token=HF_TOKEN)

    # Initialize the HuggingFaceEndpoint with the provided model
    logger.info(f"Loading model from repo: {REPO_ID}")
    llm = HuggingFaceEndpoint(repo_id=REPO_ID, max_length=40, temperature=0.7, token=HF_TOKEN)

    # Create the prompt for the model
    prompt = f"You are a summarizer assistant. Generate a summary of the following meeting transcript without including the original text: {text}"
    
    # Generate the summary
    logger.info("Generating summary...")
    result = llm.invoke(prompt)
    return result

# Example usage
if __name__ == "__main__":
    
    file_path = "artifacts/generated_transcription.txt"  
    text = read_text_file(file_path)

    # Generate and print the summary
    summary = generate_summary(text)
    print("Summary:", summary)
    print("Length of summary:",count_words(summary))
    save_summary_to_file(summary, "artifacts/generated_summary.txt")
