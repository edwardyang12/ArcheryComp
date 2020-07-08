import random
import math

def move(initial, velocity, final_y, angle, wind):
    wind = wind * time
    horizontal_vel = velocity * math.cos(angle * math.pi / 180)
    vertical_vel = velocity * math.sin(angle * math.pi / 180)
    horizontal_dist = 0
    vertical_dist = 0

    while((vertical_dist>=final_y) or (vertical_vel>0)):
        horizontal_dist = horizontal_vel * time + horizontal_dist
        vertical_dist = vertical_vel * time + vertical_dist
        vertical_vel = vertical_vel + gravity * time
        horizontal_vel = horizontal_vel + wind
    return horizontal_dist, vertical_dist

# units: m/s or m
tries = 3
distance = random.uniform(0,240)
velocity = random.uniform(0,70)
y_height = random.uniform(0,10)
gravity = -9.81
wind_vel = random.uniform(-5,5)
time = 0.01
print(distance, y_height)
print(velocity)


while(tries>0):

    # to be changed later
    angle = input("Get angle: ")
    angle = float(angle)
    while(angle>90 or angle<0):
        angle = input("Angle must be between 0 and 90 degrees: ")
        angle = float(angle)

    horizontal_dist, vertical_dist = move([0,0],velocity,y_height,angle,wind_vel)

    reward = math.sqrt((distance - horizontal_dist)**2 + (final_y -vertical_dist)**2)
    tries = tries -1
