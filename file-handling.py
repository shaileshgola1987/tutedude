f = open('test.txt',"x")
with open('test.txt',"a") as f:
    f.write("Hello how are you\m")
    f.close()
f = open("test.txt","r")
print(f.read())