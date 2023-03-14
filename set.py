

s1 = {'fla','men','go'}
s = set()

s.add(1980)
s.add(1981)
s.add(1982)
s.add(1983)
s.add(1981)
s.add(2009)

print(len(s))

print(1992 in s)

s.remove(2009)
#s.remove(2019)
s.discard(2020)

print(len(s))

for valor in s:
    print(valor)
