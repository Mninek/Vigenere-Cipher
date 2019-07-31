import tkinter
decrypted_phrase = ""
encrypted_phrase = ""

#creating my main window
window = tkinter.Tk()
window.title("Vigenere Cipher")
window.geometry("400x600")

#creating the text boxes
t_text = tkinter.Text(window, height = 15, width = 44, wrap = tkinter.WORD)
b_text = tkinter.Text(window, height = 15, width = 44, wrap = tkinter.WORD)

#my functions

def vigenereEn():
    global encrypted_phrase
    encrypted_phrase = ""
    key_text = key.get()
    if key_text.isalpha() is False:
         invalidKeyE()
    else:    
        phrase = t_text.get(1.0, tkinter.END)
        i = 0
        j = 0
        upper = False
    
        while i < len(phrase)-1:
            if phrase[i] == " ":
                encrypted_phrase = encrypted_phrase + " "
                i = i + 1
                continue
            if j >= len(key_text):
                j = 0
            if ord(phrase[i]) < 65 or ord(phrase[i]) > 122 or ord(phrase[i]) > 90 and ord(phrase[i]) < 97:
                encrypted_phrase = encrypted_phrase + phrase[i]
                i = i + 1
                j = j + 1
                continue
            if ord(phrase[i]) > 96 and ord(phrase[i]) < 123:
                upper = True
            if ord(key_text[j]) >= 97: 
                keyval = ord(key_text[j]) - 97
            else:
                keyval = ord(key_text[j]) - 65
            
            temp = chr(ord(phrase[i]) + keyval)
            if ord(temp) > 122:
                temp = chr(((ord(temp)%122) -1)+97)
            elif ord(temp) > 90:
                if upper:
                    pass
                else:
                    temp = chr(((ord(temp)%90) - 1) + 65)
                    print(temp)
            encrypted_phrase = encrypted_phrase + temp
            i = i + 1
            j = j + 1
            
def vigenereDec():
    global decrypted_phrase
    decrypted_phrase = ""
    key_text = key.get()
    if key_text.isalpha() is False:
        invalidKeyD() 
    else:
        phrase = b_text.get(1.0, tkinter.END)
        i = 0
        j = 0
        lower = False
        while i < len(phrase)-1:
            if phrase[i] == " ":
                decrypted_phrase = decrypted_phrase + " "
                i = i + 1
                continue
            if j >= len(key_text):
                j = 0
            if ord(phrase[i]) < 65 or ord(phrase[i]) > 122 or ord(phrase[i]) > 90 and ord(phrase[i]) < 97:
                decrypted_phrase = decrypted_phrase + phrase[i]
                i = i + 1
                j = j + 1
                continue
            if ord(phrase[i]) > 64 and ord(phrase[i]) < 90:
                lower = True
            if ord(key_text[j]) >= 97: 
                keyval = ord(key_text[j]) - 97
            else:
                keyval = ord(key_text[j]) - 65
            
            temp = chr(ord(phrase[i]) - keyval)
            if ord(temp) < 65:
                temp = chr(91 - (65 - ord(temp)))
            elif ord(temp) < 97:
                if lower:
                    pass
                else:
                    temp = chr(123 - (97 - ord(temp)))
                    print(temp)
    
            decrypted_phrase = decrypted_phrase + temp
            i = i + 1
            j = j + 1
        
def invalidKeyE():
    b_text.delete(1.0, tkinter.END)
    b_text.insert(tkinter.END,"ERROR: KEY MUST ONLY CONTAIN ALPHABETICAL CHARACTERS!")
def invalidKeyD():
    t_text.delete(1.0, tkinter.END)
    t_text.insert(tkinter.END,"ERROR: KEY MUST ONLY CONTAIN ALPHABETICAL CHARACTERS!")
def enButtonPress():
    b_text.delete(1.0, tkinter.END)
    vigenereEn()
    b_text.insert(tkinter.END, encrypted_phrase)
    
def decButtonPress():
    t_text.delete(1.0, tkinter.END)
    vigenereDec()
    t_text.insert(tkinter.END, decrypted_phrase)


#creating all my widgets
en_b = tkinter.Button(window, text = "Encrypt", width = 10, command = lambda : enButtonPress())
dec_b = tkinter.Button(window, text= "Decrypt", width = 10, command = lambda : decButtonPress())
key = tkinter.Entry(window,)
tkinter.Label(window, text = "Key:").place(x=125, y = 280, anchor = tkinter.CENTER)

#placing all my widgets
en_b.place(x=150,y=300, anchor = tkinter.CENTER)
dec_b.place(x=250,y=300, anchor = tkinter.CENTER)
key.place(x = 200,y = 280, anchor = tkinter.CENTER)
t_text.place(x=25, y = 20, anchor = tkinter.NW)
b_text.place(x=25,y=330, anchor= tkinter.NW)

window.mainloop()
