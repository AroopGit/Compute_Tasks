def check_first_last_same(nums):
  if nums[0] == nums[-1]:
    return True
  else:
    return False

nums = [1, 2, 3, 4, 5]
if check_first_last_same(nums):
  print("The first and last numbers are the same.")
else:
  print("The first and last numbers are not the same.")
