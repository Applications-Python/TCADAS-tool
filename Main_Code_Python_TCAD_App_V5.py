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
output1 = 'beforeprogramwith' + a1 +'Width='+ b1 + vcg+'(V)'
output2 = 'programwith' +a1 + 'um' + 'Width=' + b1 +'um'+ tprogram + 's'
output3 = 'memorywindow' +a1 +'um' + 'Width=' + b1 +'um'+ tprogram + 's'
output4 = 'erasewith' + a1 + 'um' + 'Width=' + b1 +'um'+ terase + 's' + vcg2+'(V)'
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
    output1 = pd.read_csv("Cgate1.csv",delimiter='\t')
    output1 = output1[:][3:-1]
    input1 = [output1.iloc[i].tolist()[0].split() for i in range(0, output1.index[-1] - 2)]
    print ( input1 )
    output2 = pd.read_csv ( "Drain1.csv", delimiter='\t' )
    output2 = output2[:][3:-1]
    input2 = [output2.iloc[i].tolist ()[0].split () for i in range ( 0, output2.index[-1] - 2 )]
    print ( input2 )
    output3 = pd.read_csv ( "Substrate1.csv", delimiter='\t' )
    output3 = output3[:][3:-1]
    input3 = [output3.iloc[i].tolist ()[0].split () for i in range ( 0, output3.index[-1] - 2 )]
    print ( input3 )
    output4 = pd.read_csv ( "Cgate2.csv", delimiter='\t' )
    output4 = output4[:][3:-1]
    input4 = [output4.iloc[i].tolist ()[0].split () for i in range ( 0, output4.index[-1] - 2 )]
    print ( input4 )
    output5 = pd.read_csv ( "Drain2.csv", delimiter='\t' )
    output5 = output5[:][3:-1]
    input5 = [output5.iloc[i].tolist ()[0].split () for i in range ( 0, output5.index[-1] - 2 )]
    print ( input5 )
    output6 = pd.read_csv ( "Substrate2.csv", delimiter='\t' )
    output6 = output6[:][3:-1]
    input6 = [output6.iloc[i].tolist ()[0].split () for i in range ( 0, output6.index[-1] - 2 )]
    print ( input6 )
    output7 = pd.read_csv ( "Cgate3.csv", delimiter='\t' )
    output7 = output7[:][3:-1]
    input7 = [output7.iloc[i].tolist ()[0].split () for i in range ( 0, output7.index[-1] - 2 )]
    print ( input7 )
    output8 = pd.read_csv ( "Drain3.csv", delimiter='\t' )
    output8 = output8[:][3:-1]
    input8 = [output8.iloc[i].tolist ()[0].split () for i in range ( 0, output8.index[-1] - 2 )]
    print ( input8 )
    output9 = pd.read_csv ( "Substrate3.csv", delimiter='\t' )
    output9 = output9[:][3:-1]
    input9 = [output9.iloc[i].tolist ()[0].split () for i in range ( 0, output9.index[-1] - 2 )]
    print ( input9 )
    nameFile1 = 'Data Simulation with' + ' ' + a + ' ' + 'um ' + b + ' ' + 'um ' + ' ' + vcg + ' ' + 'V ' + tprogram + ' ' + 's ' + terase + ' ' + 's ' + '.xlsx'
    workbook = xlsw.Workbook(nameFile1)
    worksheet = workbook.add_worksheet('Simulation 1')
    col = 0
    for row, data in enumerate(input1):
        worksheet.write_row(row + 1, col, data)
    worksheet.write(0, 0,'Voltage Cgate')
    worksheet.write(0, 1, 'Current Cgate')
    col = 2
    for row, data in enumerate ( input2 ):
        worksheet.write_row ( row + 1, col, data )
    worksheet.write ( 0, 2, 'Voltage Drain' )
    worksheet.write ( 0, 3, 'Current Drain' )
    col = 4
    for row, data in enumerate ( input3 ):
        worksheet.write_row ( row + 1, col, data )
    worksheet.write ( 0, 4, 'Voltage Substrate' )
    worksheet.write ( 0, 5, 'Current Substrate' )
    worksheet = workbook.add_worksheet ( 'Simulation 2' )
    col = 0
    for row, data in enumerate ( input4 ):
        worksheet.write_row ( row + 1, col, data )
    worksheet.write ( 0, 0, 'Voltage Cgate' )
    worksheet.write ( 0, 1, 'Current Cgate' )
    col = 2
    for row, data in enumerate ( input5 ):
        worksheet.write_row ( row + 1, col, data )
    worksheet.write ( 0, 2, 'Voltage Drain' )
    worksheet.write ( 0, 3, 'Current Drain' )
    col = 4
    for row, data in enumerate ( input6 ):
        worksheet.write_row ( row + 1, col, data )
    worksheet.write ( 0, 4, 'Voltage Substrate' )
    worksheet.write ( 0, 5, 'Current Substrate' )
    worksheet = workbook.add_worksheet ( 'Simulation 3' )
    col = 0
    for row, data in enumerate ( input7 ):
        worksheet.write_row ( row + 1, col, data )
    worksheet.write ( 0, 0, 'Voltage Cgate' )
    worksheet.write ( 0, 1, 'Current Cgate' )
    col = 2
    for row, data in enumerate ( input8 ):
        worksheet.write_row ( row + 1, col, data )
    worksheet.write ( 0, 2, 'Voltage Drain' )
    worksheet.write ( 0, 3, 'Current Drain' )
    col = 4
    for row, data in enumerate ( input9 ):
        worksheet.write_row ( row + 1, col, data )
    worksheet.write ( 0, 4, 'Voltage Substrate' )
    worksheet.write ( 0, 5, 'Current Substrate' )
    workbook.close()
def Importdata():
    original = r'C:\Users\lop94\Desktop\Tools\pythonProject1\pythonProject1\Input.IN'
    target = r'C:\Users\lop94\Desktop\Tools\TCAD\Code\Input.IN'
    target1 = r'C:\Users\lop94\Desktop\Tools\TCAD\Code'
    shutil.copyfile(original,target)
    input1 = 'Floating-gate MOS with' + ' ' + a + ' ' + 'um ' + b + ' ' + 'um ' + ' ' + vcg + ' ' + 'V ' + tprogram + ' ' + 's ' + terase + ' ' + 's ' + '.in'
    shutil.copyfile(original, input1)
    shutil.move(input1,target1) #move file source code
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