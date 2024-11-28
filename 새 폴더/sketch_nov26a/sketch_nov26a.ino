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
