from fonction import Combi, Permut

#-----------------------------------------------------
#permutation avec repetition
def resort_permutrep(ensemble:list):
    result = []
    for i in range(len(ensemble)):
        for j in range(len(ensemble)):
            result.append((ensemble[i],ensemble[j]))
    
    return result
#-----------------------------------------------------
#permutation sans repetition
#-----------------------------------------------------
def resort_permut(ensemble:list):
    result = []
    for i in range(len(ensemble)):
        for j in range(len(ensemble)):
            if ensemble[i]!=ensemble[j]:
                result.append((ensemble[i],ensemble[j]))
    return result
#-----------------------------------------------------
#combinaison avec repetition
#-----------------------------------------------------
def resort_combirep(ensemble: list):
    result = []
    for i in range(len(ensemble)):
        for j in range(i, len(ensemble)):
            result.append((ensemble[i],ensemble[j]))
    return result
#-----------------------------------------------------
#combinaison sans repetition
#-----------------------------------------------------
def resort_combi(ensemble: list):
    result = []
    for i in range(len(ensemble)):
        for j in range(i, len(ensemble)):
            if ensemble[i]!=ensemble[j]:
                result.append((ensemble[i],ensemble[j]))
    return result
#-----------------------------------------------------
def Nuplet(s:list, n_uplet:int):
    card = len(s)
    print(card)
#-----------------------------------------------------



ensemble = [1,2,3]

print(f'votre ensemble est: {ensemble}')

cardinal = len(ensemble)
