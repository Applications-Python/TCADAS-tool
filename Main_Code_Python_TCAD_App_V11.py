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


    os.startfile("C:\Program Files\Shortcuts\DeckBuild")


def Addparameters():
    var11 = entry1.get ()
    var21 = entry2.get ()
    var31 = entry3.get ()
    var41 = entry4.get ()
    var51 = entry5.get ()
    var61 = entry6.get ()
    var71 = entry7.get ()
    var81 = entry8.get ()
    var91 = entry9.get ()
    var101 = entry10.get ()
    var111 = entry11.get ()
    var121 = entry12.get ()
    var131 = entry13.get ()
    var141 = entry14.get ()
    var151 = entry15.get ()

    a1 = 'set' + ' ' + 'width =' + ' ' + var11
    b1 = 'Length =' + ' ' + var21

    output11 = 'beforeprogramwith' + var21 + 'Width=' + var11 + 'um' + var121 + 'V' + '.log'
    output21 = 'programwith' + var21 + 'um' + 'Width=' + var11 + 'um' + var121 + 'V' + '.log'
    output31 = 'memorywindow' + var21 + 'um' + 'Width=' + var11 + 'um' + var121 + 'V' + '.log'
    output41 = 'erasewith' + var21 + 'um' + 'Width=' + var11 + 'um' + var121 + 'V' + '.log'

    directory = 'Simulation with' + ' ' + var11 + ' ' + var21
    Input1 = '#Width:' + var11 + '\n' + '#Length:' + var21 + '\n' + '#Silicon Doping:' + var41 + '\n' + '#Epitaxial:' + var51 + '\n' + '#Pwell:' + var61 + '\n' + '#Tunnel Oxide:' + var71 + '\n' + '#Channel Doping:' + var81 + '\n' + '#IPD layer::' + var91 + '\n' + '#Control gate:' + var101 + '\n' + '#S/D Creation:' + var111 + '\n' + '#Parameters for Program Operation:' + var121 + '\n' + '#Parameters for Erase Operation:' + '-' + var121
    path_dir = r"C:\Users\lop94\Desktop\Tools\pythonProject1\pythonProject1"
    if not os.path.exists ( directory ):
        os.mkdir ( os.path.join ( path_dir, directory ) )
        dirname = pathlib.Path ( directory ).absolute ()
        os.chmod ( dirname, stat.S_IRWXO )

def Exportdata():
    var12 = entry1.get ()
    var22 = entry2.get ()
    var32 = entry3.get ()
    var42 = entry4.get ()
    var52 = entry5.get ()
    var62 = entry6.get ()
    var72 = entry7.get ()
    var82 = entry8.get ()
    var92 = entry9.get ()
    var102 = entry10.get ()
    var112 = entry11.get ()
    var122 = entry12.get ()
    var132 = entry13.get ()
    var142 = entry14.get ()
    var152 = entry15.get ()

    a2 = 'set' + ' ' + 'width =' + ' ' + var12
    b2 = 'Length =' + ' ' + var22

    output12 = 'beforeprogramwith' + var22 + 'Width=' + var12 + 'um' + var122 + 'V' + '.log'
    output22 = 'programwith' + var22 + 'um' + 'Width=' + var12 + 'um' + var122 + 'V' + '.log'
    output32 = 'memorywindow' + var22 + 'um' + 'Width=' + var12 + 'um' + var122 + 'V' + '.log'
    output42 = 'erasewith' + var22 + 'um' + 'Width=' + var12 + 'um' + var122 + 'V' + '.log'

    directory = 'Simulation with' + ' ' + var12 + ' ' + var22
    Input2 = '#Width:' + var12 + '\n' + '#Length:' + var22 + '\n' + '#Silicon Doping:' + var42 + '\n' + '#Epitaxial:' + var52 + '\n' + '#Pwell:' + var62 + '\n' + '#Tunnel Oxide:' + var72 + '\n' + '#Channel Doping:' + var82 + '\n' + '#IPD layer::' + var92 + '\n' + '#Control gate:' + var102 + '\n' + '#S/D Creation:' + var112 + '\n' + '#Parameters for Program Operation:' + var122 + '\n' + '#Parameters for Erase Operation:' + '-' + var122
    path_dir = r"C:\Users\lop94\Desktop\Tools\pythonProject1\pythonProject1"
    if not os.path.exists ( directory ):
        os.mkdir ( os.path.join ( path_dir, directory ) )
        dirname = pathlib.Path ( directory ).absolute ()
        os.chmod ( dirname, stat.S_IRWXO )
    os.startfile ( directory )

