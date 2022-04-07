from re import search
import eel
import desktop
import main

app_name="html"
end_point="index.html"
size=(700,600)

@ eel.expose
def cat_search(word, csv_name):
    main.cat_search(word, csv_name)
    
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)