entry = input("> ")
numList = []
while entry != "done":
    entry = int(entry)
    numList.append(entry)
    entry = input("> ")
sum = 0
for num in numList:
    sum += num
answer = sum/len(numList)
print("Average:", answer)
