import lib.make as make

led = make.light(0)

while True:
  led.toggle()
  make.wait(0.1)
