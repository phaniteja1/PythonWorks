__author__ = 'phaniteja'

message = "This is the wonderful message"

f = open("test.txt", "w")

f.write(message)

f.close()

f = open("test.txt", "r+")

contents = f.read()

print(contents)


