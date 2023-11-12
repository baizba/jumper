import numpy as np
from gymnasium import Env
from gymnasium.spaces import Discrete, Box
from tensorflow import int32

from KangarooJackGame import KangarooJackGame


class KangarooEnvironment(Env):

    def __init__(self):
        # instantiate game
        self.kangaroo_game = KangarooJackGame()

        # action space only 2 actions (up and down)
        self.action_space = Discrete(2)

        # observation space (1st dimension distance to water, 2nd dimension height above ground)
        # self.observation_space = Box(low=-100, high=800, shape=(2,), dtype=np.int32)
        # self.observation_space = Box(low=np.ndarray([-300, 0]), high=np.ndarray([800, 100]), shape=int32)
        observations = np.array([800, 200], dtype=np.float32)
        self.observation_space = Box(-observations, observations, dtype=np.float32)

        # initial state
        self.state = None

    def step(self, action):
        # make a step
        self.kangaroo_game.step(action)

        # calculate reward
        if 15 > self.distance_to_water() > -75 and self.height_above_water() > 0:
            reward = 1
        else:
            reward = 0

        # is the episode done (kangaroo crashed or we skipped over 100 potholes)
        done = self.kangaroo_game.is_crash() or self.kangaroo_game.score == 100

        # info
        info = {"distance to water": self.distance_to_water()}

        # new state
        self.state = (self.distance_to_water(), self.height_above_water())
        return np.array(self.state, dtype=np.float32), reward, done, info

    def render(self, mode):
        self.kangaroo_game.render(40)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        info = {"score": self.kangaroo_game.score}
        self.kangaroo_game.reset_game()
        self.state = (self.distance_to_water(), self.height_above_water())
        return np.array(self.state, dtype=np.float32)

    def distance_to_water(self):
        return self.kangaroo_game.blue_water.water_x - (self.kangaroo_game.kangaroo_jack.kangaroo_x + self.kangaroo_game.kangaroo_jack.kangaroo_width)

    def height_above_water(self):
        return self.kangaroo_game.blue_water.water_y - (self.kangaroo_game.kangaroo_jack.kangaroo_y + self.kangaroo_game.kangaroo_jack.kangaroo_height)


# env = KangarooEnvironment()
# print(env.observation_space.sample())
# print(np.array([114, 418]))
# check_env(env)

'''
episodes = 5
for episode in range(1, episodes):
    print("episode ", episode)
    env.reset()
    terminated = False
    while not terminated:
        obs, reward, terminated, truncated, information = env.step(1)
        env.render()
'''
