import rclpy
from rclpy.node import Node
import time

def main(args=None):
    rclpy.init(args=args)
    node = Node('node_hello')
    while rclpy.ok():
        node.get_logger().info('Hello World!!!')
        time.sleep(0.5)

    node.destroy_node()
    rclpy.shotdown()