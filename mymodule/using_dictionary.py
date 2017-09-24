def mydict(**phonelist):
    print(phonelist.items())
    # dict_items([('wanghang', 130), ('jack', 122)]),
    # 由输出结果猜想，字典就是一个所含元素为tuple的list
    for item in phonelist.items():
        print(item)


mydict(wanghang=130, jack=122)


# d = {key : value1 , key2 : value2}，字典的基本结构
mydictionary = {
    "wanghang": 'wanghang@love.com',
    'gaoguan': 'gaoguan@happy.com'
}

print(mydictionary)

print("gaoguan's email is", mydictionary['gaoguan'])
for name, email in mydictionary.items():
    print("{}'s email is {}".format(name, email))
# gaoguan's email is gaoguan@happy.com
# wanghang's email is wanghang@love.com
# 可以看出字典是不会给里面的元素进行排序的
