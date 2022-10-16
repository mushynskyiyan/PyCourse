class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start

    def set_max(self, max_max):
        self.max_value = max_max

    def set_min(self, min_min):
        self.min_value = min_min

    @staticmethod
    def step_up():
        if counter.current >= counter.max_value:
            raise ValueError('You better stop!')
        else:
            counter.current += 1

    @staticmethod
    def step_down():
        if counter.current <= counter.min_value:
            raise ValueError('Here we go again,right?')
        else:
            counter.current -= 1

    def get_current(self):
        return self.current


counter = Counter()
counter.set_current(7)
counter.set_max(10)
counter.step_up()
print(counter.get_current())
counter.step_up()
print(counter.get_current())
counter.step_up()
print(counter.get_current())  # 10

try:
    counter.step_up()  # ValueError
except ValueError as e:
    print('ACHTUNG!ACHTUNG! ' + str(e))
print(counter.get_current())  # 10


counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
print(counter.get_current())  # 7
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print('Damn! ' + str(e)) # Достигнут минимум
print(counter.get_current())  # 7