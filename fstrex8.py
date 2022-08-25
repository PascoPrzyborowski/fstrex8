

#Task1

import time

text1 = "I am finding Nemo !"
print()
print(text1)
print()
time.sleep(1)
print("searching ...")
print()
time.sleep(1)
print("I found Nemo at: " + str(text1.index("Nemo")) + "!" )
print()
text2 = "Nemo is me !"
print()
print(text2)
print()
time.sleep(1)
print("searching ...")
print()
time.sleep(1)
print("I found Nemo at: " + str(text2.index("Nemo")) + "!" )
print()
text3 = "I Nemo am !"
print()
print(text3)
print()
time.sleep(1)
print("searching ...")
print()
time.sleep(1)
print("I found Nemo at: " + str(text3.index("Nemo")) + "!" )
print()
text4 = "Hello World"
print()
print(text4)
print()
time.sleep(1)
print("searching ...")
print()
time.sleep(1)
#print("I found Nemo at:" + str(text4.index("Nemo")) + "!" )
if text4.find("Nemo") == -1:
    print("I Can't find Nemo:(")



