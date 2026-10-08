#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class publicador(Node):
    def __init__(self):
        super().__init__("sebastiao")
        self.pub = self.create_publisher(String, '/topic_sebastiao', 10)
        
def main():
    rclpy.init()
    no = publicador()
    rclpy.spin(no)
    rclpy.shutdown()
if __name__ == '__main__':
    main()
