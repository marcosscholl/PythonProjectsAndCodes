int ledPin = 13;  // choose the pin for the LED  
int val = 0;      // variable for reading the pin status  
char msg = '  ';   // variable to hold data from serial  
int var = 0;   
int aux = 0;  

void setup() {  
  pinMode(ledPin, OUTPUT);      // declare LED as output  
  Serial.begin(9600);  
  Serial.print("Program Iniciado\n");    
}  

void loop(){  
        // While data is sent over serial assign it to the msg  
    while (Serial.available()>0){   
        msg=Serial.read();  
    }  
  
  // Turn LED on/off if we recieve 'Y'/'N' over serial   
  if (msg=='S') {              
    digitalWrite(ledPin, HIGH);  // turn LED ON  
    Serial.print("LED Ativado\n");  
    msg=' ';  
    var = 0;
    aux=0;
  } else if (msg=='N') {  
     if (var == 0) {
       Serial.print("LED Desativado\n"); 
       var++;
       msg=' ';
       aux=0;
     }
     
    digitalWrite(ledPin, LOW); // turn LED OFF  
  } else if (msg=='f') {  
      if (aux == 0) {
        Serial.print("sair\n"); 
       msg=' ';
        aux++;
        var=0;
      }
      
   

  }  
}  
