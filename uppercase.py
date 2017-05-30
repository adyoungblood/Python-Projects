meme = []
while True:
    memes = input("some inproperly formatted text: ")
    for char in memes:
        meme.append(char)
    meme = meme[::-1]
    print(meme)
    meme.clear()
