class RemoteControl:

    def __init__(self):
        self.channels = ['CN','sports HD', 'Imax', 'music']
        self.index = 0 #the tv is off

    def __iter__(self):

        return self

    def __next__(self):

        self.index += 1 #meaning when the tv is on

        if self.index == len(self.channels):

            raise StopIteration

        return self.channels[self.index]

if __name__ == '__main__':

    rc = RemoteControl()
    itr = iter(rc)

    print(next(itr))
    print(next(itr))
    print(next(itr))