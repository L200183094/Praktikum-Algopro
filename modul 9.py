#ACTIVITY 1
file = open("L200183094", "w")
file.write("L200183094" +"\n")
file.write("21-05-2000" + "\n")
file.write("Farah Husna Paramadina" + "\n")
file.close()

##==========================================================
##ACTIVITY 2
newFile = open("L200183094", "r")
NIM = newFile.readline()
TTL = newFile.readline()
NAME = newFile.readline()
newFile.close()

import shelve
newFile1 = shelve.open("Farah.txt")
newFile1["file"] = [NIM, TTL, NAME]
newFile1.close()

##==============================================
##ACTIVITY 3
newFile2 = shelve.open("Farah.txt")
for i in newFile2["file"]:
    print (i)
newFile2.close()