class Phone:
    
    def calling(self):
        '''
        print("5g call")
        '''
        pass

    def message(self):
        pass
    def music(self):
        pass
    def flahlight(self):
        pass
class Vivo(Phone):
    def camera(self):
        print('300px zoom')
    def calling(self):
        print("Special call")
class Sony(Phone):
    def camera(self):
        print('100px,zoom')
    def calling(self):
        print("Free call")
a=Vivo()
a.calling()
a.camera()
y=Sony()
y.calling()
y.camera()
