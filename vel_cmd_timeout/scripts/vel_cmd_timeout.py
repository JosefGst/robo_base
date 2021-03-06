#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDriveStamped

class SendEmptyWatchdog(object):
    def __init__(self, datatype, topic, send_value=None):
        self.timeout = rospy.get_param('~timeout', '1.0')
        self.datatype = datatype

        if send_value is None:
            self.send_value = datatype()
        else:
            self.send_value = send_value

        self.twist_subscriber = rospy.Subscriber(topic, self.datatype, self.message_callback, queue_size=1)
        self.twist_publisher = rospy.Publisher(topic, self.datatype, queue_size=1)
        self.timer = rospy.Timer(rospy.Duration(self.timeout), self.timer_callback, oneshot=True)
        self.timeout_triggered = False

    def message_callback(self, msg):
        rospy.logdebug("SendEmptyWatchdog{}: Message Callback".format(self.datatype))
        if self.timeout_triggered:
            self.timeout_triggered = False
        else:
            self.timer.shutdown()
            self.timer = rospy.Timer(rospy.Duration(self.timeout), self.timer_callback, oneshot=True)

    def timer_callback(self, event):
        rospy.logwarn("SendEmptyWatchdog{}: Timeout Triggered. Received no message for {} seconds".format(self.datatype, self.timeout))

        self.timeout_triggered = True
        self.twist_publisher.publish(self.send_value)

if __name__ == '__main__':
    rospy.init_node("command_watchdog")
    twist_watchdog = SendEmptyWatchdog(Twist, "cmd_vel")
    ackermann_watchdog = SendEmptyWatchdog(AckermannDriveStamped, "cmd_ackermann")
    rospy.spin()