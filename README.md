# google-translate-conversation
## Description
This simple project will prompt a user for the native language and a target language. Each turn will record the user and convert the text and output the transcript as will as an auditory text-to-speech. 
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
Simply run the program through the command line, and you'll be prompted for the native language and the language that will be converted to. Once running you will have 5 seconds to record a small conversation that will be recorded and translated to the other supported language. You will be prompted each time to continue the conversation.

That's it! Enjoy!

---
## MIT License
A short and simple permissive license with conditions only requiring preservation of copyright and license notices. Licensed works, modifications, and larger works may be distributed under different terms and without source code.