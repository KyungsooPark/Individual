# -*- coding: utf-8 -*-
class Person:
    # 눈 두 개, 코 하나, 입 하나...
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2
    arms = 2
    legs = 2

    # 먹고 자고 이야기하고...
    def eat(self):
        print ('얌냠...')

    def sleep(self):
        print ('쿨쿨...')

    def talk(self):
        print ('주절주절...')

class Student(Person):
    def study(self):
        print('시험 홧팅 !')

class Proggrammer(Person):
    def programming(self):
        print('Programming ...')

kyungsoo = Student()
kyungsoo.eat()
kyungsoo.sleep()
kyungsoo.talk()
kyungsoo.study()

kicher = Proggrammer()
kicher.eat()
kicher.talk()
kicher.programming()