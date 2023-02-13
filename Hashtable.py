

#d = dict()
#d = {}
d = dict(alemanha=4, italia=4, argentina=2, frança=1, uruguai=2, inglaterra=1)
d = {'alemanha':4, 'italia':4, 'argentina':2, 'frança':1, 'uruguai':2, 'inglaterra':1}

print(len(d))

print('brasil' in d)

d['brasil'] = 5
d['espanha'] = 1
d['frança'] = 2

print(len(d))

print('brasil' in d)

print(d["alemanha"])

print(d["argentina"])
d["argentina"] = 3
print(d["argentina"])

del d['argentina']

print(len(d))

#Pelos chaves
for valor in d.keys():
    print(valor)

#Pelos valores
for valor in d.values():
    print(valor)