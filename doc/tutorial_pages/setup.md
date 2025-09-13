# Setting up to use MAKE

There are two ways you might use MAKE, each of which require a different
level of setup.  The first is to use it *as a user*, in which case you only
interact with the library in order to operate a robot.  The second is to use it
*as a developer*, in which case you will be editing the library itself to
alter or introduce behavior.

## As a user

1.  Navigate to our [Online IDE][learn2code], a login-less website that
    provides both a block- and line-based interface for writing code with MAKE.

    -   Alternatively, use your own IDE to write code --- anything will do.
1.  Plug your robot's brain into your computer using the USB port --- it should
    show up like a flash drive would, with the name `CIRCUITPY`.

    -   If it doesn't show up, make sure the brain is powered on!
1.  Once you've written a program, save it to a file named `main.py` and place
    it in the `CIRCUITPI` drive.

    -   This should replace the previous `main.py`, if one already existed.
    -   Leave the rest of the drive alone --- especially the folder `lib` and
        the file `boot_out.txt`.
1.  After the code has been uploaded, unplug the robot from your computer.
1.  To start your program, press the `A` button and wait one second --- to
    reset the program, press the `Reset` button and wait one second.

## As a developer

1.  Clone the [Github repository][github] onto your machine.
1.  Read the `README.md` file for an overview of the project, including:

    -   How the library is laid out, technically speaking.
    -   How to install an updated version of MAKE onto a brain (or install it
        on a fresh brain).

---

Back to the [Index][].

[learn2code]: https://learn2code-proto.github.io
[github]: https://github.com/ctwiebe23/PROTO
[Index]: ./index.md
