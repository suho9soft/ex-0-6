#define myled 2

void setup() {
  Serial.begin(9600);
  //LED를 제어하려면 출력으로 설정해야함!
  pinMode(myled,OUTPUT);
}
void loop() {
  //파이썬이 보낸 데이터를 어떻게 수신하지?
  //파이썬에서 보낸 데이터가 뭔가 존재한다!
  if(Serial.available() > 0){
    //파이썬이 문자 1개를 보내준다고 약속했다!
    char data = Serial.read();
    if(data == '0'){
      //LED 끈다
      digitalWrite(myled,LOW);
    }else if(data == '1'){
      //LED 켠다
      digitalWrite(myled,HIGH);
    }
  }
}

