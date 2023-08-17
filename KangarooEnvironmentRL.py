import numpy as np
from gym import Env
from gym.spaces import Discrete, Box
from gym.utils.env_checker import check_env

from KangarooJackGame import KangarooJackGame


class KangarooEnvironment(Env):

    def __init__(self):
        # instantiate game
        self.kangaroo_game = KangarooJackGame()

        # action space only 2 actions (up and down)
        self.action_space = Discrete(2)

        # observation space (1st dimension distance to water, 2nd dimension height above ground)
        self.observation_space = Box(low=-100, high=800, shape=(2,), dtype=np.int32)

        # initial state
        self.state = np.array([self.distance_to_water(), self.height_above_water()])

    def step(self, action):
        # make a step
        self.kangaroo_game.step(action)

        # calculate reward
        if 10 > self.distance_to_water() > -75 and self.height_above_water() > 0:
            reward = 1
        else:
            reward = 0

        # is the episode done (kangaroo crashed or we skipped over 100 potholes)
        done = self.kangaroo_game.is_crash() or self.kangaroo_game.score == 100

        # info
        info = {"distance to water": self.distance_to_water(), "height above water": self.height_above_water()}

        # new state
        self.state = np.array([self.distance_to_water(), self.height_above_water()])
        return self.state, reward, done, False, info

    def render(self):
        self.kangaroo_game.render(40)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        info = {"score": self.kangaroo_game.score}
        self.kangaroo_game.reset_game()
        return self.state, info

    def distance_to_water(self):
        return self.kangaroo_game.blue_water.water_x - (self.kangaroo_game.kangaroo_jack.kangaroo_x + self.kangaroo_game.kangaroo_jack.kangaroo_width)

    def height_above_water(self):
        return self.kangaroo_game.blue_water.water_y - (self.kangaroo_game.kangaroo_jack.kangaroo_y + self.kangaroo_game.kangaroo_jack.kangaroo_height)


env = KangarooEnvironment()
# print(env.observation_space.sample())
# print(np.array([114, 418]))
# check_env(env)

episodes = 5
for episode in range(1, episodes):
    print("episode ", episode)
    env.reset()
    terminated = False
    while not terminated:
        obs, reward, terminated, truncated, information = env.step(1)
        env.render()
