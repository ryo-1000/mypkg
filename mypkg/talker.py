import rclpy                     
from rclpy.node import Node      
from person_msgs.srv import Query

def cb(request, response):
    if request.name == "海老沢亮":
        response.age = 21
    else:
        response.age = 255

    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)
