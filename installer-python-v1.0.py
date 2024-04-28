from tkinter import *
import tkinter as ttk
import subprocess
import os
import shutil


hasNvidium=True

userPath = os.path.expanduser(f'~{os.getlogin()}')+'\AppData\Roaming'


hasLegacy=False
hasTlauncher=False
apps = os.listdir(userPath)
if '.minecraft' in apps:
    hasTlauncher = True
if '.tlauncher' in apps and 'legacy' in os.listdir(os.path.expanduser(f'~{os.getlogin()}')+'\AppData\Roaming\.tlauncher'):
    hasLegacy=True
# Modifie ici les valeurs de base de hasMc et hasLegacy
highPerf=False
launchers = hasLegacy+hasTlauncher

# Définition des fonctions d'installation des fichiers -> Zone à modifier : fonction "install()"
def highPerfPc():
    global highPerf
    highPerf=True
    buttonYes.grid_forget()
    buttonNo.grid_forget()
    labelQuestion.grid_forget()
    root.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=5)
    if launchers>1:
        choix_launcher()
    else : install(userPath,0)

def lowPerfPc():
    global highPerf
    highPerf = False
    buttonYes.grid_forget()
    buttonNo.grid_forget()
    labelQuestion.grid_forget()
    root.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=5)
    if launchers>1:
        choix_launcher()
    else: install(userPath,0)
    


def legacy():
    install(userPath, 1)

def minecraft():
    install(userPath, 2)


def install(userPath, x):
    hasLegacy=False
    hasTlauncher=False
    apps = os.listdir(userPath)
    if '.minecraft' in apps:
        hasTlauncher = True
    if '.tlauncher' in apps and 'legacy' in os.listdir(os.path.expanduser(f'~{os.getlogin()}')+'\AppData\Roaming\.tlauncher'):
        hasLegacy=True
    if x==1:
        hasTlauncher=False
    elif x==2:
        hasLegacy=False
    if launchers==0 :
        labelNotSupported.grid(row=4, column=5)
        return ""
    if hasTlauncher:
        userPath+='\.minecraft'
    if hasLegacy:
        userPath+='\.tlauncher\legacy\Minecraft\game'
    try:
        os.listdir(userPath+'\mods')
    except:
        os.mkdir(userPath+'\mods')
    print(userPath)
    if not(len(os.listdir(userPath+'\mods'))==0 or (len(os.listdir(userPath+'\mods'))==1 and os.listdir(userPath+'\mods')[0][:4]=='tl_skin_cape'[:4])):
        try:
            shutil.copytree(userPath+'\mods', os.path.join(os.path.expanduser('~'), 'Desktop\Ancien_Mods'))
        except:pass
    shutil.rmtree(userPath+'\mods')
    shutil.move('files/mods', userPath+'\mods')
    try :
        shutil.rmtree(userPath+os.path.join('\config', 'fabric_potions'))
    except : pass
    shutil.move('files/config/fabric_potions', userPath+os.path.join('\config', 'fabric_potions'))
    try :
        shutil.rmtree(userPath+os.path.join('\config', 'bobby.conf'))
    except : pass
    shutil.move('files/config/bobby.conf', userPath+os.path.join('\config', 'bobby.conf'))
    try :
        shutil.rmtree(os.path.join(userPath, 'versions', 'fabric-loader-0.15.7-1.20.1'))
    except : pass
    shutil.move('files/fabric-loader-0.15.7-1.20.1', os.path.join(userPath, 'versions', 'fabric-loader-0.15.7-1.20.1'))
    try :
        shutil.rmtree(userPath+os.path.join('\config', 'immersive_weathering-common.json'))
    except : pass
    shutil.move('files/config/immersive_weathering-common.json', userPath+os.path.join('\config', 'immersive_weathering-common.json'))
    if hasNvidium :
        try :
            shutil.move('files/nvidium-0.2.6-beta.jar', os.path.join(userPath+'\mods', 'nvidium-0.2.6-beta.jar'))
        except : pass
    try :
        shutil.rmtree(os.path.join(userPath, 'resourcepacks\Connected_World_v1.4_for_1.20'))
    except : pass
    shutil.move('files/Connected_World_v1.4_for_1.20', os.path.join(userPath, 'resourcepacks\Connected_World_v1.4_for_1.20'))
    labelEnd.grid(row=4, column=5)
    if highPerf:
        try :
            shutil.rmtree(userPath +'\options.txt')
        except : pass
        shutil.move('files/options1.txt', userPath +'\options.txt')
        shutil.rmtree('files')
    else :
        try :
            shutil.rmtree(userPath +'\options.txt')
        except : pass
        shutil.move('files/options0.txt', userPath +'\options.txt')
        shutil.rmtree('files')

    # labelNotSupported.grid(row=4, column=5)
    """
    La dernière ligne en note, c'est pour afficher le texte disant que le Launcher n'est pas pris en compte. Tu peux l'utiliser si tu ne détecte rien, je te laisse voire,
    mais ca pourrait être bien que l'utilisateur soit au courant si il faut qu'il dl maunellement, ca éviterait des demandes inutiles.
    Si tu l'utilise pas, tu peux le delete à la ligne 77. 
    """


