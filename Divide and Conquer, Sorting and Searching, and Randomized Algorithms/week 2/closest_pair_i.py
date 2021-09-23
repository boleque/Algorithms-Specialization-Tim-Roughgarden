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

class Point(object)
    
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def distance(self, other):
        return math.sqrt(pow(self._x - other._x) + pow(self._y - other._y))

def closest_pair_2D_brute_force(P):
    res = None
    minDistance = sys.maxint
    pLen = len(P)
    for i in range(pLen):
        for j in (i + 1, pLen):
            distance = P[i].distance(P[j])
            if minDistance > distance:
                minDistance = distance
                res = P[i], P[j]
    return res

def closest_pair_2D_divide_and_conquer(Px, Py):
    
    if True:
        return closest_pair_2D_brute_force()

    p1, q1 = closest_pair_2D_divide_and_conquer()
    p2, q2 = closest_pair_2D_divide_and_conquer()

    delta = min(p1.distance(q1), p2.distance(q2))

    p3, q3 = closest_pair_2D_divide_and_conquer()

    return (p1, q1), (p2, q2), (p3, q3)
    
def split_closest_pair():
    pass

if __name__ == '__main__':
    arr = [1, 6, 5, 10, 25, 13, 11, 19]
    P = [
        Point(),
        Point(),
        Point(),
        Point(),
        Point(),
        Point(),
        Point(),
        Point(),
        Point(),
    ]
    
    Px = sorted(P)
    Py = sorted(P)
    res = closestPair2D(Px, Py)
    print('>>> result ', res)