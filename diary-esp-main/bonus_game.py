from random import choise
import time
from speech import speech

fases = {

"facil": ["agenda", "ami", "souris"],
"intermedio": ["ordinateur", "algorithme", "développeur"],
"dificil": ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"]
}

def wasa(fases):
    palabras=fases.get(fases, [])
    if not palabras:
        print("Nivel de dificultad erroneo")
        return
    puntaje=0
    intentos=3
    for _ in range (len(palabras)):
        palabra_aleatoria=choise(palabras)
        print("Porfa pronuncia la palabra indicada caballero: ", palabra_aleatoria)
        recog_word=speech()
        print(recog_word)
    if palabra_aleatoria == recog_word:
        print("Bien dicho mi causa")
        puntaje += 1
    else:
        print("Muy mal dicho la palabra era: ",palabra_aleatoria)
    
    time.sleep(2)
    print("Game Over, tu puntacion es: ", puntaje)

selecciona_el_nivel = input("Selecciona la dificultad que quieres caballero (facil/intermedio/dificil), ¿Cual eliges?".lower()) 
wasa(selecciona_el_nivel)