import random
cats = []
num = 0
while True:
    num += 1
    print(f'Enter Cat Name {num}: ')
    s = input()
    if s != '':
        print(f'The name you entered is: {s}')
        cats.append(s)
    else:
        break

for index, cat in enumerate(cats):
    index += 1
    print(f"CatName {str(index).ljust(20,'.')} {cat.rjust(20)}")
random.shuffle(cats)
print(cats)
