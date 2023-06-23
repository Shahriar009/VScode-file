'''

You have a list of your favourite marvel super heros
heros=['spider man','thor','hulk','iron man','captain america']
Using this list
'''
heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
heros[1:3]=['doctor strange']
print(heros)
heros.sort()
print(heros)