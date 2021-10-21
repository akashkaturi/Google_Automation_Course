def print_picnic(items_list,left,right):
    print('Picnic Items'.center(left+right, '*'))
    for item,quan in picnic_items.items():
        print(item.ljust(left,'.') + str(quan).rjust(right))
picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000,'coke':50,'sprite':50,'boost':100,'water':50}

print_picnic(picnic_items,20,5)
print_picnic(picnic_items,25,5)