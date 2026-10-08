#!/usr/bin/env python3

import sys
import rclpy
from rclpy.node import Node
from minhas_interfaces.srv import AddTwoInts

class ServiceClient(Node):

    def __init__(self):
        super().__init__('client_node_sebastiao')
        self.client = self.create_client(AddTwoInts, 'add_two_ints')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Aguardando serviço de soma...')
        self.req = AddTwoInts.Request()

    def send_request(self, a, b):
        self.req.a = a
        self.req.b = b
        return self.client.call_async(self.req)

def main():
    if len(sys.argv) < 3:
        print('Uso: ros2 run pacote_test client_node num_a num_b')
    rclpy.init()
    node = ServiceClient()
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    future = node.send_request(a, b)
    print(node, future, a, b)
    rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        response = future.result()
        node.get_logger().info(f'Resposta da some de {a} + {b} = {response.sum}')
    else:
        node.get_logger().error(f'Falha na chamada')


    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

