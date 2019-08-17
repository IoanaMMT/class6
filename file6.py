import time

print("one at the time")
sentance = "one at the time"
words = sentance.split()
print(words)


for word in words:
	print(word)
	time.sleep(.7)