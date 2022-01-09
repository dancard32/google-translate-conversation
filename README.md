# google-translate-conversation
## Description
This simple project uses a recorded *.mp3* file and then uses Google Translate API to convert the speech to text, then text to the other person's native language and back to a *.mp3* file format.
## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
## Installation
There are several dependencies such as SpeechRecognition, pydub, googletrans, gTTS
```
pip install SpeechRecognition pydub googletrans gTTS mpyg321
```

For playing the text-to-speech in the command line, install the following for MacOS
```
brew install mpg321
```
## Usage
Simply record a *.mp3* sound and drop into the root folder and run the python script. Once running, there will be a prompt for a native language, as well as the language that this sound sample will be exported as.

That's it! Enjoy!

---
## MIT License
A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.