import math
import numpy as np
from particle import Particle

class Molecule:
    ''' A class that represents a molecule with two particles and the bond between them.'''
    def __init__(self, pos1, pos2, m1, m2, k, L0):
        self.p1 = Particle(pos1, m1)
        self.p2 = Particle(pos2, m2)
        self.k = k
        self.length = L0
        
    def get_displ(self):
        return self.p2.pos2-self.p1.pos1
    
    #def get_force()