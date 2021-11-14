add_library(log-statements log-statements.cpp)
target_include_directories(
  log-statements
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
)