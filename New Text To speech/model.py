from tkinter import *
from gtts import gTTS
from playsound import playsound
from tkinter.messagebox import *
from tkinter.simpledialog import *
import os

root = Tk()
root.geometry("630x600")
root.configure(background='black')
root.title("Speech It")


Label(root, text = "Speech It", font = "Times 30 bold", bg = 'black', fg = 'white').pack(ipadx=30, ipady=60)

Label(root,text ="Enter Text", font = 'Calibri 16 bold', bg = 'black', fg = 'white').place(x=20, y=140)

entry_field = Text(root,width ='40', font=("Calibri 20"))
entry_field.place(x=20,y=180, height = 150)
COUNTER = 0

def Text_to_speech():
    Message = entry_field.get("0.0", "end")
    try:
        speech = gTTS(text = Message)
    except:
        Message = "Nothing entered"
        speech = gTTS(text=Message)
    audio_name = "tobedeleted"
    speech.save(audio_name + '.mp3')
    playsound(audio_name + '.mp3')
    os.remove("tobedeleted"  + ".mp3")

def store():
    global COUNTER
    Message = entry_field.get("0.0","end")
    try:
        speech = gTTS(text=Message)
    except:
        Message = "Nothing entered"
        speech = gTTS(text=Message)
    audio_name = askstring("Audio Name", "What to save your file as?", parent=root)
    speech.save(audio_name + str(COUNTER) + '.mp3')
    COUNTER += 1
    showinfo("Audio stored", "Your audio is stored :)")

def Exit():
    root.destroy()

def Reset():
    entry_field.delete("0.0", "end")

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4', bg = 'blue').place(x=120,y=340)

Button(root, text = "SAVE", font = 'arial 15 bold' , command = store,width = '4', bg = 'blue').place(x=250,y=340)

Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'red').place(x=250 , y = 440)

Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset, bg = 'blue').place(x=380 , y = 340)

root.mainloop()
