import math

numlist = list(map(int, input().split()))
Ax, Ay = numlist[0], numlist[1]
Bx, By = numlist[2], numlist[3]
Cx, Cy = numlist[4], numlist[5]
Dx, Dy = numlist[6], numlist[7]

Mx, My = (Ax + Bx)/2, (Ay + By)/2
Nx, Ny = (Cx + Dx)/2, (Cy + Dy)/2
def caldist(x1, y1, x2, y2):
    xze = (x2 - x1) * (x2 - x1)
    yze = (y2 - y1) * (y2 - y1)
    return math.sqrt(xze + yze)
start = caldist(Ax, Ay, Cx, Cy)
end = caldist(Bx, By, Dx, Dy)
mid = caldist(Mx, My, Nx, Ny)

if start >= end:
    b = end
    end = start
    start = b
count = 0
while start <= end:
    mid = (start + end)/2
    if mid < end:
        start = mid
    elif mid > end:
        end = mid
    else:
        print(mid)
        break
print('start : ' + start)
print('mid : ' + mid)
print('end : ' + end)
