import time
import bisect
#時間計測開始
start = time.clock()
#テキストファイル読み込み
#crossingFile = open("sample0.txt")
crossingFile = open("crossing.txt")
crs = list(map(int,crossingFile.readlines()))
count = 0
Max = 0
Min = 99999999
newList = []
#交差点の数の算出
for i in range(len(crs)):
    val = crs[i]
        if Max < val:
            Max = val
                newList.append(val)
        elif Min > val:
            Min = val
                newList.insert(0,val)
                count += i
        else:
            count += len(newList) - bisect.bisect_left(newList,val)
                bisect.insort_left(newList,val)
#時間計測結果
proc = time.clock() - start
print("count",count)
print("Time is",proc)
#結果書き込み
answer = open("answer0.txt","w")
answer.write(str(count)+","+str(round(proc))+"\n")
answer.write("ENV: Python\n")
#入力待ち
input()
