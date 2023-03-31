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

showStatusbar=True
showToolbar=True
fontFamily="Arial"
url=""
fontSize=12
textChanged=False



# print("Full path: " + absolute_path)
# print("Directory Path: " + os.path.dirname(absolute_path))
# print(Directory)
# import Calculator
# import Calculator

root = tk.Tk()
root.title("Welcome to TCADAS Tool")
root.resizable(False,False)
root.iconbitmap(r'1.ico')
absolute_path = os.path.abspath(__file__)
Directory = os.path.dirname(absolute_path)
print(Directory)
# root.geometry("800x500")
bg = PhotoImage(file='test.png')
# root.geometry("380x550+850+200")
# root.resizable(False,False)
# root = tk.Tk()
# root.title("Welcome to Calculator")
# root.geometry("380x550+850+200")

myFont = font.Font(family='Arial', size=12, weight='bold')
# entry_box=Entry(font='verdana 14 bold', width = 22, bd = 10)
# entry_box.place(x=200,y=400)
a1 = input ( "Please input Width (um):" )
b1 = input ( "Please input Length (um):" )
a = 'set' + ' ' + 'width =' + ' ' + a1
b = 'Length =' + ' ' + b1
c = 'c' + '.' + input ( "Please input Silicon Dopant (Enter: Dopant Material = Dose):" )
d = 'temp' + ' ' + '=' + ' ' + input ( "Please input Epitaxial Temperature:" ) + ' ' + 't.final' + ' ' + '=' + ' ' + '1000' + ' ' + 'c' + '.'+ input ( "Please input Epitaxial Dopant (Enter: Dopant Material = Dose):" )+ ' ' +'thickness'  + ' ' + '=' +input ( "Please input Epitaxial Thickness (um):" )
e = input ( "Please input Pwell Dopant Material:" ) + ' ' + 'dose' + ' ' + '=' + ' ' + input ( "Please input Pwell Dopant Dose:" ) + ' ' + 'energy' + ' ' + '=' + ' ' + input ( "Please input Pwell Dopant Energy:" )
g = 'temp' + ' ' + '=' + ' ' + input ( "Please input Oxidation Temperature (Tunnel Oxide):" ) + ' ' + input ( "Please enter dryo2 or weto2:" )
hy = input ( "Please input Channel Dopant Material:" ) + ' ' + 'dose' + ' ' + '=' + ' ' + input ( "Please input Channel Dopant Dose:" ) + ' ' + 'energy' + ' ' + '=' + ' ' + input ( "Please input Channel Dopant Energy:" )
hx = input ( "Please input Floating gate Material:" ) + ' ' + 'thick' + ' ' + '=' + ' ' + input ( "Please input Floating gate Thickness (um):" )
hz = input ( "Please input Floating gate Dopant Material:" ) + ' ' + 'dose' + ' ' + '=' + ' ' + input ( "Please input Floating gate Dopant Dose:" ) + ' ' + 'energy' + ' ' + '=' + ' ' + input ( "Please input Floating gate Dopant Energy:" )
IPD1 = input ( "Please input First IPD layer Material:" ) + ' ' + 'thick' + ' ' + '=' + ' ' + input ( "Please input First IPD layer Thickness (um):" )
IPD2 = input ( "Please input Second IPD layer Material:" ) + ' ' + 'thick' + ' ' + '=' + ' ' + input ( "Please input Second IPD layer Thickness (um):" )
IPD3 = input ( "Please input Third IPD layer Material:" ) + ' ' + 'thick' + ' ' + '=' + ' ' + input ( "Please input Third IPD layer Thickness (um):" )
xx = input ( "Please input Control gate Material:" ) + ' ' + 'thick' + ' ' + '=' + ' ' + input ( "Please input Control gate Thickness (um):" )
xz = input ( "Please input Control gate Dopant Material:" ) + ' ' + 'dose' + ' ' + '=' + ' ' + input ( "Please input Control gate Dopant Dose:" ) + ' ' + 'energy' + ' ' + '=' + ' ' + input ( "Please input Control gate Dopant Energy:" )
yy = input ( "Please input Protect Device layer Material:" ) + ' ' + 'thick' + ' ' + '=' + ' ' + input ( "Please input Protect Device layer Thickness (um):" )
zz = input ( "Please input S/D Regions Dopant Material:" ) + ' ' + 'dose' + ' ' + '=' + ' ' + input ( "Please input S/D Regions Dopant Dose:" ) + ' ' + 'energy' + ' ' + '=' + ' ' + input ( "Please input S/D Regions Dopant Energy:" )
xyz = input ( "Please input Contact S/D Material:" ) + ' ' + 'thick' + ' ' + '=' + ' ' + input ( "Please input Contact S/D Thickness (um):" )
final = 'temp' + ' ' + '=' + ' ' + input ( "Please input Temperature to create S/D Regions:" )
vcg = input ( "Please input Vcontrol for programming (V):")
vs = input ( "Please input Vsource for programming (V):" )
vd = input ( "Please input Vdrain for programming (V):" )
tprogram = input ( "Please input time for programming (s):" )
vcg2 = input ( "Please input Vcontrol for erasing (V):" )
vs2 = input ( "Please input Vsource for erasing (V):" )
vd2 = input ( "Please input Vdrain for erasing (V):" )
fgate = input ( "Please input Fgate charge for erasing (C):" )
terase = input ( "Please input time for erasing (s):" )
output1 = 'beforeprogramwith' + a1 +'Width='+ b1 + vcg+'(V)'+'.log'
output2 = 'programwith' +a1 + 'um' + 'Width=' + b1 +'um'+ tprogram + 's'+'.log'
output3 = 'memorywindow' +a1 +'um' + 'Width=' + b1 +'um'+ tprogram + 's'+'.log'
output4 = 'erasewith' + a1 + 'um' + 'Width=' + b1 +'um'+ terase + 's' + vcg2+'(V)'+'.log'
directory = 'Simulation with' + ' ' + a + ' ' + b
Input = '#Width:' + a1 + '\n' + '#Length:' + b1 +  '\n' + '#Silicon Doping:' + c +  '\n' + '#Epitaxial:' + d + '\n' + '#Pwell:' + e + '\n' + '#Tunnel Oxide:' + g +  '\n' + '#Channel Doping:' + hy +  '\n' + '#Floating gate:' + hy + hz +  '\n' + '#IPD layer::' + IPD1 + IPD2 + IPD3 +  '\n' + '#Control gate:' + xx + xz +  '\n' + '#Protect Device:' + yy +  '\n' + '#S/D Creation:' + zz + xyz + final +  '\n' + '#Parameters for Program Operation:' + vcg + vd + vs + tprogram + '\n' + '#Parameters for Erase Operation:' + vcg2 + vd2 + vs2 + terase
path_dir = r"C:\Users\lop94\Desktop\Tools\pythonProject1\pythonProject1"
if not os.path.exists ( directory ):
    os.mkdir ( os.path.join ( path_dir, directory ) )
    dirname = pathlib.Path ( directory ).absolute ()
    #os.chmod (dirname,stat.S_IRWXO)
