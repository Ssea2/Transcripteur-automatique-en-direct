# =========================================================
# crée le 18/05/2023
# =========================================================

# ==================== OBJECTIF ===========================
# lire le fluw audio et le transcrire en texte que seras 
# envoyer dans un fichier ou dans la page d'affiché a 
# l'écran 
# =========================================================


# bibliothèque importé
import speech_recognition as sr 
import asyncio

recognizer = sr.Recognizer()

async def audio_entry( languages='fr-FR', timeout=0.08, phrase_time_limit=3.5):
    global mic, is_running
    with sr.Microphone() as mic:
        while is_running:
            try:
                audio = recognizer.listen(mic, 
                              timeout=timeout, 
                              phrase_time_limit=phrase_time_limit
                              )   
                transcription = recognizer.recognize_google(audio_data=audio, language=languages)
                print(transcription)
                with open('record', 'a') as txt:
                    txt.write(transcription+ " ")           
            except (sr.UnknownValueError, sr.RequestError, sr.WaitTimeoutError):
                pass

asyncio.run(audio_entry())
   
                    
