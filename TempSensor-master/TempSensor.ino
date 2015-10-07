/* Temperature Sensor (LM35)
 * Ozan Caglayan 2012 - Medical Informatics 2nd Project
 *
 * The temperature in Celsius is sent through the serial link (TX)
 * which is read and transmitted by the DIN of the XBEE Router.
 * The coordinator can then read the values over its serial port.
 */

int sensorPin = 5;    // select the input pin for the potentiometer
float temperature = 0.0;  // variable to store the value coming from the sensor

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Read from sensor, divide by 1024 and multiply by 5000
  // restore mV value, divide by 10 to have temperature in C.

  temperature = 0.0;
  // Smooth the readings by accumulating 8 readings
  // and then taking the average.
  for (int i = 0; i < 8; ++i)
    temperature += (5.0 * analogRead(sensorPin) * 100.0) / 1024.0;

  temperature /= 8.0;

  // Send the data over serial line for further Xbee processing
  Serial.println(temperature,1);

  // Delay for 1000 miliseconds
  delay(1000);
}
