from cobra import Reaction,Metabolite, Model
import cobra
model=Model('first_model')

#reactions#

​v0.name='v0'
v0.lower_bound=1
v0.upper_bound=1

v1=Reaction('v1')
v1.name='v1'
v1.lower_bound=0
v1.upper_bound=1000

v2=Reaction('v2')
v2.name='v2'
v2.lower_bound=0
v2.upper_bound=1000

v3=Reaction('v3')
v3.name='v3'
v3.lower_bound=.9
v3.upper_bound=.9


v4=Reaction('v4')
v4.name='v4'
v4.lower_bound=0
v4.upper_bound=1000

M=Reaction('M')
M.name='M'
M.lower_bound=0
M.upper_bound=1000
v0=Reaction('v0')


#metobolites#

A=Metabolite('A',compartment='c')
B=Metabolite('B',compartment='c')
C=Metabolite('C',compartment='c')
ATP=Metabolite('ATP',compartment='c')

#combine reactions and metabolites#

################ V1 : A======>B #################
v1.add_metabolites({A:-1,B:1})
​
################ V2 : B======>C #################
v2.add_metabolites({B:-1,C:1})
​
################ V0 : ======>A #################
v0.add_metabolites({A:1})
​
################ M : C======> #################
M.add_metabolites({C:-1})
​
​
################ v3 : A======>ATP #################
v3.add_metabolites({A:-1,ATP:1})
​
################ v4 : ATP======> #################
v4.add_metabolites({ATP:-1})

#combine reactions with the model#

model.add_reactions([v0,v1,v2,v3,v4,M])

#objective

model.objective='M'
model.optimize()

model.summary()
