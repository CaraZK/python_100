class GrandFather():
    money = 10000000

class Father(GrandFather):
    money = 1000
    face = "帅气的一张脸"

class Me(Father):
    pass
# 实例化
myself = Me()
print(myself.money)
print(myself.face)


# 多继承（社会角度）
class Python():
    def luoji(self):
        print("语法阶段培养逻辑思路")
class Spider():
    def paqu(self):
        print("爬虫阶段学会了抓自己感兴趣的小姐姐图片")
class Think():
    def fenxi(self):
        print("数据分析阶段我学会了数据分析科学的方法")
class MySelf(Think,Spider,Python):
    pass
me = MySelf()
me.luoji()
me.paqu()
me.fenxi()


# 多继承带来的BUG-菱形继承
class Human():
    def say(self):
        print("人类向天怒吼：人定胜天！")
class Man(Human):
    def say(self):
        super().say()
        print("男人向天怒吼：女孩的心思我不懂~")
class WoMan(Human):
    def say(self):
        super().say()
        print("女人向天怒吼：男人你们能不能别猜我心思了")
class Child(Man,WoMan):
    def say(self):
        super().say()
        print("小孩向天怒吼：哇哇哇~")
# 实例化
child = Child()
# child.say()
# mro列表
print(Child.mro())
print(child.say())

# super()  实际是调用 mro列表的上一级关系