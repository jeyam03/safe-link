from tkinter import *


def morse(txt):
    d = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
         '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
         '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
         '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
         '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
         '--..': 'Z', '......': ' ', '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
         '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/',
         '-....-': '-', '-.--.': '(', '-.--.-': ')'}

    translation = ''
    if txt.startswith('.') or txt.startswith('-'):
        txt = txt.split(' ')
        for x in txt:
            try:
                translation += d[x]
            except KeyError:
                print("Enter a valid input")

    b = Button(window, text=translation.strip())
    b.pack()


window = Tk()
window.geometry("1280x720")
# a = PhotoImage(file="bg.png")
# c = Label(window, image=a)

morse_pic = PhotoImage(file='morsecode.png')
morse_icon = Label(window, image=morse_pic)

window.title("Morse")
l1 = Label(window, text="Morse Code Converter", font=("Ubuntu", 60))
e2 = Entry(window, width=50, bd=5, font='Ubuntu', textvariable=StringVar())

sub_btn = PhotoImage(file='submit.png')
but = Button(window, image=sub_btn, border=0, command=lambda: morse(e2.get()))

# ans = Label(window, text=morse(e2.get()))

# c.place(x=0, y=0)
morse_icon.pack()
l1.pack(padx=20, pady=20)
e2.pack()
but.pack(padx=50, pady=50)

window.mainloop()