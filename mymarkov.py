import random


class Generator(object):
    def __init__(self, file_name):
        self.probs = {}
        self.words = self.init_dictionary(file_name)
        self.init_database()

    def init_dictionary(self, file_name):
        with open(file_name, 'r') as f:
            data = f.read()
            return [w.strip() for w in data.split()]

    def triples(self):
        if len(self.words) < 3:
            print 'Unable to generate triples, too few words provided'
            return

        for i in range(len(self.words)-3):
            yield (self.words[i], self.words[i+1], self.words[i+2])

    def init_database(self):
        for w1, w2, w3 in self.triples():
            key = (w1, w2)
            if key in self.probs:
                self.probs[key].append(w3)
            else:
                self.probs[key] = [w3]

    def get_random_word(self):
        return self.words[random.randint(0, self.words)]

    def get_random_pair(self):
        return self.probs.keys()[random.randint(0, len(self.probs))]

    def generate_sentence(self, length):
        w1, w2 = self.get_random_pair()
        res = []
        for i in xrange(length):
            res.append(w1)
            w1, w2 = w2, random.choice(self.probs[(w1, w2)])

        return res



if __name__ == "__main__":
    print 'Starting markov generator'
    g = Generator(file_name='/home/jj/git/markov/train.txt')
    sentence = g.generate_sentence(length=50)
    print sentence
