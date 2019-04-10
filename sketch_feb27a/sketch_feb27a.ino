#include <LiquidCrystal.h>
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

unsigned int intToBin(int num) {
  int t;
  lcd.setCursor(0, 0);
  while (num > 0) {
    t*=10;
    if (num % 2 != 0) {
      t++;
    }
    num /= 2;
  }
  return t;
}
int binToInt(byte b)
{
  int dec = 0;
  int power = 1;
  byte mask;
  int weight;
  for (mask = 0x01; mask; mask <<= 1)
  {
    if (b & mask)
    {
      weight = 1;
    }
    else
    {
      weight = 0;
    }

    dec = dec + (power * weight);
    power = power * 2;
  }
  return dec;
}

void setup() {
  lcd.begin(16, 2);

  unsigned int val = intToBin(10);
  //int val = binToInt(101);

  lcd.print(val);
}
void loop() {
}
