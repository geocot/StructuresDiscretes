#Fait par Martin Couture
#Source: https://github.com/geocot/StructuresDiscretes

def pgcdSoustraction(a,b, verbeux):
    if verbeux:
        print("a = {}, b ={}".format(a,b))
    while a!=b:
        if a>b:
            if verbeux:
                 print("a > b, donc a ={}-{} = {}".format(a,b,a-b))
            a = a-b
        else:
            if verbeux:
                print("b > a, donc b ={}-{} = {}".format(b, a, b-a))
            b = b-a
    if verbeux:
        print("a est maintenant égal à b, soit {}".format(a))
        print("Le pgcd est {}".format(a))
    return a


def pgcdMod(a,b,verbeux):
    if b != 0:
        if verbeux:
            print("pgcd({}, {} mod {})".format(b,a,b))
        return pgcdMod(b, a % b, verbeux)
    else:
        print("pgcd({}, {} mod {})".format(b, a, b))
        print("Donc le pgcd est {}".format(a))
        return a

if __name__ == "__main__":
    print(pgcdSoustraction(120,80, False))
    print(pgcdMod(120, 80, True))
