#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class Square(Node):
    def __init__(self):
        super().__init__("Square_Node_Created")
        self.publisher_=self.create_publisher(Twist,"/turtle1/cmd_vel", 10)
        self.subscriber_=self.create_subscription(Pose, "/turtle1/Pose", self.calll_back, 10)
        self.timer=self.create_timer(1.0, self.call_back)
        self.counter=0

    def call_back(self):
        msg=Twist()

        if self.counter<4:
            msg.linear.x=2.0
            msg.angular.z= 0.0

        elif self.counter<5:
            msg.linear.x=0.0
            msg.angular.z= math.radians(90)
            self.get_logger.info("Turning at Right Angle")
        

        self.publisher_.publish(msg)
        self.counter+=1


        if self.counter>=6:
            self.counter=0

    def calll_back(self,msg):
        self.current_theta= msg.theta     




def main(args=None):
    rclpy.init(args=args)
    node=Square()
    rclpy.spin(node)
    rclpy.shutdown()