def pcontrol(error,perror,integral,kp,ki,kd,dt):
    integral+=error*dt
    derivative=error-perror/dt
    input=kp*errror+ki*integral+kd*derivative
    return input,integral
def sysCall_init():
    sim = require('sim')

    # do some initialization here
    # This function will be executed once when the simulation starts
    
    # Instead of using globals, you can do e.g.:
    # self.myVariable = 21000000
    self.Ljoint=sim.getObject('/left_joint')
    self.Rjoint=sim.getObject('/right_joint')
    self.dangle=0
    self.integralL=0
    self.integralR=0
    self.perrorL=0
    self.perrorR=0
    ######## ADD YOUR CODE HERE #######
    # Hint: Initialize the scene objects which you will require
    #       Initialize algorithm related variables here
    
    ##################################
    
def sysCall_actuation():
    # put your actuation code here
    # This function will be executed at each simulation time step

    ####### ADD YOUR CODE HERE ######
    # Hint: Use the error feedback and apply control algorithm here
    #       Provide the resulting actuation as input to the actuator joint
    cangleL=sim.getJointPosition(self.Ljoint)
    cangleR=sim.getJointPosition(self.Rjoint)
    errorL=self.dangle-cangleL
    errorR=self.dangle-cangleR
    dt=sim.getSimulationTimeStep()
    inputL,self.integralL=pcontrol(errorL,self.perrorL,self.integralL,kp=1,ki=1,kd=1,dt=dt)
    inputR,self.integralR=pcontrol(errorR,self.perrorR,self.integralR,kp=1,ki=1,kd=1,dt=dt)
    self.perrorL=errorL
    self.perrorR=errorR
    sim.setJointTargetVelocity(self.Ljoint,inputL)
    sim.setJointTargetVelocity(self.Rjoint,inputR)
