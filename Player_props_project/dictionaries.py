# A mapping between keys -> values
# Physics Analogy: like a configuration block
# Label -> data     mass = 2. 0
# Parameter -> value   velocity = 3.5 
# Name -> property     time_step = 0.01
# In python, this is one OBJECT

particle = {
    "mass": 2.0,        #Groups related data
    "velocity": 3.5,    #Each key is a label
    "charge": -1        #Values can be any type
}

particle["velocity"] = 4.2        #Dictionaries are mutable 
particle["energy"] = 11.9   #you can update state (simulation state)

for key, value in particle.items():
    print(key, ":", value)

#Physics formula KE= 1/2mv^2

particle = {
    "mass": 2.0,
    "velocity": 3.5
}

kinetic_energy = 0.5 * particle["mass"] * particle["velocity"] ** 2
particle["kinetic_energy"] = kinetic_energy 

for key, value in particle.items():
    print(f"({key}: {value}")
