from tkinter import *
import pyttsx3
from nltk.corpus import wordnet
import nltk

nltk.download('wordnet')

#Function to speak the audio
def speak(audio):
    #Initialize pyttsx3 engine
    engine=pyttsx3.init('sapi5')
    
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def find_synonyms(word):
    syn_words=set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            syn_words.add(lemma.name())
    return list(syn_words)

#Function to get the meaning of a word using NLTK's WordNet
def meaning():
    query=str(text.get())   
    synsets=wordnet.synsets(query)
    res=''

    if synsets:
        for syn in synsets:
            res+=f"{syn.definition()}\n"

        spokenText.set(res) 
        speak("This meaning is:" +res)
    else:
        res="Meaning not found"
        spokenText.set(res)
        speak(res) 


wn=Tk()
wn.title("Dictionary")
wn.geometry('700x500')
wn.config(bg="SlateGray1")

text=StringVar(wn)
spokenText=StringVar(wn)

Label(wn,text='Rowdy:Speak the Meaning',bg='SlateGray1',fg='gray30',font=('Times',20,'bold')).place(x=100,y=10)
Label(wn,text='Please enter the word',bg='SlateGray1',font=('calibre',13,'normal'),anchor="e",justify=LEFT).place(x=20,y=70)
Entry(wn,textvariable=text,width=35,font=('calibre',13,'normal')).place(x=20,y=110)

queryLabel=Label(wn,textvariable=spokenText,bg="SlateGray1",anchor="e",font=('calibre',13,'normal'),justify=LEFT,wraplength=500).place(x=20,y=130)
spokenText.set("Which word you want to find the meaning of,Sir/Madam?")
speak("Which word you want to find the meaning of,Sir/Madam?")

Button(wn,text="Speak Meaning",bg='SlateGray4',font=('calibre',13),command=meaning).place(x=230,y=350)

wn.mainloop()