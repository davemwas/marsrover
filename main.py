from rover import Rover
from plateau import Plateau

plateau_ = Plateau(5, 5)
rov = Rover(plateau_, [1, 2], 'N')
print(rov.process('LMLMLMLMM'))
rov.update_position([3, 3], 'E')
print(rov.process('MMRMMRMRRM'))
