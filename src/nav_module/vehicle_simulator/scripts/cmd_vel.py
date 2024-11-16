#!/usr/bin/env python

import rospy
from geometry_msgs.msg import TwistStamped, Twist

class CmdVelConverterNode:
    def __init__(self):
        # Initialize the node
        rospy.init_node('cmd_vel_converter_node')

        # Subscriber: subscribe to /cmd_vel_input (TwistStamped)
        self.cmd_vel_input_sub = rospy.Subscriber('/cmd_vel_input', TwistStamped, self.cmd_vel_input_callback)

        # Publisher: publish to /cmd_vel (Twist)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # Scaling factor to reduce speed
        self.linear_speed_scale = 0.3
        self.angular_speed_scale = 0.5

    def cmd_vel_input_callback(self, msg):
        # Convert TwistStamped to Twist
        twist_msg = Twist()

        # Scale down linear velocities
        twist_msg.linear.x = msg.twist.linear.x * self.linear_speed_scale
        twist_msg.linear.y = msg.twist.linear.y * self.linear_speed_scale        
        twist_msg.linear.z = msg.twist.linear.z * self.linear_speed_scale

        # Scale down angular velocities
        twist_msg.angular.x = msg.twist.angular.x * self.angular_speed_scale
        twist_msg.angular.y = msg.twist.angular.y * self.angular_speed_scale
        twist_msg.angular.z = msg.twist.angular.z * self.angular_speed_scale

        # Publish the converted message
        self.cmd_vel_pub.publish(twist_msg)

    def run(self):
        # Keep the node running
        rospy.spin()

if __name__ == '__main__':
    try:
        node = CmdVelConverterNode()
        node.run()
    except rospy.ROSInterruptException:
        pass
