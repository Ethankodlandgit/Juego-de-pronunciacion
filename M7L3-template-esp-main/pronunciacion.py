import speech_recognition as speech_recog
import random
import time
niveles = {
    "facil": ["agenda", "hola", "casa"],
    "medio": ["bye", "algorithm", "bed"],
    "dificil": ["réseau neuronal", "apprentissage automatique", "inteligencia artificial"]
}

def speech(language="es-ES"):
    recog = speech_recog.Recognizer()
    mic = speech_recog.Microphone()
    try:
        with mic as audio_file:
            recog.adjust_for_ambient_noise(audio_file)
            print("Por favor, di la palabra...")
            audio = recog.listen(audio_file, timeout=10)  
            return recog.recognize_google(audio, language=language)
    except speech_recog.UnknownValueError:
        print("hmmmm, no se entendio nada intantalo denuevo")
        return None
    except speech_recog.RequestError:
        print("Error con el reconocimiento de voz.")
        return None
    except speech_recog.WaitTimeoutError:
        print("Parece que te desaparesiste no dijiste nada y se fue el tiempo")
        return None

def play_game():
    print("Selecciona el nivel de dificultad: fácil, medio, difícil")
    nivel = input("Escribe que nivel quieres: ").lower()
    
    if nivel not in niveles:
        print("Ese nivel no existe pero despues lo implementaresmos (talvez si no me olvido)")
        return
    
    palabras = niveles[nivel]
    language = {"facil": "es-ES", "medio": "en-EN", "dificil": "fr-FR"}[nivel]
    score = 0
    intentos_totales = 3

    for palabra in palabras:
        intentos = intentos_totales
        while intentos > 0:
            print(f"Tienes {intentos} intentos para decir: '{palabra}'")
            inicio = time.time()
            respuesta = speech(language)
            tiempo_transcurrido = time.time() - inicio
            
            if tiempo_transcurrido > 5:
                print("¡Se consumio el tiempo!")
                break
            
            if respuesta is None:
                intentos -= 1
            elif respuesta.lower() == palabra.lower():
                print("Exelente!")
                score += 1
                break
            else:
                print("Incorrecto, te equivocaste esta vez inténtalo de nuevo.")
                intentos -= 1

        if intentos == 0:
            print(f"No lograste decir '{palabra}' correctamente.")
    
    if score == len(palabras):
        if nivel == "dificil":
            print("No puede ser ganaste muy bien")
        else:
            print("Has pasado al otro nivel")
    else:
        print("Inténtalo denuevo puedeser que mejores")
    
    print(f"Tu puntuacion es: {score}/{len(palabras)}")

if __name__ == "__main__":
    play_game()