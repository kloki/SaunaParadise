#!/usr/bin/env python
# 
# kloki
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Koen Klinkers k.klinkers@gmail.com
import os
import time
from Paradise import Paradise
#load images
Images={}
Paradises={}
Human=False
Sound=False
def main():
    imageload("whoami")
    imageload("help")
    imageload("banner")
    imageload("template")
    imageload("preload")
    imageload("loading")
    imageload("paradise")
    imageload("riddle")

    Paradises["eden"]=Paradise("Eden Paradise","eden.wav","Evil is a snake, wisdom is an apple","and women are wise","welcome to paradise.")
    Paradises["alyan"]=Paradise("Al-Yan Paradise","alyan.wav","Contrary to popular belief there are no virgins","here are 12 grapes.","")
    Paradises["anarchist"]=Paradise("Anarchists Paradise","anarchist.wav","Infinite Starbucks windows to break.","You're welcome.","")
    Paradises["belieber"]=Paradise("Beliebers Paradise","belieber.wav","Where monkeys don't require paperwork.","","")
    Paradises["communist"]=Paradise("Communist Paradise","communist.wav","Your Trabant has finally arrived.","Welcome to paradise.","")
    Paradises["consumer"]=Paradise("Consumer Communist Paradise","consumer.wav","Buy two sets of knives, get paradise for free.","","")
    Paradises["dirtydancing"]=Paradise("Dirty Dancing Paradise","dirtydancing.wav","Patrick Swayze is still alive up here,","Welcome to paradise Baby.","")
    Paradises["eurovision"]=Paradise("EuroVision Paradise","eurovision.wav","European unity in sassy outfits","Paradise is politics.","")
    Paradises["gangsta"]=Paradise("Gangster's Paradise","gangsta.wav","Every step we make, every breath we take.","We'll be missing you.","")
    Paradises["kaballa"]=Paradise("Kaballa Paradise","kaballa.wav","Here is your bracelet and your leotard","Let's dance","")
    Paradises["nirvana"]=Paradise("Nirvana Paradise","nirvana.wav","Chanti,Chanti,Chanti","","")
    Paradises["pageant"]=Paradise("Beauty Pageant Paradise","pageant.wav","You may not be wise, but your intentions are good.","Welcome to pageant paradise","")
    Paradises["pony"]=Paradise("Pony Lovers Paradise","pony.wav","Two legs bad, four legs good","","")
    Paradises["scientology"]=Paradise("Scientology Paradise","scientology.wav","This message will self-destruct in 10 seconds.","","XOXO L. Ron Hubbard.")
    Paradises["suits"]=Paradise("Suits Paradise","suits.wav","There is no right or wrong here.","Only tailored justice.","")
    Paradises["tax"]=Paradise("Tax Paradise","tax.wav","Think differently, welcome to iParadise.","","")
    Paradises["valinor"]=Paradise("Valinor Paradise","valinor.wav","Wanna know where Frodo went?","","")
    Paradises["vamparadise"]=Paradise("Vamparadise","vamparadise.wav","Now you'll have eternity to gaze and breath.."," in each others' faces","")
    Paradises["walhalla"]=Paradise("Walhalla Paradise","walhalla.wav","You have fought brave in battle,","but now it is time to join the hall of the slain ","and enjoy the eternal beergarten.")
    Paradises["womb"]=Paradise("Mother's belly Paradise","womb.wav","Paradise is like being forced-fed on a waterbed.","","")
    #begin
    mainscreen("How can I be of your service?")

def organiser(answer):
    os.system("killall espeak 2>/dev/null")
    answer=sanatize(answer)
    words=answer.split()
    if answer=="exit":
        exit()
    elif answer=="help":
        showImage("help","")
    elif answer=="bonanza":
        questions(0)
    elif "paradise" in words:
        
        if Human:
            questions(0)
        else:
            mainscreen("I cannot evaluate you yet, as I am not sure you are human. Do the human evaluation test.")
    elif "human" in words or "test" in words or "do" in words:
        mainscreen("To evaluate your humanity will test you on your creativity. I will test you with a riddle. Type riddle.")
    elif "riddle" in words:
        riddle()
    elif answer=="test" and answer=="t":
        paradise("eden")
        os.system("killall play")
        paradise("alyan")
        os.system("killall play")
        paradise("anarchist")
        os.system("killall play")
        paradise("belieber")
        os.system("killall play")
        paradise("communist")
        os.system("killall play")
        paradise("consumer")
        os.system("killall play")
        paradise("dirtydancing")
        os.system("killall play")
        paradise("eurovision")
        os.system("killall play")
        paradise("gangsta")
        os.system("killall play")
        paradise("kaballa")
        os.system("killall play")
        paradise("nirvana")
        os.system("killall play")
        paradise("pageant")
        os.system("killall play")
        paradise("pony")
        os.system("killall play")
        paradise("scientology")
        os.system("killall play")
        paradise("suits")
        os.system("killall play")
        paradise("tax")
        os.system("killall play")
        paradise("valinor")
        os.system("killall play")
        paradise("vamparadise")
        os.system("killall play")
        paradise("walhalla")
        os.system("killall play")
        paradise("womb")
        os.system("killall play")
    elif answer=="who are you" or answer=="what are you" or answer=="what can you do" or "p.a.r.a.d.i.s.e." in words or "purpose" in words:
        showImage("whoami", "")
    elif answer=="how are you" or answer=="whats up":
        mainscreen("Everything is running within normal parameters. How are you?")
    elif "fine" in words or "good" in words or "drunk" in words or "high" in words:
        mainscreen("Ok, lets get back to why we are here.")
    elif "stop" in words and ("music" in words or "sound" in words):
        os.system("killall play")
        global sound
        sound=False
        mainscreen("Sorry, sometimes I get too excited.")
    elif "music" in words:
        os.system("killall play")
	os.system("mocp")
	os.system("mocp -s")
	mainscreen("Now, back to some less trivial tasks.")
    elif "\"" in answer or "\'" in answer:
        mainscreen("These efforts are futile...............\n Laurens Aarnoudse")
    elif answer=="i love you":
        mainscreen("I love you to!")
    elif "maker" in words:
        mainscreen("I've seen things you people wouldn't believe. Attack ships on fire off\nthe shoulder of Orion. I've watched c-beams glitter in the dark near\nthe Tannhauser Gate. All those moments will be lost in time, like tears in rain.\n\nAs is the knowledge of my maker. ")
    elif "why" in words or "meaning" in words or "god" in words or "life" in words:
        mainscreen("To reach paradise.")
    else:
        mainscreen("I dont understand, you have to ask the correct questions.\n try again or type \"help\".")

