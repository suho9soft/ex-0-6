# ex-0-6
Python
아두이노 코드 (4개의 LED 제어)
아두이노의 핀 4개에 LED를 연결하고, 파이썬으로 버튼 신호를 보내 제어합니다.
///

#define LED1 2
#define LED2 3
#define LED3 4
#define LED4 5

void setup() {
    Serial.begin(9600);
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
    pinMode(LED4, OUTPUT);
}

void loop() {
    if (Serial.available() > 0) {
        char data = Serial.read();

        switch (data) {
            case '1': // LED1 ON
                digitalWrite(LED1, HIGH);
                break;
            case '2': // LED1 OFF
                digitalWrite(LED1, LOW);
                break;
            case '3': // LED2 ON
                digitalWrite(LED2, HIGH);
                break;
            case '4': // LED2 OFF
                digitalWrite(LED2, LOW);
                break;
            case '5': // LED3 ON
                digitalWrite(LED3, HIGH);
                break;
            case '6': // LED3 OFF
                digitalWrite(LED3, LOW);
                break;
            case '7': // LED4 ON
                digitalWrite(LED4, HIGH);
                break;
            case '8': // LED4 OFF
                digitalWrite(LED4, LOW);
                break;
            default:
                break;
        }
    }
}


///
파이썬 코드 (4개의 버튼으로 제어)
파이썬 프로그램에 4개의 버튼을 추가하여 각각의 LED를 켜고 끌 수 있도록 설정합니다.
그리고 Python 이게 명령프롬프트 에서 작성 하는 것니다 그리고 폼으로 도 작성해 보겠습니다
///

import serial
import time

# 아두이노 포트를 설정하세요
arduino_port = 'COM3'  # 실제 포트로 변경
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
        '8': '8'   # LED4 OFF
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
    exit: 종료
    """)
    user_input = input("버튼 번호를 입력하세요: ")
    if user_input.lower() == 'exit':
        print("프로그램 종료")
        break
    control_led(user_input)

# 직렬 포트 닫기
arduino.close()


///
