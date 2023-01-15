class Model:
    def __init__(self):
        self.value = '0'
        self.operator = self.prev_val = None

    def calculate(self, title: str):
        if title == 'C':
            self.value = '0'

        elif title == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value

        elif title == '%':
            pass

        elif title == '=':
            self.value = self._evaluate()

        elif title == '.':
            if title not in self.value:
                self.value += title

        elif isinstance(title, int):
            if self.value == '0':
                self.value = ''

            self.value += str(title)

        else:
            if self.value:
                self.operator = title
                self.prev_val = self.value
                self.value = ''

        return self.value

    def _evaluate(self):
        return eval(self.prev_val + self.operator + self.value)
