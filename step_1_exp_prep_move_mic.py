from pyOptoSigma import *
from common_parameters import *

stages = Session(Controllers.SHOT_304GS)
stages.append_stage(Stages.OSMS26_100)
stages.append_stage(Stages.OSMS26_100)
stages.append_stage(Stages.OSMS20_85)

stages.connect(portname='COM2')
amount_c = 1000000 * (focal_point[2]) # in meters

stages.move(stage = 3, amount=amount_c)