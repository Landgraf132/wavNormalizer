import math
import sys

targetDb = -24 #-23 ва
maxWavValue = 65534
curWavValue = 0

curWavValue = (math.pow(10,targetDb/20))*maxWavValue
print(curWavValue)
print(curWavValue/maxWavValue)
 
ans2 = 20*math.log10(curWavValue/maxWavValue)
print(ans2)
