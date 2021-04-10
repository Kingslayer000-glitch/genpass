#Bibliotek
import random
import time

#Creator (c)Kingslayer

#nameprog
print("""
░██████╗░███████╗███╗░░██╗██████╗░░█████╗░░██████╗░██████╗
██╔════╝░██╔════╝████╗░██║██╔══██╗██╔══██╗██╔════╝██╔════╝
██║░░██╗░█████╗░░██╔██╗██║██████╔╝███████║╚█████╗░╚█████╗░
██║░░╚██╗██╔══╝░░██║╚████║██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗
╚██████╔╝███████╗██║░╚███║██║░░░░░██║░░██║██████╔╝██████╔╝
░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░""")
print("\t\t\t\t\t\t(c)Kingslayer")
#Main words
mainname = input("Enter the first word: ")
mainname2 = input("Enter the second word: ")
mainname3 = input("Enter the third word: ")

#generation password
file = open("pass.txt", "w")
#Step 1
for i in range(3000):
    steppass = mainname+str(i)+"\n"
    steppass2 = mainname+mainname2+str(i)+"\n"
    steppass3 = mainname+mainname3+str(i)+"\n"
    file.write(steppass)
    file.write(steppass2)
    file.write(steppass3)
#Step2
for i in range(3000):
    steppass = mainname+"-"+str(i)+"\n"
    file.write(steppass)
#Step3
file.write(mainname+mainname2+mainname3+"\n"+mainname+mainname2+"\n"+mainname2+mainname+"\n"+mainname3+mainname+"\n"+mainname3+mainname2+mainname+"\n"+mainname2+mainname3+mainname+"\n"+mainname+mainname3+mainname2)
#Step4
file.write(mainname.upper()+"\n"+mainname2.upper()+"\n"+mainname3.upper()+"\n"+mainname2.upper()+mainname.upper()+"\n"+mainname3.upper()+mainname.upper()+"\n"+mainname.upper()+mainname3.upper())
file.close()
#load funny
x = 1
while x>0:
    x+=1
    print(str(x)+"%")
    time.sleep(0.1)
    if x>=100:
        break
