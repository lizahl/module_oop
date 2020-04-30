class Score:
    def __init__(self, time, name, score):
        self.time = time
        self.name = name
        self.score = score

    def __str__(self):
        return "{}: {}".format(self.name, self.score)

    def __repr__(self):
        return self.__str__()

    @staticmethod

    def records(fp):
        with open(fp, 'r') as records:
            objects = list()
            for line in records:
                listing = line[:-1].split('\t')
                record = Score(listing[0][:-1], listing[1], int(listing[2]))
                objects.append(record)
            f = open('scores.txt', 'w')
            f.close()
        return objects

    def write_result(self):
        with open(r'scores.txt', 'a') as output:
            string = "{},\t{}\t{}\n".format(self.time, self.name, self.score)
            output.write(string)
            output.close()

class GameOver(Exception):
    def GameExit(self):
        pass

class EnemyDown(Exception):
    def EnemyLose(self):
        pass

