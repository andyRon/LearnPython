import random
# 批量生成数学题

for i in range(2000):
    maxnum = random.randint(0, 99)
    minnum1=random.randint(0, 9)
    minnum2 = random.randint(0, 9)
    fu1=["-","+"]
    funumber=random.randint(0, 1)
    if i % 2 ==0 :
        # print(minnum1,"×",minnum2,fu1[funumber],maxnum,"=" )
        lastnumber=0
        if fu1[funumber] == "-" :
            lastnumber=minnum1*minnum2-maxnum
        if fu1[funumber] == "+":
            lastnumber = minnum1 * minnum2 + maxnum
        data=str(minnum1)+"×"+str(minnum2)+str(fu1[funumber])+str(maxnum)+"="
        print(data)
        if lastnumber>=0:
            f = open("zhuke.txt", "a")
            f.write(data+"\n")
            f.close()
    else:
        # print(maxnum, fu1[funumber],minnum1, "×", minnum2, "=" )
        lastnumber=0
        if fu1[funumber] == "-" :
            lastnumber=maxnum - minnum1 * minnum2
        if fu1[funumber] == "+":
            lastnumber = maxnum + minnum1 * minnum2
        data = str(maxnum) +str( fu1[funumber]) + str(minnum1) +  "×"+ str(minnum2) + "="
        print(data)
        if lastnumber >= 0:
            f = open("zhuke.txt", "a")
            f.write(data + "\n")
            f.close()
