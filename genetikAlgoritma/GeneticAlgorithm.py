# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 13:33:12 2022

@author: Fettah


   fitness function:   Min (donem_basina_ort_maliyet) 
"""

import numpy as np
import random as rd
import math

class GeneticAlg:
    
    
    def __init__(self,pop_size,generation_timer,A, h, b):
        self.pop_size=pop_size
        self.fitness_of_members=[]
        self.new_population=[]
        self.success_values=[]
        self.next_generation=[]
        self.generation_timer=generation_timer
        self.elimination_limit=int(math.ceil(self.pop_size*0.1))
        self.all_result=[]
        self.A=A
        self.h=h
        self.b=b
        self.min=0
        
   
    class Member:
        def __init__(self,chromosome):
            self.chromosome=chromosome
            self.fitness=0
        
    
    def randomGene(self,min_value,max_value):
        
        self.new_values= [rd.randint(min_value,max_value) for _ in range(self.pop_size)]
        return self.new_values
        
    
    def createPopulation(self,population1,population2,):
        
        for i in range(self.pop_size):
            self.a=[rd.choices(population1)[0],rd.choices(population2)[0]]
            self.new_population.append(self.Member(self.a))
            
        return self.new_population
    
    
# =============================================================================
#     def infoGeneration(self):
#         for member,k in zip(self.new_population,range(len(self.success_values))):
#             print("\tchromosome : ",member.chromosome," |\t fitness==> ",member.fitness," |\tavarage :",self.success_values[k])
# =============================================================================
    
    def showPopulation(self,population):
        for member in population:
            print(member.chromosome)
    
    
    def calculateFitness(self):
        
        self.success_values.clear()
        self.fitness_of_members.clear()
        indexes=[]
        
       
        self.success_values=self.fitnessFunction()
        temp=self.success_values.copy()
     

        self.success_values=sorted(self.success_values,reverse=False)
        
        
        # populasyonu sıralamak için indexleri kaydediyor.
        for value in self.success_values:
            indexes.append(temp.index(value))
        
        # print("indexes : ",indexes)
        # print("_____________________________________________________________________________________")
        
        self.new_population=self.sortPopulation(indexes)
        
        # print("\n"*5,self.success_values)
        # self.showPopulation()

        # for member,k in zip(self.new_population,range(len(self.success_values))):
        #     member.fitness=0
        #     member.fitness=k
        #     self.fitness_of_members.append(k)
            
        return self.new_population
            
        
    def nextGenerations(self):
        
        print("initial population is : \n")
        self.showPopulation(self.new_population)
        num_of_generation=1
        
        while(self.generation_timer>0):
            
            
            self.next_generation.clear()
        
            print("\n"*3,num_of_generation,".generation ")    
            print("\n"*1,"#######################"*3)    
        
            self.new_population=self.calculateFitness()  
            self.next_generation=self.killWeaks(self.new_population)
            print("success values : ",self.success_values)
            
            
            while (len(self.next_generation)<self.pop_size):
                v=np.random.uniform(0,1)
                    
                if v>0.96:
                    self.next_generation.append(self.mutation())
                else:            
                    self.next_generation.append(self.crossOver())
            
            num_of_generation+=1

            
            self.new_population.clear()
            self.new_population=self.next_generation.copy()
            
            print("\n"*2)
            self.showPopulation(self.new_population)
            print("\n"*2)
            
            self.generation_timer-=1
            
        print("success values : ",self.success_values)
        print("en iyi sonuç : ",self.new_population[self.min].chromosome," ===>\t",self.all_result[self.min])
        
        #  mutasyonlar eklenecek ve jenarasyonlar yönetilecek
        
        
    def killWeaks(self,new_population):
        
        self.next_generation=new_population[:-self.elimination_limit]
        return self.next_generation

    
    
    def crossOver(self):
        
        offspring=[]
        
        temp=len(self.next_generation)*0.6
        limit=int(math.ceil(temp))
        is_append=False
        counter=0
        while not(is_append):
            new_members=[rd.choice(self.new_population[0:limit]) for i in range(2)]
            # print("new_members : ",new_members)
            # print("\nchromosomes : ",new_members[0].chromosome,"---",new_members[1].chromosome)


            if (~(new_members[0].chromosome[0]==new_members[1].chromosome[0])and ~(new_members[0].chromosome[1]==new_members[1].chromosome[1])):
                num=rd.randint(0,1)
                if (num== 0):
                    offspring.append(self.Member([new_members[0].chromosome[0],new_members[1].chromosome[1]]))
                    is_append=True
                else:
                    offspring.append(self.Member([new_members[1].chromosome[0],new_members[0].chromosome[1]]))
                    is_append=True

            elif(counter<3):
                offspring.append(self.mutation())
                
            counter+=1
     
            
        print("new choromosomes : ",offspring[0].chromosome)
        return offspring[0]


    def mutation(self):
        rand=rd.randint(0, 1)
        
        if rand==0:
            member=rd.choice(self.new_population)
            member.chromosome[0]=int(np.random.uniform(20,50))
            

        else:
            member=rd.choice(self.new_population)
            member.chromosome[1]=int(np.random.uniform(10,20))

        print("mutatated member : ",member.chromosome)

        return member


        
    def sortPopulation(self,indexes):
        temp_pop=[i for i in range(self.pop_size)]
        for index,counter in zip(indexes,range(self.pop_size)):
            temp_pop[counter]=self.new_population[index]
        
        return temp_pop
    
    
    
    def fitnessFunction(self):
        
                
        self.tum_durumlar=[]
        self.yoksatma_maliyeti=list()
        self.stok_maliyeti=list()
        self.siparis_maliyeti=list()
        self.donem_basina_ort_maliyet=list()
        self.toplam_maliyet=0
        
        self.yoksatma=[]
        self.stok=[]
        self.siparis=[]
        self.talep=[]
        donem=100000
        self.lead_time=round(np.random.normal(4, 1))
        self.population=self.new_population
        print("A=",self.A," b=",self.b," h=",self.h)
        
        for member in self.population:
        
            self.q,self.r=member.chromosome    
            print("..........................................................")
            self.stok.append(20)
            tekrar=0
            
            for k in range(donem):
                self.talep.append(round(np.random.normal(15, 2)))
                if self.talep[k]>self.stok[k]:
                    self.stok[k]=0
                    self.yoksatma.append(self.talep[k]-self.stok[k])
                    self.yoksatma_maliyeti.append(self.yoksatma[k]*self.b)
                    self.stok_maliyeti.append(0)
                else:
                    self.stok[k]-=self.talep[k]
                    self.stok_maliyeti.append(self.stok[k]*self.h)
                    self.yoksatma.append(0)
                    self.yoksatma_maliyeti.append(0)
                
                if self.r>=self.stok[k]:
                    self.siparis.append(self.q-self.stok[k])
                    self.siparis_maliyeti.append(self.A)
                    if self.lead_time==0:
                        self.stok.append(self.stok[k]+self.siparis[k])
                        self.lead_time=np.random.randint(3,6)
                    self.stok.append(0)
                    self.lead_time-=1
                else :
                    self.stok.append(self.stok[k])
                    self.siparis.append(0)
                    self.siparis_maliyeti.append(0)
            
                self.toplam_maliyet+=(self.stok_maliyeti[k]+self.yoksatma_maliyeti[k]+self.siparis_maliyeti[k])
            self.donem_basina_ort_maliyet.append(self.toplam_maliyet/(k+1))
                
            # print("Q=",q," r=",r ," icin dönem başına ort. maliyet : ",
            #       self.donem_basina_ort_maliyet[donem-1])
            
            data={"Q":self.q,
                  "r":self.r,
                  "db_ort_maliyet":self.donem_basina_ort_maliyet[tekrar],
                  "toplam_maliyet":self.toplam_maliyet}
            
            self.tum_durumlar.append(data)
            print(data)
            tekrar=tekrar+1
            
            
            self.yoksatma.clear()
            self.stok.clear()
            self.siparis.clear()
            self.talep.clear()
            
            self.yoksatma_maliyeti.clear()
            self.stok_maliyeti.clear()
            self.siparis_maliyeti.clear()
            self.donem_basina_ort_maliyet.clear()
            self.toplam_maliyet=0
    
        
        
        print("\n########################################\n")
        
        self.ortalama_maliyetler=[]
        
        for item in self.tum_durumlar:
           self.ortalama_maliyetler.append(item["db_ort_maliyet"])
        
        index=self.ortalama_maliyetler.index(min(self.ortalama_maliyetler))
        print("en düşük ortalma maliyet : \n",self.tum_durumlar[index])
             
        self.min=self.ortalama_maliyetler.index(min(self.ortalama_maliyetler))
        self.all_result = self.tum_durumlar
             
        return self.ortalama_maliyetler
 
    
    
    
    
    
    
    
    
    
    
    
