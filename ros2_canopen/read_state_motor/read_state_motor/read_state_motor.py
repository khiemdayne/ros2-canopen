import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
# from canopen_interfaces.msg import COData

class RpdoSubscriber(Node):
    def __init__(self):
        super().__init__('rpdo_subscriber')
        self.subscription = self.create_subscription(
            Int16,
            '/cia402_device_1/rpdo',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info('Received data: %d', msg.data)

def main(args=None):
    rclpy.init(args=args)

    rpdo_subscriber = RpdoSubscriber()

    rclpy.spin(rpdo_subscriber)

    rpdo_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()