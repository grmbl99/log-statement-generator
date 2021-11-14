add_custom_command(
  OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/LogLib.cpp ${CMAKE_CURRENT_SOURCE_DIR}/LogLib.h
  COMMAND ${PROJECT_SOURCE_DIR}/generate-cpp/generate-cpp.py ${PROJECT_SOURCE_DIR}/log-interface.json ${CMAKE_CURRENT_SOURCE_DIR}/LogLib.cpp ${CMAKE_CURRENT_SOURCE_DIR}/LogLib.h
  DEPENDS ${PROJECT_SOURCE_DIR}/generate-cpp/generate-cpp.py ${PROJECT_SOURCE_DIR}/log-interface.json
)
add_library(LogLib LogLib.cpp)
target_include_directories(LogLib INTERFACE ${CMAKE_CURRENT_SOURCE_DIR})