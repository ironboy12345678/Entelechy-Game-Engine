class PlatformerGravity(): #All the functions for gravity in platformers.
    def __init__(self, mass1,
                 mass2, radius):
        self.m1 = mass1
        self.m2 = mass2
        self.r = radius
    
    def grav_force(self): 
        return (6.674*(10**-11))*(self.m1*self.m2)/(self.r**2)
    
    def free_fall(self, time, init_vel):
        return init_vel + (self.grav_force()/self.m1) * time

if __name__ == '__main__':
    for i in range(250):
        print PlatformerGravity(80, 5.97219*10**24, 6371000).free_fall(i/5.0, -40)
