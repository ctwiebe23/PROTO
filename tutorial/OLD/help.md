# Common Problems

1. Indentation - Code within loops and `if` statments must be indented to the
   same level- and indentation and spaces **cannot** be mixed.

   ```python
   # example of mismatched indentation

   while not button.pressed():
       motor1.spin(speed=25, seconds=2)
         motor2.spin(speed=25, seconds=2)
       arm.spin(speed=50, seconds=1)
       # ^ indented at different levels; code will not run ^
   ```

2. Naming - Typos and spaces in variable names.
3. Code order - Code runs top to bottom and only one line at a time; when in
   doubt, talk through the code *one step at a time*.
   1. Conditions and loops - conditions are only checked once per `while` loop,
      same with `if` statements.

      ```python
      # example of common loop mistake

      while not button.pressed():
          motor.spin(speed=50, seconds=1)
          # ^ spin motor for 1 second ^
          make.wait(seconds=1)
          # ^ wait for 1 second ^

          # **then** check if the button is pressed or not

      # only checks whether or not the button is pressed at
      # the very moment it loops, *not* during the 'body' of
      # the loop
      ```

Start: [Start](../readme.md)
| Previous: [Advanced Topics](./advanced.md)
