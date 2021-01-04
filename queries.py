init = input().split(' ')
s = input()
l = int(init[0])
qs = int(init[1])

for i in range(qs):
    q = input().split(' ')
    start = int(q[0]) - 1
    end = int(q[1])
    substring = s[start:end]
    myset = set(substring)
    mylist = list(myset)
    counts = []
    countofcounts = []

    for j in range(len(mylist)):
        counts.append(substring.count(mylist[j]))
    print(counts)