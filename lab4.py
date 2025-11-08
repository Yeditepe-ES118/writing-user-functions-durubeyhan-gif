import numpy as np
def throw_rock(m,v0,theta):
    g= 9.81 #in m/s
    tf= 2*v0* np.sin(theta*np.pi/180)/g #in second
    R= v0**2 * np.sin(2*theta* np.pi/180)/g #in meters
    hm= v0**2* (np.sin(theta* np.pi/180)**2)/(2*g)
    vh= v0* np.cos(theta*np.pi/180)
    Kh= 0.5* m* vh* hm**2 #in joule
    
    print("For a rock with %5.3f kg mass thrown with %5.3f m/s at an angle of %5.2f degrees:\nTime of flight is %10.1e s\nThe range in x-direction is %10.1e m\nMaximum height is %10.1e m\nThe speed at maximum height is %10.1e m/s\nKinetic energy at the maximum height is %8.2e J" % (m,v0,theta,tf,R, hm,vh,Kh))
    return tf, R, hm, vh,Kh
my_result= throw_rock(1.5,0.3,35.20)
