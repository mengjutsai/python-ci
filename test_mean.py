from mean import *
# from mean01 import *

# pytest will collect the function starting with test_
# then check if the function is successfully run

def test_ints():
    nums = [4, 5, 28, 3]
    obs = mean(nums)
    exp = 10
    assert obs == exp

# should be start with "test_"
def test_zero():
    nums = [-3, 0, 3]
    obs = mean(nums)
    exp = 0
    assert obs == exp

def test_neg():
    nums = [-1, 1]
    obs = mean(nums)
    exp = 0
    assert obs == exp

def test_neg_er():
    nums = [-1, 1]
    obs = mean(nums)
    exp = 19
    assert obs == exp
