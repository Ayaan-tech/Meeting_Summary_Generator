
# Meeting Summarizer

A smart tool to automate the transcription, summarization, and documentation of meeting conversations. MeetMind uses **Whisper_mic** for real-time transcription of speech, which utilizes **OpenAI's Whisper** model under the hood. Whisper_mic is a Python package that simplifies live transcription by capturing microphone input and continuously transcribing it, making it ideal for real-time applications like meetings. The tool then employs **Mistral** (a **L**arge **L**anguage **M**odel) to generate concise summaries, including agendas and resolutions. Users can download a professionally formatted Word document containing all the relevant meeting details.

##  Features
- Real-time Transcription: Uses Whisper_mic for accurate, real-time transcription of meeting conversations.
- AI-Powered Summarization: Employs Mistral to generate concise summaries, agendas, and resolutions.
- Customizable Inputs: Allows users to provide meeting-specific details (e.g., date, initiator, participants).
- Document Export: Download meeting details as a Word document containing summaries, agendas, and resolutions.
- Cloud Integration: Stores generated meeting documents securely on **Cloudinary**.
- User-Friendly API: Built with **FastAPI** for seamless backend operations.

## Tech Stack
- Whisper_mic: For real-time transcription of meeting conversations (a wrapper around OpenAI's Whisper model).
- Whisper: OpenAI's Automatic Speech Recognition (ASR) model used for transcribing speech into text.
- Mistral: Language model for generating high-quality summaries.
- FastAPI: Backend framework handling API operations.
- Hugging Face API: To access and utilize the Mistral model.
- Python-docx: For generating Word documents with meeting details.
- MongoDB: Stores meeting-specific details (e.g., participants, date).
- Cloudinary: Stores and manages generated meeting documents.

### Whisper and Whisper_mic
**Whisper**: Whisper is OpenAI's Automatic Speech Recognition (ASR) model that can transcribe audio files or streams into text. It's highly accurate and supports multiple languages.

**Whisper_mic**: whisper_mic is a Python package that acts as a wrapper around Whisper, enabling real-time transcription from a microphone. It listens to the microphone input continuously and transcribes speech on-the-fly, making it ideal for live transcription during meetings or conversations.

In essence, Whisper performs the transcription, and whisper_mic simplifies using Whisper for live, real-time speech-to-text conversion.

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
