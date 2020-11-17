basic.forever(function () {
    for (let X = 0; X <= 4; X++) {
        led.plot(2, 2 - X)
        led.plot(2, 2 + X)
        led.plot(2 + X, 2)
        led.plot(2 - X, 2)
        basic.pause(500)
    }
    for (let X = 0; X <= 4; X++) {
        led.unplot(2 - X, 2)
        led.unplot(2 + X, 2)
        led.unplot(2, 2 - X)
        led.unplot(2, 2 + X)
        basic.pause(500)
    }
})
