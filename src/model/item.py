class Item:
    def __init__(self, name, color, size, item_type):
        self.name = name 
        self.color = color
        self.size = size 
        self.item_type = item_type
    def __str__(self):
        return '------- Item -------\nName: {}\nColor: {}\nSize: {}\nType: {}'.format(self.name, self.color, self.size, self.item_type)
