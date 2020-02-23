class Node:
    def __init__(self, _data, _left= None, _right= None):
        self.data = _data
        self.left = _left
        self.right = _right
    
    def Insert(self, _value):
        if _value <= self.data:
            if self.left == None:
                self.left = Node(_value)
            else:
                return self.left.Insert(_value)
        else:
            if self.right == None:
                self.right = Node(_value)
            else:
                return self.right.Insert(_value)

    def InsertMultiple(self, _valueArray):
        for value in _valueArray:
            self.Insert(value)

    def Contains(self, _value):
        print('checking if ', str(_value), " = ", str(self.data))
        if _value == self.data:
            return True
        else:
            if _value <= self.data:
                if self.left == None:
                    return False
                else:
                    return self.left.Contains(_value)
            else:
                if self.right == None:
                    return False
                else:
                    return self.right.Contains(_value)

    def PrintInOrder(self):
        if self.left != None:
            self.left.PrintInOrder()
        
        print(self.data)

        if self.right != None:
            self.right.PrintInOrder()

nodey = Node(10)
nodey.InsertMultiple([2,5,7,6])

nodey.PrintInOrder()

