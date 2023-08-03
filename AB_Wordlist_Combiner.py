# A-B Wordlist Combiner
# Brute Force Combining all with all
# Author: Hermann Knopp 2023
# Version 0.1a / 1.7.2023
# use: Python 3.10.10 x64/amd64
# Contact:hermann.knopp@gmx.at
#

# Title Message
print("Hermanns A-B Wordlist Combiner")
print("")
print("Importing Libs...")

# Libraries
import sys
import os
import random
import codecs

print("")
print("Importing Wordlists..")
print("")


# Select Straigh/Shuffled Wordlists
sta=int(input("do you want to 1=straight or 2=shuffled Wordlists (Enter 1/2) "))
if sta =="" or sta > 2 or sta < 1:
   sta=1
if sta==1:
   straight_flag=1
   print("I will use straight Worldists")
if sta==2:
   straight_flag=2 
   print("I will use shuffled Wordlists")


# Enter Wordlist A
print("")
print("Enter Path Wordlist A (Name_A.txt) or use sample:(./colors.txt) with Enter")
a=input(">")
if a=="":
   fileA="colors.txt"
   wordspath=os.path.dirname(os.path.realpath(__file__))
   wordspath=wordspath+"\\"+fileA
  
else:
    fileA=str(a)
    wordspath=fileA


# Importing Wordlist A
print("")
print("Wordsfile A: "+ wordspath)
filename=wordspath
filename=filename.replace('"','')

with open(filename, encoding="utf8") as f:
  words = f.readlines()
  words = [x.strip() for x in words]
  anz = len(words) 
  if straight_flag==2:
     random.shuffle(words)


# Enter Wordlist B
print("")
print("Enter Path Wordlist B (Name_B.txt) or use sample:(./colors.txt) with Enter")
b=input(">")
if b=="":
   fileB="colors.txt"
   wordspath2=os.path.dirname(os.path.realpath(__file__))
   wordspath2=wordspath2+"\\"+fileB
else:
   fileB=str(b)
   wordspath2=fileB


# Importing Wordlist B
print("")
print("Wordsfile B: "+ wordspath2)
filename2=wordspath2
filename2=filename2.replace('"','')


# Open File for writing
with open(filename2, encoding="utf8") as g:
  words2 = g.readlines()
  words2 = [y.strip() for y in words2]
  anz2 = len(words2) 
  if straight_flag==2:
     random.shuffle(words2)
  

# Select Separator
fod=int(input("do you want to use 1='-'or  2='Space 'or 3='Custom' Separator (Enter 1/2/3) "))
if fod =="":
   fod="N"
if fod==1:
   sep_flag=1
   print("using '-' as Word Separator")
   sep_string="-"
 
if fod==2:
   sep_flag=0
   print("using 'Space ' as Word Separator")
   sep_string=" "

if fod==3:
   sep_flag=2
   print("using 'Custom' as Word Separator")
   print("")
   c=input("Enter Separator String>")
   sep_string=""
   sep_string=sep_string +" " + str(c) +" "
   print("")
   print("Your Word Separator is: ",str(sep_string))


print("")
print("")
print("Open File for writing...")


# Get Working Directory
filepath=os.path.dirname(os.path.realpath(__file__))
textfile = filepath + "\\combinations.txt"
file = codecs.open(textfile, "w", "utf-8")


# Get all Combinations Counter Variable
print("")
am=anz*anz2

# Status Message
print("You will combine the amount of ",str(am)," words")
if am>5000 and am<15000:
   print("This is a little Combining Task,...this will take some Seconds")
if am>15000:
   print("This is a huge Combining Task,...this will take very long Time...please wait")
   
print("Start doing Combinations Work...")
a=input("Press Enter Key, to start")

# Set Counter
counter=0

# Main Combining Loop
for i in range(1,anz):
         
        
    print("Combining the Word: ",str(words[i]))
    print("iteration-i: ",i, "Word: ",str(words[i]))

    # Do all with all Text Combinations
    for j in range(1,anz2):
        #print("iteration-j:",j," Combining: ", str(words[i]),"-",str(words2[j]))

        counter=counter+1
        print("Combination ",str(counter), "/",str(anz*anz2), "iter-i",str(i),"/",str(anz)," iter-j:",str(j),"/",str(anz2)," ", str(words[i]),"-",str(words2[j]))

        # Word A(n) with Word B(n) combining
          
        text= words[i] + sep_string + words2[j] + "\n"
      
        # Save Words to file
        file.write(text)

# Close File
file.close()

# Satus Message Done
print("")
print("Mangeling Done..File 'combinations.txt' saved to .py working folder")
a=input("Wait Key")
exit()


