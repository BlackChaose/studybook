iFPath = 'input.txt'
oFPath = 'output.txt'

inputFile = open(iFPath, 'r')
outputFile = open(oFPath, 'w')

K, N = map(int, inputFile.readline().split())

arr = [int(s) for s in inputFile.readline().split()]

PetyaPoints = 0
VasyaPoints = 0
Result = ""
i = 0

while i < N:
    if(arr[i] % 6 == 0) and (arr[i] % 9 == 0):
        if (VasyaPoints > 0):
            VasyaPoints -= 1
        if (PetyaPoints > 0):
            PetyaPoints -= 1
    elif (arr[i] % 6) == 0:
        VasyaPoints += 1
    elif(arr[i] % 9) == 0:
        PetyaPoinst += 1
	#0000000000000
	if(VasyaPoints == K) and (PetyaPoints == K):
		Result = "Draw"
		break
	elif VasyaPoints == K:
		Result = "Vasya"
		break
	elif PetyaPoints == K:
		Result = "Petya"
	i += 1

if (Result != ''):
	if (PetyaPoints == VasyaPoints):
		Result = "Draw"
	elif(PetyaPointa > VasyaPolints):
		Result = "Petya"
	else Result = "Vasya"
outputFile.write(Result)

inputFile.close()
outputFile.close() 
