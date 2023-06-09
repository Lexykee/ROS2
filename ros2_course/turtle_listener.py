import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from ros2_course.turtle import TurtleFractalDragon

class TurtleListener(Node):
    def __init__(self):
        super().__init__('turtle_listener')
        self.subscription = self.create_subscription(
            Int32,
            'fractal_dragon_level',
            self.listener_callback,
            10
        )
        self.subscription

        self.turtle_fractal_dragon = TurtleFractalDragon()

    def listener_callback(self, msg):
        self.get_logger().info(f'Received fractal_dragon_level: {msg.data}')
        level = msg.data
        self.turtle_fractal_dragon.screen.clear()
        self.turtle_fractal_dragon.level = level
        self.turtle_fractal_dragon.draw_fractal_dragon()

def main(args=None):
    rclpy.init(args=args)
    turtle_listener = TurtleListener()
    rclpy.spin(turtle_listener)
    turtle_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

