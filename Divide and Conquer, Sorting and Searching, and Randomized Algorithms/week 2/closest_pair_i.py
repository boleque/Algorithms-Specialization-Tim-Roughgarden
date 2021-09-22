import sys
import math

def closestPair1D(P):
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

def closestPair2DBruteForce(pointsArr):
    res = None
    minDistance = sys.maxint
    for pointX in pointsArr:
        for pointY in pointsArr:
            distance = pointX.distance(pointY)
            if minDistance > pointX.distance(pointY):
                minDistance = distance
                res = pointX, pointY
    return res

def closestPair2D(Px, Py):
    res = []
    minDistance = sys.maxint
    arrSorted = sorted(arr)
    arrLen = len(arr)
    for i in range(len(arr)):
        pass
    for i, v in arrSorted:
        pass
        
if __name__ == '__main__':
    arr = [1, 6, 5, 10, 25, 13, 11, 19]
    res = closestPair1D(arr)
    print('>>> result ', res)