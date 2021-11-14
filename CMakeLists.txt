cmake_minimum_required(VERSION 3.7)
project(test-logging VERSION 1.0)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Werror")

add_subdirectory(log-lib)
add_executable(test-logging test-logging.cpp)
target_link_libraries(test-logging PUBLIC log-lib)