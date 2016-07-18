cmake_minimum_required(VERSION 3.5)
project(PiHomeAutoLib)

set(PY_MODULE_NAME rcswitch)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -DRPI -lwiringPi")

set(RCSWITCH_FILES rc-switch/RCSwitch.h rc-switch/RCSwitch.cpp)

add_library(rcswitch SHARED ${RCSWITCH_FILES} bindings.cpp)

set_target_properties(rcswitch PROPERTIES
	LIBRARY_OUTPUT_DIRECTORY "rcswitch"
)

add_custom_command(
	TARGET rcswitch POST_BUILD
	COMMAND ${CMAKE_COMMAND} -E copy
		${CMAKE_SOURCE_DIR}/rcswitch.py
		${CMAKE_CURRENT_BINARY_DIR}/rcswitch/__init__.py)

