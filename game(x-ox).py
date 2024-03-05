g=[1,2,3,4,5,6,7,8,9]

def draw():
    return print(f"""
                 {g[0]} | {g[1]} | {g[2]} 
                -----------
                 {g[3]} | {g[4]} | {g[5]}
                -----------
                 {g[6]} | {g[7]} | {g[8]} 
    """
        )
draw()
while True:
    x = int(input("X qaysi katakka = "))
    g[x-1] = "X"
    draw()

    if (g[0] == g[1] == g[2] or g[0] == g[3] == g[6] or g[0] == g[4] == g[8] or 
        g[1] == g[4] == g[7] or g[2] == g[5] == g[8] or g[2] == g[4] == g[6] or 
        g[3] == g[4] == g[5] or g[6] == g[7] == g[8]):
        print("X yutdi! Tamom!!!")
        break

    O = int(input("O qaysi katakka = "))
    if x != O:
        g[O-1] = "O"
    else:
        print("U katakda X bor! Boshqa yerga joylashtiring!")
        O = int(input("O qaysi katakka = "))
        g[O-1] = "O"

    if (g[0] == g[1] == g[2] or g[0] == g[3] == g[6] or g[0] == g[4] == g[8] or 
        g[1] == g[4] == g[7] or g[2] == g[5] == g[8] or g[2] == g[4] == g[6] or 
        g[3] == g[4] == g[5] or g[6] == g[7] == g[8]):
        print("O yutdi! Tamom!!!")
        draw()
        break
    draw()
