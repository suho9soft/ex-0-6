import serial
import time

# 아두이노 포트를 설정하세요
arduino_port = 'COM10'  # 실제 포트로 변경
baud_rate = 9600

# 직렬 포트 연결
try:
    arduino = serial.Serial(arduino_port, baud_rate, timeout=1)
    print(f"아두이노가 {arduino_port}에 연결되었습니다.")
    time.sleep(2)  # 초기화 시간 대기
except Exception as e:
    print(f"아두이노 연결 오류: {e}")
    exit()

# LED 제어 함수
def control_led(button):
    commands = {
        '1': '1',  # LED1 ON
        '2': '2',  # LED1 OFF
        '3': '3',  # LED2 ON
        '4': '4',  # LED2 OFF
        '5': '5',  # LED3 ON
        '6': '6',  # LED3 OFF
        '7': '7',  # LED4 ON
        '8': '8',  # LED4 OFF
        '9': '9',  # LED5 ON
        'A': 'A',  # LED5 OFF
        'B': 'B',  # LED6 ON
        'C': 'C',  # LED6 OFF
        'D': 'D',  # LED7 ON
        'E': 'E',  # LED7 OFF
        'F': 'F',  # LED8 ON
        'G': 'G'   # LED8 OFF
    }

    if button not in commands:
        print("잘못된 입력입니다. 유효한 버튼 번호를 입력하세요.")
        return

    try:
        arduino.write(commands[button].encode())
        print(f"명령 전송: {commands[button]}")
    except Exception as e:
        print(f"데이터 전송 오류: {e}")

# 버튼 입력 루프
while True:
    print("""
    1: LED1 ON    2: LED1 OFF
    3: LED2 ON    4: LED2 OFF
    5: LED3 ON    6: LED3 OFF
    7: LED4 ON    8: LED4 OFF
    9: LED5 ON    A: LED5 OFF
    B: LED6 ON    C: LED6 OFF
    D: LED7 ON    E: LED7 OFF
    F: LED8 ON    G: LED8 OFF
    exit: 종료
    """)
    user_input = input("버튼 번호를 입력하세요: ")
    if user_input.lower() == 'exit':
        print("프로그램 종료")
        break
    control_led(user_input)

# 직렬 포트 닫기
arduino.close()
