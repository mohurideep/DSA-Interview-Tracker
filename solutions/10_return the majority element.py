# Boyer–Moore Majority Vote Algorithm
# The trick is based on pair cancellation:
# If the majority element appears > n/2 times,
# then even if every other element tries to “fight” it, the majority will still survive after cancellations.
def majority_element(nums: list[int]) -> int:
    candidate = None
    vote = 0
    
    for num in nums:
        if vote == 0:
            candidate = num
            vote =1
        elif num == candidate:
            vote +=1
        else :
            vote -=1
    return candidate