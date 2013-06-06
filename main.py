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

#load images
Images={}

def main():
    imageload("roanne")
    imageload("koen")
    imageload("whoami")
    imageload("help")
    imageload("banner")
    imageload("template")
    imageload("loading")
    #begin
    mainscreen("How can I be of you service?")
    
def organiser(answer):
    answer=sanatize(answer)
    words=answer.split()
    if answer=="exit":
        exit()
    elif answer=="help":
        showImage("help","")
    elif answer=="paradise":
        questions(1)
    elif answer=="test":
        showImage("template","this is the last line")
    elif answer=="who are you" or answer=="what are you" or "p.a.r.a.d.i.s.e." in words:
        showImage("whoami", "")
    elif "face" in words and "her" in words:
        showImage("roanne", "this is her face")
    elif "face" in words and "his" in words:
        showImage("koen", "this is his face")
    elif "\"" in answer or "\'" in answer:
        mainscreen("These efforts are futile...............\n Laurens Aarnoudse")
    elif answer=="i love you":
        mainscreen("I love you to!")
    else:
        mainscreen("I dont understand, you have to ask the correct questions.\n try again or type \"help\".")

def questions(number):

    if number == 1:
        print "Do you need to die for paradise? Yes, no or only on the inside."
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            questions(2)
        elif answer=="no":
            questions(4)
        elif answer=="only on the inside":
            questions(10)  
        else:
            print "That is no valid answer."
            questions(1)
    elif number == 2:
        print "Aah, the conservative type, Less is more?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            questions(3)
        elif answer=="no":
            paradise("walhalla")
        else:
            print "That is no valid answer."
            questions(2)
    elif number == 3:
        print "Is bacon important in your life?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            paradise("eden")
        elif answer=="no":
            paradise("alyan")
        else:
            print "That is no valid answer."
            questions(3)
    elif number == 4:
        print "Can you buy paradise?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            questions(5)
        elif answer=="no":
            questions(7)
        else:
            print "That is no valid answer."
            questions(4)
    elif number == 5:
        print "Is paradise run by guns or law?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="guns":
            paradis("gangsta")
        elif answer=="laws":
            questions(6)
        else:
            print "That is no valid answer."
            questions(5)
    elif number == 6:
        print "The bold or the beautiful"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="bold":
            paradise("tax")
        elif answer=="beautiful":
            paradise("suits")
        else:
            print "That is no valid answer."
            questions(6)
    elif number == 7:
        print "There is no I in team?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            questions(8)
        elif answer=="no":
            questions(9)
        else:
            print "That is no valid answer."
            questions(7)
    elif number == 8:
        print "How long would you stay in paradis? \n As long as I want. \n I have a 5 year plan. \n For eternity. "
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="As long as I want":
            paradise("anarchist")
        elif answer=="i have a 5 year plan":
            paradise("communist")
        elif answer=="for eternity":
            paradise("valinor")
        else:
            print "That is no valid answer."
            questions(8)
    elif number == 9:
        print "No strings attached?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            paradise("nirvana")
        elif answer=="no":
            paradise("womb")
        else:
            print "That is no valid answer."
            questions(9)
        
    elif number == 10:
        print "In paradise, will you express yourself with your body"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            questions(11)
        elif answer=="no":
            questions(14)
        else:
            print "That is no valid answer."
            questions(10)


    elif number == 11:
        print "Are there losers in paradise?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            questions(12)
        elif answer=="no":
            questions(13)
        else:
            print "That is no valid answer."
            questions(11)
    
    elif number == 12:
        print "Is nationality important in paradise?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            paradise("eurovision")
        elif answer=="no":
            paradise("pagent")
        else:
            print "That is no valid answer."
            questions(12)

    elif number == 13:
        print "Baby oh OR Baby no?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="baby oh":
            paradise("dirtydancing")
        elif answer=="baby no":
            paradise("bebieber")
        else:
            print "That is no valid answer."
            questions(13)
            
    elif number == 14:
        print "Fame or fortune?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="fame":
            questions(15)
        elif answer=="fortune":
            questions(16)
        else:
            print "That is no valid answer."
            questions(14)

    elif number == 15:
        print "Is it almost impossible to get into paradise?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            paradise("kaballa")
        elif answer=="no":
            paradise("kaballa")
        else:
            print "That is no valid answer."
            questions(15)

    elif number == 16:
        print "Is fortune unlimited or soulless?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="umlimited":
            paradise("pony")
        elif answer=="soulless":
            paradise("vamparadise")
        else:
            print "That is no valid answer."
            questions(16)



def paradise(paradise):
    imageprint("loading")
    mainscreen("You are in "+paradise)


def mainscreen(message):
    os.system("clear")
    imageprint("banner")
    answer=raw_input(message+"\ntype :    ")
    organiser(answer)

def showImage(image,message):
    os.system("clear")
    imageprint("banner")
    imageprint(image)
    answer=raw_input(message+"\ntype :    ")
    organiser(answer)

def sanatize(answer):
    
    blacklist=[".",",","!","?"]
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
#-------------------------------
if __name__ == "__main__":
    main()
