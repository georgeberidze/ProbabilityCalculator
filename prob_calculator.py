import random

def unpack(dictionary):
    'Turns dictionary into a list of strings. Duplicates are counted'
    result = []
    for color, number in dictionary.items():
            for i in range(number):
                result.append(color)
    return result

class Hat:
    def __init__(self, **kwargs):
        self.contents = unpack(kwargs)
        self.contents_backup = unpack(kwargs) # store the original content for each hat

    def draw(self, balls):
        'Randomly removes the number of balls that are given'
        self.contents = self.contents_backup.copy() # everytime we run draw(), contents will go back to the original state
        self.picked = [] # list of balls that are randomly removed

        if balls < len(self.contents):
            'Number of balls picked is less than balls in the hat'
            for ball in range(balls):
                random_pos = random.randint(0,len(self.contents)-1) # randomly pick a position
                self.picked.append(self.contents[random_pos])
                self.contents.pop(random_pos)
        else:
            'Number of balls picked is more than the balls in the hat'
            self.picked = self.contents.copy()
            self.contents.clear()
        
        return sorted(self.picked) # list is sorted in alphabetical order
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    'Run N number of experiments and calculate how many times correct balls were picked'
    match = 0
    for i in range(num_experiments):
        'Run this N times'
        compare = hat.draw(num_balls_drawn)
        for color in sorted(unpack(expected_balls)):
            'Check each color'
            temp_match = 1
            if color in compare:
                'Color expeted matches color drawed'
                compare.remove(color)
            else:
                temp_match = 0
                break
        match += temp_match

    return match / num_experiments # number of successful experiments / number of experiments = probability
