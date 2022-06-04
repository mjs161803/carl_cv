import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2 # OpenCV library
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Image, 'video_frames', 10)
        # We will publish a message every 0.1 seconds
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

        # Create a VideoCapture object
        self.cap = cv2.VideoCapture(0)

        self.br = CvBridge()

    def timer_callback(self):
        ret, frame = self.cap.read()

        if ret == True:
            self.get_logger().info('Publishing video frame')

    def main(args=None):

        rclpy.init(args=args)

        image_publisher = ImagePublisher()

        rclpy.spin(image_publisher)

        image_publisher.destroy_node()

        rclpy.shutdown()

    if __name__ == '__main__':
        main()

