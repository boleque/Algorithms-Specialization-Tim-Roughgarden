import sys
import math


def closest_pair_1d(P):
    res = None
    minDistance = sys.maxint
    arrSorted = sorted(arr)
    arrLen = len(arr)
    for i in range(arrLen):
        if i + 1 == arrLen:
            break
        distance = arrSorted[i+1] - arrSorted[i]
        if minDistance > distance:
            minDistance = distance
            res = arrSorted[i+1], arrSorted[i]
    return res

class Point(object):
    
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def distance(self, other):
        return math.sqrt(pow(self._x - other._x, 2) + pow(self._y - other._y, 2))
    
    def __repr__(self):
        return "Point x={} y={}".format(self._x, self._y)

def closest_pair_2D_brute_force(P):
    best_pair = None
    min_dist = sys.maxint
    pLen = len(P)
    for i in range(pLen):
        for j in range(i + 1, pLen):
            distance = P[i].distance(P[j])
            if min_dist > distance:
                min_dist = distance
                best_pair = P[i], P[j]
    return min_dist, best_pair

def closest_pair_2D_divide_and_conquer(Px, Py):
    pLen = len(Px)
    if pLen <= 3:
        return closest_pair_2D_brute_force(Px)
    
    #Q - left half of P
    #R - right half of P
    middle = pLen // 2
    Qx, Qy = Px[:middle], Py[:middle]
    Rx, Ry = Px[middle:], Py[middle:]

    dist1, pair1 = closest_pair_2D_divide_and_conquer(Qx, Qy)
    dist2, pair2 = closest_pair_2D_divide_and_conquer(Rx, Ry)

    delta = min(dist1, dist2)

    dist3, pair3 = split_closest_pair(Px, Py, delta)
    
    best_pair = None
    min_dist = min(dist1, dist2, dist3)
    if min_dist == dist1:
        best_pair = pair1
    elif min_dist == dist2:
        best_pair = pair2
    else:
        best_pair = pair3

    return min_dist, best_pair

def split_closest_pair(Px, Py, delta):
    pLen = len(Px)
    # x - max coord in left of P
    x = Px[:pLen // 2][-1]._x
    # let Sy be the points of P with x within the range
    Sy = [p for p in Py if (x - delta) < p._x < (x + delta)]

    min_dist = delta
    best_pair = None
    sLen = len(Sy)
    for i in range(sLen):
        for j in range(min(7, sLen-1)):
            distance = Sy[i].distance(Sy[j])
            if distance < min_dist:
                min_dist = distance
                best_pair = Sy[i], Sy[j]
    return min_dist, best_pair

if __name__ == '__main__':
    arr = [1, 6, 5, 10, 25, 13, 11, 19]
    P = [
        Point(7,4),
        Point(2,2),
        Point(4,5),
        Point(2,6),     
        Point(1,1),
    ]

    Px = sorted(P, key=lambda p: p._x)
    Py = sorted(P, key=lambda p: p._y)
    res = closest_pair_2D_divide_and_conquer(Px, Py)
    print("closest pair ", res)