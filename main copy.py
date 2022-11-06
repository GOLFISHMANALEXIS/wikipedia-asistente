import pyttsx3
import wikipedia

wikipedia.set_lang("es")
asistente = pyttsx3.init()

entrada = input("¿Qué quieres saber? ")
resultado = wikipedia.summary(entrada, sentences=1)

while (True):
    print (resultado)
    asistente.say(resultado)
    asistente.runAndWait()
    entrada = input("¿Qué quieres saber? ")
    resultado = wikipedia.summary(entrada, sentences=1)





