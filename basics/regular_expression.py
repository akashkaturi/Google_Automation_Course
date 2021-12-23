import re 
pattern=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mobile_number="456-789-1234"
g=pattern.search(mobile_number)
print(g.group())
