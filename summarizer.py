import logging
import requests
import re
from huggingface_hub import login
from langchain_huggingface import HuggingFaceEndpoint
import time

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

HF_TOKEN = "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"  # Add your Hugging Face token here
REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"

def generate_summary(text):
    logger.info("Logging in to Hugging Face...")
    login(token=HF_TOKEN)

    logger.info(f"Loading model from repo: {REPO_ID}")
    llm = HuggingFaceEndpoint(repo_id=REPO_ID, max_length=200, temperature=0.7, token=HF_TOKEN)

    # Defining the roles
    system_prompt = """You are an intelligent meeting assistant. Your role is to analyze meeting transcripts and 
    extract key information. You will provide the agenda, a brief summary, and any important resolutions of the meeting."""
    
    # Combining the system role and user input in the prompt
    user_prompt = f"""
    Here is a meeting transcript: "{text}"
    
    Please identify:
    Agenda: Identify the main topics or goals discussed in the meeting.
    Summary: Provide a brief summary of the discussion.
    Resolution: Highlight the decisions or resolutions reached at the meeting.
    """

    prompt = system_prompt + user_prompt

    retries = 0
    while True:
        try:
            logger.info("Generating summary, agenda, and resolution...")
            result = llm.invoke(prompt)
            
            # Parse the output to separate agenda, summary, and resolution
            agenda = re.search(r"Agenda:(.*?)(?=Summary:|Resolution:|$)", result, re.DOTALL)
            summary = re.search(r"Summary:(.*?)(?=Agenda:|Resolution:|$)", result, re.DOTALL)
            resolution = re.search(r"Resolution:(.*?)(?=Agenda:|Summary:|$)", result, re.DOTALL)

            summary_data = {
                "agenda": agenda.group(1).strip() if agenda else "Not found",
                "summary": summary.group(1).strip() if summary else "Not found",
                "resolution": resolution.group(1).strip() if resolution else "Not found"
            }
            
            save_output_to_file(summary_data)
            return summary_data
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:  # Rate limit error
                retries += 1
                wait_time = min(60 * (2 ** retries), 300)  # Wait up to 5 minutes
                logger.warning(f"Rate limit reached. Waiting for {wait_time} seconds before retrying...")
                time.sleep(wait_time)  # Exponential backoff
            else:
                logger.error("An error occurred: %s", e)
                raise

def save_output_to_file(summary_data):
    """Saves the generated summary data to a text file."""
    output_file = "artifacts/generated_summary.txt"
    with open(output_file, 'w') as file:
        file.write("Agenda:\n")
        file.write(f"{summary_data['agenda']}\n\n")
        file.write("Summary:\n")
        file.write(f"{summary_data['summary']}\n\n")
        file.write("Resolution:\n")
        file.write(f"{summary_data['resolution']}\n")
    logger.info(f"Summary data saved to {output_file}.")
