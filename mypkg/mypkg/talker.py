#ROS 2のクライアントのためのライブラリ
import rclpy
 #ノードを実装するためのNodeクラス（クラスは第10回で）
from rclpy.node import Node
#通信の型（16ビットの符号付き整数）
from person_msgs.srv import Query

rclpy.init()
node = Node("talker")

def cb(request, response):
    if request.name == "上田隆一":
        response.age = 46
    else:
        response.age = 255
 
    return response
 
 
def main():
    srv = node.create_service(Query, "query", cb) #サービスの作成     
    rclpy.spin(node)
