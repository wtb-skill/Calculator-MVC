

class Model:
    def __init__(self):
        self.value = ''


    def calculate(self, caption):
        if caption == 'C':
            self.value = ''

        elif isinstance(caption, int):
            self.value += str(caption)


        return self.value
