#!/usr/bin/python3
import rospy
from std_msgs.msg import Float32MultiArray

def talker():
    pub = rospy.Publisher('ncrl_mqtt_pack', Float32MultiArray, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = [0, 333, 3, 3, 6, 7, 4, 3, 3, 2]
        float_msg = Float32MultiArray(data = msg)

        rospy.loginfo(float_msg)
        pub.publish(float_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass