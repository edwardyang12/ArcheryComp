# test agent
import random
import gym
import archery_env

env = gym.make('archerycomp-v1')


for t in range(1000):

    env.reset()
    # print observation
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    env.render()
    print(reward)
    if done:
        print("Episode finished after {} timesteps".format(t+1))
        break
    
