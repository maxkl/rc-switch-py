cmake_minimum_required(VERSION 3.5)
project(rc-switch-py CXX)

set(CMAKE_CXX_STANDARD 11)
add_definitions(-DRPI)

add_library(rcswitch SHARED
	"rc-switch/RCSwitch.h"
	"rc-switch/RCSwitch.cpp"
	"bindings.cpp"
)

target_link_libraries(rcswitch wiringPi)

set_target_properties(rcswitch PROPERTIES
	LIBRARY_OUTPUT_DIRECTORY "rcswitch"
)

add_custom_command(TARGET rcswitch
	POST_BUILD
	COMMAND ${CMAKE_COMMAND} -E copy
		"${CMAKE_SOURCE_DIR}/rcswitch.py"
		"${CMAKE_CURRENT_BINARY_DIR}/rcswitch/__init__.py"
)
