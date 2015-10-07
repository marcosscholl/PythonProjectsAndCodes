#include <LiquidCrystal.h>
#include <stdio.h> 
#include <rtc.h>
#include <Wire.h>
#include <Nunchuk.h>



Nunchuk nunchuk;
#define BPS 19200 //velocidade de comunicação

RTC relogio;

int nunx;  // DEFINIR PINAGEM!!!
int nuny;
int acelerometro;
int nb1; // nunchuck botão
int nb2;
int pot1;
int pot2;
int pot3;
boolean led1;
boolean led2;
boolean led3;
boolean led4;
int RESET;

int erro;
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);


// QUAL O TIPO DAS VARIAVEIS?
int NUNX;
int NUNY; 
int ACELEROMETROX;
int ACELEROMETROY;
int ACELEROMETROZ;
int NB1;
int NB2 ;
int POT1;
int POT2 ;
int POT3;
int RTCDia;
int RTCMes;
int RTCHora;
int RTCMin;
int RTCseg;
boolean LED1;
boolean LED2;
boolean LED3;
boolean LED4;


String IDENTIFICATION = "NX-01";

char cmd[25];      // Buffer de armazenamento de comandos
byte cmdCaractere; // Posicao apos o ultimo caractere armazenado
byte cmdErro;      // Ultimo codigo de erro

void setup(){
  
    relogio.init();
  //relogio.setDate(07,30,06,13);
  //relogio.setTime(23,59,50);
  //relogio.set(23,59,50,07,30,06,13);
  
  pinMode (pot1, INPUT);
  pinMode (pot2, INPUT);
  pinMode (pot3, INPUT);
  pinMode (led1, OUTPUT);
  pinMode (led2, OUTPUT);
  pinMode (led3, OUTPUT);
  pinMode (led4, OUTPUT);
  
    Serial.begin(BPS);
    lcd.begin(16, 2);
    cmdCaractere = 0; // Nao ha caracteres no buffer de comandos
    cmdErro = 0;
  

      
} // fim do setup

void loop() {
  
     NUNX = nunchuk.joystick_x();
     NUNY = nunchuk.joystick_y();
     ACELEROMETROX= nunchuk.x_acceleration();
     ACELEROMETROY= nunchuk.y_acceleration();
     ACELEROMETROZ= nunchuk.z_acceleration();
     NB1 = nunchuk.z_button();
     NB2 = nunchuk.c_button();
     POT1 = analogRead(pot1);
     POT2 = analogRead(pot2);
     POT3 = analogRead(pot3);
     RTCDia= relogio.day();
     RTCMes= relogio.month();
     RTCHora= relogio.hour();
     RTCMin= relogio.minutes();
     RTCseg= relogio.seconds();
  
    if (Serial.available()) {
        if (lerComando()) { // Processa o comando, se verdadeiro
           cmdErro = processarComando();
           aviso();
        } // Segue a vida  
    } 
} //fim do loop

/*
 * lerComando() - Le o caractere disponivel na porta serial e o armazena no buffer de comandos
 *                Se o caractere for um ;, retorna verdadeiro, pois o comando foi completado
 *                Caso contrario, retorna falso, pois ainda nao tem um comando para processar
 */
char lerComando() {
   cmd[cmdCaractere] = Serial.read();
   return cmd[cmdCaractere++] == ';';  
}

