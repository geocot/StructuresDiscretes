def pgcd(a,b, verbeux):
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

if __name__ == "__main__":
    print(pgcd(825,975, True))
