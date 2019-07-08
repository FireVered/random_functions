import random

def gen_id():
    lst = [] #a,b,c,d,e,o1,o2,o3,o4,o5,o6,o7,o8,o9  || 14 numbers

    for i in range(0,5):
        lst.append(random.random() * random.randint(-1000,1000))

    for i in range(0,9):
        lst.append(random.randint(0,4))

    return lst




#0 -
#1 +
#2 *
#3 /
#4 **
    
def func(lst,abcde):
    num = 0
    for i in range(5):
        if i == 0:
            if lst[4+1] == 0:
                num += abcde[i]-lst[i]
            if lst[4+1] == 1:
                num += abcde[i]+lst[i]
            if lst[4+1] == 2:
                num += abcde[i]*lst[i]
            if lst[4+1] == 3:
                num += abcde[i]/lst[i]
            if lst[4+1] == 4:
                num += abcde[i]**lst[i]

        else:
            if lst[4+i] == 0:
                if lst[5+i] == 0:
                    num -= abcde[i]-lst[i]
                if lst[5+i] == 1:
                    num -= abcde[i]+lst[i]
                if lst[5+i] == 2:
                    num -= abcde[i]*lst[i]
                if lst[5+i] == 3:
                    num -= abcde[i]/lst[i]
                if lst[5+i] == 4:
                    num -= abcde[i]**lst[i]
                    
            if lst[4+i] == 1:
                if lst[5+i] == 0:
                    num += abcde[i]-lst[i]
                if lst[5+i] == 1:
                    num += abcde[i]+lst[i]
                if lst[5+i] == 2:
                    num += abcde[i]*lst[i]
                if lst[5+i] == 3:
                    num += abcde[i]/lst[i]
                if lst[5+i] == 4:
                    num += abcde[i]**lst[i]
                    
            if lst[4+i] == 2:
                if lst[5+i] == 0:
                    num *= abcde[i]-lst[i]
                if lst[5+i] == 1:
                    num *= abcde[i]+lst[i]
                if lst[5+i] == 2:
                    num *= abcde[i]*lst[i]
                if lst[5+i] == 3:
                    num *= abcde[i]/lst[i]
                if lst[5+i] == 4:
                    num *= abcde[i]**lst[i]
                
            if lst[4+i] == 3:
                if lst[5+i] == 0:
                    num /= abcde[i]-lst[i]
                if lst[5+i] == 1:
                    num /= abcde[i]+lst[i]
                if lst[5+i] == 2:
                    num /= abcde[i]*lst[i]
                if lst[5+i] == 3:
                    num /= abcde[i]/lst[i]
                if lst[5+i] == 4:
                    num /= abcde[i]**lst[i]

            if lst[4+i] == 4:
                if lst[5+i] == 0:
                    num **= abcde[i]-lst[i]
                if lst[5+i] == 1:
                    num **= abcde[i]+lst[i]
                if lst[5+i] == 2:
                    num **= abcde[i]*lst[i]
                if lst[5+i] == 3:
                    num **= abcde[i]/lst[i]
                if lst[5+i] == 4:
                    num **= abcde[i]**lst[i]

    return(num)
