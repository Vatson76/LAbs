import random, time

f = open('MPSS/wordlist.10000.txt')
d = iter(f)
dictionary = {}
a1 = []
a2 = []

try:
    while d:
        a = next(d)[:-1]
        b = next(d)[:-1]
        a1.append(a)
        a2.append(b)
        dictionary[a] = b

except StopIteration:
    pass
f.close()

start_time = time.time()
for i in range(50000):

    chislo = random.randint(0, len(a1)-1)

    search_word = a1[chislo]
    res = a2[a1.index(search_word)]
print("---{} seconds---".format(time.time()-start_time))

start_time = time.time()
for i in range(50000):

    chislo = random.randint(0, len(a1)-1)
    search_word = a1[chislo]
    res = dictionary[search_word]
print("---{} seconds---".format(time.time()-start_time))

