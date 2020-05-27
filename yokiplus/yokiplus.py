def reward_function(params):
    '''
    Hyperparameter
    Value
    Gradient descent batch size
    64
    Entropy
    0.01
    Discount factor
    0.999
    Loss type
    Huber
    Learning rate
    0.0003
    Number of experience episodes between each policy-updating iteration
    20
    Number of epochs
    10
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 10.0
    elif distance_from_center <= marker_2:
        reward = 5
    elif distance_from_center <= marker_3:
        reward = 1
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    return float(reward)
