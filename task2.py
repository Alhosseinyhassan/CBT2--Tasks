import cobra
from cobra import Reaction,Metabolite,Model
model_a
#model
model_a=Model('model_a')
#reactions 
##=======>metabolite
v0=Reaction('v0')
v0.name="v0"
v0.lower_bound=1
v0.upper_bound=1
v1=Reaction('v1')
v1.name="v1"
v1.lower_bound=0
v1.upper_bound=1000
​
v2=Reaction('v2')
v2.name="v2"
v2.lower_bound=0
v2.upper_bound=1000
​
m=Reaction('m')
m.name="m"
m.lower_bound=0
m.upper_bound=1000
​
biomass
glc=Metabolite('glc',compartment='c')
AA=Metabolite('AA',compartment='c')
biomass=Metabolite('biomass',compartment='c')
#add metabolites to reactions Vs
v0.add_metabolites({glc:1})
v1.add_metabolites({glc:-1,AA:1})
v2.add_metabolites({AA:-9.09,biomass:1})
m.add_metabolites({biomass:-1})
a
model_a.add_reactions([v0,v1,v2,m])
​
=
model_a.objective=('m')
_a
model_a.optimize()
Optimal solution with objective value 0.110
fluxes	reduced_costs
v0	1.000000	0.220022
v1	1.000000	0.000000
v2	0.110011	0.000000
m	0.110011	0.000000
