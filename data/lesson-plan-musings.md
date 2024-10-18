# Lesson Plan Musings

## Concepts

### Naming (Variables)

```python
name = make.componant(port number)
```

Componants:

- Button
- Motors
- Drivetrain

### Actions (Functions)

```python
componant.action()
componant.action(values)
make.action(values)
```

Actions:

- `button.pressed()`
- `motor.spin(power, seconds)` & `motor.stop()`
- `drivetrain.drive(power, seconds)`, `drivetrain.turn(power, seconds)`,
  `drivetrain.curve(left power, right power, seconds)`, `drivetrain.stop()`
- `make.wait(seconds)` & `make.wait_until(button.pressed)`
- `led.on(seconds)` & `led.off()`

### Code Order

Reads top to bottom, doesn't go to the next line until the previous one
finishes.

### Program Format

```python
import make

name = make.componant(port)
name = make.componant(port)
name = make.componant(port)

name.action(values)
name.action(values)
make.action(values)
name.action()
name.action(values)
```

## Example Lesson Code

### General Program

```python
# All programs must start with:
import make

# Then, you name all of your componants:
stopbutton = make.button(1)
grabbyarm = make.smallmotor(6)
leftmotor = make.largemotor(7)
rightmotor = make.largemotor(8)
myrobot = make.drivetrain(leftmotor, rightmotor)
firstled = make.led(1)
lastled = make.led(13)

# Now you do all your actions
grabbyarm.spin(power=70)
make.wait_until(stopbutton.pressed)
grabbyarm.stop()

firstled.on()

myrobot.drive(power=100, seconds=2)
myrobot.turn(power=-40, seconds=0.5)
myrobot.curve(left_power=90, right_power=60, seconds=5)

lastled.on(seconds=2)
firstled.off()

make.wait(seconds=2)
myrobot.turn(power=10)
make.wait_until(stopbutton.pressed)

# Remember, code reads top to bottom! Each line won't run until the one above
# it finishes, and once the program reaches the end of the code everything
# stops
```

\newpage

### Common Loop Mistake

```python
import make

stopbutton = make.button(2)
motor = make.smallmotor(3)

while not stopbutton.pressed():
    motor.spin(50, 2)
    make.wait(2)
```
