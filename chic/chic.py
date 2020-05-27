'''
4m/s三档速度，7个角度最大探索导致不稳定
Gradient descent batch size
64
Entropy
0.01
Discount factor
0.999
Loss type
Huber
Learning rate
0.001
Number of experience episodes between each policy-updating iteration
20
Number of epochs
3
'''

def reward_function(params):
    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    progress = params['progress']
    steps = params['steps']
    speed = params['speed']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    norm_dist_from_ctr = (distance_from_center*2)/track_width

    reward = 6.0 * norm_dist_from_ctr*norm_dist_from_ctr
    #克隆1把离心惩罚放在前面, 而速度+在轨+完成度的顺序放在后面)

    if all_wheels_on_track and steps > 0:
        reward = reward * (progress/steps)*speed*speed
    else:
        # Give a very low reward by default
        return reward * float(0.0001)#惩罚X10


    if progress == 100:
        reward *= 20#奖励X10
    return float(reward)
