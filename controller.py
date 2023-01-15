from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def on_button_click(self, title: str):
        res = self.model.calculate(title)
        self.view.entry_val.set(res)


if __name__ == '__main__':
    controller = Controller()
    controller.main()
