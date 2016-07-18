
#include <wiringPi.h>

#include "rc-switch/RCSwitch.h"

extern "C" {

void setup() { wiringPiSetupSys(); }

RCSwitch* RCSwitch_RCSwitch() { return new RCSwitch(); }
void RCSwitch_enableTransmit(RCSwitch *s, int pin) { s->enableTransmit(pin); }
void RCSwitch_disableTransmit(RCSwitch *s) { s->disableTransmit(); }
void RCSwitch_switchOn(RCSwitch *s, const char *group, const char *device) { s->switchOn(group, device); }
void RCSwitch_switchOff(RCSwitch *s, const char *group, const char *device) { s->switchOff(group, device); }

}
