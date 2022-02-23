from math import *
#Exercice 1.1

def average(Tab):
    sum=0
    for element in Tab:
        sum+=element
    return sum/len(Tab)

#Exercice 1.2

def variance(Tab):
    variance=0
    for element in Tab:
        variance+=(element)**2
    return ((variance/(len(Tab)))-(average(Tab))**2)

def ecart_type(Tab):
    return (variance(Tab))**(1/2)

#Exercice 2.1

def mediane(Tab):
    Tab.sort()
    if(len(Tab)%2==1): # si taille du tableau est impair
        return  Tab[len(Tab)//2] # on prend l'element à la moitié du tableau
    else:
        return (Tab[(((len(Tab) // 2) -1))] + Tab[len(Tab)//2])/2 # sinon on calcule la médiane
    
#exercice 2.2

def sous_serie_statistique(Tab):
    Tab1=[]
    Tab2=[]
    Tab.sort()
    if(len(Tab)%2==1): # si taille du tableau est impair
        for i in range(0,(len(Tab)//2)): # sous ensemble 1
            Tab1.append(Tab[i])
        for j in range(len(Tab)//2+1 ,len(Tab)): #sous ensemble 2 (+1 car tableau impair pour passer la valeur médiane)
            Tab2.append(Tab[j])
        return mediane(Tab),Tab1,Tab2
    else:
        for i in range (0,len(Tab)//2):
                Tab1.append(Tab[i])
        for j in range(len(Tab)//2,len(Tab)):
            Tab2.append(Tab[j])
        return mediane(Tab), Tab1, Tab2
        
        
 
 
#exercice 2.3

def quartiles_serie_statistique(Tab):
    Tab1=[]
    Tab2=[]
    Tab.sort()
    if(len(Tab)%2==1):
        for i in range(0,(len(Tab)//2)):
            Tab1.append(Tab[i])
        for j in range(len(Tab)//2 +1 ,len(Tab)):
            Tab2.append(Tab[j])
        return mediane(Tab), mediane(Tab1), mediane(Tab2)
    else:
        for i in range (0,len(Tab)//2):
                Tab1.append(Tab[i])
        for j in range(len(Tab)//2,len(Tab)):
            Tab2.append(Tab[j])
        return mediane(Tab), mediane(Tab1), mediane(Tab2)

 



#Exercice 3.1


def max(Tab):
    max=Tab[0]
    for element in Tab:
        if(max<=element):
            max=element
    return max


#Exercice 3.2


def modalité_effectif(Tab):
    Tab.sort()
    M=[]
    e=[]
    for element in Tab:
        M.append(element)
        if(M.count(element)>1): # si il y a un doublon on le supprime
            M.remove(element)
        else:
            e.append(Tab.count(element)) #sinon on compte son nombre d'apparation dans le tableau global
    return M,e

#Exercice 3.3
#frequence = effectif/nombre d'element
def serie_statistique_tabStatistique(Tab):
    Tab.sort()
    frequence=[]
    effectif_cumule = []
    frequence_cumule = []
    effectif_cumule_stock=modalité_effectif(Tab)[1][0]
    effectif_cumule.append(modalité_effectif(Tab)[1][0])
    modalité_effectif(Tab)
    for element in modalité_effectif(Tab)[1]:
        frequence.append(element/len(Tab))
    frequence_cumule_stock = frequence[0]
    frequence_cumule.append(frequence[0])
    for i in range(1,len(frequence)):
        frequence_cumule_stock+=frequence[i]
        frequence_cumule.append(frequence_cumule_stock)
        effectif_cumule_stock+=modalité_effectif(Tab)[1][i]
        effectif_cumule.append(effectif_cumule_stock)
    return modalité_effectif(Tab)[0],modalité_effectif(Tab)[1],frequence,effectif_cumule,frequence_cumule # bug frequence cumule car total != 1

#Exercice 3.4


def mode(Tab):
    mode=[]
    mode.append(modalité_effectif(Tab)[0][Tab.index(max(modalité_effectif(Tab)[1]))]) # on retourne un des modes
    return mode


#Exercice 3.5

def trouver_indices_maximums(Tab):
    max_reference = max(Tab)  # defini le maximum de la liste
    indice_maximums = []
    indice_maximums.append(Tab.index(max(Tab)))
    Tab.remove(max(Tab))
    cpt=1  #on a supprimer un element

    for element in Tab:
        if (element == max_reference):
            indice_maximums.append(Tab.index(max(Tab))+cpt) # +cpt car la taille du tableau est réduite car on enleve à chaque fois le maximum
            Tab.remove(max(Tab))
            cpt+=1                  # plus on enleve d'element plus cpt doit prendre +1 pour compenser la taille réduite
    return indice_maximums

def modes(Tab):
    modes=[]
    for element in (trouver_indices_maximums(modalité_effectif(Tab)[1])):# indice maximum du 2nd élement du tuple (tableau des effectifs)
        modes.append(modalité_effectif(Tab)[0][element]) #on veut les elements avec les plus présent
    return modes






Tableau=[0,0,2,3,3,5,6]
print(average(Tableau))
print(variance(Tableau))   
print(ecart_type(Tableau))
print(mediane(Tableau))
print(sous_serie_statistique(Tableau))
print(quartiles_serie_statistique(Tableau))
print(max(Tableau))
print(modalité_effectif(Tableau))
print(serie_statistique_tabStatistique(Tableau))
print(mode(Tableau))
print(modes(Tableau))
