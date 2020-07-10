# test agent

import gym
import archery_competition
env = gym.make('ArcheryEnv') # call our env
env.reset()

for _ in range(1000):
    observation = env.reset()
    env.render()
    # print observation
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
    
env.close()

