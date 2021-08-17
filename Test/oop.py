class Singer:
    def __init__(self) -> None:
        self.age = 0
        self.name = ''
        self.sex = ''
        self.genre = ''

    def sing(self):
        return "Lalalal~"
    
    def sign(self):
        return self.name
    
    def info(self):
        print('age:', str(self.age))
        print('name:', self.name)
        print('sex:', self.sex)
        print('genre:', self.genre)

ricky = Singer()
ricky.age = 33
ricky.name = 'ricky'
ricky.sex = 'M'
ricky.genre = 'POP'
ricky.info()
print(ricky.sing())
print(ricky.sign())

def order_programming():
    singer_name = "ricky"
    singer_age = 33
    singer_sex = "M"
    singer_genre = "pop"

    # Sing a song
    print("lalalal")

    # Sign
    print(singer_name)

    # info
    # ...

order_programming()

kyungsoo = Singer()
kyungsoo.age = 33
kyungsoo.name = 'kyungsoo'
kyungsoo.sex = 'M'
kyungsoo.genre = 'K-pop'
kyungsoo.info()
print(kyungsoo.sing())
print(kyungsoo.sign())