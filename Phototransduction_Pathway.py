import numpy as np
import math 
import random

class Synapse():
    def __init__(self):
        self.duration = 1000

        # phototransduction varaibles
        self.Vm = np.zeros(self.duration)
        self.ELeak = -70      # all voltages are in mV
        self.rhodopsin = 0 
        self.g_alpha = 0
        self.pde = 0
        self.cGMP = 0
        self.Nacurrent = 0.1

        # set initial values
        self.Vm[0] = self.ELeak        # this will be useful later

    # Light is a boolean type
    # index is a integer value that specifies mathematical relationship; ex: sigmoidal, linear
    # Return value is a integer that represents the amount of activated rhodopsin 
    def ActivateRhodopsin(self, light, index):

        # linear relationship 
        if index == 0:
            pass 
        # sigmoidal relationship
        elif index == 1:
            pass

        return self.rhodopsin
    
    def ActivateGprotein(self, rhodopsin, index):

        # linear relationship 
        if index == 0:
            pass
        # sigmoidal relationship
        elif index == 1:
            pass

        return self.g_alpha
    
    def ActivatePde(self, g_alpha, index):
        
        # linear relationship 
        if index == 0:
            pass
        # sigmoidal relationship
        elif index == 1:
            pass

        return self.pde

    def MetabolizecGMP(self, pde, index):
        
        # linear relationship 
        if index == 0:
            pass
        # sigmoidal relationship
        elif index == 1:
            pass

        return self.cGMP

    def VoltageRecording(self, cGMP, t, index):
        
        # relate cGMP to NaCurrent
        # linear relationship 
        if index == 0:
            pass
        # sigmoidal relationship
        elif index == 1:
            pass

        return self.Vm[t]
