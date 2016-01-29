#do multiple things at the same time
#whenever you are making a messeges program: sending and listening
#you dont need to wait for sending the message before you can start typing
#you need to build two objects: one for sending out and one for listening messages

import threading


class BuckyMessenger(threading.Thread):
    def run(self):
        for _ in range(50):   # just want to loop for 10 times and dont care about the variable
            print(threading.currentThread().getName())  # return the name of the thread


x = BuckyMessenger(name="Send out messages") # we need to give every thread a name
y = BuckyMessenger(name="Receive messages")
x.start()  # whenever you use a start function, it will go to the object and run the run function
y.start()
