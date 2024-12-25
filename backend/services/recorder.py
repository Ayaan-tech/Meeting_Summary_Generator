import os
from whisper_mic import WhisperMic
from backend.services.utils.logging import logger
import warnings

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
warnings.filterwarnings(
    "ignore",
    category=FutureWarning,
    message="You are using torch.load with weights_only=False.*"
)

class Recorder:
    def __init__(self, transcription_file):
        self.transcription_file = transcription_file
        self.mic = WhisperMic()
        self.transcriptions = []  # Store transcriptions in memory

    def start_recording(self):
        try:
            logger.info("Recording started.")
            with open(self.transcription_file, "a") as file:
                result = self.mic.listen()
                if result.strip():  # Only write if there's a non-empty result
                    file.write(result + "\n")
                    file.flush()  # Ensure the result is immediately written to the file
                    self.transcriptions.append(result)  # Store in memory
                    logger.info(f"Transcription: {result}")
        except Exception as e:
            logger.error(f"Error during recording: {e}")

    def stop_recording(self):
        try:
            logger.info("Recording stopped.")
        except Exception as e:
            logger.error(f"Error stopping recording: {e}")

    def get_transcriptions(self):
        return self.transcriptions
