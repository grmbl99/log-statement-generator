add_custom_command(
  OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/log-statements.cpp ${CMAKE_CURRENT_SOURCE_DIR}/log-statements.h
  COMMAND ${PROJECT_SOURCE_DIR}/generate-cpp/generate-cpp.py ${PROJECT_SOURCE_DIR}/log-interface.json ${CMAKE_CURRENT_SOURCE_DIR}/log-statements.cpp ${CMAKE_CURRENT_SOURCE_DIR}/log-statements.h
  DEPENDS ${PROJECT_SOURCE_DIR}/generate-cpp/generate-cpp.py ${PROJECT_SOURCE_DIR}/log-interface.json
)
add_library(log-statements log-statements.cpp)
target_include_directories(
  log-statements
  INTERFACE ${CMAKE_CURRENT_SOURCE_DIR}
)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14 -Werror")