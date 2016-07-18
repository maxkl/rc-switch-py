
# Building

This requires wiringPi

```
mkdir build && cd build
cmake ..
make
```

`build/rcswitch` is the final python module

# Usage

Copy `build/rcswitch` to your python project, use it like this:

```
import rcswitch

rcswitch.setup()

my_switch = rcswitch.RCSwitch()
my_switch.enable_transmit(4)
my_switch.switch_on('01101', '10000')
my_switch.switch_off('01101', '01000')
```