#Trước lập trình
    results1 = f'{output12[:-4]}.csv'
    log_df = pd.read_csv ( output12, skiprows=20, sep=' ', header=None )
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
    log_df.to_csv(f'{path_dir}/{results1}')


    shutil.copy ( results1, directory )

    # Trong lập trình
    results2 = f'{output22[:-4]}.csv'
    log_df = pd.read_csv ( output22, skiprows=20, sep=' ', header=None )
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
    log_df.to_csv ( f'{path_dir}/{results2}' )
    shutil.copy ( results2, directory )

    # Sau lập trình
    results3 = f'{output32[:-4]}.csv'
    log_df = pd.read_csv ( output32, skiprows=20, sep=' ', header=None )
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

    log_df.to_csv ( f'{path_dir}/{results3}' )
    shutil.copy ( results3, directory )

    # Quá trình xóa
    results4 = f'{output42[:-4]}.csv'
    log_df = pd.read_csv ( output42, skiprows=20, sep=' ', header=None )
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

    log_df.to_csv ( f'{path_dir}/{results4}' )
    shutil.copy ( results4, directory )

    os.startfile(directory)

def Importdata():
    var1 = entry1.get ()
    var2 = entry2.get ()
    var3 = entry3.get ()
    var4 = entry4.get ()
    var5 = entry5.get ()
    var6 = entry6.get ()
    var7 = entry7.get ()
    var8 = entry8.get ()
    var9 = entry9.get ()
    var10 = entry10.get ()
    var11 = entry11.get ()
    var12 = entry12.get ()
    var13 = entry13.get ()
    var14 = entry14.get ()
    var15 = entry15.get ()

    a = 'set' + ' ' + 'width =' + ' ' + var1
    b = 'Length =' + ' ' + var2

    output1 = 'beforeprogramwith' + var2 + 'Width=' + var1 + 'um' + var12 + 'V' + '.log'
    output2 = 'programwith' + var2 + 'um' + 'Width=' + var1 + 'um' + var12 + 'V' + '.log'
    output3 = 'memorywindow' + var2 + 'um' + 'Width=' + var1 + 'um' + var12 + 'V' + '.log'
    output4 = 'erasewith' + var2 + 'um' + 'Width=' + var1 + 'um' + var12 + 'V' + '.log'

    directory = 'Simulation with' + ' ' + var1 + ' ' + var2
    Input = '#Width:' + var1 + '\n' + '#Length:' + var2 + '\n' + '#Silicon Doping:' + var4 + '\n' + '#Epitaxial:' + var5 + '\n' + '#Pwell:' + var6 + '\n' + '#Tunnel Oxide:' + var7 + '\n' + '#Channel Doping:' + var8 + '\n' + '#IPD layer::' + var9 + '\n' + '#Control gate:' + var10 + '\n' + '#S/D Creation:' + var11 + '\n' + '#Parameters for Program Operation:' + var12 + '\n' + '#Parameters for Erase Operation:' + '-' + var12
    path_dir = r"C:\Users\lop94\Desktop\Tools\pythonProject1\pythonProject1"
    if not os.path.exists ( directory ):
        os.mkdir ( os.path.join ( path_dir, directory ) )
        dirname = pathlib.Path ( directory ).absolute ()
        os.chmod ( dirname, stat.S_IRWXO )
    filename = "Conventional_FG.in"

    with open ( filename, 'r+' ) as f:
        text = f.read ()

        text = re.sub ( '#width', var1, text )
        text = re.sub ( '#length', var2, text )
        text = re.sub ( '#orientation', var3, text )
        text = re.sub ( '#silicondose', var4, text )
        text = re.sub ( '#epitaxialdose', var5, text )
        text = re.sub ( '#pwelldose', var6, text )
        text = re.sub ( '#oxidationtemperature', var7, text )
        text = re.sub ( '#channeldose', var8, text )
        text = re.sub ( 'IPDlayers', var9, text )
        text = re.sub ( '#controlgatedose', var10, text )
        text = re.sub ( '#S/Ddose', var11, text )
        text = re.sub ( '#vcgate', var12, text )
        text = re.sub ( '#vsource', var13, text )
        text = re.sub ( '#vdrain', var14, text )
        text = re.sub ( '#vsubstrate', var15, text )
        text = re.sub ( '#output1', output1, text )
        text = re.sub ( '#output2', output2, text )
        text = re.sub ( '#output3', output3, text )
        text = re.sub ( '#output4', output4, text )
        text = re.sub ( '#Input', Input, text )
        f.seek ( 0 )

        y = text

        with open ( "Input.IN", "w" ) as h:
            h.write ( y )

    original = r'C:\Users\lop94\Desktop\Tools\pythonProject1\pythonProject1\Input.IN'
    target = r'C:\Users\lop94\Desktop\Tools\TCAD\Code\Input.IN'
    target1 = r'C:\Users\lop94\Desktop\Tools\TCAD\Code'
    shutil.copyfile(original,target)
    input1 = 'Floating-gate MOS with' + ' ' + var1 + ' ' + 'um ' + var2 + ' ' + 'um ' + ' ' + var12 + ' ' + 'V ' + '.in'
    shutil.copyfile(original, input1)
    shutil.copy(input1, directory)

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