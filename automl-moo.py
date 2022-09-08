'''Project description'''

from pymoo.core.problem import Problem
from autosklearn.regression import AutoSklearnRegressor

class AutoMlMoo(Problem, AutoSklearnRegressor):
    pass

if issubclass(AutoMlMoo, (Problem, AutoSklearnRegressor)):
    print('AutoMlMoo is subclass of Problem and AutoSklearnRegressor')