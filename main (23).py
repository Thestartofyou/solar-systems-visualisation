
import matplotlib.pyplot as plt
import numpy as np

# Define the properties of the planets
# The data is taken from NASA's Solar System Exploration website
# https://solarsystem.nasa.gov/
planet_data = [
    # planet_name, semimajor_axis, eccentricity, period
    ("Mercury", 0.3871, 0.2056, 0.241),
    ("Venus", 0.7233, 0.0067, 0.615),
    ("Earth", 1.0000, 0.0167, 1.000),
    ("Mars", 1.5237, 0.0934, 1.881),
    ("Jupiter", 5.2028, 0.0483, 11.86),
    ("Saturn", 9.5388, 0.0542, 29.46),
    ("Uranus", 19.1914, 0.0472, 84.01),
    ("Neptune", 30.0611, 0.0086, 164.8),
]

# Define the time range for the simulation
t = np.linspace(0, 2*np.pi, 1000)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Plot the orbits of the planets
for planet_name, semimajor_axis, eccentricity, period in planet_data:
    # Calculate the radius of the orbit
    r = semimajor_axis*(1 - eccentricity**2)/(1 + eccentricity*np.cos(t))
    
    # Calculate the x and y coordinates of the orbit
    x = r*np.cos(t)
    y = r*np.sin(t)
    
    # Plot the orbit
    ax.plot(x, y, label=planet_name)

# Add a legend and title
ax.legend()
ax.set_title("Solar System")

# Set the aspect ratio to 1:1 and show the plot
ax.set_aspect("equal")
plt.show()
