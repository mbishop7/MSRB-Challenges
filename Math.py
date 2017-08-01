def accrued():
    accrued = float(input())
    x= str(accrued)
    i=x.find('.')
    n = x[:i+4]
    print (round(float(n), 2))

def dollar():
    dollar = float(input())
    x = str(dollar)
    i = x.find('.')
    n = x[:i + 4]
    print(round(float(n), 2))

def yeld():
    yeld = float(input())
    x = str(yeld)
    i = x.find('.')
    n = x[:i + 4]
    print(round(float(n), 2))