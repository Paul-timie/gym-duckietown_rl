import numpy as np
import os
import matplotlib
#import args
from args import get_ddpg_args_test
from matplotlib import pyplot as plt

policy_name = "DDPG"

args = get_ddpg_args_test()

# Taking user seed input and creating a matching filename
file_name = "{}_{}".format(
    policy_name,
    str(args.seed),
)

# Checking that results exist
if not os.path.exists("./results"):
    print("This action cannot be completed")
else:
    data = np.load("results/rewards.npz")

    reward = data[data.files[0]]
    timestep = data[data.files[1]]

    # plt.plot(timestep, reward)
    plt.plot(reward)
    plt.title("Reward vs. Timesteps")
    plt.xlabel("# of Evalutations (1 eval = 5000 timesteps)")
    plt.ylabel("Avg. Reward per episode")
    plt.show()

    m = np.mean(reward)
    s = np.std(reward)
    
    for i in reward:
        norm_data = (reward - m)/s

    # plt.plot(norm_data)
    # plt.title("Normalized Reward vs. Timesteps")
    # plt.xlabel("# of Evalutations (1 eval = 5000 timesteps)")
    # plt.ylabel("Normalized Avg. Reward per episode")
    # plt.show()


