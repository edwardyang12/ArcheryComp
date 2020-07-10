# test agent
import random
import gym
from ArcheryEnv import ArcheryEnv

y_height = random.uniform(0,10)
distance = random.uniform(0,240)
archery = ArcheryEnv(y_height, distance)
archery.reset()

for _ in range(1000):
    observation = archery.reset()
    archery.render()
    # print observation
    action = archery.action_space.sample()
    observation, reward, done, info = archery.step((action[0], action[1]))
    if done:
        break

archery.close()
