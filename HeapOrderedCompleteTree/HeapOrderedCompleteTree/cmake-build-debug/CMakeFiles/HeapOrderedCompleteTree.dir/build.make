# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.21

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/mac/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/HeapOrderedCompleteTree.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/HeapOrderedCompleteTree.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/HeapOrderedCompleteTree.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/HeapOrderedCompleteTree.dir/flags.make

CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.o: CMakeFiles/HeapOrderedCompleteTree.dir/flags.make
CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.o: ../main.cpp
CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.o: CMakeFiles/HeapOrderedCompleteTree.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.o -MF CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.o.d -o CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.o -c /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/main.cpp

CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/main.cpp > CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.i

CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/main.cpp -o CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.s

CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.o: CMakeFiles/HeapOrderedCompleteTree.dir/flags.make
CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.o: ../PriorityQueueInAVector.cpp
CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.o: CMakeFiles/HeapOrderedCompleteTree.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.o"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.o -MF CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.o.d -o CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.o -c /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/PriorityQueueInAVector.cpp

CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.i"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/PriorityQueueInAVector.cpp > CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.i

CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.s"
	/Library/Developer/CommandLineTools/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/PriorityQueueInAVector.cpp -o CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.s

# Object files for target HeapOrderedCompleteTree
HeapOrderedCompleteTree_OBJECTS = \
"CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.o" \
"CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.o"

# External object files for target HeapOrderedCompleteTree
HeapOrderedCompleteTree_EXTERNAL_OBJECTS =

HeapOrderedCompleteTree: CMakeFiles/HeapOrderedCompleteTree.dir/main.cpp.o
HeapOrderedCompleteTree: CMakeFiles/HeapOrderedCompleteTree.dir/PriorityQueueInAVector.cpp.o
HeapOrderedCompleteTree: CMakeFiles/HeapOrderedCompleteTree.dir/build.make
HeapOrderedCompleteTree: CMakeFiles/HeapOrderedCompleteTree.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable HeapOrderedCompleteTree"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/HeapOrderedCompleteTree.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/HeapOrderedCompleteTree.dir/build: HeapOrderedCompleteTree
.PHONY : CMakeFiles/HeapOrderedCompleteTree.dir/build

CMakeFiles/HeapOrderedCompleteTree.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/HeapOrderedCompleteTree.dir/cmake_clean.cmake
.PHONY : CMakeFiles/HeapOrderedCompleteTree.dir/clean

CMakeFiles/HeapOrderedCompleteTree.dir/depend:
	cd /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/cmake-build-debug /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/cmake-build-debug /Users/kooshesh/2022spring/cs315/HeapOrderedCompleteTree/cmake-build-debug/CMakeFiles/HeapOrderedCompleteTree.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/HeapOrderedCompleteTree.dir/depend

