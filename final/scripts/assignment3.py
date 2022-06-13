#!/usr/bin/env python

import rospy
from std_srvs.srv import *
import os

""" this program makes the user control robot's behaviour """

# 1- teleop keyboard
# 2- movebase client
# 3- assistance to avoid collisions

def state():
   
   x = input ('''choose the robot behaviour:
   
   w. use keyboard.
   s. autonomously reach your destination.
   d. robot using collision avoidance.
   
   input: ''')
   
   if x == 'w':
   
       rospy.set_param('robot_state', 'w')
       print("teleop keyboard")
       
   elif x == 's':
      
       rospy.set_param('robot_state', 's')
       print("movebase client")
   
   elif x == 'd':
      
       rospy.set_param('robot_state', 'd')
       print("assistance to avoid collisions")
   

def main():

   rospy.init_node('assignment3')
   rospy.set_param('robot_state', '0')
   rate = rospy.Rate(20)
   
   while not rospy.is_shutdown():
       if (rospy.get_param('robot_state')) == '0':
           state()
       else:
           rate.sleep()
           continue 
       rate.sleep()
           
if __name__ == '__main__':
    main()
   
   
   
   
   
   
   
