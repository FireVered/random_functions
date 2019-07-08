npiv = 2

import random

def gen_id():
    lst = [] #a,b,c,d,e,o1,o2,o3,o4,o5,o6,o7,o8,o9  || 14 numbers

    for i in range(0,npiv):
        lst.append(random.random() * random.randint(-1000,1000))

    for i in range(0,(npiv*2)-1):
        lst.append(random.randint(0,4))

    return lst




#0 -
#1 +
#2 *
#3 /
#4 **
    
def func(lst,abcde):
    num = 0
    for i in range(npiv):
        if i == 0:
            if lst[npiv] == 0:
                num += abcde[i]-lst[i]
            if lst[npiv] == 1:
                num += abcde[i]+lst[i]
            if lst[npiv] == 2:
                num += abcde[i]*lst[i]
            if lst[npiv] == 3:
                num += abcde[i]/lst[i]
            if lst[npiv] == 4:
                num += abcde[i]**lst[i]

        else:
            if lst[(npiv-1) + i] == 0:
                if lst[npiv + i] == 0:
                    num -= abcde[i]-lst[i]
                if lst[npiv + i] == 1:
                    num -= abcde[i]+lst[i]
                if lst[npiv + i] == 2:
                    num -= abcde[i]*lst[i]
                if lst[npiv + i] == 3:
                    num -= abcde[i]/lst[i]
                if lst[npiv + i] == 4:
                    num -= abcde[i]**lst[i]
                    
            if lst[(npiv-1) + i] == 1:
                if lst[npiv + i] == 0:
                    num += abcde[i]-lst[i]
                if lst[npiv + i] == 1:
                    num += abcde[i]+lst[i]
                if lst[npiv + i] == 2:
                    num += abcde[i]*lst[i]
                if lst[npiv + i] == 3:
                    num += abcde[i]/lst[i]
                if lst[npiv + i] == 4:
                    num += abcde[i]**lst[i]
                    
            if lst[(npiv-1) + i] == 2:
                if lst[npiv + i] == 0:
                    num *= abcde[i]-lst[i]
                if lst[npiv + i] == 1:
                    num *= abcde[i]+lst[i]
                if lst[npiv + i] == 2:
                    num *= abcde[i]*lst[i]
                if lst[npiv + i] == 3:
                    num *= abcde[i]/lst[i]
                if lst[npiv + i] == 4:
                    num *= abcde[i]**lst[i]
                
            if lst[(npiv-1) + i] == 3:
                if lst[npiv + i] == 0:
                    num /= abcde[i]-lst[i]
                if lst[npiv + i] == 1:
                    num /= abcde[i]+lst[i]
                if lst[npiv + i] == 2:
                    num /= abcde[i]*lst[i]
                if lst[npiv + i] == 3:
                    num /= abcde[i]/lst[i]
                if lst[npiv + i] == 4:
                    num /= abcde[i]**lst[i]

            if lst[(npiv-1) + i] == 4:
                if lst[npiv + i] == 0:
                    num **= abcde[i]-lst[i]
                if lst[npiv + i] == 1:
                    num **= abcde[i]+lst[i]
                if lst[npiv + i] == 2:
                    num **= abcde[i]*lst[i]
                if lst[npiv + i] == 3:
                    num **= abcde[i]/lst[i]
                if lst[npiv + i] == 4:
                    num **= abcde[i]**lst[i]

    return(num)


print(func([-35.609044339104734, 470.2526268610348, 0, 1, 2],[2,3]))
