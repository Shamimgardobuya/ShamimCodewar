
import unittest

class User:
    def __init__(self):
        self.levels = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
        self.progress_data = 0 
        self.rank_ = -8
    def rank(self,rank_up_levels=None):
        for index, value in enumerate(self.levels):      
            if rank_up_levels:
                self.rank_ = self.levels[index + rank_up_levels]
                break
        return self.rank_
    
    def progress(self, point=None):
        if point == None:
            self.progress_data += 0

        else:    

            self.progress_data +=  point
            if self.progress_data >= 100: 
                levels = self.progress_data // 100 
                self.rank(levels)
                self.progress_data = self.progress_data - (levels * 100)

                
        return self.progress_data
        
        
    def inc_progress(self,comp_act_rank):
        points = 0
        rank_index = self.levels.index(self.rank(None)) 
        comp_act_rank_index = self.levels.index(comp_act_rank)
        diff =  rank_index - comp_act_rank_index
        
        if rank_index > comp_act_rank_index and diff == 1 :#completed an activity rank less than their users rank
            points = 1
        elif ( comp_act_rank_index > rank_index ) : #completed an activtiy rank higher than their users rank
            if (comp_act_rank == 1) :
                comp_act_rank = 0
            value = self.rank(None) - comp_act_rank
            points = 10 * value * value

        elif(comp_act_rank_index == rank_index):
            points = 3
        else:
            points = 0
        self.progress(points)

        
        return points
        
        
# user = User()
# # print(user.rank)
# # print(user.progress())
# print(user.inc_progress(-8))
# print(user.rank())
# print(user.progress())
# # print(user.inc_progress(-5)) # will add 90 progress
# # print(user.progress()) # => 0 # progress is now zero
# # print(user.rank()) #-7
# # print(user.inc_progress(-4)) # will add 1 progress
# # print(user.progress())
# # print(user.rank())

class TestAddFunction(unittest.TestCase):


    def test_(self):
        user = User()
        user.inc_progress(-8)
        self.assertEqual(user.rank(), -8)
        self.assertEqual(user.progress(), 3)
        user.inc_progress(-7)
        self.assertEqual(user.rank(), -8)
        self.assertEqual(user.progress(), 10)
        
        user.inc_progress(-6)
        self.assertEqual(user.rank(), -8)
        self.assertEquals(user.progress(), 40)
            
            
        user.inc_progress(-5)
        self.assertEquals(user.rank(), -8)
        self.assertEquals(user.progress(), 90)

        user.inc_progress(-4)
        # self.assertEquals(user.rank(), -7)
        self.assertEquals(user.progress(), 60)
        
        user.inc_progress(1)
        self.assertEquals(user.rank(), -2)
        self.assertEquals(user.progress(), 40)
        user.inc_progress(1)
        self.assertEquals(user.rank(), -2)
        self.assertEquals(user.progress(), 80)


if __name__ == '__main__':
    unittest.main()


