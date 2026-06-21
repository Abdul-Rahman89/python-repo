f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

f = open("demo.txt","a")

f.write("\n after node.js")

f.close()