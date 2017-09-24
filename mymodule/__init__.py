# 关于列表的一些简单实用
shoplist = ['apple', 'orange', 'banana']
print('i have', len(shoplist), 'items to purchase')
print('these items are:', end=' ')
for item in shoplist:
    print(item, end=' ')
print('\nI also need buy rice ')
shoplist.append('rice')
print('my shoplist is now', shoplist)
print('I will sort my list now')
shoplist.sort(reverse=True)
print('the sorted list is:', shoplist)
print('the first item i will buy is:', shoplist[0])
print('i bought the', shoplist[0])
del shoplist[0]
shoplist.sort()
print('now my shoplist is:', shoplist)


