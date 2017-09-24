# 关于元祖的简单实用
# 括号并非必须，但是这样更加明了，显式优于隐式
zoo = ('monkey', 'elephant', 'tiger')
print(zoo)
print(len(zoo))
print('the zoo have these animals', end=' ')
for animal in zoo:
    print(animal, end=' ')
new_zoo = ('python', zoo)
print('\nnew zoo', new_zoo)
print(len(new_zoo))  # 这样得到的并不是所有动物个数
length = len(new_zoo) - 1 + len(zoo)
print('the really animal count', length)  # 4

print(new_zoo[1])  # ('monkey', 'elephant', 'tiger')
print(new_zoo[1][1])  # elephant
# tuple没有append方法，一旦创建元组是无法改变的，下面这种使用方法其实是重新创建一个tuple
zoo = ('monkey', 'elephant', 'camel')
print('\n', zoo)

