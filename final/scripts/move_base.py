#!/usr/bin/env python
from time import sleep
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import os
import time

       
def movebase():
    
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    # Creates a new goal 
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    # ask user to define goal position 
    x = input("Enter goal position x: ")
    goal.target_pose.pose.position.x = x
    y = input("Enter goal y position: ")
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.w = 1.0
    
    
    # waits for the server to respond
    client.wait_for_server()
    #sends the goal to server
    client.send_goal(goal)
    #gets result of the action excecuted
    client.get_result()
    
def main():
    
    rospy.init_node('move_base')
    rospy.set_param('robot_state','0')
    rate = rospy.Rate(20)
   
    while not rospy.is_shutdown():
         if rospy.get_param('robot_state')=='s':
             movebase()
         else:
             rate.sleep()
             continue
         rate.sleep()
if __name__ == '__main__':
    main()
            