def runTools():
    # os.system("C:\sedatools\etc\GuiAppStarter.exe -lib-dir-name deckbuild -exe-name deckbuild")
    os.startfile("C:\sedatools\Shortcuts\DeckBuild")
    # df = pd.DataFrame ( {'Length':[],'Width':[]})

    # df.to_excel ( './Input.xlsx' )
    # os.startfile ( 'Input.xlsx' )
    # for widget in frame.winfo_children():
    #     widget.destroy()
    # frame = tk.Frame ( root, bg="#DCDCDC" )
    # frame.place ( relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1 )
# def addParameters():
    # os.system("C:/Users/lop94/PycharmProjects/pythonProject1/Calculator.py")
# apps = []
# def addApp():
#     pas
#     # for widget in frame.winfo_children():
#     #     widget.destroy()
#     # filename = filedialog.askopenfilename(initialdir="/",title="Select Tool",
#     #                                       filetypes=(("All files", "*.*"),("Executables", "*.exe")))
#     # apps.append(filename)
#     # print(filename)
#     # for app in apps:
#     #
#     #
# def runOthersTools():
#     pas
#
#     # for app in apps:
#     #     os.startfile(app)

def Addparameters():
    filename = "Conventional_FG.in"

    with open(filename, 'r+') as f:
        text = f.read()


        text = re.sub('set width=a', a, text)
        text = re.sub('Length = x', b, text)
        text = re.sub('c.boron=c', c, text)
        text = re.sub('temp = d t.final = 1000 c.arsenic=e thickness = f', d, text)
        text = re.sub('boron dose=g energy=g', e, text)
        text = re.sub('temp=f dryo2X', g, text)
        text = re.sub('boron dose=h energy=h', hy, text)
        text = re.sub ( 'poly thick=hx', hx, text )
        text = re.sub ( 'phos dose=hz energy=hz', hz, text )
        text = re.sub ( 'oxide thick=IPD1', IPD1, text )
        text = re.sub ( 'nitride thick=IPD2', IPD2, text )
        text = re.sub ( 'oxide thick=IPD3', IPD3, text )
        text = re.sub ( 'poly thick=xx', xx, text )
        text = re.sub ( 'phosphor dose=xz energy=xz', xz, text )
        text = re.sub ( 'oxide thick=yy', yy, text )
        text = re.sub ( 'arsenic dose=zz energy=zz', zz, text )
        text = re.sub ( 'alumin thick=xyz', xyz, text )
        text = re.sub ( 'temp=final', final, text )
        text = re.sub ( 'vcg1', vcg, text )
        text = re.sub ( 'vs1', vs, text )
        text = re.sub ( 'vd1', vd, text )
        text = re.sub ( 'tprogram', tprogram, text )
        text = re.sub ( 'vcg2', vcg2, text )
        text = re.sub ( 'vs2', vs2, text )
        text = re.sub ( 'vd2', vd2, text )
        text = re.sub ( 'fgate1', fgate, text )
        text = re.sub ( 'terase', terase, text )
        text = re.sub ( 'output1', output1, text )
        text = re.sub ( 'output2', output2, text )
        text = re.sub ( 'output3', output3, text )
        text = re.sub ( 'output4', output4, text )
        text = re.sub ( '#Input', Input, text )
        f.seek(0)
        # open(a+b+.in)
        y = text

        # f.write ( text )
        # f.truncate ()
        with open("Input.IN", "w") as h:
            h.write(y)



