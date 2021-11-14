add_custom_command(
  OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/log-lib.cpp ${CMAKE_CURRENT_SOURCE_DIR}/log-lib.h
  COMMAND ${PROJECT_SOURCE_DIR}/generate-cpp/generate-cpp.py ${PROJECT_SOURCE_DIR}/log-interface.json ${CMAKE_CURRENT_SOURCE_DIR}/log-lib.cpp ${CMAKE_CURRENT_SOURCE_DIR}/log-lib.h
  DEPENDS ${PROJECT_SOURCE_DIR}/generate-cpp/generate-cpp.py ${PROJECT_SOURCE_DIR}/log-interface.json
)
add_library(log-lib log-lib.cpp)
target_include_directories(log-lib INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})