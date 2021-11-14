cmake_minimum_required(VERSION 3.7)
project(TestLogging VERSION 1.0)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Werror")

add_subdirectory(LogLib)
add_executable(TestLogging TestLogging.cpp)
target_link_libraries(TestLogging PUBLIC LogLib)