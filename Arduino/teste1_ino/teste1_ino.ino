void setup() {
    Serial.begin(9600);
}

void loop() {
    for(int i=1;i<=3;i++){
        String servo = Serial.readStringUntil(':');
        if(servo!=""){
            //here you could check the servo number
            String pos = Serial.readStringUntil('&');
            int int_pos=pos.toInt();
            Serial.println("Pos");
            Serial.println(int_pos);
        }
    }
}
