import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import math
from sensor_msgs.msg import LaserScan

class TurtleLine(Node):

    def __init__(self):
        super().__init__('turtle_line')
        self.subscription = self.create_subscription(LaserScan, '/scan',self.timer_callback ,10)
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.cmd = Twist()

    def timer_callback(self, msg):
        if min(msg.ranges) < 0.8:
            self.cmd.linear.x = 0.0
        else:
            self.cmd.linear.x = 1.0

        self.pub.publish(self.cmd)

def main(args=None):
    rclpy.init(args=args)

    turtlesim_ridar = TurtleLine()

    rclpy.spin(turtlesim_ridar)

    # Destroy the node explicitly
    turtlesim_ridar.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()