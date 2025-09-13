# NAME

MAKE --- PROTO's embedded python library

# DESCRIPTION

MAKE is Python library that runs on top of [CircuitPython][], creating an
interface for controlling sensors and motors connected to an RP2040-based PCB.

[circuitpython]: https://circuitpython.org/

The goal of the project is to create a simple-to-use library that can be
brought into elementary / middle schools and taught with minimal programming
experience on either side --- student *or* teacher.  It prioritizes readability
and simplicity over efficiency, and was designed under many constraints
imposed by the RP2040, CircuitPython, and its intended environment.

```py
!((cat doc/tutorial_pages/example_code/drive_until_stopped.py))!
```

# FUNCTIONS AND CLASSES

# INSTALL

MAKE must be installed on a system that already has CircuitPython set up. If
this is not the case, first follow this guide to [install
CircuitPython][install-circuitpython] on your board.  To determine if
CircuitPython has been installed, plug the board into your computer via a USB
--- the board should pop up in your file system as a USB device named
`CIRCUITPY`.

[install-circuitpython]: https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython

Once CircuitPython is working and you have found the `CIRCUITPY` drive, enter
it and copy the `./src/lib` folder from this Github repository to the drive.
This folder (`CIRCUITPY/lib`) is where CircuitPython searches for libraries,
and the `./src/lib` folder in the repo contains everything MAKE needs ---
well, almost.

Depending on your board, additional libraries may need to be installed ---
these can be found in `./src/component_libraries`.  The only such library that
is currently needed is the Adafruit motor library --- if your board is the
[MakerPI RP2040][makerpi], this comes pre-installed, but otherwise you likely
will need to copy `./src/component_libraries/adafruit_motor` into
`CIRCUITPY/lib`.

[makerpi]: https://www.cytron.io/p-maker-pi-rp2040-simplifying-robotics-with-raspberry-pi-rp2040

The final step to get code running is to place a `main.py` file at the root of
`CIRCUITPY`.  This is the file that CircuitPython will run when the board
starts up, and is where you will write the "main method" for your program.  To
upload a new program, simply overwrite `CIRCUITPY/main.py`.

# EXAMPLES

# INDEX

CHANGELOG.md
:   foo

justfile
:   foo

LICENSE
:   foo

pyproject.toml
:   foo

README.md
:   This file.

data/
:   foo

doc/
:   foo

    fonts.html
    :   foo

    pandoc.yml
    :   foo

    source.md
    :   foo

    styles.css
    :   foo

    example_code/
    :   foo

    www/
    :   foo

src/
:   foo

    main.py
    :   foo

    component_libraries/
    :   foo

    lib/
    :   foo

        make.py
        :   foo

        proto/
        :   foo

            \*/\_\_init\_\_.py
            :   foo

            system.py
            :   foo

            general/
            :   foo

            input/
            :   foo

            motion/
            :   foo

            schemata/
            :   foo
