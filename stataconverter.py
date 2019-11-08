import pandas as pd
import PySimpleGUI as sg

while True:
    layout = [
            [sg.Text('Stata file to convert')],
            [sg.In(), sg.FileBrowse()],
            [sg.Text('Flags (optional)', size=(15, 1)),      
               sg.Drop(values=('','convert_categoricals=False'), size=(25, 1))],      
            [sg.Open('Convert'), sg.Cancel('Exit')]]
    window = sg.Window('Stata converter', layout)
    event, values = window.Read()
    fname = values[0]
    success = True
    if fname:
        if values[1] == '':
            try:
                df = pd.read_stata(fname)
            except Exception as e:
                sg.Popup(e)
                success = False
        elif values[1] == 'convert_categoricals=False':
            df = pd.read_stata(fname, convert_categoricals=False) 
        if success:
            try:
                df.to_stata(fname[0:-4]+"converted.dta")
            except Exception as e:
                sg.Popup(e)
    if event == 'Exit' or event == None:
        break
    elif not fname:
        sg.Popup("File not found")
window.Close()
