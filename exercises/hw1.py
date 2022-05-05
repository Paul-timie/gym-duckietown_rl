#Homework 1 by Paul Ayodele
# COURSE :ELEC- 6672
#AIM: Lane Following

from PIL import Image
import time
import sys
import argparse
import math
import numpy as np
import gym
import pyglet
from pyglet.window import key
from gym_duckietown.envs import DuckietownEnv

parser = argparse.ArgumentParser()
parser.add_argument("--env-name", default=None)
parser.add_argument("--map-name", default="udem1")
parser.add_argument("--no-pause", action="store_true", help="don't pause on failure")
parser.add_argument("--distortion", default=False, action="store_true")
parser.add_argument("--draw-curve", action="store_true", help="draw the lane following curve")
parser.add_argument("--domain-rand", action="store_true", help="enable domain randomization")
args = parser.parse_args()

if args.env_name is None:
    env = DuckietownEnv(map_name=args.map_name, domain_rand=False, draw_bbox=False)
else:
    env = gym.make(args.env_name)

obs = env.reset()
env.render()

total_reward = 0
env.unwrapped.cam_angle[0] = 0
@env.unwrapped.window.event
def on_key_press(symbol, modifiers):
    if symbol == key.ESCAPE:  #You can Press ESC Key to end the simulation
        env.close()
        sys.exit(0)
key_handler = key.KeyStateHandler()
env.unwrapped.window.push_handlers(key_handler)

while True:

    robot_lane_position = env.get_lane_pos2(env.cur_pos, env.cur_angle)
    road_center_dist = robot_lane_position.dist
    angle_from_straight_in_rads = robot_lane_position.angle_rad

    #The speed

    robot_speed = 0.065

    #The angle of the duckiebot in rads/s
    robot_angle = ((12 * road_center_dist) + (1.2 * angle_from_straight_in_rads))

    obs, reward, done, info = env.step([robot_speed, robot_angle])
    total_reward += reward

    print(
        "stage = %s, instant reward=%.3f, total reward=%.3f, PRESS ESC KEY TO END SIMULATION"
        % (env.step_count, reward, total_reward)
    )

    env.render()
    if env.step_count == 10200:
        print("Done! Finished the whole map,")
        break


    