#!/usr/bin/python3
import rospy
import struct 
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
import numpy as np
import binascii



def callback_pack(msg):
    
    data = np.array(msg.data)
    # Convert the float array to a binary string
    packed_data = struct.pack('<{}f'.format(len(data)), *data)

    # Calculate the checksum value
    checksum = sum(bytearray(packed_data)) & 0xFF

    # Add the checksum byte to the end of the packed data
    packed_data += struct.pack('<B', checksum)
    packet_hex = binascii.hexlify(packed_data).decode('ascii')

    #send packed data
    mqtt_packer.publish(packet_hex)


def callback_unpack(msg):
    # Unpack the binary string into a float array and checksum byte
    
    packet = binascii.unhexlify(msg.data)
    
    # Extract the float array and checksum from the packet
    float_bytes = packet[:-1]
    checksum = packet[-1]

    # Verify the checksum
    if sum(float_bytes) & 0xff != checksum:
        print('Checksum error')
        exit()

    # Unpack the float array from the bytes
    float_array = struct.unpack('<' + 'f' * (len(float_bytes) // 4), float_bytes)

    float_msg = Float32MultiArray(data = float_array)
    
    mqtt_unpacker.publish(float_msg)



if __name__ == '__main__':
    rospy.init_node('ncrl_mqtt_bridge', anonymous=True)
    
    # subscribe from user topic (ncrl_mqtt_pack) and publish to mqtt topic
    rospy.Subscriber("ncrl_mqtt_pack", Float32MultiArray, callback_pack)
    mqtt_packer = rospy.Publisher('/ping/ros', String, queue_size=10)

    # subscribe from mqtt_topic and publich to user topic (ncrl_mqtt_unpack)
    rospy.Subscriber("/pong/ros", String, callback_unpack)
    mqtt_unpacker = rospy.Publisher('ncrl_mqtt_unpack', Float32MultiArray, queue_size=10)
    
    
    rospy.spin()
