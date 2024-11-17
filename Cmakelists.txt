cmake_minimum_required(VERSION 3.21)

add_library(drivers INTERFACE)

function(add_driver NAME)
    if (NOT TARGET driver_${NAME})
        # Choosing not to add LIB_HARDWARE_ defines to avoid command line bloat pending a need (they aren't
        #   super interesting except to determine functionality as they are mostly passive accessors, however
        #   they could be useful to determine if the header is available.
        # pico_add_sdk_impl_library(driver_${NAME})
        add_library(driver_${NAME} INTERFACE)

        file(GLOB SOURCES ${CMAKE_CURRENT_LIST_DIR}/Src/*)
        target_sources(drivers PUBLIC ${SOURCES})

        target_include_directories(driver_${NAME} INTERFACE
                ${CMAKE_CURRENT_LIST_DIR}/Inc)
        target_link_libraries(drivers INTERFACE driver_${NAME})
    endif()
endfunction()

option(ENABLE_HAL_DRIVER "Enable HAL driver" ON)
option(ENABLE_LL_DRIVER "Enable LL driver" ON)
option(ENABLE_SYSTEM_XXX_C "Enable system_XXX.c" ON)
option(ENABLE_STARTUP_FILE "Enable startup file" ON)
option(ENABLE_LD_SCRIPT "Enable linker script" ON)
option(ENABLE_DEBUG_DEFINE "Enable debug define" ON)
set(MCU_MODEL "PY32F030x6" CACHE STRING "MCU model, like PY32F030x6")


set(MCU_MODEL_LOWER $<LOWER_CASE:${MCU_MODEL}>)
if("${MCU_MODEL}" MATCHES "PY32F002A|PY32F003|PY32F030")
    set(MCU_FAMILY "PY32F0xx")
    set(MCU_FAMILY_LOWER $<LOWER_CASE:${MCU_FAMILY}>)
endif()

target_include_directories(drivers INTERFACE CMSIS/Include)

if(${ENABLE_SYSTEM_XXX_C})
    target_sources(drivers PUBLIC CMSIS/Device/PY32F0xx/Source/system_${MCU_FAMILY_LOWER}.c)
    target_include_directories(drivers INTERFACE CMSIS/Device/PY32F0xx/Include)
endif()

if(${ENABLE_HAL_DRIVER})
    add_subdirectory(${MCU_FAMILY}_HAL_Driver)
endif()
if(${ENABLE_LL_DRIVER})
    add_subdirectory(${MCU_FAMILY}_LL_Driver)
endif()

# Startup file
if(${ENABLE_STARTUP_FILE})
    if("${MCU_MODEL}" MATCHES "PY32F002A")
        target_sources(drivers PUBLIC ${CMAKE_CURRENT_LIST_DIR}/CMSIS/Device/PY32F0xx/Source/gcc/startup_py32f002a.s)
    elseif("${MCU_MODEL}" MATCHES "PY32F003")
        target_sources(drivers PUBLIC ${CMAKE_CURRENT_LIST_DIR}/CMSIS/Device/PY32F0xx/Source/gcc/startup_py32f003.s)
    elseif("${MCU_MODEL}" MATCHES "PY32F030")
        target_sources(drivers PUBLIC ${CMAKE_CURRENT_LIST_DIR}/CMSIS/Device/PY32F0xx/Source/gcc/startup_py32f030.s)
    elseif("${MCU_MODEL}" MATCHES "PY32F002B")
        target_sources(drivers PUBLIC ${CMAKE_CURRENT_LIST_DIR}/CMSIS/Device/PY32F0xx/Source/gcc/startup_py32f002b.s)
    endif()
endif()

# ld_script
if(${ENABLE_STARTUP_FILE})
    set(LINKER_SCRIPT ${CMAKE_CURRENT_LIST_DIR}/LDScripts/${MCU_MODEL_LOWER}.ld)
    target_link_options(drivers INTERFACE -T ${LINKER_SCRIPT})
endif()

if(${ENABLE_DEBUG_DEFINE})
    target_compile_definitions(drivers INTERFACE -DDEBUG)
endif()

target_compile_definitions(drivers INTERFACE -D${MCU_MODEL})