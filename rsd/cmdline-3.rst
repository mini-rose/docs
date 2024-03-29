RSD 3: cmdline
==============

:Header: Copyright (c) 2022-2023 mini-rose
:Name: cmdline-3
:Desc: Program command line
:Revision: 2


Abstract
--------

This document describes the look & feel of command line arguments in any CLI
programs. In order to provide a simple work enviroment, the most used arguments
& flags have to be standardized, and that is what this document is for. Also
contains some information about how these apps should behave when being passed
such arguments.


1. Definitions
--------------

There are 2 types of command line options, a short and long option which
can both take or not take a value. [a] A short command line option contains
a single dash followed by a single upper or lowercase character::

        -h -F -v                            /-[A-z]/

[b] A long option is a lowercase name prefixed with two dashes. Note that
there cannot be any upper case character in the name, and any spaces should
be replaced with another dash::

        --help --find-file --version        /--[a-z][a-z-]+/

[c] A flag is a "switch" that does not take any value as an argument. And
stores only a bool value if it has been found in the command line.

[d] An option is a flag that takes an argument after a single space.
Depending on the option, it may take many comma-seperated arguments::

        --param val1,val2

[e] When a short option takes an argument, it may be placed in the same arg as
the flag, or after a space. The following two options mean the same::

        -fvalue
        -f value


2. Standard flags
-----------------

Each program should have a minimal working set of flags, which make the
user experience more pleasant, because each program is similar to the other,
which also alignes with the Unix philosophy.

[a] -h, --help
        Only the "--help" flag is actually required, but it does not have to
        appear in the usage page. The short, "-h" flag on the other hand is not
        required in the program, but if it is present the extended usage page
        must show it and must open the usage page and exit the program after it.

[b] -v, --version
        The lowercase "v" should always provide the program version. Some tools
        may offer 2 different version styles, for example "-v" showing only the
        version ID, while the long "--version" would show the string version,
        the author and copyright information.

TLDR: The only actual required flag is "--help".


3. Usage page
-------------

The aforementioned usage page is required to contain the "usage line", which
is the first line of the usage page and it tells the user how to use the
command::

        usage: program [-hv] <file>

This example usage line tells the user that "program" can be called with the
optional -h and -v flags, and the required file argument. (a) Single
character flags are to be grouped into a single optional block, with the
chars being alphabetically sorted.

[b] Required arguments are surrouned with lower than and greater than signs
(<arg>). If there arguments are not prefixed with a flag, they must be
interpreted positionally, meaning no matter the order of the arguments, the
first argument will always be the first positional argument represented in
the usage line.

[c] Long options should be placed in their respective blocks, for example::

        usage: program [-hv] [--help] [--version] <file>

[d] If the program chooses to do so, it may provide an extended usage page
which contains information about all the flags the user may use for the
program. The extended usage page for the usage line above may look like
this::

        usage: program [-hv] [--help] [--version] <file>

        This program does literally nothing.

          file              path to a file
          -h, --help        show the usage page and exit
          -v, --version     show the version and exit

The whole page is split into 3 sections: the already explained usage line,
a short sentence about the program itself, and the option list. The option
list must begin with listing all the required positional (and named)
arguments (in this case <file>). After that all flags must be alphabetically
listed. In case the option takes an argument, the syntax is the following::

        -f, --file <file>   path to a file

This means that the "-f" or "--file" option must be provided a single value,
in this case being some arbitrary path to a file. The whole option section
should be indented with 2 spaces.
