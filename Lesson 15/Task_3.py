class TVController:
    def __init__(self, channels=None, current_channel=0):
        if channels is None:
            channels = ["BBC", "Discovery", "TV1000"]
        self.current_channel = current_channel
        self.channels = channels

    def first_channel(self):
        self.current_channel = 0
        return self.channels[self.current_channel]

    def last_channel(self):
        self.current_channel = len(self.channels) - 1
        return self.channels[self.current_channel]

    def turn_channel(self, num_):
        if num_ > len(self.channels) or num_ < 1:
            return "No such channel"
        else:
            self.current_channel = num_ - 1
            return self.channels[self.current_channel]

    def next_channel(self):
        if self.current_channel + 1 == len(self.channels):
            self.current_channel = 0
            return self.channels[self.current_channel]
        else:
            self.current_channel += 1
            return self.channels[self.current_channel]

    def previous_channel(self):
        if self.current_channel == 0:
            self.current_channel = len(self.channels) - 1
            return self.channels[self.current_channel]
        else:
            self.current_channel -= 1
            return self.channels[self.current_channel]

    def name_of_channel(self):
        return self.channels[self.current_channel]

    def is_exist(self, data):
        if data.isdigit():
            try:
                return self.channels[int(data) - 1]
            except ValueError:
                return 'num'
        else:
            try:
                return self.channels.index(data) + 1
            except ValueError:
                return "str"



if __name__ == '__main__':
    remote = TVController()

    while True:
        choice = input("""
1 Turn on first channel
2 Turn on last channel
3 Turn on selected channel
4 Turn on next channel
5 Turn on previous channel
6 Get the name of the current channel
7 Info if such channel name or channel number exists
8 Turn off the tv \n """)
        if choice == '1':
            print(remote.first_channel())
        elif choice == '2':
            print(remote.last_channel())
        elif choice == '3':
            num = int(input("Select your channel, numbers only: "))
            print(remote.turn_channel(num))
        elif choice == '4':
            print(remote.next_channel())
        elif choice == '5':
            print(remote.previous_channel())
        elif choice == '6':
            print(remote.name_of_channel())
        elif choice == '7':
            chan_name = input('Enter channel name or number: ')
            print(remote.is_exist(chan_name))
        elif choice == '8':
            break

