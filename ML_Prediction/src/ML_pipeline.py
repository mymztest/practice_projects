class Pipeline():
    def __init__(self, steps):
        self.steps = steps

    def run(self, data=None):
        for step in self.steps:
            data = step.process(data)
            #return data
