from tkinter import *
from tkinter import ttk
from library import download_image_from_url , set_desk_bg_img
from Pokeapi import Get_poke_list , get_poke_image
import os
import sys
import ctypes


def main():
    
    script_dir = sys.path[0]
    img_dir = os.path.join(script_dir, 'images')
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)

    root = Tk()
    root.title('Pokemon Image Viewer')
    app_id = 'pokemon.image.viewer'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    root.iconbitmap(os.path.join(script_dir, 'Poke_Icon.ico'))

    frm = ttk.Frame(root)
    frm.grid(sticky=(N,S,E,W))

    img_poke = PhotoImage(file =os.path.join(script_dir, 'PokeImage.png'))
    lbl_img = ttk.Label(frm, image=img_poke)
    lbl_img.grid(row=0,column=0,padx=10,pady=10)
    
    pokemon_list = Get_poke_list()
    pokemon_list.sort()
    pokemon_list = [p.capitalize() for p in pokemon_list]
    cbo_poke = ttk.Combobox(frm, values=pokemon_list, state='readonly')
    cbo_poke.set('Select a Pokemon ;-)')
    cbo_poke.grid(row=2, column=0, padx =10, pady=10)

    
    def handle_poke_slct(event):
        spoke_name = cbo_poke.get()
        img_url = get_poke_image(spoke_name)
        img_path = os.path.join(img_dir, spoke_name + '.png')
        download_image_from_url(img_url,img_path)
        img_poke['file'] = img_path
        


    cbo_poke.bind('<<ComboboxSeleted>>', handle_poke_slct)



    root.mainloop()



main()