# Examples

```python
import make

on_button  = make.button(1)
off_button = make.button(2)
motor = make.dc(7)

make.pause_until(on_button.is_pressed)

while True:
    if on_button.is_pressed():
        motor.spin(50)
    if off_button.is_pressed():
        motor.spin(0)
    make.pause()
```

Start: [Start](../readme.md)
| Previous: [Basics of Make](./make.md)
| Next: [Advanced Topics](./advanced.md)
