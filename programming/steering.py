def steering_func(steering, throttle=1):
    if steering < -0.5:
        left = throttle
        right = (0.5 + steering)*throttle
    elif steering > 0.5:
        left = (0.5 - steering)*throttle
        right = throttle
    else:
        left = (0.5 - steering)*throttle
        right = (0.5 + steering)*throttle
    return left, right

for steering in range(-10,10):
    print(steering/10, steering_func(steering/10))