#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from minhas_interfaces.srv import AddTwoInts

class ServiceServer(Node):

    def __init__(self):
        super().__init__('server_node_sebastiao')
        self.server = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)
        self.get_logger().info('Servidor de soma pronto para receber requisições')

    def add_two_ints_callback(self, request, response):
        self.get_logger().info(f'Requisição recebida para soma: a={request.a}, b={request.b}')
        response.sum = request.a + request.b
        self.get_logger().info(f'Enviando resposta da soma: sum={response.sum}')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ServiceServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

