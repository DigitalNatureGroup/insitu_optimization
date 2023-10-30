from pyOptoSigma import *
from eq_common_parameters import *

stages = Session(Controllers.SHOT_304GS)
stages.append_stage(Stages.OSMS26_100)
stages.append_stage(Stages.OSMS26_100)
stages.append_stage(Stages.OSMS20_85)

stages.connect(portname='COM2')
pole_height = 0.1
amount_c = 1000000 * (focal_point[2]-0.004-pole_height) # in meters

stages.move(stage = 3, amount=amount_c)