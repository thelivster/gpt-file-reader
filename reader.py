import os
from pick import pick

title = 'Which files do you want to have copy pastable?'
options = ['Get all files', 'Get templates', 'Get models/views/urls', 'Get templates/views']
option, index = pick(options, title)


# actual reading/writing
txt = open('txt.txt', 'r+', encoding="ISO-8859-1")



if index == 0:
    for file in os.listdir():
        path = os.path.join(file)
        if os.path.isfile(path):
            tocopy = open(path, 'r')
            content = tocopy.readlines()
            txt.write('filename : '+path + '\n') 
            txt.writelines(content)
            txt.writelines('END OF ' + path + '\n' + '\n')
        elif os.path.isdir(path):
            for subfile in os.listdir(path):
                subpath = os.path.join(path, subfile)
                if os.path.isfile(subpath):
                    copy = open(subpath, 'r', encoding="ISO-8859-1")
                    subcontent = copy.readlines()
                    txt.write('filename : ' + subpath + '\n')
                    txt.writelines(subcontent)
                    txt.writelines('END OF ' + subpath + '\n' + '\n')  
                else : 
                    pass
        else : 
            pass
elif index == 1:
    for file in os.listdir():
        path = os.path.join(file)
        if os.path.isdir(path) and path == 'templates':
            for subfile in os.listdir(path):
                subpath = os.path.join(path, subfile)
                copy = open(subpath, 'r', encoding="ISO-8859-1")
                subcontent = copy.readlines()
                txt.write('filename : ' + subpath + '\n')
                txt.writelines(subcontent)
                txt.writelines('END OF ' + subpath + '\n' + '\n')
elif index == 2:
    for file in os.listdir():
        path = os.path.join(file)
        if os.path.isdir(path):
            for subfile in os.listdir(path):
                if subfile == 'models.py' or subfile == 'views.py' or subfile == 'urls.py':
                    subpath = os.path.join(path, subfile)
                    copy = open(subpath, 'r', encoding="ISO-8859-1")
                    subcontent = copy.readlines()
                    txt.write('filename : ' + subpath + '\n')
                    txt.writelines(subcontent)
                    txt.writelines('END OF ' + subpath + '\n' + '\n')
elif index == 3:
    for file in os.listdir():
        path = os.path.join(file)
        if os.path.isdir(path) and path == 'templates':
            for subfile in os.listdir(path):
                subpath = os.path.join(path, subfile)
                copy = open(subpath, 'r', encoding="ISO-8859-1")
                subcontent = copy.readlines()
                txt.write('filename : ' + subpath + '\n')
                txt.writelines(subcontent)
                txt.writelines('END OF ' + subpath + '\n' + '\n')
    for file in os.listdir():
        path = os.path.join(file)
        if os.path.isdir(path):
            for subfile in os.listdir(path):
                if subfile == 'views.py':
                    subpath = os.path.join(path, subfile)
                    copy = open(subpath, 'r', encoding="ISO-8859-1")
                    subcontent = copy.readlines()
                    txt.write('filename : ' + subpath + '\n')
                    txt.writelines(subcontent)
                    txt.writelines('END OF ' + subpath + '\n' + '\n')
    

    





    





            
                


    

