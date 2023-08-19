import customtkinter
import pyperclip
from password_generator import generate_password
import string
import secrets
import random
import sys, os

# * How compile it shit
# * icon - https://github.com/TomSchimansky/CustomTkinter/discussions/939
# * customtkinter error - https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging

# todo @Author #h4L

def resource(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def get_random(list):
    rand = random.choice(list)
    return rand

def generate_password(length,chinise,japanese):
    
    # Define Unicode ranges for Chinese and Japanese alphabets
    chinese_range = (0x4E00, 0x9FFF)
    japanese_range = (0x3040, 0x30FF)
    
    # Create a list of all characters from Chinese and Japanese alphabets
    chinese_characters = [chr(code) for code in range(chinese_range[0], chinese_range[1] + 1)]
    japanese_characters = [chr(code) for code in range(japanese_range[0], japanese_range[1] + 1)]
    
    eng_characters = string.ascii_letters
    numbers = string.digits
    punctuation = string.punctuation
    special_chars = string.octdigits
    
    
    # alphabet =  japanese_characters + eng_characters.split() + numbers.split() + punctuation.split() 

    pwd =''
    if chinise and japanese:
        for i in range(length):
            pwd +=get_random(get_random([chinese_characters,japanese_characters,eng_characters,numbers,punctuation]))
    elif chinise:
        for i in range(length):
            pwd +=get_random(get_random([chinese_characters,eng_characters,numbers,punctuation]))
    elif japanese:
        for i in range(length):
            pwd +=get_random(get_random([japanese_characters,eng_characters,numbers,punctuation]))
    else:
        for i in range(length):
            pwd +=get_random(get_random([eng_characters,numbers,punctuation]))
        

    return pwd

if __name__ =='__main__':
    customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
    # customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

    app = customtkinter.CTk()  # create CTk window like you do with the Tk window
    app.geometry("400x240")
    app.title('UltimatePasswordGen V.1')
    app.iconbitmap(resource('icon.ico'))

    def button_function():
        chin_val = bool(lang_chinise.get())
        jap_val = bool(lang_jap.get())
        
        
        passw = generate_password(length=round(slider.get()),japanese=jap_val,chinise=chin_val)
        text.delete(0,customtkinter.END)
        text.insert(0,passw)

    def on_slider_change(event):
        chr_count = round(slider.get())
        label.configure(text=f'char count: {chr_count}')

    def copy():
        pyperclip.copy(text.get())

    text = customtkinter.CTkEntry(master=app)
    text.grid(row=0,column=0,padx=20,pady=20)

    lang_jap = customtkinter.CTkCheckBox(master=app,text='jp',width=10,height=10)
    lang_jap.grid(row=0,column=1,padx=20,pady=20)
    lang_jap.select()

    lang_chinise = customtkinter.CTkCheckBox(master=app,text='ch',width=10,height=10)
    lang_chinise.grid(row=0,column=2,padx=20,pady=20)
    lang_chinise.select()


    label = customtkinter.CTkLabel(master=app,text='char count: 54')
    label.grid(row=2,column=0,padx=10,pady=20)

    slider = customtkinter.CTkSlider(master=app,from_=8,to=100,number_of_steps=20,width=120,command=on_slider_change)
    slider.grid(row=2,column=1,padx=10,pady=20)

    button = customtkinter.CTkButton(master=app, text="GeneratePass", command=button_function)
    button.grid(row=3,column=0,padx=1,pady=20)

    button_copy = customtkinter.CTkButton(master=app, text="Copy", command=copy,width=70)
    button_copy.grid(row=3,column=1,padx=1,pady=20)



    app.mainloop()