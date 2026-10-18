import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Practice(Node):
    def __init__(self):
        super().__init__("Practice_node")
        self.publisher_=self.create_publisher(String,"std_msgs/msg/String",10)
        # self.subscriber_=self.create_subscription()
        self.timer=self.create_timer(2.0, self.callback)

        self.i=0

    def callback(self):
        cmd=String()
        cmd.data= f"Hello Everyone...: {self.i}"

        self.get_logger().info(f"{cmd.data}")

        self.publisher_.publish(cmd)
        self.i+=1


def main(args=None):
    rclpy.init(args=args)
    node=Practice()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()