from skpy import SkypeEventLoop, SkypeNewMessageEvent, Skype

sk = Skype('arghalexander300@gmail.com', 'D@vid0614')
ch = sk.chats.chat(id='19:85c81c1e5a194c46b315f633b192a39b@thread.skype')
users = ch.userIds

sch = {'alex' : users[0], 'boramac' : users[1], 'joshmob' : users[2], 'josh' : users[3], 'bora' : users[5], 'max' : users[6], 'maxmob' : users[7], 'alexbox' : users[8], 'louiemob' : users[9], 'louie' : users[10]}

joshWords = ['can anyone play', 'can anybody play', 'can you play', 'Can anyone play', 'Can anybody play', 'Can you play', 'm']

class SkypePing(SkypeEventLoop):
    def __init__(self):
        super(SkypePing, self).__init__("arghalexander300@gmail.com", "D@vid0614")
        
    def onEvent(self, event):
        #print(repr(event))
        if isinstance(event, SkypeNewMessageEvent):
            print('Message Content: ' + event.msg.content)
            print('Poster: ' + checkID(event.msg.userId))
            if event.msg.userId == sch['josh'] or event.msg.userId == sch['joshmob']:
                if any(con in event.msg.content for con in joshWords):
                    event.msg.chat.sendMsg("No")

def checkID(id):
    if id == sch['alex']:
        return 'Alexander'
    elif id == sch['josh'] or id == sch['joshmob']:
        return 'Josh'
    elif id == sch['louie'] or id == sch['louiemob']:
        return 'Louie'
    elif id == sch['max'] or id == sch['maxmob']:
        return 'Max'
    elif id == sch['bora'] or id == sch['boramob']:
        return 'Bora'

jb = SkypePing()

jb.loop()

