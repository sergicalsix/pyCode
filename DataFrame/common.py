import datetime

class Timer():
    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.end_time = None


    def __call__(self, message=None):
        self.end_time = datetime.datetime.now()
        if message != None:
            print(message, "=", self.end_time - self.start_time)
        else:
            print(self.end_time - self.start_time)
    
