def on_forever():
    for X in range(5):
        for Y in range(5):
            led.plot(2, 2 - Y)
            led.plot(2, 2 + Y)
            led.plot(2 + X, 2)
            led.plot(2 - X, 2)
            basic.pause(100)
    for X2 in range(5):
        for Y2 in range(5):
            led.unplot(2 - X2, 2)
            led.unplot(2 + X2, 2)
            led.unplot(2, 2 - Y2)
            led.unplot(2, 2 + Y2)
            basic.pause(100)
basic.forever(on_forever)
