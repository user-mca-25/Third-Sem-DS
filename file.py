fr = open("test.txt","r")

print(fr.read())

fw = open("test.txt","a")

fw.write("Fine, wau")


fw.close()

print(fr.read())