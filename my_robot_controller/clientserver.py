#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
from turtlesim.srv import SetPen
from functools import partial

class TurtleControl(Node):
    def __init__(self):
        super().__init__("Turtle_Controller")
        self.previous_x_= 0
        self.publisher= self.create_publisher(Twist,"/turtle1/cmd_vel", 10)
        self.subscriber=self.create_subscription(Pose,"/turtle1/pose", self.call_back, 10)
        self.get_logger().info("Turtle Controller Started")


    def call_back(self, pose:Pose):
        cmd= Twist()
        if pose.x>9.0 or pose.x<2.0 or pose.y>9.0 or pose.y<2.0:
            cmd.linear.x=1.0
            cmd.angular.z=math.radians(90)
        else:
            cmd.linear.x=3.0
            cmd.angular.z=0.0

        self.publisher.publish(cmd)

        if pose.x>5.5 and self.previous_x_<=5.5:
            self.previous_x_ = pose.x
            self.get_logger().info("Set Colour To Red")
            self.call_pen_set_service(255,0,0,3,0)

        elif pose.x <=5.5 and self.previous_x_>5.5:
            self.previous_x_ = pose.x
            self.get_logger().info("Set Colour To Green")
            self.call_pen_set_service(0,255,0,3,0)

    def call_pen_set_service(self,r,g,b,width,off):
        client=self.create_client(SetPen, "/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Service.....")


        request= SetPen.Request()
        request.r=r
        request.g=g
        request.b=b
        request.width=width
        request.off=off

        future=client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))

    def callback_set_pen(self,future):
        try:
            response= future.result()
        except Exception as e:
            self.get_logger().error("Service call failed: %r0" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node=TurtleControl()
    rclpy.spin(node)
    rclpy.shutdown()