# Creation de la fenêtre
root=ttk.Tk()
root.title("Installeur Descartes")
root.geometry("720x360")
root.resizable(width=False, height=False)
root.grid()
root.columnconfigure((2,4), weight=10)
root.columnconfigure((1,5), weight=20)
root.columnconfigure((0,6), weight=100)
root.rowconfigure((0,1,2,3),weight=10)

# Mise en place de l'arrière plan
bg=PhotoImage(file="./files/assets/background.png")
labelBackground=ttk.Label(root,image=bg, borderwidth=0)
labelBackground.place(x=0, y=0)

# Création des widgets
labelQuestion=ttk.Label(root, text="Votre ordinateur est-il puissant ?", font=("Verdana", 16, "bold"), background="#513B56", fg="#D6D5C9")
buttonYes=ttk.Button(root, text="Oui", font=("Verdana", 16, "bold"), command=highPerfPc, width=5, background="#513B56", fg="#D6D5C9")
buttonNo=ttk.Button(root, text="Non", font=("Verdana", 16, "bold"), command=lowPerfPc, width=5, background="#513B56", fg="#D6D5C9")

labelEnd=ttk.Label(root, text='Installation terminée ! Vous pouvez dès à présent vous connecter au serveur. \n Pensez bien à lancer le jeu dans la version "fabric-loader-0.15.7-1.20.1"', font=("Verdana", 12), width=650, background="#513B56", fg="#D6D5C9")
labelNotSupported=ttk.Label(root, text="Votre launcher n'est pas supporté par notre installateur.\nVous pouvez essayer de télécharger les mods manuellement.\nPour obtenir de l'aide, vous pouvez nous contacter via la section aide de notre Discord :\nhttps://discord.gg/zeZA28V4vA", font=("Verdana", 12), width=650, background="#513B56", fg="#D6D5C9")

def choix_launcher():
    labelLauncher=ttk.Label(root, text="Sélectionnez votre launcher :", font=("Verdana", 16, "bold"), background="#513B56", fg="#D6D5C9")
    buttonMc=ttk.Button(root, text="Minecraft Launcher/TLauncher", font=("Verdana", 16, "bold"), background="#513B56", fg="#D6D5C9", command=minecraft)
    buttonLegacy=ttk.Button(root, text="Legacy Launcher", font=("Verdana", 16, "bold"), background="#513B56", fg="#D6D5C9", command=legacy)
    labelLauncher.grid(row=1, column=4)
    buttonMc.grid(row=4, column=4)
    buttonLegacy.grid(row=5, column=4)

# Placement des widgets
labelQuestion.grid(row=0, column=1, columnspan=5)
buttonNo.grid(row=1, column=4)
buttonYes.grid(row=1,column=2)


# Chargement de la page
root.mainloop()
