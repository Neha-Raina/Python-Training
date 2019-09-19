x = 0    #Global

def update():
    global x
    x = 1
    x +=1            # Local
    return x
print(x)
print(update())
