SublimeLinter-lua
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-lua.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-lua)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [luac -p](http://www.lua.org). It will be used with files that have the “Lua” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before using this plugin, you must ensure that `lua` (which includes `luac`) is installed on your system. To install `lua`, do one of the following:

1. Install a binary from the [binaries downloads page](http://luabinaries.sourceforge.net).

1. On Mac OS X, use [homebrew](http://brew.sh) to install by typing the following in a terminal:
   ```
   brew install lua
   ```

   Note that more recent versions of lua may be available via `brew`, type `brew search lua` to check.

1. On Windows, you can install with [Lua for Windows](https://code.google.com/p/luaforwindows/).

In order for `luac` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
