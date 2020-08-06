# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
    n_to = ''
    s_to = ''
    e_to = ''
    w_to = ''
#

    def __str__(self):
        return ("name: {} description: {}".format(self.name, self.description))
