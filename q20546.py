# 기적의 매매법
n = int(input())
a = list(map(int, input().split()))
jHave = 0
jCash = n
sHave = 0
sCash = n
    
BNP = jHave*a[13]+jCash
TIMINNG = sHave*a[13]+sCash

upCnt = 0
downCnt = 0
for i in range(13):
    if a[i]<=jCash:
        jHave += jCash/a[i]
        jCash -= jHave*a[i]
    if a[i]<a[i+1]:
        upCnt+=1
        downCnt=0
    if a[i]>a[i+1]:
        downCnt+=1
        upCnt=0
        
    if downCnt == 3:
        sHave += sCash/a[i]
        sCash -= sHave*a[i]
        downCnt = 0
    if upCnt == 3:
        sCash += sHave*a[i]
        sHave = 0
    print("jHave:", jHave, "jCash:", jCash, "sHave:", sHave, "sCash:", sCash)
    print(i, "번째 : ", BNP, " and ", TIMINNG)
        
        
if a[13]<jCash:
    jHave += jCash/a[13]
    jCash -= jHave*a[13]

if BNP > TIMINNG:
    print("BNP")
    print(BNP)
    print(TIMINNG)
elif BNP < TIMINNG:
    print("TIMING")
    print(TIMINNG)
else: print("SAMESAME")
    