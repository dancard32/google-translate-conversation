from googletrans import Translator  # Google Translate API
from gtts import gTTS               # Text-to-speech Module
import os
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def recordData():
    pass
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def convertRecord(fid):
    import speech_recognition as sr
    from pydub import AudioSegment

    #sound=AudioSegment.from_mp3(f'{fid}.mp3')
    #sound.export(f'{fid}.wav',format='wav')
    AUDIO_FILE= f'{fid}.wav'

    os.system(f"mpg321 {fid}.mp3")
    r=sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
            audio=r.record(source)
            print('\n\nTranscription: '+r.recognize_google(audio))
            return r.recognize_google(audio)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~            
def translateText(txt, lang_out, lang_in):
    return Translator().translate(txt, dest=lang_out, src=lang_in).text
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def textToSpeech(txt, lang_out):
    myobj = gTTS(text=txt, lang=lang_out, slow=False)
  
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("welcome.mp3")
  
    # Playing the converted file
    os.system("mpg321 welcome.mp3")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def main():
    recordData()
    transcript = convertRecord('test')
    converted = translateText(transcript, 'es', 'en')
    textToSpeech(converted, 'es')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    main()