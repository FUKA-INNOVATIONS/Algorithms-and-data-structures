'''
Seuraava pseudokoodi esittää funktion count, joka laskee summan 1+2+⋯+n.

    function count(n)
        total = 0
        for i = 1 to n
            total += i
        return total

Toteuta pseudokoodia vastaava funktio Pythonilla tai Javalla.
'''



def count(n):
    total = 0
    for i in range(n+1):
        total += i
    return total

if __name__ == "__main__":
    print(count(1)) # 1
    print(count(2)) # 3
    print(count(3)) # 6
    print(count(10)) # 55
    print(count(123)) # 7626