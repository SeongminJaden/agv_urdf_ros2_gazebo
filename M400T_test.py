import serial
import time

# 시리얼 포트 설정
ser = serial.Serial('/dev/ttyUSB0', baudrate=19200, timeout=1)

# Checksum 계산 함수
def calculate_checksum(packet):
    checksum_value = sum(packet) & 0xFF
    checksum = (~checksum_value + 1) & 0xFF
    return checksum

# RPM 값을 받아 패킷 전송하는 함수
def send_packet(rpm1, rpm2):
    # 음수 처리 (2의 보수로 unsigned 16bit 변환)
    rpm1_unsigned = rpm1 & 0xFFFF
    rpm2_unsigned = rpm2 & 0xFFFF

    # 바이트 분리
    rpm1_low = rpm1_unsigned & 0xFF
    rpm1_high = (rpm1_unsigned >> 8) & 0xFF
    rpm2_low = rpm2_unsigned & 0xFF
    rpm2_high = (rpm2_unsigned >> 8) & 0xFF

    # 패킷 생성
    packet = [183, 184, 1, 207, 7, 1, rpm1_low, rpm1_high, 1, rpm2_low, rpm2_high, 0]

    # Checksum 계산
    checksum = calculate_checksum(packet)

    # 패킷에 Checksum 추가
    packet.append(checksum)

    # 디버깅 출력
    print(f"Sending packet: {packet}")

    # 시리얼로 전송
    ser.write(bytearray(packet))

# 모터 1: 2000 RPM, 모터 2: -1500 RPM
send_packet(2000, -1500)
time.sleep(2)
ser.close()
