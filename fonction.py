# fonction de cacul de combinaison


def verif(a, b) -> bool:
    if a<1 or b<1 or a<b:
        return False
    else:
        return True

def Fact(a:int):
    result= 1
    for i in range(1, a+1):
        result *= i

    return result


def Permut(nb_ele:int, num_couple:int = 1, repeat = False):
    try:
        print("Permutation: ")
        if verif(nb_ele, num_couple):
            if repeat :
                print('avec repetition')
                return pow(nb_ele, num_couple)
            else:
                print('sans repetition')
                val = Fact(nb_ele)/(Fact(nb_ele-num_couple))
                return val
        else:
            print('error (cardinal de la classe inferieur a r_permutations)')
            return False
        
    except:
        print("error")
        return False
               



def Combi(nb_ele:int, num_couple:int = 1, repeat = False):
    try:
        print("combinaison: ")
        if verif(nb_ele, num_couple):
            if nb_ele==0 or num_couple==0:
                print('error')
                return False
            else:
                if repeat :
                    print('avec repetition')
                    val = Fact(nb_ele+num_couple-1)/(Fact(num_couple)*Fact(nb_ele-1))
                    return val
                else:
                    print('sans repetition')
                    val = Fact(nb_ele)/(Fact(num_couple)*Fact(nb_ele-num_couple))
                    return val
        else:
            print('error (cardinal de la classe inferieur a r_combinaison)')
            return False
        
    except:
        print("error")
        return False



if __name__=="__main__":
    print("Test\n")
    print(Permut(2,2))

