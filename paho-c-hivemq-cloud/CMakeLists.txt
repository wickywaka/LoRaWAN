cmake_minimum_required(VERSION 3.22)
project(pahoo_mqtt)

set(CMAKE_CXX_STANDARD 14)
add_executable(pahoo_mqtt main.cpp)

target_link_libraries(pahoo_mqtt paho-mqtt3cs)

target_include_directories(pahoo_mqtt
        PRIVATE
        /home/waqar/workspace/myspace/paho-c-hivemq-cloud)
