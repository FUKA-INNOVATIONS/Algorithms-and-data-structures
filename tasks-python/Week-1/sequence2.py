'''
Lukujonon jokainen alkio on pienin positiivinen kokonaisluku,
jota ei ole vielä esiintynyt lukujonossa ja jossa on yksi tai useampi toistuva numero.

Lukujono alkaa näin:
11,22,33,44,55,66,77,88,99,100,101,110,111,112,113,114,…

Tehtäväsi on etsiä lukujonon kohdassa n oleva luku. Voit olettaa, että n on enintään 1000.
'''

def generate(n):
    sequence = []

    # outerLoops = 0
    # innerLoops = 0

    for i in range( 11, 3000 ):

        if (len(sequence) - 1 == n):
            # print(f'seeking index: {n}, outer loops total: {outerLoops}, inner loops total: {innerLoops}')
            return int( sequence[n-1] )

        # outerLoops += 1

        if (len( sequence ) > 999):
            break
        elif (len( sequence ) < 999):
            i = str(i)
            for d in i:
                # innerLoops += 1
                if ( i.count(d) > 1 ) and not ( len(sequence) > 1000 ):
                    sequence.append( i )
                    break

    # print(f'seeking index: {n}, outer loops total: {outerLoops}, inner loops total: {innerLoops}')
    # print(len(f'removed: {sequenceNotIncluded}'))
    # return int( sequence[n-1] )


if __name__ == "__main__":
    print(generate(1)) # 11
    print(generate(2)) # 22
    print(generate(3)) # 33
    print(generate(10)) # 100
    print(generate(123)) # 505
