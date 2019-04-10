
#include <LiquidCrystal.h>
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

int timeoutKey=200;
int lcd_key=5;
int ch;

#define btnRIGHT  0
#define btnUP     1
#define btnDOWN   2
#define btnLEFT   3
#define btnSELECT 4
#define btnNONE   5

int read_LCD_buttons()
{
  int adc_key_in = analogRead(0);      // read the value from the sensor
  // my buttons when read are centered at these valies: 0, 144, 329, 504, 741
  // we add approx 50 to those values and check to see if we are close
  if (adc_key_in > 1000) return btnNONE; // We make this the 1st option for speed reasons since it will be the most likely result
  if (adc_key_in < 50)   return btnRIGHT;
  if (adc_key_in < 195)  return btnUP;
  if (adc_key_in < 380)  return btnDOWN;
  if (adc_key_in < 555)  return btnLEFT;
  if (adc_key_in < 790)  return btnSELECT;
  return btnNONE;  // when all others fail, return this...
}

void setup() {
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("LCD&Serial test");
  delay(1000);
  lcd.clear();
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    delay(100);
    lcd.clear();
    lcd.setCursor(0, 0);
    while (Serial.available() > 0) {
      ch=Serial.read();
      if (ch==10) {
        lcd.setCursor(0, 1);
        continue;
      }
      lcd.write(ch);
    }
  }
  lcd.setCursor(0, 1);           // move to the begining of the second line
  
  lcd_key = read_LCD_buttons();
  switch (lcd_key)
  {
    case btnRIGHT:
      {
        delay(timeoutKey);
        if(read_LCD_buttons()==lcd_key){
          Serial.print("rr");
        }else{
          Serial.print("r");
        }
        break;
      }
    case btnLEFT:
      {
        delay(timeoutKey);
        if(read_LCD_buttons()==lcd_key){
          Serial.print("ll");
        }else{
          Serial.print("l");
        }
        break;
      }
    case btnUP:
      {
        delay(timeoutKey);
        if(read_LCD_buttons()==lcd_key){
          Serial.print("uu");
        }else{
          Serial.print("u");
        }
        break;
      }
    case btnDOWN:
      {
        delay(timeoutKey);
        if(read_LCD_buttons()==lcd_key){
          Serial.print("dd");
        }else{
          Serial.print("d");
        }
        break;
      }
    case btnSELECT:
      {
        delay(1000);
        if(read_LCD_buttons()==lcd_key){
          Serial.print("ss");
        }else{
          Serial.print("s");
        }
        break;
      }
    case btnNONE:
      {
        //Serial.print("NONE  ");
        break;
      }
  }
  while(read_LCD_buttons()<5){delay(1);}
}
