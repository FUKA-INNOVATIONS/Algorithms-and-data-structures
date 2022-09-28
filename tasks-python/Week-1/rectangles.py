'''
Tasossa on kolme suorakulmiota, joiden sivut ovat vaaka- ja pystyakselien suuntaisia.
Tehtäväsi on laskea sen alueen pinta-ala, jota peittää vähintään yksi annetuista suorakulmioista.

Esimerkiksi seuraavassa kuvassa (kuva tehtävän sivulla) suorakulmioiden peittämän alueen pinta-ala on 16.
Kuva vastaa koodipohjissa olevaa esimerkkiä.

Voit olettaa, että kaikki koordinaatit ovat kokonaislukuja välillä −109…109.

Huomaa, että on liian hidasta käydä läpi kaikki pisteet suorakulmioiden alueelta,
vaan sinun tulee keksiä tehokkaampi matemaattinen ratkaisu.

Python

Toteuta funktio area(rec1, rec2, rec3), joka antaa kysytyn pinta-alan.
Funktiolle annetaan kolme tuplea, joista jokainen määrittelee yhden suorakulmion.
Jokaisessa tuplessa on neljä kokonaislukuax1, y1, x2 ja y2:
suorakulmion vasen ylänurkka on (x1,y1) ja oikea alanurkka on (x2,y2).
'''



def area(rec1, rec2, rec3):
    xLengthRec1 = abs(rec1[0] - rec1[2])
    yLengthRec1 = abs(rec1[1] - rec1[3])
    areaRec1 = xLengthRec1 * yLengthRec1

    xLengthRec2 = abs(rec2[0] - rec2[2])
    yLengthRec2 = abs(rec2[1] - rec2[3])
    areaRec2 = xLengthRec2 * yLengthRec2

    xLengthRec3 = abs(rec3[2] - rec3[0])
    yLengthRec3 = abs(rec3[1] - rec3[3])
    areaRec3 = xLengthRec3 * yLengthRec3

    # return ( (xLengthRec1 * yLengthRec1) + (xLengthRec1 * yLengthRec1) + (xLengthRec1 * yLengthRec1) )
    # return f'{1: x -> {xLengthRec1} y -> {yLengthRec1} area  -> {areaRec1}}'
    # return f'{xLengthRec1, yLengthRec1, areaRec1}'
    # return f'{xLengthRec2, yLengthRec2, areaRec2}'
    # return f'{xLengthRec1, yLengthRec1, areaRec1}'

    left: rec1[0]
    right: rec1[0] + rec2[0]
    top: rec1[1]
    bottom: rec1[1] + rec2[3]

    x_overlap = max(0, min(rec1.right, rect2.right) - Math.max(rect1.left, rect2.left))
    y_overlap = Math.max(0, Math.min(rect1.bottom, rect2.bottom) - Math.max(rect1.top, rect2.top))
    overlapArea = x_overlap * y_overlap


    return areaRec3

if __name__ == "__main__":
    rec1 = (-1,1,1,-1)  # 2
    rec2 = (0,3,2,0)    # 2
    rec3 = (0,2,3,-2)   # 12
    print(area(rec1,rec2,rec3)) # 16