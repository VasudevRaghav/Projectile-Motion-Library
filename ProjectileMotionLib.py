import math
import matplotlib.pyplot as graph

PI=math.pi

def HELP():
    print("Basics:")
    print("Create an object with ProjectileMotion(initialVelocity,Throw angle,gravity,time frame)")
    print("Velocity-> in m/s, Throw angle=> radians, gravity=> m/s^2, time frame=> fraction of seconds for plotting")
    print("gravity is set to 9.8 m/s^2 by default")
    print("time frame is set to 0.1 of a second by default")
    print("Methods of the object are:")
    print("1. Ux()=>gives horizontal component of velocity")
    print("2. timeOfFlight()=>gives time of flight")
    print("3. horizontalDistance(t)=>gives horizontal distance from y-axis after t seconds")
    print("4. Uy(t)=>gives vertical velocity after t seconds; if Uy() is called without any parameteres, it will give vertical component at origin")
    print("5. verticleDistance(t)=>gives vertical distance from x-axis after t seconds")
    print("6. maxHeight()=>gives maximum height achieved by body during its trijectory")
    print("7. range()=>gives range of the body, i.e, first touch on x-axis after throw")
    print("8. plot()=>plot the trijectory of body from t=0 to t=timeOfFlight()")
    
class ProjectileMotion:
    #This initializes the body in motion with some initial velocity, angle of throw, gravity, and time frame for graph plot
    def __init__(self,initialVelocity:float,angleOfThrow:float,g=9.8,timeFrame=0.1):
        self.u=initialVelocity
        self.ō=angleOfThrow
        self.g=g
        self.timeFrame=timeFrame
    
    #This function returns horizontal component of body in motion
    def Ux(self):
        return self.u*math.cos(self.ō)
    
    #This funcion returns Time of Flight of the body in motion from the point of throw to 1st hit on the ground
    def timeOfFlight(self):
        return 2*self.u*math.sin(self.ō)/self.g
    
    #This function return horizontal distance of the body in motion at a certain time frame assuming t=0 at throw
    def horizontalDistance(self,t):
        if(t<self.timeOfFlight() or t>=0):
            return self.Ux()*t
        else:
            print("Time",t,"is not within time of flight, i.e,0-",self.timeOfFlight())
    
    #This function returns vertical component of velocity at the given time, which will vary as the gravity is in effect
    def Uy(self,t=0.0):
        if(t<self.timeOfFlight() or t>=0):
            return self.u*math.sin(self.ō)-self.g*t
        else:
            print("Time",t,"is not within time of flight, i.e,0-",self.timeOfFlight())
    
    #This function returns vertical distance of the body in motion at a certain time frame assuming t=0 at throw
    def verticalDistance(self,t):
        if(t<self.timeOfFlight() or t>=0):
            return self.Uy()*t-0.5*self.g*t*t
        else:
            print("Time",t,"is not within time of flight, i.e,0-",self.timeOfFlight())
    
    #This function returns maximum height achieved by the body in motion throughout the journey
    def maxHeight(self):
        return (self.Uy()**2)/(2*self.g)
    
    #This function returns maximum horizontal distance traveresed by the body in motion from t=0 at throw to time of flight 
    def range(self):
        return 2*self.Ux()*self.Uy()/self.g
    
    #This function plots the graph by creating temparory x,y co-ordinates for the given time frame slice during initialization
    def plot(self):
        x,y=[],[]
        landingTime=self.timeOfFlight()
        i=0
        while i<landingTime:
            x.append(self.horizontalDistance(i))
            y.append(self.verticalDistance(i))
            i+=self.timeFrame
        x.append(self.range())
        y.append(0)
        setting=graph.figure()
        viewRatio=self.range()/self.maxHeight()
        setting.set_figwidth(math.floor(2*viewRatio)+1)
        setting.set_figheight(math.floor(viewRatio)+1)
        graph.scatter(x,y,s=2,cmap='brg')
        
        print("From T->",0,"s to T->",landingTime,"s")
        print("Range:",self.range(),"m")
        print("Max Height:",self.maxHeight(),"m")
        print("Time of Flight:",self.timeOfFlight(),"s")