import math
'''импортирует библеотеку math '''

def area(r):
    '''принимает число r , возвращает площадь '''
    return math.pi * r * r


def perimeter(r):
    '''принимает r, возвращает периметр круга'''
    return 2 * math.pi * r

x = int(input())
print(area(x))