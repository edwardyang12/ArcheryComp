import gym
from gym import spaces
import math
import random
time = 0.01
gravity = -9.81

class ArcheryEnv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}


    # velocity is the velocity of the arrow
    # angle is the initial angle of the arrow
    # final_y is the height of the target
    # viewer is the turtle simulation
  def __init__(self, final_y):
    super(CustomEnv, self).__init__()
    self.target_x = -1
    self.target_y = target_y
    self.winnableRange = 5 # angle within 5 meters
    self.viewer = None

    # used for spaces
    self.max_angle = 90
    self.min_angle = 0
    self.max_speed = 70
    self.min_speed = 0
    self.min_distance = 0
    self.max_distance = 500 # arbitrary

    self.winnableDist = 5

    self.velocity = 0
    self.angle = 0
    self.horizontal_dist =0
    self.vertical_dist =0

    self.distance = random.uniform(0,240)
    self.wind_vel = random.uniform(-5,5)

    self.action_space = spaces.Box(
        low = np.array([self.min_angle, self.min_speed]),
        high = np.array([self.max_angle, self.max_speed]),
        dtype = np.float32
    )

    self.observation_space = spaces.Box(
        low = np.array([self.min_distance]),
        high = np.array([self.max_distance]),
        dtype = np.float32
    )

  def step(self, action):
    # Execute one time step within the environment
    # their action: power and angle
    
    power, angle = self.action

    self.state = (angle)

    finalLocation, vertical_dist = calcArrowLocation(velocity, angle, self.wind_vel)
    self.horizontal_dist = finalLocation
    self.vertical_dist = vertical_dist

    done = bool()
    if (finalLocation - self.distance) <self.winnableDist:
        done = True
    # returns ( wind dir)
    # you chooose power and angle
    self.wind = random.randint(-5, 5)
    return self._get_obs(), self._get_reward(), done, {}

  def calcArrowLocation(velocity, angle, windDir):
    self.velocity = velocity
    self.angle = angle

    wind = windDir * time
    horizontal_vel = velocity * math.cos(angle * math.pi / 180)
    vertical_vel = velocity * math.sin(angle * math.pi / 180)
    horizontal_dist = 0
    vertical_dist = 0

    while((vertical_dist>= self.final_y) or (vertical_vel>0)):
        horizontal_dist = horizontal_vel * time + horizontal_dist
        vertical_dist = vertical_vel * time + vertical_dist
        vertical_vel = vertical_vel + gravity * time
        horizontal_vel = horizontal_vel + wind

    return horizontal_dist, vertical_dist

  def _get_obs(self):
    euclidean_distance = math.sqrt((self.distance - self.horizontal_dist)**2 + (self.final_y - self.vertical_dist)**2)

    wind = 0
    if(self.wind_vel > 0):
        wind = 1
    else:
        wind = -1

    return [self.velocity, self.angle, euclidean_distance, wind]

  def _get_reward(self):
    return math.sqrt((self.distance - self.horizontal_dist)**2 + (self.final_y - self.vertical_dist)**2)

  def reset(self):
    # Reset the state of the environment to an initial state
    self.target_x = random.uniform(5,235)
    self.target_y = random.uniform(5, 235)
    return

  def render(self, mode='human', close=False):
    if self.viewer is None:
        self.viewer = Viewer()
    if !(close):
        self.viewer.move(self.velocity, self.angle, self.final_y)
