import whisper
import os
from openai import OpenAI

file_path = os.path.join(os.getcwd(), "lesson_1.mp3") 

print(file_path)

# model = whisper.load_model("base")
# result = model.transcribe(file_path)
# transcription_text = result['text']

# with open("lesson_1_text.txt", 'w' , ) as file:
#     file.write(transcription_text)

client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)


# from openai import OpenAI
# client = OpenAI()

# audio_file= open("/path/to/file/audio.mp3", "rb")
# transcription = client.audio.transcriptions.create(
#   model="whisper-1", 
#   file=audio_file
# )
# print(transcription.text)