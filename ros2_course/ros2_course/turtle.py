import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from turtle import Screen, Turtle

class TurtleFractalDragon(Node):
    def __init__(self):
        super().__init__('turtle_fractal_dragon')
        self.level = 5
        self.length = 5

        self.declare_parameter('dragon_level', self.level)
        self.declare_parameter('dragon_length', self.length)

        self.level = self.get_parameter('dragon_level').value
        self.length = self.get_parameter('dragon_length').value

        self.screen = Screen()
        self.screen.setup(1200, 1400)
        self.screen.setworldcoordinates(0, 0, 1000, 800)

        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)
        self.turtle.penup()

        self.publisher = self.create_publisher(Int32, 'fractal_dragon_level', 10)

        self.timer = self.create_timer(1.0, self.publish_level)

        self.draw_fractal_dragon()

    def draw_forward(self, distance):
        self.turtle.pendown()
        self.turtle.forward(distance)

    def draw_turn(self, angle):
        self.turtle.right(angle)

    def fractal_dragon(self, level, distance, is_forward=True):
        if level == 0:
            self.draw_forward(distance)
        else:
            if is_forward:
                self.fractal_dragon(level - 1, distance, True)
                self.draw_turn(90)
                self.fractal_dragon(level - 1, distance, False)
            else:
                self.fractal_dragon(level - 1, distance, True)
                self.draw_turn(-90)
                self.fractal_dragon(level - 1, distance, False)

    def draw_fractal_dragon(self):
        self.turtle.penup()
        self.turtle.goto(500, 200)  # Starting position
        self.turtle.pendown()

        self.fractal_dragon(self.level, self.length)

    def publish_level(self):
        msg = Int32()
        msg.data = self.level
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    turtle_fractal_dragon = TurtleFractalDragon()
    rclpy.spin(turtle_fractal_dragon)
    turtle_fractal_dragon.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

