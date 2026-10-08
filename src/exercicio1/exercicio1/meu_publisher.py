#!/usr/bin/env python3
import rclpy
import sys
from rclpy.node import Node
from std_msgs.msg import String
class publicador(Node):
    def __init__(self):
        super().__init__("sebastiao")
        self.pub = self.create_publisher(String, '/topic_sebastiao', 10)
        
    def publish(self, msg_to_publish):
        msg = String()
        msg.data = msg_to_publish
        self.pub.publish(msg)

def main():
    rclpy.init()
    no = publicador()
    if len(sys.argv) != 2:
        no.get_logger().error(f'Número de argumentos incorreto: {len(sys.argv)}')
    else:
        no.publish(sys.argv[1])
        #rclpy.spin(no)
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()
