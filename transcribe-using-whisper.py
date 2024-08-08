import warnings
from whisper_mic import WhisperMic
import time
import keyboard

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

mic = WhisperMic()
transcription_file = "transcription.txt"
stop_key = "q"  # You can change this to any key you want to use to stop recording

print(f"Recording... Press '{stop_key}' to stop and save the transcription.")

try:
    with open(transcription_file, "a") as file:
        while True:
            if keyboard.is_pressed(stop_key):
                print(f"'{stop_key}' pressed. Stopping recording.")
                break  # Exit the loop if the stop key is pressed
            result = mic.listen()
            if result.strip():  # Only write if there's non-empty result
                file.write(result + "\n")
                file.flush()  # Ensure the result is immediately written to the file
                print(result)
                print("Appended transcription to transcription.txt")
except Exception as e:
    print(f"Error occured: {e}")
finally:
    print(f"Transcription saved to {transcription_file}. Exiting and closing file.")