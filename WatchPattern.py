def line(n):
    for i in range(n):
        if i == 0:
            print(8*" " + "||" + "-"*7 + "||")
        else:
            print(8*" " + "||" + " "*7 + "||")
    print(8*" " + "++" + "-"*7 + "++")

def halfcircle(n):
    dem = 6
    tmp = 5
    for i in range(n-1):
        if i == 0:
            print(dem*" "+"++" + tmp*" " + "12" + tmp*" "+"++")
            tmp += 10
            dem -= 2
        elif i <=2:
            print(dem*" "+"++" + tmp*" "+"++")
            dem -= 2
            tmp += 4
        else:
            print(dem*" "+"++"+tmp*" "+"++")
    tmp1 = (tmp // 2) - 2
    tmp = (tmp // 2) - 1
    print(dem*" "+"++9"+tmp1*" "+"〇"+" "*tmp+"3++")

def anotherhalfcircle(n):
    dem = 0
    tmp = 23
    for i in range(n-1):
        if i <=2:
            print(dem*" "+"++"+tmp*" "+"++")
        else:
            dem +=2
            tmp -= 4
            print(dem*" "+"++"+tmp*" "+"++")
    dem = 6
    tmp = 5
    print(dem*" "+"++"+tmp*" " + "6" + tmp*" " +"++")

def lastline(n):
    for i in range(n):
        if i == 0:
            print(8*" " + "||" + "-"*7 + "||")
        else:
            print(8*" " + "||" + " "*7 + "||")
    print(8*" " + "||" + "-"*7 + "||")

line(15)
halfcircle(6)
anotherhalfcircle(6)
lastline(15)