char processarComando(){
    erro = 0; // Inialmente funcionando
    
        switch (cmd[0]) {
    //WHO?
            case 'W' : Serial.write(255); // Endereco da variavel
                   Serial.print(IDENTIFICATION);
                   Serial.write(';'); // Termina a comunicacao
                   break;
   //Reset                
            case 'R' : Serial.write(0); // Endereco da variavel
                   digitalWrite(RESET, HIGH);
                   digitalWrite(RESET, LOW);
                   Serial.write(';'); // Termina a comunicacao
                   break;    
    //get           
            case 'G' : switch (cmd[1]) {
                     case 1: 
                             Serial.write(1); // Endereco da variavel
                             Serial.print(NUNX, DEC);
                             Serial.write(';'); // Termina a comunicacao
                             break;
                     case 2: 
                             Serial.write(2); 
                             Serial.print(NUNY, DEC);
                             Serial.write(';');
                             break;              
                     case 3: 
                             Serial.write(3); 
                             Serial.print(ACELEROMETROX, DEC);
                             Serial.write(';');   
                             break;
                             
                     case 4: 
                             Serial.write(4); 
                             Serial.print(ACELEROMETROY, DEC);
                             Serial.write(';');   
                             break;
                             
                     case 5: 
                             Serial.write(5); 
                             Serial.print(ACELEROMETROZ, DEC);
                             Serial.write(';');   
                             break;
                     case 6: 
                             Serial.write(6); 
                             Serial.print(NB1, DEC);
                             Serial.write(';');   
                             break;
                     case 7: 
                             Serial.write(7);
                             Serial.print(NB2, DEC);
                             Serial.write(';');  
                             break;
                     case 8: 
                             Serial.write(8); 
                             Serial.print(POT1, DEC);
                             Serial.write(';'); 
                             break;
                     case 9:
                             Serial.write(9); 
                             Serial.print(POT2, DEC);
                             Serial.write(';'); 
                             break;
                     case 10:
                             Serial.write(10); 
                             Serial.print(POT3, DEC);
                             Serial.write(';'); 
                             break;
                      case 11:
                             Serial.write(11); 
                             Serial.print(LED1, DEC);
                             Serial.write(';'); 
                             break;             
                      case 12:
                             Serial.write(12); 
                             Serial.print(LED2, DEC);
                             Serial.write(';'); 
                             break;           
                      case 13:
                             Serial.write(13); 
                             Serial.print(LED3, DEC);
                             Serial.write(';');   
                             break;    
                      case 14:
                             Serial.write(14); 
                             Serial.print(LED4, DEC);
                             Serial.write(';');   
                             break;    
     
                      case 15:
                             Serial.write(15);
                             Serial.print(RTCDia);
                             Serial.write(';');
                             break;
                      case 16:
                             Serial.write(16); 
                             Serial.print(RTCMes);
                             Serial.write(';');
                             break;
                             
                      case 17:
                             Serial.write(17); 
                             Serial.print(RTCHora);
                             Serial.write(';');
                             break;
                             
                      case 18:
                             Serial.write(18); 
                             Serial.print(RTCMin);
                             Serial.write(';');
                             break;
                             
                      case 19:
                             Serial.write(19); 
                             Serial.print(RTCseg);
                             Serial.write(';');
                             break;
                             
             
               default: erro = 2;  //se achar o G, e nao funcionar é pq a sintaxe ta errada
                   } // fim do switch do get
                   
                   break; // break do get    
                   
           case 'M' :  switch (cmd[2]) {
                         
             
             
                     case 1: 
                             Serial.write(1); // Endereco da variavel
                             lcd.print(NUNX, DEC);
                             Serial.write(';'); // Termina a comunicacao
                             break;
                     case 2: 
                             Serial.write(2); 
                             lcd.print(NUNY, DEC);
                             Serial.write(';');
                             break;              
                     case 3: 
                             Serial.write(3); 
                             lcd.print(ACELEROMETROX, DEC);
                             Serial.write(';');   
                             break;
                             
                     case 4: 
                             Serial.write(4); 
                             lcd.print(ACELEROMETROY, DEC);
                             Serial.write(';');   
                             break;
                             
                     case 5: 
                             Serial.write(5); 
                             lcd.print(ACELEROMETROZ, DEC);
                             Serial.write(';');   
                             break;
                     case 6: 
                             Serial.write(6); 
                             lcd.print(NB1, DEC);
                             Serial.write(';');   
                             break;
                     case 7: 
                             Serial.write(7);
                             lcd.print(NB2, DEC);
                             Serial.write(';');  
                             break;
                     case 8: 
                             Serial.write(8); 
                             lcd.print(POT1, DEC);
                             Serial.write(';'); 
                             break;
                     case 9:
                             Serial.write(9); 
                             lcd.print(POT2, DEC);
                             Serial.write(';'); 
                             break;
                     case 10:
                             Serial.write(10); 
                             lcd.print(POT3, DEC);
                             Serial.write(';'); 
                             break;
                      case 11:
                             Serial.write(11); 
                             lcd.print(LED1, DEC);
                             Serial.write(';'); 
                             break;             
                      case 12:
                             Serial.write(12); 
                             lcd.print(LED2, DEC);
                             Serial.write(';'); 
                             break;           
                      case 13:
                             Serial.write(13); 
                             lcd.print(LED3, DEC);
                             Serial.write(';');   
                             break;    
                      case 14:
                             Serial.write(14); 
                             lcd.print(LED4, DEC);
                             Serial.write(';');   
                             break;    
     
                      case 15:
                             Serial.write(15);
                             lcd.print(RTCDia);
                             Serial.write(';');
                             break;
                      case 16:
                             Serial.write(16); 
                             lcd.print(RTCMes);
                             Serial.write(';');
                             break;
                             
                      case 17:
                             Serial.write(17); 
                             lcd.print(RTCHora);
                             Serial.write(';');
                             break;
                             
                      case 18:
                             Serial.write(18); 
                             lcd.print(RTCMin);
                             Serial.write(';');
                             break;
                             
                      case 19:
                             Serial.write(19); 
                             lcd.print(RTCseg);
                             Serial.write(';');
                             break;
         }
                   
            // limpa o LCD
          case 'C' : Serial.write(20); 
                     lcd.clear();
                     Serial.write(';'); // Termina a comunicacao
                     break;        
                   
        case 'N' :   Serial.write(42); 
                     Serial.print(NUNX, DEC);
                     Serial.print(NUNY, DEC);
                     Serial.print(ACELEROMETROX, DEC);
                     Serial.print(ACELEROMETROY, DEC);
                     Serial.print(ACELEROMETROZ, DEC);
                     Serial.print(NB1, DEC);
                     Serial.print(NB2, DEC);
                     Serial.write(';'); // Termina a comunicacao  
                     break;  
     
        case 'U' : switch (cmd[3]) {


          
                     case 1: 
                             Serial.write(1); // Endereco da variavel
                             NUNX = nunchuk.joystick_x();
                             Serial.write(';'); // Termina a comunicacao
                             break;
                     case 2: 
                             Serial.write(2); 
                             NUNY = nunchuk.joystick_y();
                             Serial.write(';');
                             break;              
                     case 3: 
                             Serial.write(3); 
                             ACELEROMETROX= nunchuk.x_acceleration();
                             Serial.write(';');
                             break;
                     case 4: 
                             Serial.write(4); 
                             ACELEROMETROY= nunchuk.y_acceleration();
                             Serial.write(';');
                             break;
                     case 5: 
                             Serial.write(5); 
                             ACELEROMETROZ= nunchuk.z_acceleration();
                             Serial.write(';');
                             break;
                          
                     case 6: 
                             Serial.write(6); 
                             NB1 = nunchuk.z_button();     //ler nb1
                             Serial.write(';'); 
                             break;
                     case 7: 
                             Serial.write(7);
                             NB2 = nunchuk.c_button();
                             Serial.write(';');   
                             break;
                     case 8: 
                             Serial.write(8); 
                             POT1 = analogRead(pot1);
                             Serial.write(';'); 
                             break;
                      case 9:
                             Serial.write(9); 
                             POT2 = analogRead(pot2);
                             Serial.write(';');   
                             break;
                      case 10:
                             Serial.write(10); 
                             POT3 = analogRead(pot3);
                             Serial.write(';');
                             break;
                      case 11:
                             Serial.write(11);
                             RTCDia= relogio.day();
                             Serial.write(';');
                             break;
                      case 12:
                             Serial.write(12); 
                             RTCMes= relogio.month();
                             Serial.write(';');
                             break;
                             
                      case 13:
                             Serial.write(13); 
                             RTCHora= relogio.hour();
                             Serial.write(';');
                             break;
                             
                      case 14:
                             Serial.write(14); 
                             RTCMin= relogio.minutes();
                             Serial.write(';');
                             break;
                             
                      case 15:
                             Serial.write(15); 
                             RTCseg= relogio.seconds();
                             Serial.write(';');
                             break;
                        
                        default: erro=2;      }   
                            
        default: erro = 1;            
    } // fim do switch geral

  cmdCaractere = 0; // Reseta o buffer para receber um novo comando
    return erro;

}// fim da função

void aviso(){
  if (erro==1){
    Serial.println("comando inexiste");
  }
  if (erro==2){
    Serial.println("erro de sintaxe");
  }
}

