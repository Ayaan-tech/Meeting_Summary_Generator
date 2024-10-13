import warnings
from whisper_mic import WhisperMic
import time
import keyboard

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")
warnings.filterwarnings(
    "ignore",
    category=FutureWarning,
    message="You are using `torch.load` with `weights_only=False`.*"
)
mic = WhisperMic()
transcription_file = "artifacts/generated_transcription.txt"
stop_key = "q"  # You can change this to any key you want to use to stop recording
print(f"Recording... Press '{stop_key}' to stop and save the transcription.")

try:
    with open(transcription_file, "a") as file:
        if keyboard.is_pressed(stop_key):
            print(f"'{stop_key}' pressed. Stopping recording.")
        else:
            result = mic.listen()
            if result.strip():  # Only write if there's a non-empty result
                file.write(result + "\n")
                file.flush()  # Ensure the result is immediately written to the file
                print(result)
                print("Appended transcription to transcription.txt")  
   
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    print(f"Transcription saved to {transcription_file}. Exiting and closing file.")
