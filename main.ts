input.onGesture(Gesture.LogoUp, function () {
    index = randint(0, coll.length)
    word = coll[index]
    basic.showString("" + (word))
})
input.onGesture(Gesture.ScreenDown, function () {
    game.addScore(1)
})
let word = ""
let index = 0
let coll: string[] = []
game.startCountdown(30000)
coll.push("chicken")
coll.push("pizza")
coll.push("sub")
coll.push("fries")
coll.push("candy")
