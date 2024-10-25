import os
from whisper_mic import WhisperMic
import warnings
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
warnings.filterwarnings(
    "ignore",
    category=FutureWarning,
    message="You are using `torch.load` with `weights_only=False`.*"
)

class Recorder:
    def __init__(self, transcription_file):
        self.transcription_file = transcription_file
        self.mic = WhisperMic()
        self.transcriptions = []  # Store transcriptions in memory

    def start_recording(self):
        print("Recording started...")
        with open(self.transcription_file, "a") as file:

            result = self.mic.listen()
            if result.strip():  # Only write if there's a non-empty result
                file.write(result + "\n")
                file.flush()  # Ensure the result is immediately written to the file
                self.transcriptions.append(result)  # Store in memory
                print(result)  # Display in terminal

    def stop_recording(self):
        print("Recording stopped.")

    def get_transcriptions(self):
        return self.transcriptions