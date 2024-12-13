
# Meeting Summarizer

A smart tool to automate the transcription, summarization, and documentation of meeting conversations. Meeting Summarizer leverages Whisper Automatic Speech Recognition (ASR) for real-time transcription and Mistral (an LLM) to generate concise summaries, including key details such as agendas and resolutions. Additionally, users can download a professionally formatted Word document with all the relevant meeting information.

##  Features
- Real-time Transcription: Uses Whisper for accurate, real-time transcription of meeting conversations.
- AI-Powered Summarization: Employs Mistral to generate concise summaries, agendas, and resolutions.
- Customizable Inputs: Allows users to provide meeting-specific details (e.g., date, initiator, participants).
- Document Export: Download meeting details as a Word document containing summaries, agendas, and resolutions.
- Cloud Integration: Stores generated meeting documents securely on Cloudinary.
- User-Friendly API: Built with FastAPI for seamless backend operations.

## Tech Stack
- Whisper: For real-time transcription of meeting conversations.
- Mistral: Language model for generating high-quality summaries.
- FastAPI: Backend framework handling API operations.
- Hugging Face API: To access and utilize the Mistral model.
- Python-docx: For generating Word documents with meeting details.
- MongoDB: Stores meeting-specific details (e.g., participants, date).
- Cloudinary: Stores and manages generated meeting documents.

## Installation
### Prerequisites
- Python 3.12.3 installed
- Access to MongoDB and a Cloudinary account
  
### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/Khan-Ramsha/MeetSummarizer.git
    cd MeetSummarizer
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI server:
    ```bash
    python app.py
    ```

4. Navigate to `http://127.0.0.1:8000` in your browser to access the application.

## Usage

- Fill in the meeting details such as date, initiator, and participants.
- Start Recording: Record audio using the integrated Whisper functionality.
- Once the transcription is complete, a summary will be generated.
- Review the summary, agenda, and resolutions.
- Download the meeting details as a Word document.

## Contributing

Feel free to open issues or contribute to the project. If you want to help enhance the project, please submit a pull request.
