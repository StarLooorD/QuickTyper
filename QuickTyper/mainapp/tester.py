class Tester:

    def __init__(self, text, input_text='', start_time=0, end_time=0):
        self.text = text
        self.input_text = input_text
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = 0
        self.accuracy = 0
        self.wpm = 0
        self.level = 'unknown'

    def set_total_time(self):
        self.total_time = round(self.end_time - self.start_time)

    def set_accuracy_and_wpm(self):
        counter = 0
        words = len(self.text.split(' '))
        for i in range(len(self.text)):
            try:
                print(self.text[i], self.input_text[i])
                if self.text[i] == self.input_text[i]:
                    counter += 1
            except:
                pass
        self.accuracy = round(counter / len(self.text) * 100, 1)
        self.wpm = round(words * 60 / self.total_time, 1)

    def set_level(self):
        count = self.wpm * self.accuracy / 100
        if count > 50:
            self.level = 'Octopus'
        elif 40 < count < 50:
            self.level = 'Monkey'
        elif 30 < count < 40:
            self.level = 'Pigeon'
        elif 20 < count < 30:
            self.level = 'Bear'
        elif 0 < count < 20:
            self.level = 'Sloth'
        else:
            self.level = 'unknown'
