#1操作列表
My_bookshelf=[] #这是一个空列表，像一个空的书架一样
# 书架的特点：
# 有序的：书放在第1层、第2层、第3层…位置是固定的
# 可变的：你可以随时放新书上去，也可以把书拿下来
# 索引从0开始：第1本书的位置是0，第2本是1，以此类推

# 为什么列表能当栈用？
# 栈的原理是“后进先出”，就像一摞盘子：
# 最后放上去的盘子，最先被拿走
# 你不能从中间抽盘子，只能操作最上面那个
#  而Python列表的 append() 和 pop() 操作，完美符合这个特性：
# 就比如说append()这个列表的函数，总在末尾添加；而pop这个列表函数，总在末尾删除

plates = [] #这是一个盘子架
while True :
    User_Plates=input("请输入放入盘子1，盘子2.....放完盘子按\'Q\'退出,按1查看当前盘子数量,如果要拿出盘子请输入\'拿出\'\n")

    if User_Plates=="Q" : #退出程序
        print("已退出")
        break
    elif User_Plates == '1':
        if len(plates)==0 :
            print("现在架子上面并没有盘子")
        else:
            amount=len(plates)
            print("当前盘子的数数量是",amount,'个')
    elif User_Plates=="拿出" :
        plates.pop()
        print("当前已拿走一个盘子")
    else:
        plates.append(User_Plates)
        print("当前已放入",User_Plates)

    print("*"*30)



# plates = []  # 这是一个盘子架
#
# while True:  # 使用一个无限循环，让程序持续运行，直到用户选择退出
#     user_input = input("请输入要放入的盘子名，或输入指令：\n"
#                        "  '1' 查看当前盘子\n"
#                        "  '拿出' 拿出一个盘子\n"
#                        "  'Q' 退出程序\n")
#
#     if user_input == "Q":
#         print("程序结束。")
#         break  # 退出循环
#
#     elif user_input == "1":
#         print(f'当前盘子有: {plates}')
#         print(f'总共有 {len(plates)} 个盘子')
#
#     elif user_input == "拿出":
#         if len(plates) == 0:
#             print("盘子架已经是空的了，没有盘子可以拿！")
#         else:
#             removed_plate = plates.pop()
#             print(f"拿出了盘子: {removed_plate}")
#
#     else:  # 如果不是以上任何指令，就当成是放入新盘子
#         plates.append(user_input)
#         print(f"已放入盘子: {user_input}")
#
#     print("-" * 20) # 打印一个分隔线，让每次操作更清晰




