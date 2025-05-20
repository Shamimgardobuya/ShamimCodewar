
import unittest

class User:
    def __init__(self):
        self.levels = [-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8]
        self.progress_data = 0 
        self.rank_ = -8
    
    @property
    def rank(self):
        if self.rank_ > 8:
            raise ValueError("Rank cannot be greater than 8")
        return self.rank_
    @property
    def progress(self):
        return self.progress_data
        
        
    def inc_progress(self,comp_act_rank):
        points = 0
        rank_index = self.levels.index(self.rank) 
        comp_act_rank_index = self.levels.index(comp_act_rank)
        diff =  rank_index - comp_act_rank_index
        
        if diff == 1:  # completed an activity rank less than their user's rank
            points = 1
        elif ( comp_act_rank_index > rank_index ) : #completed an activity rank higher than the user's rank
            value = comp_act_rank_index - rank_index
            points = 10 * value * value

        elif(comp_act_rank_index == rank_index):
            points = 3
        else:
            points = 0
            
        self.progress_data +=  points
        index = self.levels.index(self.rank_)  # single lookup
        while self.progress_data >= 100 and self.rank_ < 8:
            level_ups = self.progress_data // 100
            new_index = index + level_ups
            if new_index >= len(self.levels):
                self.rank_ = 8
                self.progress_data = 0
                break
            else:
                self.rank_ = self.levels[new_index]
                self.progress_data -= level_ups * 100
                index = new_index  # important to update index for next iteration

                                
                            

        
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
        # user.inc_progress(-8)
        # self.assertEqual(user.rank(), -8)
        # self.assertEqual(user.progress(), 3)
        # user.inc_progress(-7)
        # self.assertEqual(user.rank(), -8)
        # self.assertEqual(user.progress(), 10)
        
        # user.inc_progress(-6)
        # self.assertEqual(user.rank(), -8)
        # self.assertEquals(user.progress(), 40)
            
            
        # user.inc_progress(-5)
        # self.assertEquals(user.rank(), -8)
        # self.assertEquals(user.progress(), 90)

        # user.inc_progress(-4)
        # # self.assertEquals(user.rank(), -7)
        # self.assertEquals(user.progress(), 60)
        
        user.inc_progress(1)
        self.assertEquals(user.rank, -2)
        self.assertEquals(user.progress, 40)
        user.inc_progress(1)
        self.assertEquals(user.rank, -2)
        self.assertEquals(user.progress, 80)


if __name__ == '__main__':
    unittest.main()


