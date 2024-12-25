
# VocalScribe

VocalScribe is an intelligent tool that automates transcription, summarization, and documentation of conversations. It uses **Whisper_mic** for real-time transcription, which leverages **OpenAI's Whisper** model to capture and transcribe speech live via a microphone. Whisper_mic allows the use of Whisper with a microphone in real time, making it ideal for live transcription. The tool then uses **Mistral 7B**, a powerful **Large Language Model**, to generate summaries, agendas, and resolutions from the transcriptions. Users can download a professionally formatted Word document containing all relevant meeting details, making it easy to keep records and stay organized.

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

- Fill in the meeting details: Provide meeting-specific details such as date, initiator, and participants.
- Start Recording: Record audio using the integrated Whisper_mic functionality, which allows real-time transcription using OpenAI's Whisper model with a microphone.
- Transcription: As the audio is recorded, Whisper_mic utilizes Whisper to transcribe the speech in real time.
- Generate Summary: Once the transcription is complete, a summary, agenda, and resolutions will be generated.
- Review and Download: Review the summary, agenda, and resolutions. Then, download the meeting details as a professionally formatted Word document.

## Contributing

Feel free to open issues or contribute to the project. If you want to help enhance the project, please submit a pull request.
