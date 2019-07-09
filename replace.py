import fileinput
import os

def replace():
    yourpath = 'D:\Laravel\python'

    List = ["index.php", ".DS_Store",".htaccess","assets","favicon.ico","robots.txt","storage","svg","web.config"] 
    image_possible_changes =['<img src="','<img src ="','<img src= "','img src = "']
    font_possible_changes=['src: url(']

    for directoryfile in os.listdir(yourpath):
        if (directoryfile in List):  
            continue   # Don't touch other files
        directorypath = 'D:\Laravel\python\\'+directoryfile  
        for root, dirs, files in os.walk(directorypath, topdown=False):
            for filename in files:
                if filename.endswith(".php"):
                    filepath="D:\Laravel\python\\"+directoryfile+"/"+filename
                    for changes in image_possible_changes:
                        with open(filepath, encoding="utf8") as f:
                            newText=f.read().replace(changes, '<img src="'+directoryfile+'/')
                            with open(filepath, "w", encoding="utf8") as f:
                                f.write(newText)
                    for changes in font_possible_changes:
                        with open(filepath, encoding="utf8") as f:
                            newText=f.read().replace(changes, 'src: url('+directoryfile+'/')
                            with open(filepath, "w", encoding="utf8") as f:
                                f.write(newText)

    print("Replace Successfull")