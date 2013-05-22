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
    imageload("mainscreen")
    imageload("help")


    #begin
    mainscreen("How can I be of you service?")
    
def organiser(answer):
    words=answer.split()
    if answer=="exit":
        exit()
    elif answer=="help":
        helpscreen()
    elif "face" in words and "her" in words:
        showImage("roanne", "this is her face")
    elif "face" in words and "his" in words:
        showImage("koen", "this is his face")
    elif "\"" in answer or "\'" in answer:
        mainscreen("These efforts are futile.")
    else:
        mainscreen("I dont understand, try again.")


def mainscreen(message):
    os.system("clear")
    imageprint("mainscreen") 
    answer=raw_input(message+"\ntype :    ")
    organiser(answer)

def helpscreen():
    os.system("clear")
    imageprint("help")
    answer=raw_input("\ntype :    ")
    organiser(answer)


def showImage(image,message):
    os.system("clear")
    imageprint(image)
    answer=raw_input(message+"\ntype :    ")
    organiser(answer)

    

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
