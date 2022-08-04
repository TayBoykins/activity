def on_gesture_logo_up():
    global index, word
    index = randint(0, len(coll))
    word = coll[index]
    basic.show_string("" + (word))
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_gesture_screen_down():
    game.add_score(1)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

word = ""
index = 0
coll: List[str] = []
coll.append("puppy")
coll.append("clock")
coll.append("night")
coll.append("cat")
coll.append("cow")
game.start_countdown(30000)