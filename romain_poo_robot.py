# -*- coding:utf-8 -*-

class Robot:

    def __init__(self, name, position = (0,0), direction = 'Est'):
        self._name = str(name)
        self._position = {'x':int(position[0]), 'y':int(position[1])}
        self._direction_possible = ['nord', 'est', 'sud', 'ouest']
        self._nb_pas = 1

        direction = direction.lower()

        if direction in self._direction_possible:
            self._direction = direction
        else:
            raise TypeError(f'La direction : {direction} est incorrecte ! Veuillez choisir entre : {self._direction_possible}\n')

    def afficher(self):
        print(f"""Nom nom est : {self._name}
Ma position est : {self._position['x']} x {self._position['y']} y
Ma direction est : {self._direction}\n""")

    def avance(self):
        if self._direction == 'nord':
            self._position['y'] += self._nb_pas

        elif self._direction == 'est':
            self._position['x'] += self._nb_pas

        elif self._direction == 'sud':
            self._position['y'] -= self._nb_pas

        elif self._direction == 'ouest':
            self._position['x'] -= self._nb_pas

        print(f'\nJ\'ai avancé de : {self._nb_pas} pas, dans la direction : {self._direction} !\n')

    def droite(self):
        nb_direction = self._direction_possible.index(self._direction)

        try:
            self._direction = self._direction_possible[nb_direction + 1]

        except IndexError:
            self._direction = self._direction_possible[0]


class RobotNg(Robot):

    def __init__(self, name, position = (0,0), direction = 'Est'):
        Robot.__init__(self, name, position, direction)
        self.__turbo = False

    def afficher(self):
        print_string = f"""Nom nom est : {self._name}
Ma position est : {self._position['x']} x {self._position['y']} y
Ma direction est : {self._direction}\n"""

        if self.__turbo is True:
            print_string += 'Le mode turbo est activé !\n'
        else:
            print_string += 'Le mode turbo est désactivé !\n'

        print(print_string)

    def avance(self, nb_pas = 1):

        if self.__turbo == True:
            nb_pas = nb_pas *3

        self._nb_pas = nb_pas
        Robot.avance(self)

    def gauche(self):
        nb_direction = self._direction_possible.index(self._direction)

        try:
            self._direction = self._direction_possible[nb_direction - 1]

        except IndexError:
            self._direction = self._direction_possible[-1]

    def demi_tour(self):
        nb_direction = self._direction_possible.index(self._direction)

        try:
            self._direction = self._direction_possible[nb_direction +2]

        except IndexError:

            if nb_direction == 2:
                self._direction = self._direction_possible[0]

            elif nb_direction == 3:
                self._direction = self._direction_possible[1]

    def turbo(self):
        if self.__turbo is False:
            self.__turbo = True
            print('\nMode turbo activé !\n')
        else:
            self.__turbo = False
            print('\nMode turbo désactivé !\n')