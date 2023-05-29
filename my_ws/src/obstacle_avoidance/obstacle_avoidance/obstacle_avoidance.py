import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


class ObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance')

        self.laser_subscriber = self.create_subscription(
            LaserScan,
            '/scan',
            self.laser_callback,
            10
        )

        self.velocity_publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.velocity_msg = Twist()

    def laser_callback(self, msg):
        is_obstacle_in_front = min(msg.ranges[0:30] + msg.ranges[330:360]) < 0.5  # Check front sector for obstacles

        if is_obstacle_in_front:
            self.velocity_msg.linear.x = 0.0  # Stop
            self.velocity_msg.angular.z = 0.5  # Turn right
        else:
            self.velocity_msg.linear.x = 0.2  # Move forward
            self.velocity_msg.angular.z = 0.0  # Stop turning

        self.velocity_publisher.publish(self.velocity_msg)


def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidance()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()

