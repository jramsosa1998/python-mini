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
