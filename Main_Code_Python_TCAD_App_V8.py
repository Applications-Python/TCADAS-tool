import os
import re
import tkinter as tk
from tkinter import *
import pandas as pd
import xlsxwriter as xlsw
from tkinter import font
import shutil
import pathlib
import sys
import stat
from PIL import ImageTk, Image

showStatusbar=True
showToolbar=True
fontFamily="Arial"
url=""
fontSize=12
textChanged=False


root = tk.Tk()
root.title("Welcome to TCADAS Tool")
root.resizable(False,False)
root.iconbitmap(r'1.ico')
absolute_path = os.path.abspath(__file__)
Directory = os.path.dirname(absolute_path)
print(Directory)
bg = PhotoImage(file='Conventiona_FG_Structure.png')
myFont = font.Font(family='Arial', size=12, weight='bold')

canvas = tk.Canvas(root, height=700, width=1010, bg="Orange")

img= ImageTk.PhotoImage(Image.open("Conventiona_FG_Structure.png"))
canvas.create_image(500,315,anchor=NW,image=img)

#canvas.create_image(50,120,anchor=NW,image=bg)

canvas.pack()





label1 = tk.Label ( root, text='Width (um):', bg="Orange", justify = "left")
label1.config (font = myFont, justify = "left")
canvas.create_window (61, 50, window=label1 )
entry1 = tk.Entry ( root )
canvas.create_window ( 380, 50, window=entry1 )


label2 = tk.Label ( root, text='Length (um):', bg="Orange", justify = "left")
label2.config (font = myFont, justify = "left")
canvas.create_window ( 67, 100, window=label2 )
entry2 = tk.Entry ( root )
canvas.create_window ( 380, 100, window=entry2 )


label3 = tk.Label ( root, text='Wafer orientation:', bg="Orange", justify = "left")
label3.config (font = myFont, justify = "left")
canvas.create_window ( 87, 150, window=label3 )
entry3 = tk.Entry ( root )
canvas.create_window ( 380, 150, window=entry3 )


label4 = tk.Label ( root, text='Silicon dopant:', bg="Orange", justify = "left")
label4.config (font = myFont, justify = "left")
canvas.create_window ( 75, 200, window=label4 )
entry4 = tk.Entry ( root )
canvas.create_window ( 380, 200, window=entry4 )


label5 = tk.Label ( root, text='Epitaxial dopant:', bg="Orange", justify = "left")
label5.config (font = myFont, justify = "left")
canvas.create_window ( 81, 250, window=label5 )
entry5 = tk.Entry ( root )
canvas.create_window ( 380, 250, window=entry5 )


label6 = tk.Label ( root, text='Pwell dopant:', bg="Orange", justify = "left")
label6.config (font = myFont, justify = "left")
canvas.create_window ( 70, 300, window=label6 )
entry6 = tk.Entry ( root )
canvas.create_window ( 380, 300, window=entry6 )


label7 = tk.Label ( root, text='Temperature of oxidation (Celsius):', bg="Orange", justify = "left")
label7.config (font = myFont, justify = "left")
canvas.create_window ( 150, 350, window=label7 )
entry7 = tk.Entry ( root )
canvas.create_window ( 380, 350, window=entry7 )


label8 = tk.Label ( root, text='Channel dopant:', bg="Orange", justify = "left")
label8.config (font = myFont, justify = "left")
canvas.create_window ( 80, 400, window=label8 )
entry8 = tk.Entry ( root )
canvas.create_window ( 380, 400, window=entry8 )


label9 = tk.Label ( root, text='Materials of IPD:', bg="Orange", justify = "left")
label9.config (font = myFont, justify = "left")
canvas.create_window ( 80, 450, window=label9 )
entry9 = tk.Entry ( root )
canvas.create_window ( 380, 450, window=entry9 )


label10 = tk.Label ( root, text='Control gate dopant:', bg="Orange", justify = "left")
label10.config (font = myFont, justify = "left")
canvas.create_window ( 95, 500, window=label10 )
entry10 = tk.Entry ( root )
canvas.create_window ( 380, 500, window=entry10 )


label11 = tk.Label ( root, text='S/D regions dopant:', bg="Orange", justify = "left")
label11.config (font = myFont, justify = "left")
canvas.create_window ( 92, 550, window=label11 )
entry11 = tk.Entry ( root )
canvas.create_window ( 380, 550, window=entry11 )



label12 = tk.Label ( root, text='Control gate voltage (V):', bg="Orange", justify = "left")
label12.config (font = myFont, justify = "left")
canvas.create_window ( 620, 50, window=label12 )
entry12 = tk.Entry ( root )
canvas.create_window ( 900, 50, window=entry12 )


