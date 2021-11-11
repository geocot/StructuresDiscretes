#Fait par Martin Couture
#Source: https://github.com/geocot/StructuresDiscretes
import  pgcd

def ppcm(a,b):
    print("**Calcul du pgcd**")
    pgcd_resultat = pgcd.pgcdMod(a,b,True)
    print("**Calcul du ppcm**")
    print("a x b = {}".format(a*b))
    print("{}/{}".format(a*b, pgcd_resultat))
    return (a*b)/pgcd_resultat


if __name__ == "__main__":
    print("Le ppcm est {}".format(int(ppcm(120,240))))