#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class Drawcircle(Node):

    def __init__(self):
        super().__init__("Draw_Circle")
        self.my_publisher= self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer= self.create_timer(0.5, self.send_velocity)
        self.get_logger().info("Draw Circle node has been Started")
        self.step_counter=0

    def send_velocity(self):
        msg= Twist()
        msg.linear.x=2.0
        if self.step_counter<20:
            msg.angular.z=(2.0*math.pi)/5.0
            self.get_logger().info("Turning left")
        else:
            msg.angular.z=-(2.0*math.pi)/5.0
            self.get_logger().info("Turning Right")
        # msg.linear.y=2.0
        # msg.angular.z=1.0

        self.my_publisher.publish(msg) 

        self.step_counter+=1
        if self.step_counter>=40:
            self.step_counter=0

def main(args=None):
    rclpy.init(args=args)
    node=Drawcircle()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__== "__main__":
    main() 