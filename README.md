SublimeLinter-lua
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-lua.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-lua)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [luac -p](http://www.lua.org). It will be used with files that have the “Lua” syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here](http://sublimelinter.readthedocs.org/en/latest/installation.html).

### Linter installation
Before using this plugin, you must ensure that `lua` (which includes `luac`) is installed on your system. To install `lua`, do one of the following:

1. Install a binary from the [binaries downloads page](http://luabinaries.sourceforge.net).

1. On Mac OS X, use [homebrew](http://brew.sh) to install by typing the following in a terminal:
   ```
   brew install lua
   ```

   Note that more recent versions of lua may be available via `brew`, type `brew search lua` to check.

1. On Windows, you can install with [Lua for Windows](https://code.google.com/p/luaforwindows/).

### Linter configuration
In order for `luac` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once `luac` is installed and configured, you can proceed to install the SublimeLinter-luac plugin if it is not yet installed.

### Plugin installation
Please use [Package Control](https://sublime.wbond.net/installation) to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette](http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html) and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `lua`. Among the entries you should see `SublimeLinter-lua`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings](http://sublimelinter.readthedocs.org/en/latest/settings.html). For information on generic linter settings, please see [Linter Settings](http://sublimelinter.readthedocs.org/en/latest/linter_settings.html).

In addition to the standard SublimeLinter settings, SublimeLinter-lua provides its own settings. Those marked as “Inline Setting” or “Inline Override” may also be [used inline](http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings).

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.

Thank you for helping out!
