import numpy as np

def throw_rock(m, v0, theta):
    g = 9.81
    theta = np.radians(theta)

    tf = 2 * v0 * np.sin(theta) / g
    R = v0 ** 2 * np.sin(2 * theta) / g
    hm = v0 ** 2 * np.sin(theta) ** 2 / (2 * g)
    v = v0 * np.cos(theta)
    KE = 0.5 * m * v ** 2

    print(f"For a rock with {m:.3f} kg mass thrown with {v0:.3f} m/s at an angle of  {np.degrees(theta):.2f} degrees:")
    print(f"Time of flight is    {tf:.1e} s")
    print(f"The range in x-direction is    {R:.1e} m")
    print(f"Maximum height is    {hm:.1e} m")
    print(f"The speed at maximum height is    {v:.1e} m/s")
    print(f"Kinetic energy at the maximum height is {KE:.2e} J")
    
