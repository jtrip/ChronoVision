static const uint8_t SET_BRIGHTNESS_CHARACTER = 0x08;
static int dataPins[] = {7, 8, 9, 10, 11, 12, 13, A0, A1, A2};
static int strobePin = A3;
//strobe timer stuff
const unsigned long strobe_time = 500; //timeout for the knob turn in thousandths of a second
unsigned long strobe_start_time = 0; //used for the count down timer
unsigned long current_time = millis();
#include <M66004Vfd.h> // VFD library.
#include <HpLaserJetControl.h> // Button and LED library.

#include <Encoder.h>
M66004Vfd vfd(6, 4, 5);
Encoder myEnc(2, 3);
long oldPosition  = -999;
long offset = 2014;
void setup() {
  Serial.begin(115200);
  pinMode(strobePin, OUTPUT);
  for (int i = 0; i < sizeof(dataPins) / sizeof(dataPins[0]); i++)
  {
    pinMode(dataPins[i], OUTPUT);
  }
  // Prepare the VFD library for use.
  vfd.begin(16, 1);

  // Sets all pixels on the display.
  vfd.allDisplay();

  // Enables normal character display.
  vfd.display();

  // Print some text to the display.
  vfd.print("Year: ");
}

void loop() {
  //vfd.commandCharacter(SET_BRIGHTNESS_CHARACTER | 0b111);
  // Draw heart beat.
  // vfd.write(((millis() % 1000) < 250) ? 1 : 0);
  current_time = millis();
  vfd.setCursor(8, 0);
  long newPosition = myEnc.read() / 3;


  newPosition += offset;
  if (newPosition != oldPosition) {
    Serial.println(newPosition - 849);
    	for (int j = 0; j < sizeof(dataPins) / sizeof(dataPins[0]); ++j)
		digitalWrite(dataPins[j], ((newPosition - 849) & (1 << j)));
    //output to parallel interface here--------------------------------------------------------------------------
    strobe_start_time = current_time;
    if (newPosition >= 2500)
    {
      offset -= (newPosition - 2500);
      newPosition = 2500;
    }

    oldPosition = newPosition;

    vfd.setCursor(0, 0);
    vfd.print("Year:           ");
    vfd.setCursor(6, 0);
    if (newPosition < 1500)
    {
      newPosition += -(3 * abs(newPosition - 1500));
    }
    if (newPosition < 0)
    {
      newPosition += -(3 * abs(newPosition));
    }
    if (newPosition < -1000)
    {
      newPosition += -(10 * abs(newPosition + 1000));
    }
    if (newPosition < -10000)
    {
      newPosition += -(10 * abs((newPosition + 10000)));
    }        if (newPosition < -100000)
    {
      newPosition += -(10 * abs((newPosition + 100000)));
    } if (newPosition < -1000000)
    {
      newPosition += -(10 * abs((newPosition + 1000000)));
    } if (newPosition < -10000000)
    {
      newPosition += -(10 * abs((newPosition + 10000000)));
      vfd.print("Big Bang");
    }

    else
    {
      vfd.print(abs(newPosition));

      if (newPosition >= 0) {

        vfd.print(" AD");
      } else
      {
        vfd.print(" BC");
      }
    } if (newPosition < -100000000)
    {
      offset += 15;
    }
  }
  if (current_time - strobe_start_time > strobe_time) //strobe timer loop
  {
    digitalWrite(strobePin, 1);
  } else {
    digitalWrite(strobePin, 0);
  }
}

