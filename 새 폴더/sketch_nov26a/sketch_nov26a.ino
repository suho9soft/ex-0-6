#define LED1 26
#define LED2 28
#define LED3 30
#define LED4 32
#define LED5 34
#define LED6 36
#define LED7 38
#define LED8 40

void setup() {
    Serial.begin(9600);
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
    pinMode(LED4, OUTPUT);
    pinMode(LED5, OUTPUT);
    pinMode(LED6, OUTPUT);
    pinMode(LED7, OUTPUT);
    pinMode(LED8, OUTPUT);
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
            case '9': // LED5 ON
                digitalWrite(LED5, HIGH);
                break;
            case 'A': // LED5 OFF
                digitalWrite(LED5, LOW);
                break;
            case 'B': // LED6 ON
                digitalWrite(LED6, HIGH);
                break;
            case 'C': // LED6 OFF
                digitalWrite(LED6, LOW);
                break;
            case 'D': // LED7 ON
                digitalWrite(LED7, HIGH);
                break;
            case 'E': // LED7 OFF
                digitalWrite(LED7, LOW);
                break;
            case 'F': // LED8 ON
                digitalWrite(LED8, HIGH);
                break;
            case 'G': // LED8 OFF
                digitalWrite(LED8, LOW);
                break;
            default:
                break;
        }
    }
}
