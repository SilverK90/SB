import eel
import PatientData

eel.init('web')

@eel.expose
def GetResult(name, age):
    text = PatientData.Search_js(name, age)
    print(text)
    return text

eel.start('index.html')
