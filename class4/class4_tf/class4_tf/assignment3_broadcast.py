from geometry_msgs.msg import TransformStamped

import rclpy
from rclpy.node import Node

from tf2_ros import TransformBroadcaster
from tf2_ros import TransformException

from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener


class FixedFrameBroadcaster(Node):

    def __init__(self):
        super().__init__('assignment3_broadcaster')
        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.broadcast_timer_callback)
        self.target_x = 1.5
        self.target_y = 2.6

    def broadcast_timer_callback(self):
        t = TransformStamped()
        time = self.get_clock().now
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'frame1'
        t.transform.translation.x = self.target_x
        t.transform.translation.y = self.target_y
        t.transform.translation.z = 0.0

        self.tf_broadcaster.sendTransform(t)

def main():
    rclpy.init()
    node = FixedFrameBroadcaster()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()