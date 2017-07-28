# MSRB-Challenge2
import math
def main():
    patience = 1
    while patience > 0:
        response = input('Please enter a letter and the value to round\n"A" for Accrued Interest\n"D" for Dollar Price\n"Y" for Yield\n')
        if response == "A":
            print('Enter the Accrued Interest')
            math.Accrued()
            print('Enter another letter? Enter "Y" to continue. Enter "E" to exit')
            response1 = input()
            if response1 == "E":
                quit()
            else:
                main()
        elif response == "D":
            print('Enter the dollar price')
            math.dollar()
            print('Enter another letter? Enter "Y" to continue. Enter "E" to exit')
            response1 = input()
            if response1 == "E":
                quit()
            else:
                main()
        elif response == "Y":
            print('Enter the yield')
            math.yeld()
            print('Enter another letter? Enter "Y" to continue. Enter "E" to exit')
            response1 = input()
            if response1 == "E":
                quit()
            else:
                main()
        else:
            print('Not a valid option, try again')
main()

****SEPARATE PYTHON FILE BEING REFERENCED***
def Accrued():
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
