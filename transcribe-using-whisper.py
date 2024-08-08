import warnings
from whisper_mic import WhisperMic

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

mic = WhisperMic()
result = mic.listen()
print(result)

# Save the result to a text file
with open("transcription.txt", "w") as file:
    file.write(result)

print("Transcription saved to transcription.txt")