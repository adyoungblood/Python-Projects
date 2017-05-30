memes = []
while True:
    meme = input("something: ")
    for char in meme:
        memes.append(char)
    memes = memes[::-1]
    for letter in memes:
        print(letter)
    memes.clear()
