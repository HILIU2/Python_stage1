class Mario():

    def move(self):
        print("I am Mario.")

class Shroom():

    def eat_shroom(self):
        print('How I am hig!')

class BigMario(Mario, Shroom):

    def move(self):
        print("I am BigMario")

bm = BigMario()
bm.move();
bm.eat_shroom()
