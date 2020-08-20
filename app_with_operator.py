import pyttsx3
import os

print("=================================================")
print("           * Activepresenter                     ")
print("           * Paint                               ")
print("           * VLC media player                    ")
print("           * notepad                             ")
print("           * Pycharm IDE                         ")
print("           * Eclipse IDE                         ")
print("           * Quickheal Antivirus Pro             ")
print("           * Chrome                              ")
print("=================================================")


pyttsx3.speak("Which app can  I open for you ?") 

#print(p)
#os.system(p)
while True:
    
    print("\n Which app can  I run or open for you from above mentioned list ? : ",end=' ')
    
    p = input()
    if (("run" in p) or ("execute" in p) or ("open" in p)) and (("activepresenter" in p) or ("screenrecorder" in p) or ("Activepresenter" in p)):
        os.system("ActivePresenter")
        pyttsx3.speak("ActivePresenter has closed.")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("paint" in p) or ("mspaint" in p) or ("Paint" in p)):
        os.system("mspaint")
        pyttsx3.speak("Paint has closed.")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("vlc media Player" in p) or ("player" in p) or("VLC" in p)):
        os.system("VLC media player")
        pyttsx3.speak("VLC media player has closed.")
    elif (("run" in p) or ("execute" in p) or ("open" in p)) and (("notepad" in p) or ("editor" in p) or ("Notepad" in p)):
        os.system("notepad")
        pyttsx3.speak("notepad has closed.")
    elif (("run" in p) or ("launch" in p) or ("open" in p)) and (("Pycharm64" in p) or ("Pycharm" in p)  or ("pycharm" in p)):
        os.system("Pycharm64")
        pyttsx3.speak("Pycharm has closed.")
    elif (("run" in p) or ("launch" in p) or ("open" in p)) and (("eclipse" in p)  or ("Eclipse" in p) ):
        os.system("eclipse")
        pyttsx3.speak("Eclipse has closed .")
    elif (("run" in p) or ("launch" in p) or ("open" in p)) and (("Quickheal" in p) or ("scanner" in p) or ("antivirus" in p) or ("quickheal" in p)):
        os.system("scanner")
    elif (("run" in p) or ("launch" in p) or ("open" in p)) and (("chrome" in p) or ("browser" in p) or ("Chrome" in p)):
        os.system("chrome")
        pyttsx3.speak("Chrome has closed.")
    elif ("exit" in p) or ("quit" in p):
        pyttsx3.speak("Thank you !")
        break
    else:
        print("-------------------------------------------------------------------")
        print("This app can't support   or you have entered wrong app name !")
        print("Please give your input as shown bellow.")
        print("eg :- open notepad")
        print("eg :- run notepad")
        print("-------------------------------------------------------------------\n")
        pyttsx3.speak("Please read above mentioned instructions !") 
      
        

