## PY32F0 Series MCU Drivers

PY32F0xx MCU CMSIS, BSP, HAL, LL, Examples



## see template project at [decaday/py32f0-cmake](https://github.com/decaday/py32f0-cmake)

docs : [decaday/PY32_Docs](https://github.com/decaday/PY32_Docs)

 CMSIS, BSP, HAL, LL comes from Puya data packages:

```
PY32F002B_230807
PY32F002B_231026
PY32L020_231018

PY32F030 & PY32F003 &PY32F002A_230410

PY32F040_230807
PY32F040_231018
PY32F040_231115

PY32F072&PY32F071&PY32F070_230703
PY32F072&PY32F071&PY32F070_231115
```

https://github.com/ARM-software/CMSIS-DSP

https://www.keil.arm.com/packs/py32f0xx_dfp-puya/



LDScripts and gcc startup files comes from https://github.com/IOsetting/py32f0-template



# CMake Configuration

This document describes the CMake configuration options for the py32-drivers project.

## Configuration Options

### MCU Model Selection
```cmake
set(MCU_MODEL "PY32F030x6" CACHE STRING "MCU model, like PY32F030x6")
```
Specifies the target MCU model for compilation. Set this variable to match your hardware.

The following MCU models are supported:

- PY32F002Ax5
- PY32F002Bx5
- PY32F003x4, PY32F003x6, PY32F003x8
- PY32F030x4, PY32F030x6, PY32F030x7, PY32F030x8

### Driver Options

#### HAL Driver
```cmake
option(ENABLE_HAL_DRIVER "Enable HAL driver" ON)
```
- When `ON`: Includes the Hardware Abstraction Layer (HAL) driver
- Default: `ON`

#### LL Driver
```cmake
option(ENABLE_LL_DRIVER "Enable LL driver" ON)
```
- When `ON`: Includes the Low-Level (LL) driver
- Default: `ON`

### System Configuration

#### System XXX Source
```cmake
option(ENABLE_SYSTEM_XXX_C "Enable system_XXX.c" ON)
```
- When `ON`: Includes the system configuration source file
- Default: `ON`

#### Startup File
```cmake
option(ENABLE_STARTUP_FILE "Enable startup file" ON)
```
- When `ON`: Includes the MCU startup file
- Default: `ON`

#### Linker Script
```cmake
option(ENABLE_LD_SCRIPT "Enable linker script" ON)
```
- When `ON`: Includes the linker script for memory layout
- Default: `ON`

### Debug Configuration
```cmake
option(ENABLE_DEBUG_DEFINE "Enable debug define" ON)
```
- When `ON`: Enables HAL debug symbols and definitions（-DDEBUG）
- Default: `ON`

## Usage Example

To configure your build, you can:

1. Use CMake GUI:
   ```bash
   cmake-gui /path/to/source
   ```

2. Use command line:
   ```bash
   cmake -DMCU_MODEL=PY32F030x6 -DENABLE_HAL_DRIVER=ON -DENABLE_LL_DRIVER=ON /path/to/source
   ```

3. Or modify `CMakeCache.txt` directly after initial configuration.