label13 = tk.Label ( root, text='Source voltage (V):', bg="Orange", justify = "left")
label13.config (font = myFont, justify = "left")
canvas.create_window ( 599, 100, window=label13 )
entry13 = tk.Entry ( root )
canvas.create_window ( 900, 100, window=entry13 )


label14 = tk.Label ( root, text='Drain voltage (V):', bg="Orange", justify = "left")
label14.config (font = myFont, justify = "left")
canvas.create_window ( 595, 150, window=label14 )
entry14 = tk.Entry ( root )
canvas.create_window ( 900, 150, window=entry14 )


label15 = tk.Label ( root, text='Substrate voltage (V) :', bg="Orange", justify = "left")
label15.config (font = myFont, justify = "left")
canvas.create_window ( 610, 200, window=label15 )
entry15 = tk.Entry ( root )
canvas.create_window ( 900, 200, window=entry15 )

def runTools():


    os.startfile("C:\sedatools\Shortcuts\DeckBuild")


def Addparameters():

    a1 = entry1.get ()
    b1 = entry2.get ()
    c = entry3.get ()
    d = entry4.get ()
    e = entry5.get ()
    z = entry6.get ()
    g = entry7.get ()
    hx = entry8.get ()
    j = entry9.get ()
    p = entry10.get ()
    k = entry11.get ()
    vcg = entry12.get ()
    vs = entry13.get ()
    vd = entry14.get ()
    vsub = entry15.get ()

    a = 'set' + ' ' + 'width =' + ' ' + a1
    b = 'Length =' + ' ' + "b1"

    output1 = 'beforeprogramwith' + a1 + 'Width=' + b1 + 'um' + vcg + 'V' + '.log'
    output2 = 'programwith' + a1 + 'um' + 'Width=' + b1 + 'um' + vcg + 'V' + '.log'
    output3 = 'memorywindow' + a1 + 'um' + 'Width=' + b1 + 'um' + vcg + 'V' + '.log'
    output4 = 'erasewith' + a1 + 'um' + 'Width=' + b1 + 'um' + vcg + 'V' + '.log'

    directory = 'Simulation with' + ' ' + a1 + ' ' + b1
    Input = '#Width:' + a1 + '\n' + '#Length:' + b1 + '\n' + '#Silicon Doping:' + d + '\n' + '#Epitaxial:' + e + '\n' + '#Pwell:' + z + '\n' + '#Tunnel Oxide:' + g + '\n' + '#Channel Doping:' + hx + '\n' + '#IPD layer::' + j + '\n' + '#Control gate:' + p + '\n' + '#S/D Creation:' + k + '\n' + '#Parameters for Program Operation:' + vcg + '\n' + '#Parameters for Erase Operation:' + '-' + vcg
    path_dir = r"C:\Users\lop94\Desktop\Tools\pythonProject1\pythonProject1"
    if not os.path.exists ( directory ):
        os.mkdir ( os.path.join ( path_dir, directory ) )
        dirname = pathlib.Path ( directory ).absolute ()
        os.chmod ( dirname, stat.S_IRWXO )


#Trước lập trình
    log_df = pd.read_csv (output1, skiprows=20, sep=' ', header=None )
    use_cols = [
        "Cgate Voltage", "Cgate Int.Voltage", "Cgate Current",
        "Fgate Intg Charge", "Fgate Int.Voltage", "Fgate Current",
        "Source Voltage", "Source Intg.Voltage", "Source Current",
        "Drain Voltage", "Drain Intg Voltage", "Drain Current",
        "Substrate Voltage", "Substrate Intg Voltage", "Substrate Curerent"
    ]
    log_df.columns = ["r1",
                      *use_cols,
                      "r2"]

    log_df = log_df[[
        *use_cols
    ]]

    results1 = f'{output1[:-4]}.csv'
    shutil.copy(results1, directory)

#Trong lập trình
    log_df = pd.read_csv (output2, skiprows=20, sep=' ', header=None )
    use_cols = [
        "Transient time",
        "Cgate Voltage", "Cgate Int.Voltage", "Cgate Current",
        "Fgate Intg Charge", "Fgate Int.Voltage", "Fgate Current",
        "Source Voltage", "Source Intg.Voltage", "Source Current",
        "Drain Voltage", "Drain Intg Voltage", "Drain Current",
        "Substrate Voltage", "Substrate Intg Voltage", "Substrate Curerent"
    ]
    log_df.columns = ["r1",
                      *use_cols,
                      "r2"]

    log_df = log_df[[
        *use_cols
    ]]

    results2 = f'{output2[:-4]}.csv'
    shutil.copy(results2, directory)


