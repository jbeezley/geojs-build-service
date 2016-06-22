set(CTEST_SOURCE_DIRECTORY "/Users/jbeezley/git/geojs-build-service/tmp/source")
set(CTEST_BINARY_DIRECTORY "/Users/jbeezley/git/geojs-build-service/tmp/build")

set(CTEST_BUILD_NAME "geojs-build-service")
set(CTEST_CMAKE_GENERATOR "Unix Makefiles")

find_package(Git)
set(CTEST_GIT_COMMAND ${GIT_EXECUTABLE})

set(CTEST_UPDATE_COMMAND "${CTEST_GIT_COMMAND}")

ctest_start("Experimental")
ctest_update()
