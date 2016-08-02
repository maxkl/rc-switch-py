
# Building

This requires wiringPi

```sh
mkdir build && cd build
cmake ..
make
```

`build/rcswitch` is the final python module

# Usage

Copy `build/rcswitch` to your python project, use it like this:

```py
from rcswitch import RCSwitch

RCSwitch.setup()

my_switch = RCSwitch()
my_switch.enable_transmit(4)
# my_switch.disable_transmit()
my_switch.switch_on('01101', '10000')
my_switch.switch_off('01101', '01000')
```