#Sau lập trình
    log_df = pd.read_csv (output3, skiprows=20, sep=' ', header=None )
    use_cols = [
        "Cgate Voltage", "Cgate Int.Voltage", "Cgate Current",
        "Fgate Intg Charge", "Fgate Int.Voltage", "Fgate Current",
        "Source Voltage", "Source Intg.Voltage", "Source Current",
        "Drain Voltage", "Drain Intg Voltage", "Drain Current",
        "Substrate Voltage", "Substrate Intg Voltage", "Substrate Curerent"
    ]
    log_df.columns = ["r1",
                      *use_cols,
                      "r2"]

    log_df = log_df[[
        *use_cols
    ]]

    results3 = f'{output3[:-4]}.csv'
    shutil.copy(results3, directory)

#Quá trình xóa
    log_df = pd.read_csv (output4, skiprows=20, sep=' ', header=None )
    use_cols = [
        "Transient time",
        "Cgate Voltage", "Cgate Int.Voltage", "Cgate Current",
        "Fgate Intg Charge", "Fgate Int.Voltage", "Fgate Current",
        "Source Voltage", "Source Intg.Voltage", "Source Current",
        "Drain Voltage", "Drain Intg Voltage", "Drain Current",
        "Substrate Voltage", "Substrate Intg Voltage", "Substrate Curerent"
    ]
    log_df.columns = ["r1",
                      *use_cols,
                      "r2"]

    log_df = log_df[[
        *use_cols
    ]]

    results4 = f'{output4[:-4]}.csv'
    shutil.copy(results4, directory)

    os.startfile(directory)

    filename = "Conventional_FG.in"

    with open ( filename, 'r+' ) as f:
        text = f.read ()

        text = re.sub ( 'set width=a', a, text )
        text = re.sub ( 'Length = x', b1, text )
        text = re.sub ( 'c.orientation', c, text )
        text = re.sub ( '=c.d', d, text )
        text = re.sub ( '=e', e, text )
        text = re.sub ( '=f', z, text )
        text = re.sub ( '=g', g, text )
        text = re.sub ( '=h', hx, text )
        text = re.sub ( '=p', p, text )
        text = re.sub ( '=k', k, text )
        text = re.sub ( 'output1', output1, text )
        text = re.sub ( 'output2', output2, text )
        text = re.sub ( 'output3', output3, text )
        text = re.sub ( 'output4', output4, text )
        text = re.sub ( '#Input', Input, text )
        f.seek ( 0 )

        y = text

        with open ( "Input.IN", "w" ) as h:
            h.write ( y )

    original = r'C:\Users\lop94\Desktop\Tools\pythonProject1\pythonProject1\Input.IN'
    target = r'C:\Users\lop94\Desktop\Tools\TCAD\Code\Input.IN'
    target1 = r'C:\Users\lop94\Desktop\Tools\TCAD\Code'
    shutil.copyfile(original,target)
    input1 = 'Floating-gate MOS with' + ' ' + a1 + ' ' + 'um ' + b1 + ' ' + 'um ' + ' ' + vcg + ' ' + 'V ' + '.in'
    shutil.copyfile(original, input1)
    shutil.copy(input1, directory)




def Exportdata():
    os.startfile("C:\sedatools\Shortcuts\DeckBuild")

def Importdata():
    os.startfile("C:\sedatools\Shortcuts\DeckBuild")

runTools = tk.Button(root, text="Run Simulations", padx=25, pady=5, fg="#FF0000", bg="#FFFF00", command=runTools)
runTools['font'] = myFont
runTools.pack()
Importdata = tk.Button(root, text="Import Input Data", padx=25, pady=5, fg="#FF0000", bg="#FFFF00", command=Importdata)
Importdata['font'] = myFont
Importdata.pack()
Exportdata = tk.Button(root, text="Export Output Data", padx=25, pady=5, fg="#FF0000", bg="#FFFF00" ,command=Exportdata)
Exportdata['font'] = myFont
Exportdata.pack()
Addparameters = tk.Button(root, text="Add Parameters", padx=25, pady=5, fg="#FF0000", bg="#FFFF00" ,command=Addparameters)
Addparameters['font'] = myFont
Addparameters.pack()
Importdata.place(x=275,y=625)
runTools.place(x=520,y=625)
Exportdata.place(x=760,y=625)
Addparameters.place(x=40,y=625)
root.mainloop()