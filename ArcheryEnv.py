import gym
from gym import spaces

class ArcheryEnv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}


    # velocity is the velocity of the arrow
    # angle is the initial angle of the arrow
    # final_y is the height of the target
    # viewer is the turtle simulation
  def __init__(self, arg1, arg2, ...):
    super(CustomEnv, self).__init__()
    self.velocity = velocity
    self.angle = angle
    self.final_y = final_y
    self.viewer = None
    # Define action and observation space
    # They must be gym.spaces objects
    # Example when using discrete actions:

    # all of the actions possible for an agent to take in the env
    self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)

    # Example for using image as input:
    self.observation_space = spaces.Box(low=0, high=255, shape=
                    (HEIGHT, WIDTH, N_CHANNELS), dtype=np.uint8)

  def step(self, action):
    # Execute one time step within the environment
    angle = self.state

    self.state = (angle)
    done = bool()
    return np.array(self.state), reward, done, {}

  def reset(self):
    # Reset the state of the environment to an initial state
    # where rewards are calculated
    # more reward when it is closer to target via euclidean distance

    return

  def render(self, mode='human', close=False):
    if self.viewer is None:
        self.viewer = Viewer()
    if !(close):
        self.viewer.move(self.velocity, self.angle, self.final_y)
