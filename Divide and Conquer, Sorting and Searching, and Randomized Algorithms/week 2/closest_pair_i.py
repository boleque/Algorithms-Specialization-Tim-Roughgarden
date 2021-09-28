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
        return math.sqrt(pow(self._x - other._x) + pow(self._y - other._y))
    
    def __repr__(self):
        return "Point x={} y={}".format(self._x, self._y)

def closest_pair_2D_brute_force(P):
    best_pair = None
    minDistance = sys.maxint
    pLen = len(P)
    for i in range(pLen):
        for j in (i + 1, pLen):
            distance = P[i].distance(P[j])
            if minDistance > distance:
                minDistance = distance
                best_pair = P[i], P[j]
    return best_pair

def closest_pair_2D_divide_and_conquer(Px, Py):
    pLen = len(Px)
    if pLen <= 3:
        return closest_pair_2D_brute_force(Px)
    
    #Q - left half of P
    #R - right half of P
    middle = pLen // 2
    Qx, Qy = Px[:middle], Py[:middle]
    Rx, Ry = Px[middle:], Py[middle:]

    p1, q1 = closest_pair_2D_divide_and_conquer(Qx, Qy)
    p2, q2 = closest_pair_2D_divide_and_conquer(Rx, Ry)

    delta = min(p1.distance(q1), p2.distance(q2))

    p3, q3 = split_closest_pair(Px, Py, delta)

    return best of (p1, q1), (p2, q2), (p3, q3)

def split_closest_pair(Px, Py, delta):
    pLen = len(Px)
    # x - max coord in left of P
    x = Px[:pLen // 2][-1]._x
    # let Sy be the points of P with x within the range
    Sy = [p for p in Py if (x - delta) <= p._x =< (x + delta)]

    best = delta
    best_pair = None
    sLen = len(Sy)
    
    points_to_check_i, points_to_check_j = sLen, sLen if sLen <= 7 else (Sy - 7), 7
    for i in range(points_to_check_i):
        for j in (i + 1, points_to_check_j):
            distance = Sy[i].distanceTo(Sy[j])
            if distance < best:
                best = distance
                best_pair = Sy[i], Sy[j]
    return best_pair

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