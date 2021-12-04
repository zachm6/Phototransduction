import numpy as np
import math 
import random

class PhotoTransduction():
    def __init__(self):

        # constants (value doesn't change)
        self.duration = 1000
        self.capacitance = 0.5
        self.ENa = 60   # equilibrium potential

        # numpy lists
        self.rhodopsin = np.zeros(self.duration)
        self.gProtein = np.zeros(self.duration)
        self.PDE = np.zeros(self.duration)
        self.cGMP = np.zeros(self.duration)
        self.gNa = np.zeros(self.duration)
        self.Vm = np.zeros(self.duration)

        # Taus
        self.rhodopsin_tau = 0
        self.gProtein_tau = 0
        self.PDE_tau = 0
        self.cGMP_tau = 0
        self.gNa_tau = 0

        # resting potential of rod photoreceptor
        self.Vm[0] = -40        # source: https://www.d.umn.edu/~jfitzake/Lectures/DMED/Vision/Retina/ReceptorPotential.html

    def doTimeStep(self, t, light):
        if light:
            self.rhodopsin[t] = self.rhodopsin[t-1] + 1 *(1 - self.rhodopsin[t-1])
            self.gProtein[t] = self.doActivation(self.rhodopsin[t], 2, 0, 1)
            self.PDE[t] = self.doActivation(self.rhodopsin[t], 2, 0, 1)
            self.cGMP[t] = self.doActivation(self.rhodopsin[t], 2, 0, 1)
            self.gNa[t] = self.doActivation(self.rhodopsin[t], 2, 0, 1)

    def doActivation (self, input=0, index=1, arg1=0, arg2=0):
        output = 0

        # sigmoid 
        if index == 1:
            output = np.exp(input)

        # linear     
        if index == 2:
            output = output + input
        return output