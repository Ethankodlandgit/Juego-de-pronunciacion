import speech_recognition as speech_recog

def speech():
    mic= speech_recog.Microphone()
    recog= speech_recog.Recognizer()
    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio= recog.listen(audio_file)
        return recog.recognize_google (audio, language = "en-GB")
    
    
mic= speech_recog.Microphone()
recog = speech_recog.Recognizer()
with mic as audio_file:
    print("habla por favor")
    recog.adjust_for_ambient_noise (audio_file)
    audio= recog.listen(audio_file)
    print("vamos a convertir la voz en texto!...")
    print("Tu has dicho: "+recog.recognize_google (audio, language = "en-GB"))