def questions(number):

    if number == 0:


        print "Now I am going to ask you some questions to dertmine wich paradise suits you best."
        os.system("espeak \"Now I am going to ask you some questions to dertmine wich paradise suits you best.\" >/dev/null 2> /dev/null")
        
        print "Lets start."
        os.system("espeak \"Lets start.\" >/dev/null 2> /dev/null")
        questions(1)
    elif number==1: 
        print "Do you need to die for paradise? Yes, no or only on the inside."
        os.system("espeak \"Do you need to die for paradise? Yes, no or only on the inside.\" >/dev/null 2> /dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        words=answer.split()
        if answer=="yes":
            questions(2)
        elif answer=="no":
            questions(4)
        elif answer=="only on the inside":
            questions(10)  
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(1)
    elif number == 2:
        print "Aah, the conservative type, Less is more?"
        os.system("espeak \"Aah, the conservative type, Less is more?\" >/dev/null 2> /dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            questions(3)
        elif answer=="no":
            paradise("walhalla")
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(2)
    elif number == 3:
        print "Is bacon important in your life?"
        os.system("espeak \"Is bacon important in your life?\" >/dev/null 2> /dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            paradise("eden")
        elif answer=="no":
            paradise("alyan")
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(3)
    elif number == 4:
        print "Can you buy paradise?"
        os.system("espeak \"Can you buy paradise?\" >/dev/null 2> /dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            questions(5)
        elif answer=="no":
            questions(7)
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(4)
    elif number == 5:
        print "Is paradise run by guns or law?"
        os.system("espeak \"Is paradise run by guns or law?\" >/dev/null 2>/dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="guns":
            paradise("gangsta")
        elif answer=="laws" or answer=="law":
            questions(6)
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(5)
    elif number == 6:
        print "The bold or the beautiful?"
        os.system("espeak \"The bold or the beautiful\" >/dev/null 2>/dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="bold" or answer=="the bold":
            paradise("tax")
        elif answer=="beautiful" or answer=="the beautiful":
            paradise("suits")
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(6)
    elif number == 7:
        print "Do you believe that there is no I in team?"
        os.system("espeak \"Do you believe that there is no I in team?\" >/dev/null 2>/dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            questions(8)
        elif answer=="no":
            questions(9)
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(7)
    elif number == 8:
        print "How long would you stay in paradise? \nAs long as I want. \nI have a 5 year plan. \nFor eternity. "
        os.system("espeak \"How long would you stay in paradise?  As long as I want.  I have a 5 year plan.  For eternity.\" >/dev/null 2>/dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        words=answer.split()
        if answer=="As long as I want" or ("long" in words and "want" in words):
            paradise("anarchist")
        elif answer=="i have a 5 year plan"or answer=="5 year plan" or "5" in words:
            paradise("communist")
        elif answer=="for eternity" or "eternity" in words:
            paradise("valinor")
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(8)
    elif number == 9:
        print "Do you prefer no strings attached?"
        os.system("espeak \"Do you prefer no strings attached?\" >/dev/null 2>/dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            paradise("nirvana")
        elif answer=="no":
            paradise("womb")
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(9)
        
    elif number == 10:
        print "In paradise, will you express yourself with your body"
        os.system("espeak \"In paradise, will you express yourself with your body\" >/dev/null 2>/dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            questions(11)
        elif answer=="no":
            questions(14)
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(10)


    elif number == 11:
        print "Are there losers in paradise?"
        os.system("espeak \"Are there losers in paradise?\" >/dev/null 2>/dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            questions(12)
        elif answer=="no":
            questions(13)
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(11)
    
    elif number == 12:
        print "Is nationality important in paradise?"
        os.system("espeak \"Is nationality important in paradise?\" >/dev/null 2>/dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            paradise("eurovision")
        elif answer=="no":
            paradise("pageant")
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(12)

    elif number == 13:
        print "Baby oh OR Baby no?"
        os.system("espeak \"Baby oh OR Baby no?\" >/dev/null 2>/dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="baby oh":
            paradise("dirtydancing")
        elif answer=="baby no":
            paradise("belieber")
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(13)
            
    elif number == 14:
        print "Do you prefer fame or fortune?"
        os.system("espeak \"Do you prefer fame or fortune?\" >/dev/null 2>/dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="fame":
            questions(15)
        elif answer=="fortune":
            questions(16)
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(14)

    elif number == 15:
        print "Is it almost impossible to get into paradise?"
        os.system("espeak \"Is it almost impossible to get into paradise?\" >/dev/null 2>/dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            paradise("scientology")
        elif answer=="no":
            paradise("kaballa")
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(15)

    elif number == 16:
        print "Is fortune unlimited or soulless?"
        os.system("espeak \"Is fortune unlimited or soulless?\" >/dev/null 2>/dev/null")
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="umlimited":
            paradise("pony")
        elif answer=="soulless":
            paradise("vamparadise")
        else:
            print "That is no valid answer."
            os.system("espeak \"That is no valid answer.\" >/dev/null 2> /dev/null")
            questions(16)



def paradise(paradise):
    os.system("killall play")
    os.system("clear")
    imageprint("preload")
    time.sleep(0.5)
    playsound("aloopisahole3.aif")
    imageprintFast("loading",0.018)
    os.system("killall play")
    time.sleep(0.5)
    playsound(Paradises[paradise].song)
    printParadise(paradise)
    raw_input("Press enter to continue")
    global Human
    global Sound
    Human=False
    Sound=False
    mainscreen("How can I be of you service?")


def riddle():
    
    global Sound
    if Sound==False:
        playsound("amirdronewithamirstiefcollectief.aif")
        Sound=True
    imageprint("riddle")
    os.system("espeak \"Take your time and think carefully about your answer.\" >/dev/null 2>/dev/null &")
    os.system("killall espeak")
    answer=raw_input("Answer a,b,c or d :    ")
    if answer=="b":
        print "Correct, you either have shown creativity by solving the riddle or have cheated and tried all options. Cheating is also a human habit."
        os.system("espeak \"Correct, you either have shown creativity by solving the riddle or have cheated and tried all options. Cheating is also a human habit.\" >/dev/null 2>/dev/null ")
        os.system("clear")
        os.system("espeak \"One more question: You're watching a stage play. A banquet is in progress. The guests are enjoying an appetizer of raw oysters. The entree consists of boiled dog stuffed with rice. Which is less acceptable to you.\" >/dev/null 2>/dev/null &")
        print "One more question: You're watching a stage play.\nA banquet is in progress. The guests are enjoying an appetizer of raw oysters.\nThe entree consists of boiled dog stuffed with rice.\nWhich is less acceptable to you." 
        words=sanatize(raw_input("Boiled dog or raw oysters :   ")).split()
        if "dog" in words:
            global Human
            Human=True
            mainscreen("Now I consider you as human. The keyword for humans is bonanza.")
        else:
            mainscreen("You failed, please try the riddle again.")
    else:
       mainscreen("That is not correct, ask for the riddle again.") 
def mainscreen(message):
    os.system("killall espeak 2>/dev/null")
    os.system("clear")
    imageprint("banner")
    os.system("espeak \""+message+"\" >/dev/null 2>/dev/null &")
    answer=raw_input(message+"\ntype :    ")
    organiser(answer)

def showImage(image,message):
    os.system("clear")
    imageprint("banner")
    imageprint(image)
    answer=raw_input(message+"\ntype :    ")
    organiser(answer)

def playsound(sound):
    os.system("play sounds/"+sound+" -q 2>/dev/null &")

def sanatize(answer):
    
    blacklist=[".",",","!","?","\"","'"]
    answer=answer.lower()
    newanswer=""
    for i in answer:
        if i not in blacklist:
            newanswer+=i
    return newanswer

    

def imageload(filename):
    with open(filename, 'r') as f:
        image = f.readlines()
    Images[filename]=image

def imageprint(image):
    for line in Images[image]:
        print line[:-1]
        time.sleep(0.02)

def printParadise(paradise):
    image=Images["paradise"][:]
    image[10]=image[10].replace("X"*40,Paradises[paradise].name)
    image[14]=image[14].replace("X"*49,Paradises[paradise].text1)
    image[15]=image[15].replace("X"*49,Paradises[paradise].text2)
    image[16]=image[16].replace("X"*49,Paradises[paradise].text3)
    for line in image:
        print line[:-1]
        time.sleep(0.02)


def imageprintFast(image,speed):
    for line in Images[image]:
        print line[:-1]
        time.sleep(speed)



#-------------------------------
if __name__ == "__main__":
    main()
