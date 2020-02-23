class Node:
        def __init__(self, _value, _next = None):
            self.value = _value
            self.next = _next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = None

    def GetIndex(self, _index, _returnValue = True):
        if _index < 0:
            print("Invalid index. Index must be atleast 0")
            return None
        
        currentNode = self.head

        while _index and currentNode:
            _index = _index - 1
            currentNode = currentNode.next

        return currentNode.value if currentNode and _returnValue else currentNode if currentNode else None

    def AddFirst(self, _value):
        self.head = Node(_value, self.head)

    def AddLast(self, _value):
        if(self.head): #ensures that the list is not empty
            currentNode = self.head
        else: 
            self.AddFirst(_value)
            return
        
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = Node(_value)
        
    def PushToIndex(self, _value, _index):
        if _index == 0:
            self.AddFirst(_value)
        else:    
            previousNode = self.GetIndex(_index - 1, False)
            nextNode = self.GetIndex(_index, False)
            previousNode.next = Node(_value, nextNode)

    def ReplaceIndex(self, _value, _index):
        self.GetIndex(_index, False).value = _value

    def DestroyFirst(self):
        if self.head.next:
            self.head = self.head.next
        elif self.head:
            self.head = None

    def DestroyIndex(self, _index):
        previousNode = self.GetIndex(_index - 1, False)
        nodeToDestroy = self.GetIndex(_index, False)
        previousNode.next = nodeToDestroy.next if nodeToDestroy.next else None

    # def DestroyLast(self):
    #     if self.head.next:
    #         currentNode = self.head
    #         while currentNode.next.next.next:
    #             currentNode.next = None
    #     elif self.head:
    #         self.head = None

    def __str__(self):
        currentNode = self.head
        listOfValues = ""
        while currentNode:
            #either adds a coma or doesn't after the value depending if there is a node after
            listOfValues = listOfValues + str(currentNode.value) + ", " if currentNode.next else listOfValues + str(currentNode.value)
            currentNode = currentNode.next
        return listOfValues

listy = LinkedList()
listy.AddLast(1)
listy.AddLast(2)
listy.AddLast(3)
listy.DestroyLast()


print(listy)


