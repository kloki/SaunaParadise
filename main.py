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
    #begin
    mainscreen("How can I be of you service?")
    
def organiser(answer):
    answer=sanatize(answer)
    print answer
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
        mainscreen("These efforts are futile............... Laurens Aarnoudse")
    elif answer=="i love you":
        mainscreen("I love you to!")
    else:
        mainscreen("I dont understand, you have to ask the correct questions. try again or type \"help\".")

def questions(number):

    if number == 1:
        print "Are you pretty?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            questions(2)
        elif answer=="no":
            questions(3)
        else:
            print "That is no valid answer."
            questions(1)
    elif number == 2:
        print "Are you smart?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            print "Congratulations, you are pretty and smart."
            raw_input()
            mainscreen("How can I be of you service?")
        elif answer=="no":
            print "Ohh, you are pretty but not smart."
            raw_input()
            mainscreen("How can I be of you service?")
        else:
            print "That is no valid answer."
            questions(2)
    elif number == 3:
        print "Are happy?"
        answer=sanatize(raw_input("\ntype :    "))
        if answer=="yes":
            print "That is what matter!"
            raw_input()
            mainscreen("How can I be of you service?")
        elif answer=="no":
            print "Now I am sad :("
            raw_input()
            mainscreen("How can I be of you service?")
        else:
            print "That is no valid answer."
            questions(3)
    


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
