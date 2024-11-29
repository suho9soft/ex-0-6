#define NUM_LEDS 8

// LED 핀 번호를 배열로 정의
const int myled[NUM_LEDS] = {2, 3, 4, 5, 6, 7, 8, 9};

void setup() {
  Serial.begin(9600);
  // 각 LED 핀을 출력으로 설정
  for (int i = 0; i < NUM_LEDS; i++) {
    pinMode(myled[i], OUTPUT);
  }
}

void loop() {
  // 파이썬에서 데이터를 보내는지 확인
  if (Serial.available() >= NUM_LEDS) {
    // 파이썬에서 8개의 문자 데이터를 보내준다고 가정
    for (int i = 0; i < NUM_LEDS; i++) {
      char data = Serial.read(); // 한 문자씩 읽기
      if (data == '0') {
        // 해당 LED 끄기
        digitalWrite(myled[i], LOW);
      } else if (data == '1') {
        // 해당 LED 켜기
        digitalWrite(myled[i], HIGH);
      }
    }
  }
}
