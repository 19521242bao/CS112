
def checkgiamngat(a,max1):
    n=len(a)
    if n==0:
        return 0
    for i in range(0,n):
        if a[i]!=max1-i:
            return i-n
    return 0
def checkTang(a):
    n=len(a)
    if n==0:
        return 1
    if n==1:
        return 0
    index=0
    for i in range(1,n):
        s=a[i]-a[i-1]
        if s<index:
            return (i-1-n)
        else:
            index=s
    return 0
def printA(arr):
    for i in range(0,3):
        n=len(arr[i])
        for j in range(0,n):
            print(arr[i][j],end=" ")
        print()
    print("--")
def trongso(arr,max1):
    a1 = arr[0]
    a2 = arr[1]
    a3 = arr[2]
    index1=checkTang(a1)
    index2=checkTang(a2)
    index=checkgiamngat(a3,max1)
    return index1+index2+index
def disLenArr(arr):
    n1=len(arr[0])
    n2=len(arr[1])
    n3=len(arr[2])
    return max(n1,max(n2,n3))
import copy


def atob(state):
    if len(state[0]) > 0:
        a = state[0].pop()
        state[1].append(a)


def atoc(state):
    if len(state[0]) > 0:
        a = state[0].pop()
        state[2].append(a)


def btoa(state):
    if len(state[1]) > 0:
        a = state[1].pop()
        state[0].append(a)


def btoc(state):
    if len(state[1]) > 0:
        a = state[1].pop()
        state[2].append(a)


def ctoa(state):
    if len(state[2]) > 0:
        a = state[2].pop()
        state[0].append(a)


def ctob(state):
    if len(state[2]) > 0:
        a = state[2].pop()
        state[1].append(a)


def nextstates(state):
    state1 = copy.deepcopy(state)
    state2 = copy.deepcopy(state)
    state3 = copy.deepcopy(state)
    state4 = copy.deepcopy(state)
    state5 = copy.deepcopy(state)
    state6 = copy.deepcopy(state)
    arr1=[]
    arr2=[]
    arr3=[]

    if len(state[0])>0:
        atob(state1)
        atoc(state2)
        arr1=[state1,state2]
    if len(state[0])>0:
        btoa(state3)
        btoc(state4)
        arr2=[state3,state4]
    if len(state[0])>0:
        ctoa(state5)
        ctob(state6)
        arr3=[state5,state6]

    return arr1+arr2+arr3


def solve(solution, visited, state, goalstate, depth,value):
    max1 = len(state[0]) + len(state[1]) + len(state[2]) - 1
    if depth not in visited:
        visited[depth] = {}
    if depth > 20+max1:
        return False
    if str(state[2]) == str(goalstate):
        return True
    max1=len(state[0])+len(state[1])+len(state[2])-1
    nstates = nextstates(state)


    max2=value
    for state in nstates:
        v=trongso(state, max1)

        max2=max(v,max2)
    for state in nstates:
        s=trongso(state,max1)
        if str(state) not in visited[depth] :
           if s==max2:
                solution.append(state)
                visited[depth][str(state)] = 1
                if solve(solution, visited, state, goalstate, depth+1,value):
                    return True
                solution.pop()
    return False

array = []
goalstate = []
for i in range(3):
    ip = [int(i) for i in input().split()]
    array.append(ip)
    goalstate.extend(ip)
goalstate.sort(reverse=True)
visited = dict()
visited[0] = dict()
visited[0][str(array)] = 1
depth = 0
solution = [array]

max1=len(array[0])+len(array[1])+len(array[2])-1
value=trongso(array,max1)
if solve(solution, visited, array, goalstate, depth,value):
    for state in solution:
        print(state)

