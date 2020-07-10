# test agent

import gym
import archery_competition
env = gym.make('ArcheryEnv') # call our env
env.reset()

for _ in range(1000):
    env.render()
    # print observation
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    
env.close()

