# -*- coding: utf-8 -*-
"""

STOK YÖNETİMİ SİMÜLASYONU

@author : Muhammet Fettah Koral
"""

import random as rd
import GeneticAlgorithm 






   

# TEST{'Q': 49, 'r': 11, 'db_ort_maliyet': 66.89435666666667, 'toplam_maliyet': 20068307}
######################################################{'Q': 48, 'r': 11, 'db_ort_maliyet': 66.97505666666666, 'toplam_maliyet': 20092517}

b=4
h=1
A=30

ga=GeneticAlgorithm.GeneticAlg(30,6,A,h,b)
q=ga.randomGene(20,50)
r=ga.randomGene(10,20)

population=ga.createPopulation(q,r)


ga.nextGenerations()


######################################################

# initial population generated ++







