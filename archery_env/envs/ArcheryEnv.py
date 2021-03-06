import gym
from gym import spaces
import math
import random
import numpy as np
from archery_env.envs.visualizer import Viewer

time = 0.01
gravity = -9.81

class ArcheryEnv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

    # velocity is the velocity of the arrow
    # angle is the initial angle of the arrow
    # target_y is the height of the target
    # viewer is the turtle simulation

  def __init__(self):
    super(ArcheryEnv, self).__init__()

    self.viewer = None

    # used for spaces
    self.max_angle = 90.
    self.min_angle = 0.
    self.max_speed = 70.
    self.min_speed = 0.
    self.min_target_x = 0.
    self.max_target_x = 600. # arbitrary

    self.T = 10.
    self.runtime = 0.

    self.winnableDist = 5.

    self.action_space = spaces.Box(
        low = np.array([self.min_angle, self.min_speed]),
        high = np.array([self.max_angle, self.max_speed]),
        dtype = np.float32
    )

    self.observation_space = spaces.Box(
        low = np.array([self.min_target_x,-1.]),
        high = np.array([self.max_target_x,1.]),
        dtype = np.float32
    )
    self.reset()

  def step(self, action):
    done = False
    # Execute one time step within the environment
    # their action: power and angle
    angle,velocity = action

    self.state = (angle)

    finalLocation, vertical_dist = self.calcArrowLocation(velocity, angle, self.wind_vel)
    self.horizontal_dist = finalLocation
    self.vertical_dist = vertical_dist

    if abs(finalLocation - self.target_x) < self.winnableDist:
        done = True
    # returns ( wind dir)
    # you chooose power and angle

    obs = self._get_obs()
    
    self.wind_vel = random.randint(-5, 5)
    
    if self.runtime > self.T:
      done = True
      
    self.runtime +=1
    
    return obs, self._get_reward(), done, {}

  def calcArrowLocation(self, velocity, angle, windDir):
    self.velocity = velocity
    self.angle = angle

    wind = windDir * time
    horizontal_vel = velocity * math.cos(angle * math.pi / 180)
    vertical_vel = velocity * math.sin(angle * math.pi / 180)
    horizontal_dist = 0
    vertical_dist = 0

    while((vertical_dist>= self.target_y) or (vertical_vel>0)):
        horizontal_dist = horizontal_vel * time + horizontal_dist
        vertical_dist = vertical_vel * time + vertical_dist
        vertical_vel = vertical_vel + gravity * time
        horizontal_vel = horizontal_vel + wind

    return horizontal_dist, vertical_dist

  def _get_obs(self):
    euclidean_target = math.sqrt((self.target_x - self.horizontal_dist)**2 + (self.target_y - self.vertical_dist)**2)

    wind = 0
    if(self.wind_vel > 0):
        wind = 1.
    else:
        wind = -1.

    return np.array([euclidean_target, wind])

  def _get_reward(self):
    return -math.sqrt((self.target_x - self.horizontal_dist)**2 + (self.target_y - self.vertical_dist)**2)/600

  def reset(self):
    # Reset the state of the environment to an initial state
    self.target_x = random.uniform(5,235)
    self.target_y = random.uniform(5, 235)
    self.velocity = 0
    self.angle = 0
    self.horizontal_dist =0
    self.vertical_dist =0
    self.wind_vel = random.uniform(-5,5)
    self.runtime = 0
    self.close()
    return self._get_obs()

  def close(self):
    if self.viewer:
        self.viewer.clear()
        self.viewer = None
      
  def render(self, mode='human', close=False):
    if not close:
        if self.viewer is None:
            self.viewer = Viewer()
        self.viewer.move(self.velocity, self.target_y, self.angle, self.wind_vel)
