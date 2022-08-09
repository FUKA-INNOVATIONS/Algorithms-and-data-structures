'''
Positiivinen kokonaisluku on onnenluku, jos sen numeroiden summa on jaollinen 7:llä.
Esimerkiksi luku 25743 on onnenluku, koska 2+5+7+4+3=21, joka on jaollinen 7:llä.
Tehtäväsi on tarkastaa, onko annettu luku n onnenluku. Voit olettaa, että n on kokonaisluku välillä 1…109.
'''

def check(n):
    total = 0
    for i in str(n):
        total += int(i)
    if total%7 != 0:
        return False
    else:
        return True

if __name__ == "__main__":
    print(check(14)) # False
    print(check(16)) # True
    print(check(123)) # False
    print(check(777)) # True
    print(check(9999999)) # True