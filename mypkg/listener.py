import rclpy
from rclpy.node import Node
from person_msgs.msg import Int16

def cb(msg):
    global node
    node.get_logger().info("Listen: %d" % msg.data)

rclpy.init()
node = Note("listener")
pub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)
