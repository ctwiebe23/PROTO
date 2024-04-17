# Examples

```python
import make

on_button = make.button(1)
off_button = make.button(2)

motor = make.dc(7)

make.pause_until(on_button.is_pressed)

while not off_button:
    motor.spin(50)
    make.pause(3)
    motor.spin(0)
    make.pause(3)
```

Start: [Start](../readme.md)
| Previous: [Basics of Make](./make.md)
| Next: [Advanced Topics](./advanced.md)
