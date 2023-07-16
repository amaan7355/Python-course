def game(sc):
    return sc
score=int(input("Enter the score of game: "))
game(score)
with open('hiscore.txt') as f:
    data=f.read()
if data=='':
    with open('hiscore.txt','w') as f:
        f.write(str(score))
elif int(data)<score:
    with open('hiscore.txt','w') as f:
        f.write(str(score))