import serial
import time

# 시리얼 포트 설정
ser = serial.Serial('COM9', baudrate=19200, timeout=1)

# Checksum 계산 함수
def calculate_checksum(packet):
    checksum_value = sum(packet) & 0xFF  # 모든 바이트 더함
    checksum = (~checksum_value + 1) & 0xFF  # 보완 후 1 더함
    return checksum

# RPM 값을 받아 패킷 전송하는 함수
def send_packet(rpm1, rpm2):
    # RPM을 바이트로 변환
    rpm1_low = rpm1 & 0xFF
    rpm1_high = (rpm1 >> 8) & 0xFF
    rpm2_low = rpm2 & 0xFF
    rpm2_high = (rpm2 >> 8) & 0xFF

    # 패킷 생성
    packet = [183, 184, 1, 207, 7, 1, rpm1_low, rpm1_high, 1, rpm2_low, rpm2_high, 0]

    # Checksum 계산
    checksum = calculate_checksum(packet)
    
    # 패킷에 Checksum 추가
    packet.append(checksum)

    # 전송할 패킷 출력 (디버깅 용도)
    print(f"Sending packet: {packet}")

    # 패킷을 바이트 배열로 변환 후 전송
    ser.write(bytearray(packet))

# 모터 1: 정회전 (2000 RPM), 모터 2: 역회전 (-1500 RPM)
send_packet(2000, 1500)  # 모터 1에 2000 RPM 정회전
send_packet(2000, -1500)  # 모터 2에 1500 RPM 역회전
time.sleep(2)
ser.close()
