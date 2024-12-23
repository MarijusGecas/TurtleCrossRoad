from turtle import Turtle
import random
COLORS = ["red", "orange", "grey", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
END_LINE_X = -340


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(340, random.randint(-210, 230))
        self.left(180)
        self.speed = random.randint(5, 15)
        self.hitbox_width = 70
        self.hitbox_height = 45

    def move(self, upd_speed):
        self.forward(self.speed * upd_speed)
    def reset_car(self):
        if self.xcor() <= END_LINE_X:
            self.goto(300, random.randint(-210, 230))

    def check_collision(self, player):
        # Use the dynamically calculated hitbox for collision detection
        car_x = self.xcor()
        car_y = self.ycor()

        # Define the hitbox bounds (centered on the car)
        hitbox_left = car_x - self.hitbox_width / 2
        hitbox_right = car_x + self.hitbox_width / 2
        hitbox_top = car_y + self.hitbox_height / 2
        hitbox_bottom = car_y - self.hitbox_height / 2

        # Check if the player is inside the hitbox
        if (hitbox_left < player.xcor() < hitbox_right) and (hitbox_bottom < player.ycor() < hitbox_top):
            return True
        return False