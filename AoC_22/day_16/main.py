import re


INPUT_PATH = './input.txt'
TEST_INPUT_PATH = './test-input.txt'

class Valve:
    def __init__(self, name, flow_rate, leads_to):
        self.name = name
        self.flow_rate = flow_rate
        self.leads_to = leads_to

    def __repr__(self):
        return self.name
    
    def get_valves(self, path = INPUT_PATH):
        with open(path) as input:
            for line in input:
                pass


if __name__ == "__main__":
    pass