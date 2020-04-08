#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose


def poseCallback(pose_message):
    print "pose callback"
    print ('x = %f'.%(pose_message.x)) #new in python 3
    print ('y = %f' %pose_message.y) #used in python 2
    print ('yaw = %f'.%(pose_message.theta)) #new in python 3


if __name__ == '__main__':
    try:
        
        rospy.init_node('turtle_motion', anonymous=True)
        
        position_topic = "/turtle1/pose"
        pose_subscriber = rospy.Subscriber(position_topic, Pose, poseCallback) 
        rospy.spin()
       
    except rospy.ROSInterruptException:
        rospy.loginfo("node terminated.")