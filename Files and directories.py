'''
 from pathlib import  Path

path=Path("Ecommerce")
print(path.mkdir())
'''
from pathlib import Path
path=Path()
print(path.glob('*.py'))
'''
for file in path.glob('*.py'):
   print(file)
'''