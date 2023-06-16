import speech_recognition as sr
from googletrans import Translator

def traduzir_audio():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    translator = Translator()

    print("Fale algo em alemão:")
    
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        texto_alemao = recognizer.recognize_google(audio, language='de-DE')
        traducao = translator.translate(texto_alemao, src='de', dest='pt')
        print("Tradução para o português:", traducao.text)
    except sr.UnknownValueError:
        print("Não foi possível reconhecer o áudio.")
    except sr.RequestError as e:
        print("Erro na solicitação ao serviço de reconhecimento de fala; {0}".format(e))

# Exemplo de uso
traduzir_audio()
