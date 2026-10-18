#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class Closedloop(Node):

    def __init__(self):
        super().__init__("Turtle_controller")
        self.publisher_= self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.call_back, 10)
        self.get_logger().info("Turtle Controller Started")

    def call_back(self,pose:Pose):
        cmd= Twist()
        if pose.x>9.0 or pose.x<2 or pose.y>9.0 or pose.y<2.0:
            cmd.linear.x= 1.0
            cmd.angular.z= math.radians(45)
        else:
            cmd.linear.x= 5.0
            cmd.angular.z=0.0

        self.publisher_.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = Closedloop()
    rclpy.spin(node)
    
    rclpy.shutdown()