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

class Self_tqdm():
    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.end_time = None
        #self.first_time = True

    def __call__(self , i , total):
        tmp = (i+1)*10 / total
        for j in range(1, 10):
            if (tmp == j):
                self.end_time = datetime.datetime.now()
                print(str(j)+"0% is done. Time:" ,self.end_time - self.start_time)
