cmake_minimum_required(VERSION 3.7)
project(TestLogging VERSION 1.0
        DESCRIPTION "Test generated log-statements"
        LANGUAGES CXX)
add_subdirectory(log-statements)
add_executable(test test.cpp)
target_link_libraries(test PUBLIC log-statements)

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
target_include_directories(test PUBLIC
                          "${PROJECT_BINARY_DIR}"
                          "${PROJECT_SOURCE_DIR}/log-statements"
                          )