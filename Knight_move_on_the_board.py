n=int(input("(5이상)정사각형 행열 : "))
a=int(input("X시작 위치 : "))
b=int(input("Y시작 위치 : "))

arr=[]                          #배열 생성
for i in range(n):
    arr.append([0]*n)

SX=a-1                          #X 좌표
SY=b-1                          #Y 좌표
arr[SX][SY]=1                   #시작위치 = 1

i_1=1                           #i 보조
j_1=-1                          #j 보조
Bc=0                            #비교 횟수
sij=[[a-1,b-1,1,0]]             #succeed i, j
z=[[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1]]

try:
    for i in range(2,10000000):
        i_1+=1
        if(i_1>n*n):
            break

        for j in range(0,10000000):
            j_1+=1

            if(j_1==8):
                i_1-=2
                j_1=sij[-1][3]
                SX=sij[-1][0]
                SY=sij[-1][1]
                arr[SX][SY]=0
                del sij[-1]
                Bc+=1
                SX=sij[-1][0]
                SY=sij[-1][1]
                break

            SX+=(z[j_1][0])
            SY+=(z[j_1][1])

            if(SX>=0 and SX<n and SY>=0 and SY<n and arr[SX][SY]==0):#<<-------조건 만족하면 행열에 숫자 찍기
                arr[SX][SY]=i_1
                sij+=[[SX,SY,i_1,j_1]]
                j_1=-1
                break
            else:
                if(j_1==7):#<<-------------------------위의 조건 만족 못하면 0으로 만들고 이전 숫자로 돌아가기
                    i_1=sij[-1][2]
                    j_1=sij[-1][3]
                    SX=sij[-1][0]
                    SY=sij[-1][1]
                    arr[SX][SY]=0
                    del sij[-1]
                    Bc+=1
                    SX=sij[-1][0]
                    SY=sij[-1][1]
                else:
                    SX=sij[-1][0]
                    SY=sij[-1][1]
except IndexError:
    print("답을 구할 수 없음.")
                
for i in range(0,n):#<<---------------------------------------출력
    for j in range(0,n):
        print("%3d" %arr[i][j], end=" ")
    print()

print('\n' "비교 횟수 : ", Bc)
