'''Project description'''

from autosklearn import *
from pymoo import *

class Automlmoo(autosklearn, pymoo):
    pass

if issubclass(Automlmoo, (autosklearn, pymoo)):
    print('Automlmoo is subclass of autosklearn and pymoo')