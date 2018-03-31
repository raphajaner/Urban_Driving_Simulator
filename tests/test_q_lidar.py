import json
import gym
import gym_urbandriving as uds
from gym_urbandriving import *
from gym_urbandriving.agents import *
from gym_urbandriving.assets import *
from gym_urbandriving.planning import Trajectory
import numpy as np
import IPython

with open('configs/default_config.json') as json_data_file:
    data = json.load(json_data_file)
    
data['agents']['controlled_cars'] = 2

action = [np.array([0.0,0.0])] * 2
env = uds.UrbanDrivingEnv(data)

observations,reward,done,info_dict = env.step(action)
assert(len(observations) == 2)
assert(len(observations[0]) == len(observations[1]))
state = env.current_state

assert(state.dynamic_objects['controlled_cars']['0'].vel == 0.0)