def Exportdata():
#    os.startfile(directory)
#    Python_Directory = r'C:\Users\lop94\Desktop\Tools\pythonProject1\pythonProject1'
 #   shutil.copy (output1, Python_Directory)
#    file_pth = f'{output1}.log'

    # for file_pth in file_pths:
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

def Importdata():
    original = r'C:\Users\lop94\Desktop\Tools\pythonProject1\pythonProject1\Input.IN'
    target = r'C:\Users\lop94\Desktop\Tools\TCAD\Code\Input.IN'
    target1 = r'C:\Users\lop94\Desktop\Tools\TCAD\Code'
    shutil.copyfile(original,target)
    input1 = 'Floating-gate MOS with' + ' ' + a + ' ' + 'um ' + b + ' ' + 'um ' + ' ' + vcg + ' ' + 'V ' + tprogram + ' ' + 's ' + terase + ' ' + 's ' + '.in'
    shutil.copyfile(original, input1)
    shutil.copy(input1, directory)
#    shutil.move(input1, target1) #move file source code
    #shutil.copyfile(target,dirname)
canvas = tk.Canvas(root, height=700, width=700, bg="Orange")
canvas.create_image(50,120,anchor=NW,image=bg)
# )
canvas.pack()
# frame = tk.Frame(root,bg=bg)
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1,rely=0.1)


# openFile = tk.Button(root, text="Open Files", padx=10, pady=5, fg="#FF0000", bg="#DCDCDC" ,command=addApp)
# openFile.pack()
runTools = tk.Button(root, text="Run Simulations", padx=25, pady=5, fg="#FF0000", bg="#FFFF00", command=runTools)
runTools['font'] = myFont
runTools.pack()
# runOthersTools = tk.Button(root, text="Run Others Files", padx=10, pady=5, fg="#FF0000", bg="#DCDCDC", command=runOthersTools)
# runTools.pack()
Importdata = tk.Button(root, text="Import Input Data", padx=15, pady=5, fg="#FF0000", bg="#FFFF00", command=Importdata)
Importdata['font'] = myFont
Importdata.pack()
Exportdata = tk.Button(root, text="Export Output Data", padx=16, pady=5, fg="#FF0000", bg="#FFFF00" ,command=Exportdata)
Exportdata['font'] = myFont
Exportdata.pack()
Addparameters = tk.Button(root, text="Add Parameters", padx=15, pady=5, fg="#FF0000", bg="#FFFF00" ,command=Addparameters)
Addparameters['font'] = myFont
Addparameters.pack()
Importdata.place(x=160,y=0)
# openFile.place(x=50,y=40)
runTools.place(x=334,y=0)
# runOthersTools.place(x=200,y=0)
Exportdata.place(x=512,y=0)
Addparameters.place(x=0,y=0)
root.mainloop()