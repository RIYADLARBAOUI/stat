# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 
import matplotlib.pyplot as plt

examen_effectif = [14.5,17,8,6,9,12,11,15,8,11,7.5,14.5,6,17,7.5,9,15,14,12,9]
second_examen_effectif = [14.5,16,11,3,12,13,12,15,6,11,7.5,14.5,3,16,7.5,10,15,14,12,10]



#def frequence(list):
     #   frequence =[]
     #   for element in effectif:
    #       frequence.append(element/len(list)
   #     return frequence                  
    
    
    
print("modalite,effectif:",np.unique(examen_effectif,return_counts=True))
print("frequence:")


print("moyenne:",np.mean(examen_effectif))
print("ecart_type:",np.std(examen_effectif))
print("median:",np.median(examen_effectif))
print("quantile1:",np.quantile(examen_effectif,0.25))
print("quantile2:",np.quantile(examen_effectif,0.75))

#plt.boxplot([examen_effectif,second_examen_effectif],whis=[0,100],vert=False)
#plt.show()

#Exercice 2 

effectif_exo2 = ['A','B','B','C','B','A','A','B','B','A','B','B','A','A','C','C','B','B','C','B']

print("modalité,effectif:",np.unique(effectif_exo2,return_counts=True))

tuple=np.unique(effectif_exo2,return_counts=True)
plt.pie(tuple[1],labels=tuple[0],autopct=lambda z : str(round(z,2)),pctdistance=0.7,
        labeldistance=1.2,
        normalize=True)

plt.close()

plt.bar(tuple[0],color="red",align="center",width=0.8,height=tuple[1])

plt.close()

effectif_exo=[A,A,A,C,A,B,B,B,A,C,A,C,C,B,C,A,C,A,C,A]