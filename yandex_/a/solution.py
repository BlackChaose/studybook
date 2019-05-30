iFPath = './input.txt'
oFPath = './output.txt'
inputFile = open(iFPath,'r')
outputFile = open(oFPath, 'w')
def getRow(fNum,interval, K):
    res = [fNum]
    i = fNum
    maxNum = fNum + interval * (K-1)
    while i <= (maxNum):
        i += interval
        res.append(i)
    return res
#..................................

N, X, K = map(int, inputFile.readline().split())

arr =[int(s) for s in  inputFile.readline().split()]
arr.sort()
matrix = [getRow(el, X, K) for el in arr]
t_matrix = list( map(list, zip(*matrix)))
flat_list = []
list(flat_list.extend(row) for row in t_matrix)
set_list = list(set(flat_list))
index = K - 1
outputFile.write(str(set_list[index]))

#------------------------------------
inputFile.close()
outputFile.close()
