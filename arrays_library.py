import unittest
import functools

class Cons:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        
    def to_array(self):#converts cons list to array
        # print(self.head.to_array())
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])
      

    @classmethod
    def from_array(cls, arr):
        if len(arr) == 0 :
            return None
        head = arr[0]
        tail = arr[1:]
        #TODO: convert a Python list to a cons list.
        return Cons(head, Cons.from_array(tail))
    
    def filter(self, fn):
        return   self.from_array(list(filter( fn, self.to_array())))
    
    def map(self, fn):
        return self.from_array(list(map( fn, self.to_array())))
        
        #TODO: construct a new algebraic list containing all elements
        #      resulting from applying the mapper function to a list.
    def reduce(self, fn):
        return functools.reduce(fn,self.to_array() )

print(Cons.from_array([]))
# arr_ = Cons.from_array([1,2,3,4,5])
# print(arr_.to_array())
print(Cons.from_array([1,2,3,4,5])
                           .reduce(lambda x, y: x + y ))

# print(Cons.from_array(["1","2","3","4","5"])
#                             .reduce(int)
#                             )
# class TestArrFunction(unittest.TestCase):


#     def test_(self):
#         test = Cons()    
#         test.describe("Kata Test Suite")

#         test.it("should create a list out of an array")
#         test.assertEqual(Cons.from_array([]), None)
#         test.assertEqual(Cons.from_array([1,2,3,4,5]).to_array(), [1,2,3,4,5])

#         test.it("should filter elements from a list")
#         test.assert_equals(Cons.from_array([1,2,3,4,5])
#                             .filter(lambda n: n > 3)
#                             .to_array(), [4,5])
#         test.assert_equals(Cons.from_array([1,2,3,4,5])
#                             .filter(lambda n: n > 5), None)

#         test.it("should create a new transformed list out of a source list")
#         test.assert_equals(Cons.from_array(["1","2","3","4","5"])
#                             .map(int)
#                             .to_array(), [1,2,3,4,5])

#         test.it("should filter and transform a list here")

#         test.assert_equals(Cons.from_array([1,2,3,4,5])
#                             .filter(lambda n: n % 2 == 0)
#                             .map(str)
#                             .to_array(), ["2","4"])