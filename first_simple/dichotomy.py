# 二分法
def getStep(list, findNum):
    step = 1
    nowList = list.copy()
    listLen = len(nowList)
    print("listLen", listLen)
    low = nowList[0]
    high = nowList[listLen-1]
    middle = nowList[int((listLen-1)/2)]
    while True:
        print("low", low)
        print("high", high)
        if middle == findNum:
            return step
        else:
            lowIndex = nowList.index(low)
            highIndex = nowList.index(high)
            middleIndex = int((lowIndex + highIndex) / 2)
            middle = nowList[middleIndex]
            if findNum > middle:
                low = middle
            elif findNum < middle:
                high = middle
            else:
                return step
            step = step + 1




        # listLen = len(nowList)
        # if len(nowList) == 0:
        #     print("step:", step)
        #     return step
        # if nowList[0] == findNum:
        #     break
        # else:
        #     middle = 0
        #     print("(listLen - 1) % 2", (listLen - 1) % 2)
        #     print("int((listLen - 1) / 2)", int((listLen - 1) / 2))
        #     if listLen % 2 == 0:
        #         middle = nowList[int((listLen)/2)-1]
        #         print("middle1", middle)
        #     else:
        #         middle = nowList[int((listLen-1)/2)]
        #         print("middle2", middle)
        #     # middle = (low+high)/2
        #     if findNum == middle:
        #         print("step:", step)
        #         break
        #     elif findNum > middle:
        #         low = middle
        #     else:
        #         high = middle
        #     print("nowList.index(low)", nowList.index(low))
        #     print("nowList.index(high)", nowList.index(high))
        #     nowList = nowList[nowList.index(low):nowList.index(high)+1]
        #     step = step + 1
        #     print("nowList", nowList)


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 33, 43, 47, 49, 51, 100, 120, 133]
list = [1, 2, 3, 4, 5, 6, 7]
findNum = 3
step = getStep(list, findNum)
print("step:", step)