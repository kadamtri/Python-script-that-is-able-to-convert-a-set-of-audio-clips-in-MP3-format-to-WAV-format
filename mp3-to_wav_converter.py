import os
import sys
from pydub import AudioSegment

def mp3_to_wav(mp3_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate over all files in the MP3 folder
    for file_name in os.listdir(mp3_folder):
        if file_name.endswith(".mp3"):
            mp3_path = os.path.join(mp3_folder, file_name)
            wav_path = os.path.join(output_folder, file_name.replace(".mp3", ".wav"))
            
            # Convert MP3 to WAV using pydub
            audio = AudioSegment.from_mp3(mp3_path)
            audio.export(wav_path, format="wav")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python mp3_to_wav_converter.py <mp3_folder> <output_folder>")
        sys.exit(1)
    
    mp3_folder = sys.argv[1]
    output_folder = sys.argv[2]
    
    mp3_to_wav(mp3_folder, output_folder)

