# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a*h)/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P= a + b + c

# Описание решения 

**Функция area во всех файлах позволяет найти площадь(по формулам, приведенных выше) таких фигур как:**
- Треугольник
- Круг
- Квадрат
- Прямоугольник
### Примеры вызова функций
<u>Пример вызова функции area в файле **square**:</u>
```python
def area(a):
    return a * a
x=4
print(area(x))
```

*OUTPUT: 16*

***Принимает х, выводит площадь квадрата***

Пример вызова функции area **circle**:
```python
import math
def area(r):
    return math.pi * r * r
x=4
print(area(x))
```
*OUTPUT: 50.26548245743669*

***Принимает х, выводит площадь круга***

### Пример вызова функции area **rectangle**:
```python
import math
def area(a, b):
    return a*b
x=4
y = 2
print(area(x))
```
*OUTPUT: 8*

***Принимает х, выводит площадь прямоугольника***

### Пример вызова функции area **triangle**:
```python
import math
def area(a, h):
    return (a*h) / 2
x=4
y = 2
print(area(x,y))
```
*OUTPUT: 4.0*

***Принимает х и y, выводит площадь треугольника***

**Также в файлах присутствует функция perimeter, которая считает периметр соответствующих фигур, т.е:**
- Треугольника
- Круга
- Квадрата
- Прямоугольника
<u>Пример вызова функции perimeter в файле **square**:</u>
```python

def area(a):
    return a * a
x=4
print(area(x))
```

*OUTPUT: 16*

***Принимает х, выводит площадь квадрата***

<u>Пример вызова функции perimeter в файле **circle**:</u>
```python
def perimeter(r):
    return 2 * math.pi * r
x=4
print(area(x))
```

*OUTPUT: 16*

***Принимает х, выводит площадь квадрата***

<u>Пример вызова функции perimeter в файле **rectangle**:</u>
```python
def perimeter(a,b):
    return a+b
x=4
y=2
print(area(x))
```

*OUTPUT: 6*

***Принимает х,y,  выводит площадь прямоугольника***

<u>Пример вызова функции perimeter в файле **triangle**:</u>
```python
def perimeter(r):
   return a+b+c
x=4
y=2
z=3
print(perimeter(x,y,z))
```

*OUTPUT: 9*

***Принимает x,y,z, выводит их сумму***


## История изменений
```bash
commit cb4afe54e378a2123e4be98cfc9c71b89d665e53 (newfeature-465352)
Author: Nikitka <redzernonikita@gmail.com>
Date:   Fri Sep 27 11:02:16 2024 +0300

    test

commit e184c7c345427b38a311db1e714d96e32af9605a (origin/newfeature-465352, newfeature-465352-megatest)
Author: Nikitka <redzernonikita@gmail.com>
Date:   Fri Sep 20 11:16:51 2024 +0300

    Fixed bug in rectangle.py

commit 822ae1281b01a363d169e4f94b3e7ba00c2e6500
Author: Nikitka <redzernonikita@gmail.com>
Date:   Fri Sep 20 11:15:21 2024 +0300

    Added triangle.py file

commit f6edfd2d9b6922df44ff332f69415982182702cc
Author: Nikitka <redzernonikita@gmail.com>
Date:   Fri Sep 20 11:14:20 2024 +0300

    Added new file: rectangle.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (HEAD -> documentation, origin/main, origin/HEAD, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
```