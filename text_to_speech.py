## import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound



################### Initialized window####################

root = Tk()
root.geometry('650x450')
root.resizable(True,True)
root.config(bg = 'black')
root.title('TEXT_TO_SPEECH')


##heading
Label(root, text = 'TEXT TO SPEECH' , font='arial 30 bold' , bg ='#9900ff').pack()
Label(root, text ='Developed By Nitish' , font ='arial 20 bold', bg = '#ffcc66').pack(side = BOTTOM)




#label
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='#ff6699').place(x=20,y=60)


##text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)


###################define function##############################

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('tts.mp3')
    playsound('tts.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_speech, bg = 'green', width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'Red').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset, bg = 'yellow').place(x=175 , y =140)


#infinite loop to run program
root.mainloop()
