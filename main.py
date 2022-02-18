import os                           # OS for playing sound through terminal
import json                         # Used to load in supported languages
from googletrans import Translator  # Google Translate API
from gtts import gTTS               # Text-to-speech Module     
import speech_recognition as sr     # SpeechRecognition Module
import sounddevice as sd            # Used to record voice
from scipy.io.wavfile import write  # Used to write .wav file
from pydub import AudioSegment      # Module to export .mp3 for compatibility
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def recordVoice():
    freq = 24000
    duration = 5
    
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=1)
    sd.wait()   # Waits while the recording continues in background

    write("Transcript.wav", freq, recording)
    AudioSegment.from_wav("Transcript.wav").export("Transcript.mp3", format="mp3")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def convertRecord(fid):
    # Input .mp3 file and convert to a .wav format
    sound=AudioSegment.from_mp3(f'./{fid}.mp3')
    sound.export(f'{fid}.wav',format='wav')
    AUDIO_FILE= f'{fid}.wav'

    #os.system(f"mpg321 {fid}.mp3")     # Play-back the recorded sound
    r=sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        try:
            audio=r.record(source)
            return r.recognize_google(audio)
        except:
            return "ERROR"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def translateText(txt, lang_out, lang_in):
    output = Translator().translate(txt, dest=lang_out, src=lang_in).text
    return output
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def textToSpeech(txt, lang_out):
    myobj = gTTS(text=txt, lang=lang_out, slow=False)
    myobj.save("TranslatedTranscript.mp3")       # Saving converted audio
    os.system("mpg321 TranslatedTranscript.mp3") # Playing the converted file
    print(3*'\n')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    with open('lang.json') as json_file:
        lang = json.load(json_file)

    while True:
        lang_in = input('What is the native language? ').title()
        lang_ou = input('What language is this being translated to? ').title()

        if lang_in.lower() in lang.values() and lang_ou.lower() in lang.values():
            lang_1 = list(lang.keys())[list(lang.values()).index(lang_in.lower())]
            lang_2 = list(lang.keys())[list(lang.values()).index(lang_ou.lower())]
            break
        else:
            print(f'Error: try the following supported languages\n\n{lang.values()}\n\n')

    msg = ""
    while True:
        print(f"Native language {lang_in} speak now"+3*"\n")
        while True:
            recordVoice()
            transcript = convertRecord('Transcript')
            if transcript != "ERROR":
                break
            print(f"ERROR TRY AGAIN: Native language {lang_in} speak now"+3*"\n")
        print(f"{lang_in} transcription: {transcript}")

        converted = translateText(transcript, lang_2, lang_1)
        print(f"{lang_ou} transcription: {converted}")
        textToSpeech(converted, lang_2)

        msg = input("Press any key to continue, enter ''quit'' to stop the program\t")
        if msg.lower() == "quit":
            break

        print(f"Secondary language {lang_ou} speak now"+3*"\n")
        while True:
            recordVoice()
            transcript = convertRecord('Transcript')
            if transcript != "ERROR":
                break
            print(f"ERROR TRY AGAIN: Secondary language {lang_ou} speak now"+3*"\n")
        print(f"{lang_in} transcription: {transcript}")
        
        converted = translateText(transcript, lang_1, lang_2)
        print(f"{lang_ou} transcription: {converted}")
        textToSpeech(converted, lang_1)

        msg = input("Press any key to continue, enter ''quit'' to stop the program\t")
        if msg.lower() == "quit":
            break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":    
    main()