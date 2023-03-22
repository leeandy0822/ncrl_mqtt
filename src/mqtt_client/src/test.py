#!/usr/bin/python3
import rospy
from std_msgs.msg import Float32MultiArray

def talker():
    pub = rospy.Publisher('ncrl_mqtt_pack', Float32MultiArray, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = [0.5, -333.25, 3.001, 3.55, 6.9965454, -721212.56, -4.2, 3.55, 3.45, 2.9898]
        float_msg = Float32MultiArray(data = msg)

        rospy.loginfo(float_msg)
        pub.publish(float_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass