from ntpath import join
from re import T
from tkinter import *
from tkinter import ttk
from threading import currentThread
from turtle import st

from setuptools import Command
from POKE import get_poke_info

def main():
    root = Tk()
    root.title("Pokemon Information")
    #iconchange
    root.iconbitmap("Poke_Icon.ico")

    #name
    frm_usrinpt = ttk.Frame(root)
    frm_usrinpt.grid(row=0, column=0, columnspan=2 ,padx=15, pady=15)
    #info
    frm_infrtn = ttk.LabelFrame(root, text="Info")
    frm_infrtn.grid(row=1, column=0, padx=15, pady=15, sticky=N)
    #stats
    From_stats = ttk.LabelFrame(root, text="Stats")
    From_stats.grid(row=1, column=1, padx = 9,pady=10)
    #table to display values
    name_lbl = ttk.Label(frm_usrinpt, text = "Pokemon Name:")
    name_lbl.grid(row=0,column=0, padx=9, pady=10)
    #entry to display values
    name_entry = ttk.Entry(frm_usrinpt)
    name_entry.grid(row=0, column=1,pady=10)

    #Functions for clicks in GUI
    def btn_to_click_info():
        poke_name = name_entry.get()
        poke_dict = get_poke_info(poke_name)
        if poke_dict:
            lbl_height_value['text']= str(poke_dict['height']) + ' dm'
            lbl_weight_value['text']= str(poke_dict['weight']) + ' hg'
            type_list = (t['text']['name'] for t in poke_dict['types'])
            lbl_type_value['text'] = ', '.join(type_list)
            pgp_hp['value']=poke_dict['stats'][0]['base_stat']
            pgp_attack['value']=poke_dict['stats'][1]['base_stat']
            pgp_defence['value']=poke_dict['stats'][2]['base_stat']
            pgp_special_attack['value']=poke_dict['stats'][3]['base_stat']
            pgp_special_defence['value']=poke_dict['stats'][4]['base_stat']
            pgp_speed['value']=poke_dict['stats'][5]['base_stat']

    btn_get_info = ttk.Button(frm_usrinpt, text ="Get Info", command = btn_to_click_info)
    btn_get_info.grid(column=2, row=0, padx=10, pady=10)

    #height
    lbl_height = ttk.Label(frm_infrtn, text = "Height:")
    lbl_height.grid(row=100, column=100)
    lbl_height_value = ttk.Label(frm_infrtn, text = "TBD")
    lbl_height_value.grid(row=100, column=200, padx=15, pady=7)
    #weight
    lbl_weight = ttk.Label(frm_infrtn, text = 'Weight:')
    lbl_weight.grid(row=300, column=100)
    lbl_weight_value = ttk.Label(frm_infrtn, text = "TBD")
    lbl_weight_value.grid(row=300, column=200)
    #type
    lbl_type = ttk.Label(frm_infrtn, text= 'Type:')
    lbl_type.grid(row=500, column=100)
    lbl_type_value = ttk.Label(frm_infrtn, text = "TBD")
    lbl_type_value.grid(row=500, column=200, padx=15, pady= 7)
    #HealthPoint(hp)
    lbl_hp = ttk.Label(From_stats, text = 'HP:')
    lbl_hp.grid(row=100, column=100, sticky= E)
    pgp_hp = ttk.Progressbar(From_stats, length=200, maximum=225)
    pgp_hp.grid(row=100, column=200 ,padx=10, pady=10)
    #Attack
    lbl_attack = ttk.Label(From_stats, text = 'Attack:')
    lbl_attack.grid(row=200, column=100, sticky= E)
    pgp_attack = ttk.Progressbar(From_stats, length=200 , maximum=225)
    pgp_attack.grid(row=200, column=200)
    #Defence
    lbl_defence = ttk.Label(From_stats, text = 'Defence:')
    lbl_defence.grid(row=300, column=100, sticky= E)
    pgp_defence = ttk.Progressbar(From_stats, length=200 , maximum=225)
    pgp_attack.grid(row=300, column=200, padx=10, pady=10)
    #Special Attack
    lbl_special_attack = ttk.Label(From_stats, text = 'Special Attack:')
    lbl_special_attack.grid(row=400, column=100, sticky= E)
    pgp_special_attack = ttk.Progressbar(From_stats, length=200 , maximum=225)
    pgp_special_attack.grid(row=400, column=200)
    #Special Defence
    lbl_special_defence = ttk.Label(From_stats, text = 'Special Defence:')
    lbl_special_defence.grid(row=500, column=100, sticky= E)
    pgp_special_defence = ttk.Progressbar(From_stats, length=200 , maximum=225)
    pgp_special_defence.grid(row=500, column=200, padx=10, pady=10)
    #Speed
    lbl_speed = ttk.Label(From_stats, text='Speed:')
    lbl_speed.grid(row=600,column=100, sticky= E)
    pgp_speed = ttk.Progressbar(From_stats, length=200, maximum=225)
    pgp_speed.grid(row=600, column=200)

    root.mainloop()

main()


