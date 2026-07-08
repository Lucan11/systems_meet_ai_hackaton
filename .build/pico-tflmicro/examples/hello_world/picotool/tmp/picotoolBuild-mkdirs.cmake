# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/lucan/projects/vlc_hackaton/.deps/picotool/picotool-src"
  "/home/lucan/projects/vlc_hackaton/.deps/picotool/picotool-build"
  "/home/lucan/projects/vlc_hackaton/.deps/picotool"
  "/home/lucan/projects/vlc_hackaton/.build/pico-tflmicro/examples/hello_world/picotool/tmp"
  "/home/lucan/projects/vlc_hackaton/.build/pico-tflmicro/examples/hello_world/picotool/src/picotoolBuild-stamp"
  "/home/lucan/projects/vlc_hackaton/.build/pico-tflmicro/examples/hello_world/picotool/src"
  "/home/lucan/projects/vlc_hackaton/.build/pico-tflmicro/examples/hello_world/picotool/src/picotoolBuild-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/lucan/projects/vlc_hackaton/.build/pico-tflmicro/examples/hello_world/picotool/src/picotoolBuild-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/lucan/projects/vlc_hackaton/.build/pico-tflmicro/examples/hello_world/picotool/src/picotoolBuild-stamp${cfgdir}") # cfgdir has leading slash
endif()
