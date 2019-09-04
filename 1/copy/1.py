import re
pattern=re.compile(r'(\w+) (\w+)')
matche=pattern.match('hello world')
print(matche.group())
print(matche.groups())
