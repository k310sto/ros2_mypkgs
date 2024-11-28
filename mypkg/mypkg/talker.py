#ROS 2のクライアントのためのライブラリ
import rclpy
 #ノードを実装するためのNodeクラス（クラスは第10回で）
from rclpy.node import Node
#通信の型（16ビットの符号付き整数）
from std_msgs.msg import Int16

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
n = 0

def cb():
    global n       #関数を抜けてもnがリセットされないようにしている
    msg = Int16()  #メッセージの「オブジェクト」
    msg.data = n   #msgオブジェクトの持つdataにnを結び付け
    pub.publish(msg)        #pubの持つpublishでメッセージ送信
    n += 1


def main():
    node.create_timer(0.5, cb)  #タイマー設定
    rclpy.spin(node) 
