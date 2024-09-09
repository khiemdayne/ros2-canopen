cmake_minimum_required(VERSION 3.8)
project(canopen_tests)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(lely_core_libraries REQUIRED)


cogen_dcf(cia402_system)
cogen_dcf(cia402_namespaced_system)
cogen_dcf(cia402)
generate_dcf(cia402_lifecycle)
cogen_dcf(cia402_diagnostics)
generate_dcf(robot_control)

install(DIRECTORY
  launch rviz urdf 
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
