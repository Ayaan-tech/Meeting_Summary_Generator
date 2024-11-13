
# Meeting Summarizer

A smart tool to automate the transcription, summarization, and documentation of meeting conversations. The Meeting Summarizer uses Whisper Automatic Speech Recognition (ASR) to record meetings, convert them into transcriptions, and uses Mistral (an LLM) to generate concise summaries and provide key details like the agenda and resolutions. It also allows users to download a Word document with all the relevant information.
## Features

- **Real-time Conversation Recording**: Uses Whisper for transcribing meeting conversations in real-time.
- **Summarization with Mistral**: Generate concise summaries of the meeting, including key discussions, agenda, and resolutions.
- **Customizable Inputs**: Users can input meeting-specific details such as the meeting date, initiator, and participants.
- **Word Document Export**: Once the summary is generated, users can download a Word document containing all the details of the meeting, including the summary, agenda, and resolutions.
- **API Integration**: Built with FastAPI to handle the backend operations.

## Tech Stack

- **Whisper**: Used for real-time transcription of meeting conversations.
- **Mistral**: Summarization model used for generating meeting summaries.
- **FastAPI**: Backend framework for handling API requests.
- **Hugging Face API**: Used to access and utilize the Mistral model for text summarization.
- **Python-docx**: For generating downloadable Word documents containing meeting details.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/meeting-summarizer.git
    cd meeting-summarizer
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

4. Navigate to `http://127.0.0.1:8000` in your browser to access the application.

## Usage

- Start a meeting by recording audio using the integrated Whisper microphone.
- Fill in the meeting details such as date, initiator, and participants.
- Once the transcription is complete, a summary will be generated.
- Review the summary, agenda, and resolutions.
- Download the meeting details as a Word document.

## Contributing

Feel free to open issues or contribute to the project. If you want to help enhance the project, please submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
