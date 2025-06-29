N = int(input())

command = []
num = []
arr = [] # 배열선언

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)
# Please write your code here.

def push_back(A : str) : # 맨 뒤에 정수 A를 삽입
    arr.append(A)
def pop_back() : # 맨 뒤에 정수 하나 삭제
    arr.pop()
def size() -> int : # 배열 사이즈 개수 출력
    return len(arr)
def get(k : int) -> int : # 배열에서 k번째 숫자 출력
    return arr[k-1]

for i in range(len(command)) :
    com = command[i]
    n = num[i]

    if com == "push_back" :
        push_back(n)
    elif com == "pop_back" :
        pop_back()
    elif com == "size" :
        arrSize = size()
        print(arrSize)
    elif com == "get" :
        arrItem = get(n)
        print(arrItem)


