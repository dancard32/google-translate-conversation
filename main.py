import os
import sys
import json
from googletrans import Translator  # Google Translate API
from gtts import gTTS               # Text-to-speech Module
sys.path.append('/path/to/ffmpeg')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def convertRecord(fid):
    import speech_recognition as sr
    from pydub import AudioSegment

    # Input .mp3 file and convert to a .wav format
    sound=AudioSegment.from_mp3(f'./{fid}.mp3')
    sound.export(f'{fid}.wav',format='wav')
    AUDIO_FILE= f'{fid}.wav'

    os.system(f"mpg321 {fid}.mp3")
    r=sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio=r.record(source)
        print(f'\n\nTranscription: {r.recognize_google(audio)}\n')
        return r.recognize_google(audio)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~            
def translateText(txt, lang_out, lang_in):
    output = Translator().translate(txt, dest=lang_out, src=lang_in).text
    print(f'\n{lang_out} Transcription: {output}\n\n')
    return output
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def textToSpeech(txt, lang_out):
    myobj = gTTS(text=txt, lang=lang_out, slow=False)
    myobj.save("TranslatedTranscript.mp3")       # Saving converted audio
    os.system("mpg321 TranslatedTranscript.mp3") # Playing the converted file
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    with open('lang.json') as json_file:
        langs = json.load(json_file)

    while True:
        lang_in = input('What is the native language? ')
        lang_ou = input('What language is this being translated to? ')
        if lang_in.lower() in langs.values() and lang_ou.lower() in langs.values():
            lang_in = list(langs.keys())[list(langs.values()).index(lang_in.lower())]
            lang_ou = list(langs.keys())[list(langs.values()).index(lang_ou.lower())]
            break
        else:
            print(f'Error: try the following supported languages\n\n{langs.values()}\n\n')

    transcript = convertRecord('Transcript')
    converted = translateText(transcript, lang_ou, lang_in)
    textToSpeech(converted, lang_ou)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":    
    main()