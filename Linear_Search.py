 
# Linear search
def linear_search(numbers,searched_value):

  for idx in range(len(numbers)):
    if searched_value==numbers[idx]: return searched_value 

  return '{0} is not in the array'.format(searched_value)

result=linear_search([12,67,8,9,0,11,57,122,1] ,12)
print(result)
