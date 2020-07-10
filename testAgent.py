# test agent
import random
import gym
from ArcheryEnv import ArcheryEnv

y_height = random.uniform(0,10)
distance = random.uniform(0,240)
archery = ArcheryEnv(y_height, distance)
archery.reset()

for _ in range(1000):
<<<<<<< HEAD
    observation = archery.reset()
    archery.render()
    # print observation
    action = archery.action_space.sample()
    observation, reward, done, info = archery.step((action[0], action[1]))
    if done:
        break
=======
    observation = env.reset()
    env.render()
    # print observation
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
    
env.close()
>>>>>>> 7deb445392f113523bb53cfa72f8bbfc19c3d32a

archery.close()
