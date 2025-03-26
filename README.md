# agv_urdf_ros2_gazebo
agv_urdf_ros2_gazebo </br>
![{AA1A592F-71D5-411E-9E0C-E36CB05545FF}](https://github.com/user-attachments/assets/fc7b8c57-7e9c-4c68-b1a6-3aae9ecd1b15) </br>
600*600*600 폼펙터 규격의 Dual motor AGV입니다.</br>
ros2 기반의 SLAM->Navigation을 목적으로 개발되었습니다.</br>

|부품명|카테고리|제조사|수량|단가|계|비고|
|---|---|---|---|---|---|---|
|A2M4-R|라이다 센서|SLAMTEC|1|573,410|573,410|Range : 0.2m~16m|
|MDR200|드라이빙 유닛|엠디로봇|2|409,000|818,000|0.8m/s(2.9km/h),감속비 1/30|
|MD400T|모터 드라이버|엠디로봇|1|374,000|374,000|RS485 ROS Package|
|CVCOM370|배터리|타보스|1|1,039,500|1,039,500|LG에너지솔루션 21700 셀|
|TC-700W|충전기|타보스|1|568,700|568,700|RS232|배터리 상태|모니터링 모듈 포함|
|MW-AHRS X1|IMU|엔티렉스|1|154,000|154,000|
|라즈베리파이 5|제어PC|라즈베리파이|1|117,700|117,700|구매처 - 엘레파츠|
|Arducam 1080P|RGB Cam|Arducam|4|71,500|286,000|보유재고 확인|
|TFmini Plus LiDAR|초음파 센서|Benewake|4|65,890|263,560|
|USB to UART RS485|TTL to usb컨버터|디웰전자|4|19,448|77,792|
|USB to RS232|TTL to usb컨버터|엠디로봇|1|39,600 39,600|
|PDIST30|전원분배보드|엠디로봇|1|110,000 110,000|
|PDIST80|전원분배보드|엠디로봇|1|120,000 120,000|
|STS040-C51-3-M|3단 경광등|나비엠알오|1|42,990|42,990|
|캐스터 휠|보조바퀴|한국 미스미|2|6,223|12,446|
|2040 Profile|알루미늄|프로파일|나비엠알오|10|8,390|83,900|수량 : 1000m당 1|
|AI5052|알루미늄 하우징|나비엠알오|1|95,000|95,000|수량 - 1000m^2당 1, AI6061가공 변동 가능성 있음, 6061가공시 95000원|
|하우징|가공 하우징 가공|na|1|200000|200,000|3축 CNC가공 - 진성정밀(견적 진행 후 최종 가격 재산정 필요, 자재 수급 기한, 작업일에 따름)|
|전원 박스|EMG단자 함|na|1|300000|300,000|퓨즈박스, 전원 단자 함 가공 - 부원이엔지 5,276,598|

레퍼런스 자료
![{B8BFACE7-F32D-45C8-9FA4-BF13873BBD31}](https://github.com/user-attachments/assets/82486ed2-fd0c-4855-8943-aa5956034473)
![{EEFD2A51-E3ED-48DD-8D49-9442F04C0AE6}](https://github.com/user-attachments/assets/c3a2432f-02d7-4523-84d5-769a137d98dc)

실물사진
![20241001_173311](https://github.com/user-attachments/assets/860215a6-6ba1-419f-b251-d87046763f55)
![20241016_160816](https://github.com/user-attachments/assets/53b8bcc5-1134-4890-8d56-283753a60c32)
![20241007_073647](https://github.com/user-attachments/assets/900edc4f-fe10-46d9-9853-cd276df5fe2c)
![20241007_050917](https://github.com/user-attachments/assets/b31b3b19-8d60-4ca6-8579-9f3347b03c4a)

github
[amr bringup launch package](https://github.com/SeongminJaden/ros2_amr)

# ROS2 Humble - TurtleBot3 SLAM 및 Navigation 설정

이 문서는 ROS2 Humble에서 TurtleBot3의 SLAM (Simultaneous Localization and Mapping) 및 Navigation을 설정하고 사용하는 방법을 설명합니다.

## 1. 개요

TurtleBot3는 ROS2 환경에서 로봇의 SLAM 및 Navigation을 지원하는 인기 있는 플랫폼입니다. 이 문서는 TurtleBot3에서 SLAM과 Navigation 기능을 활성화하고 이를 활용하는 데 필요한 정보를 제공합니다.

### 1.1 SLAM (Simultaneous Localization and Mapping)
SLAM은 로봇이 자신의 위치를 추정하면서 동시에 환경의 맵을 생성하는 기술입니다. TurtleBot3에서는 다양한 SLAM 알고리즘을 사용할 수 있습니다.

### 1.2 Navigation
Navigation은 로봇이 주어진 환경에서 목표 지점으로 안전하게 이동할 수 있도록 하는 기술입니다. 이 과정에서는 로봇의 위치 추정, 장애물 회피 및 경로 계획을 포함합니다.

---

## 2. TurtleBot3 설치 및 환경 설정

### 2.1 ROS2 Humble 설치

1. **ROS2 Humble**을 설치하려면 [ROS2 공식 설치 문서](https://docs.ros.org/en/humble/Installation.html)를 참조하십시오.
   
2. ROS2 Humble을 설치한 후, TurtleBot3 패키지를 설치해야 합니다:

```bash
sudo apt update
sudo apt install ros-humble-turtlebot3 ros-humble-turtlebot3-msgs
```
### 2.2 TurtleBot3 모델 설정
TurtleBot3 모델을 설정하려면 아래의 명령을 통해 환경 변수에 모델을 설정합니다. 이를 통해 다양한 TurtleBot3 모델(버거, 와플 등)을 선택할 수 있습니다.

```bash
export TURTLEBOT3_MODEL=burger  # burger, waffle, waffle_pi 중 선택
```
## 3. SLAM 사용하기
### 3.1 SLAM 설정
TurtleBot3는 Cartograper를 사용하여 SLAM을 설정합니다. 아래 명령을 통해 SLAM을 시작할 수 있습니다.

SLAM 실행:

```bash
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=True
```
이 명령은 TurtleBot3의 SLAM 기능을 활성화하고, Cartograper를 사용하여 맵을 생성합니다. 로봇을 움직이면서 주변 환경의 맵을 작성할 수 있습니다.

### 3.2 SLAM 관련 토픽
SLAM을 사용할 때 생성되는 주요 토픽은 다음과 같습니다:
```
/Cartograper/trajectory: SLAM 트래젝토리 정보
/map: 생성된 맵 데이터
/scan: LiDAR 센서로부터의 거리 측정 데이터
/tf: 로봇의 위치 및 방향을 나타내는 변환 정보
```
### 3.3 SLAM 관련 메시지 타입
SLAM에 관련된 주요 메시지 타입은 다음과 같습니다:
```
sensor_msgs/LaserScan: LiDAR 센서 데이터를 나타내는 메시지 타입으로, /scan 토픽에서 사용됩니다.
nav_msgs/OccupancyGrid: 생성된 맵 데이터를 나타내는 메시지 타입으로, /map 토픽에서 사용됩니다.
geometry_msgs/Pose: 로봇의 위치와 방향을 나타내는 메시지 타입으로, /tf 및 /slam_toolbox/trajectory에서 사용됩니다.
```
## 4. Navigation 사용하기
### 4.1 Navigation 설정
TurtleBot3의 Navigation을 설정하려면 nav2_bringup 패키지를 사용합니다. 아래 명령을 통해 Navigation을 활성화할 수 있습니다.

Navigation 실행:

```
ros2 launch turtlebot3_navigation2 navigation_launch.py
```
이 명령은 Navigation을 활성화하고 로봇이 맵에서 지정된 목표 위치로 이동할 수 있도록 합니다.

### 4.2 Navigation 관련 토픽
Navigation을 사용할 때 생성되는 주요 토픽은 다음과 같습니다:
```
/move_base_simple/goal: 목표 지점을 지정하는 토픽
/cmd_vel: 로봇의 속도 명령을 보내는 토픽
/odom: 로봇의 오도메트리 정보
/tf: 로봇의 위치와 방향을 나타내는 변환 정보
/costmap: 장애물 맵을 나타내는 토픽
```
### 4.3 Navigation 관련 메시지 타입
Navigation에 관련된 주요 메시지 타입은 다음과 같습니다:
```
geometry_msgs/PoseStamped: 목표 지점의 위치와 방향을 지정하는 메시지 타입으로, /move_base_simple/goal에서 사용됩니다.
geometry_msgs/Twist: 로봇의 선형 속도와 각속도를 나타내는 메시지 타입으로, /cmd_vel에서 사용됩니다.
nav_msgs/Odometry: 로봇의 위치와 속도 정보를 나타내는 메시지 타입으로, /odom에서 사용됩니다.
nav_msgs/OccupancyGrid: 장애물 맵 정보를 나타내는 메시지 타입으로, /costmap에서 사용됩니다.
```
## 5. 실시간 지도 업데이트 및 장애물 회피
### 5.1 지도 업데이트
SLAM을 사용하여 실시간으로 지도 정보를 업데이트하려면, 맵이 업데이트될 때마다 /map 토픽을 구독하여 새롭게 생성된 맵을 확인할 수 있습니다.

### 5.2 장애물 회피
Navigation 시스템에서는 costmap을 사용하여 장애물 회피를 수행합니다. 로봇이 주행 중 장애물을 감지하면, move_base 패키지가 이를 기반으로 경로를 조정하고 회피할 수 있습니다.

---

ROS2에서 토픽을 보내고 구독하는 방법에 대해 설명드리겠습니다. 파이썬을 기준으로 설명하며, 예시 코드도 포함할 것입니다. 주로 rclpy 라이브러리를 사용하여 ROS2 노드를 작성하고, 토픽을 송신(publish)하고 수신(subscribe)하는 방법을 설명합니다.

## 1. 토픽 메시지 송신 (Publisher)
파이썬에서 토픽 메시지를 보내는 방법은 rclpy.Publisher를 사용하여 publish() 메서드로 메시지를 전송하는 방식입니다. 아래는 geometry_msgs/Twist 메시지 타입을 사용하여 cmd_vel 토픽으로 메시지를 보내는 예시입니다.

### 1.1 Publisher 예시 코드
```
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        # Publisher 객체 생성, 'cmd_vel' 토픽에 Twist 메시지 타입으로 메시지 전송
        self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # 1초마다 메시지를 발행하는 타이머 설정
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # Twist 메시지 객체 생성
        msg = Twist()
        
        # 메시지에 속도 값 설정 (예: 선형 속도)
        msg.linear.x = 0.5  # 0.5 m/s로 전진
        msg.angular.z = 0.1  # 0.1 rad/s로 회전
        
        # 메시지를 'cmd_vel' 토픽으로 발행
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: linear.x = {msg.linear.x}, angular.z = {msg.angular.z}")

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    
    # 2초마다 노드를 실행
    rclpy.spin(minimal_publisher)
    
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
설명
create_publisher(): cmd_vel이라는 토픽에 Twist 메시지 타입을 발행하기 위해 사용됩니다.

timer_callback(): 1초마다 호출되는 콜백 함수로, Twist 메시지를 만들어서 cmd_vel 토픽으로 발행합니다.

publish(): 실제로 메시지를 전송하는 메서드입니다.

rclpy.spin(): ROS2 노드를 실행시키는 함수로, 계속해서 메시지를 발행하려면 노드를 계속 실행시켜야 합니다.

## 2. 토픽 메시지 구독 (Subscriber)
토픽을 구독하려면 rclpy.Subscriber를 사용합니다. 구독한 메시지를 받을 콜백 함수를 정의하고, subscribe() 메서드로 해당 토픽을 구독합니다.

### 2.1 Subscriber 예시 코드
```
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        
        # 'cmd_vel' 토픽을 구독하고, 구독할 메시지 타입은 Twist로 설정
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # 받은 메시지를 출력
        self.get_logger().info(f"Received: linear.x = {msg.linear.x}, angular.z = {msg.angular.z}")

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    
    # 노드를 실행하여 메시지를 수신하도록 함
    rclpy.spin(minimal_subscriber)
    
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
설명
create_subscription(): cmd_vel 토픽을 구독하고, Twist 메시지 타입을 받아올 수 있게 합니다.

listener_callback(): 메시지를 수신할 때 호출되는 콜백 함수입니다. 여기에서는 수신된 메시지를 로깅합니다.

rclpy.spin(): ROS2 노드를 실행시켜서 계속해서 메시지를 수신합니다.

## 3. 토픽 송수신 실습 예시
Publisher 실행: 위의 MinimalPublisher 코드를 실행하면, 로봇의 속도 정보를 1초마다 cmd_vel 토픽에 전송합니다.

Subscriber 실행: MinimalSubscriber 코드를 실행하면, cmd_vel 토픽을 구독하고, 로봇의 속도 정보가 수신될 때마다 해당 속도 값을 출력합니다.

## 4. 중요한 사항
콜백 함수: 구독자는 메시지를 수신할 때마다 listener_callback과 같은 콜백 함수를 호출합니다. 이 함수 내에서 메시지 처리 로직을 작성할 수 있습니다.

QoS (Quality of Service): 메시지를 전송하거나 구독할 때 QoS 설정을 조정할 수 있습니다. 이는 네트워크 환경에 따라 메시지의 신뢰성 및 전송 주기를 설정할 수 있습니다. 예를 들어, 10은 메시지 큐의 길이를 의미합니다.

```
from rclpy.qos import QoSProfile, QoSHistoryPolicy

qos_profile = QoSProfile(depth=10, history=QoSHistoryPolicy.KEEP_LAST)
```
이러한 설정은 주로 실시간 제어 시스템에서 중요한 역할을 합니다.

## 결론
ROS2에서 토픽을 사용하여 메시지를 송신하고 구독하는 방식은 매우 직관적입니다. rclpy.Publisher와 rclpy.Subscriber를 사용하면 간단하게 토픽을 통해 데이터를 전송하고 받을 수 있습니다. 위의 예시 코드를 바탕으로 토픽을 사용한 실시간 데이터 송수신을 구현할 수 있습니다.
