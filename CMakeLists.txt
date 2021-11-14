cmake_minimum_required(VERSION 3.7)
project(TestLogging)
add_subdirectory(log-statements)
add_executable(test-logging test-logging.cpp)
target_link_libraries(test-logging PUBLIC log-statements)
target_include_directories(
  test-logging PUBLIC
  "${PROJECT_BINARY_DIR}"
)