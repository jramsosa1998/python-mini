#Particle_sim_mult.py

#Dictionary of initial particles
particles = {
    "electron": {"mass": 9.11e-31, "velocity": 2e6},
    "proton"  : {"mass": 1.67e-27, "velocity": 1e5},
}

#Function to calculate KE
def kinetic_energy(mass,velocity):
    """Return kinetic energy in joules"""
    return 0.5 * mass * velocity ** 2

#Calculate KE for existing particles
for name, props in particles.items():
    props["kinetic_energy"] = kinetic_energy(props["mass"], props["velocity"])

#Interactive addition of particles
while True:
    add_more = input("Add a new particle? (y/n): ").lower()
    if add_more != 'y':
        break

    name = input("Enter particle name: ")
    mass = float(input(f"Enter mass of {name} in kg: "))
    velocity = float(input(f"Enter velocity of {name} in m/s: "))

    particles[name] = {"mass": mass, "velocity": velocity}
    particles[name]["kinetic_energy"] = kinetic_energy(mass,velocity)

#Print all particle info
print("\nAll particles with kinetic energy: ")
for name, props in particles.items():
    print(f"{name}: {props}")

#calculate total KE
total_ke = sum(props["kinetic_energy"] for props in particles.values())
print(f"\nTotal kinetic energy of all particles: {total_ke:.2e} J") 

#Save particles to file

with open("particles.txt", "w") as file:
    for name, props in particles.items():
        line = f"{name},{props['mass']}, {props['velocity']}, {props['kinetic_energy']}\n"
    file.write(line)

print("\nParticles saved to particle.txt")

#Load particles from file 

loaded_particles = {}

with open("particles.txt", "r") as file:
    for line in file: 
        name, mass, velocity, ke = line.strip().split(",")

        loaded_particles[name] = {
        "mass": float(mass),
        "velocity": float(velocity),
        "kinetic_energy": float(ke)
        }

print("\nLoaded particles from file:")
for name, props in loaded_particles.items():
    print(f"{name},{props}")
