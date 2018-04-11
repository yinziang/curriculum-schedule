#! usr/bin/python
#coding:utf-8
#实现控制台课表
#功能：1.输入课表；2.存储课表；3.打印课表；4.更新课表；5.实时课表

import datetime

DAY = 7
CLASS = 5
CLASS_TIME = ['9:00-9:45', '10:00-10:45', '14:00-14:45', '15:00-15:45', '16:00-16:45']

def menu():
    b = "***"
    print "%s课程表管理系统%s" %(b, b)
    print "%s1:查看课表\n%s2.修改课表\n%s3.重新输入课表\n%s4.实时课表\n%s5.退出\n" % (b, b, b, b, b)

def input_all():
    # 1.输入课表
    # 2.存储课表
    test_file = "test.txt"
    multilist = [[0 for col in range(DAY)] for row in range(CLASS)]   #初始化一个每项为0、五行七列的数组的最好方法
    week = ('周一','周二','周三','周四','周五','周六','周日')
    for j in range(DAY):
        for i in range(CLASS):
            multilist[i][j] = raw_input('%s第%d节:' %(week[j], i + 1))
    target = open(test_file, 'w')
    for i in range(CLASS):
        str = ' '.join(multilist[i])  # join用法:用' '中的连接数组各部分
        target.write(str)
        target.write('\n')
    target.close()
    # print "end"
    # target = open(test_file,'r')
    # print target.read()

def show_all(file_name):
    # 3.打印课表
    file = open(file_name, "r")
    print "******************************************************"
    print "*****时间      周一 周二 周三 周四 周五 周六 周日*****"
    cnt = 0
    for i in file:
#        print i.split()
        list = i.split()
        print "%12s" %CLASS_TIME[cnt],
        for j in range(len(list)):
 #           print "  " + list[j] + " ",
            print "%4s" %list[j],
        print   #换行
        cnt += 1
    print "******************************************************"

def update(file_name):
    # 4.更新课表
    d = int(raw_input("您要修改周几的课程？"))
    week = ('周一', '周二', '周三', '周四', '周五', '周六', '周日')
    c = int(raw_input("您要修改%s的第几节课？" %week[d - 1]))

    file = open(file_name, "r")
    flist = file.readlines()
    arr = flist[c - 1].split()
    # print arr
    new = raw_input("原课程（%s）修改成:" %arr[d - 1])
    # 按行读入课表到一个列表，修改指定行即给列表中元素赋值
    # print d, c
    arr[d - 1] = new
    # print arr
    str = ' '.join(arr) + '\n'  # 在末尾补加一个换行符
    # 用writelines将列表从新写入文件
    target = open(file_name, "w")
    flist[c - 1] = str
    target.writelines(flist)
    target.close()

def realtime(file_name):
    # 5.实时课程
    # 1).当前课程 2).下一节课
    cur = datetime.datetime.now()
    now_week = int(cur.strftime('%w'))
    now_hour = int(cur.hour)
    now_min = int(cur.minute)
    print "现在时间:%s.%s.%s %2d:%2d" % (cur.year, cur.month, cur.day, now_hour, now_min)
    # now_sec = int(cur.second) #姑且不考虑秒针

    next= 0
    now = 0
    if now_hour < 9:
        next = 1
    elif now_hour == 9:
        next = 2
        if now_min <= 45:
            now = 1
    elif now_hour == 10:
        next = 3
        if now_min <= 45:
            now = 2
    elif now_hour == 14:
        next = 4
        if now_min <= 45:
            now = 3
    elif now_hour == 15:
        next = 5
        if now_min <= 45:
            now = 4
    elif now_hour == 16:
        next = 0
        if now_min <= 45:
            now = 5
    # 读取当天课表
    file = open(file_name, "r")
    flist = file.readlines()

    if now:
        arr_1 = flist[now - 1].split()
        now_class = arr_1[now_week - 1]
        print "现在课程是:%s" %now_class
    else :
        print "现在没课！"
    if next:
        arr_2 = flist[next - 1].split()
        next_class = arr_2[now_week - 1]
        print "接下来课程是:%s" % next_class
    else :
        print "接下来没课！"

def main():
    input_file = "course.txt"
    # test_file = "test.txt"
    menu()
    while True:
        choice = int(raw_input("请选择:\n"))
        while (choice > 5) or (choice < 1):
            choice = raw_input("请重新输入:")
        if choice == 1:
            show_all(input_file)
        elif choice == 2:
            update(input_file)
        elif choice == 3:
            show_all(input_file)
        elif choice == 4:
            realtime(input_file)
        else :
            exit(1)

if __name__ == '__main__':
    main()