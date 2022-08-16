def  rat_food(n, unit, m, food):
  if (n*unit > sum(food)):
    return -1
  else:
    food_avl_so_far = 0
    for i in range(0,n):
      food_avl_so_far += food[i]
      if food_avl_so_far >= n*unit:
        return i+1

food = [2,3,8,5,7,4,1,2]
m = 8
n = 7
unit = 2
rat_food(n, unit, m, food)