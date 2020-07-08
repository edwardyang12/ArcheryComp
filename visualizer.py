import gym
import turtle
import math
# env = gym.make('Pendulum-v0')
#
# env.reset()
# while(True):
#     env.render()
#     env.step(env.action_space.sample())
# env.close()

class Viewer:
    def __init__(self, horizontal_dist = -100, vertical_dist = 0, gravity = -9.81, time = 0.01):
        turtle.screensize(300, 300, 'white')
        self.screen = turtle.Screen()
        self.screen.addshape("arrow1.gif")
        self.screen.addshape("arrow2.gif")
        self.theTurtle = turtle.Turtle()
        self.theTurtle.penup()
        self.theTurtle.setpos(horizontal_dist,vertical_dist)
        self.theTurtle.pendown()
        self.initial = (horizontal_dist, vertical_dist)
        self.gravity = gravity
        self.time = time

    # simulates one arrow shot
    def move(self, velocity, final_y, angle, wind):
        wind = wind * self.time
        horizontal_vel = velocity * math.cos(angle * math.pi / 180)
        vertical_vel = velocity * math.sin(angle * math.pi / 180)
        horizontal_dist = self.initial[0]
        vertical_dist = self.initial[1]
        while((vertical_dist>=final_y) or (vertical_vel>0)):
            self.update_turtle_shape(vertical_vel)
            self.theTurtle.setpos(horizontal_dist,vertical_dist)
            horizontal_dist = horizontal_vel * self.time + horizontal_dist
            vertical_dist = vertical_vel * self.time + vertical_dist
            vertical_vel = vertical_vel + self.gravity * self.time
            horizontal_vel = horizontal_vel + wind
        print(vertical_dist, horizontal_dist)
        self.end_episode()

    # update turtle shape
    def update_turtle_shape(self, vert_velocity):
        if(vert_velocity>0):
            self.theTurtle.shape("arrow2.gif")
        else:
            self.theTurtle.shape("arrow1.gif")

    # freeze turtle screen
    def freeze_screen(self):
        turtle.mainloop()

    # end current iteration
    def end_episode(self):
        self.theTurtle.penup()
        self.theTurtle.setpos(self.initial)
        self.theTurtle.pendown()
        self.update_turtle_shape(1)

if __name__ == '__main__':
    final_y = 30
    velocity = 70
    angle = 45
    wind = -3

    viewer = Viewer()
    viewer.move(velocity,final_y, angle, wind)

    angle = 10
    viewer.move(velocity,final_y, angle, wind)

    angle = 80
    viewer.move(velocity,final_y, angle, wind)
    viewer.freeze_screen()
