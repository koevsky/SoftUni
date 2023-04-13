from project.horse_specification.horse import Horse


class Thoroughbred(Horse):

    MAX_SPEED = 140
    TRAIN_VALUE = 3

    def train(self):
        if self.speed + Thoroughbred.TRAIN_VALUE > Thoroughbred.MAX_SPEED:
            self.speed = Thoroughbred.MAX_SPEED
        else:
            self.speed += Thoroughbred.TRAIN_VALUE