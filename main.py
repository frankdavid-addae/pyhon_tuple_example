fileName = input("Enter file:")
if len(fileName) < 1:
    fileName = "/Users/ffictsolutions/PycharmProjects/hello/mbox-short.txt"
handle = open(fileName)
counts = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        # print(words)
        time = words[5]
        hour = time.split(':')[0]
        # print(hour)
        counts[hour] = counts.get(hour, 0) + 1
        # print(counts)
hourList = list()

# for key, value in counts.items():
#     tempList = (key, value)
#     hourList.append(tempList)
#     hourList.sort()

# Using the List Comprehension method
# hourList = sorted((k, v) for k, v in counts.items())
for key, value in sorted((k, v) for k, v in counts.items()):
    print(key, value)
