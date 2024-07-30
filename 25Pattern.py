n = 5
arr = [[0] * n for _ in range(n)]

visit = set()
val = n * n
rtoL, ttoD, ltoR, dtoU = True, False, False, False
rightToLeft, topToDown, leftToRight, downToUp = [0, n - 1], [1, 0], [n - 1, 1], [n - 2, n - 1]
def secondIteration():
    rightToLeft[0] += 1
    rightToLeft[1] -= 1
    topToDown[0] += 1
    topToDown[1] += 1
    leftToRight[0] -= 1
    leftToRight[1] += 1
    downToUp[0] -= 1
    downToUp[1] -= 1

while val > 0:
    while rtoL:
        r, c = rightToLeft
        if (r, c) in visit:
            r, c = r + 1, c - 1
        while (r, c) not in visit:
            if min(r, c) < 0 or max(r, c) >= n:
                break
            arr[r][c] = val
            val -= 1
            visit.add((r, c))
            c -= 1
        rtoL = False
        ttoD = True
    while ttoD:
        r, c = topToDown
        while (r, c) not in visit:
            if min(r, c) < 0 or max(r, c) >= n:
                break
            arr[r][c] = val
            visit.add((r, c))
            val -= 1
            r += 1
        ltoR = True
        ttoD = False
    while ltoR:
        r, c = leftToRight
        while (r, c) not in visit:
            if min(r, c) < 0 or max(r, c) >= n:
                break
            arr[r][c] = val
            val -= 1
            visit.add((r, c))
            c += 1
        ltoR = False
        dtoU = True
    while dtoU:
        r, c = downToUp
        while (r, c) not in visit:
            if min(r, c) < 0 or max(r, c) >= n:
                break
            arr[r][c] = val
            val -= 1
            visit.add((r, c))
            r -= 1

        dtoU = False
        rtoL = True
    secondIteration()

for i in arr:
    print(i)