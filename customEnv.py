import gym
from gym import spaces
import numpy as np

class ArcheryEnv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}


    # velocity is the velocity of the arrow
    # angle is the initial angle of the arrow
    # final_y is the height of the target
    # viewer is the turtle simulation
    def __init__(self, final_y):
        super(CustomEnv, self).__init__()
        self.final_y = final_y
        self.viewer = None

        # used for spaces
        self.max_angle = 90
        self.min_angle = 0
        self.max_speed = 70
        self.min_speed = 0
        self.min_distance = 0
        self.max_distance = 500 # arbitrary
        self.left_wind = -1
        self.right_wind = 1

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

    # action should be [angle, velocity]
    def step(self, action):
    # Execute one time step within the environment

    return self._get_obs(), self._get_reward(), done

    def _get_obs(self):
      return

    def _get_reward(self):
        return

    def reset(self):
        # Reset the state of the environment to an initial state
        # where rewards are calculated
        # more reward when it is closer to target via euclidean distance
    return

    def render(self, mode='human', close=False):
        if self.viewer is None:
            self.viewer = Viewer()
        if not (close):
            self.viewer.move(self.velocity, self.angle, self.final_y, self.wind)
