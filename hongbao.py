# coding=utf-8
import random
import sys


# def calRandomValue(total, num):
#     total = float(total)
#     num = int(num)
#     min = 0.01  # 基数
#     if (num < 1):
#         return
#     if num == 1:
#         print "第%d个人拿到红包数为：%.2f" % (num, total)
#         return
#
#     i = 1
#     while (i < num):
#         max = total - min * (num - i)
#         k = int((num - i) / 2)
#         if num - i <= 2:
#             k = num - i
#         max = max / k
#         monney = random.uniform(min, max)
#         # monney = float(monney) / 100
#         total = total - monney
#         print "第%d个人拿到红包数为：%.2f, 余额为: %.2f" % (i, monney, total)
#         i += 1
#
#     print "第%d个人拿到红包数为：%.2f, 余额为: %.2f" % (i, total, 0.0)
#
#
# if __name__ == "__main__":
#     total = raw_input('输入红包总金额:')
#     num = raw_input('输入发红包数量:')
#     calRandomValue(total, num)

# coding=utf-8

people = int(raw_input("请输入红包个数："))
total = int(raw_input("请输入红包总金额："))
money_list = []

for i in range(1,people+1):
    if i < people:
        raw_input("第%d个人该抢红包啦！"%i)
        max = total - min * (num - i)
        k = int((num - i) / 2)
        if num - i <= 2:
            k = num - i
        max = max / k
        a = random.random()
        money = a * total
        b = round(money,2)
        # money_list.append()
        print "第%d个人抢到的红包是%.2f" % (i, b)
        rest = total - b
        print "红包还剩余%.2f" % rest
        total = rest
    elif i == people:
        b = rest
        print "第%d个人抢到的红包是%.2f" % (i, b)
        print "红包已抢完！"
        break