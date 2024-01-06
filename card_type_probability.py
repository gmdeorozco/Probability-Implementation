#Generalization
def get_card_probability_of_being_of_n_types( n=2 ):         
    if n==1:
        return 1/4   
    return 1/4 + get_card_probability_of_being_of_n_types(n-1)

#Implementation
''' 
In a standard deck of 52 playing cards, you draw one card. Find the probability 
that the card is either a heart or a spade.
''' 

prob = get_card_probability_of_being_of_n_types(n=4)
assert prob == 1.0, f'Incorrect probability for n=4: {prob}, expected 1.0'
print('Assertion passed successfully!')

prob = get_card_probability_of_being_of_n_types(n=3)
assert prob == 0.75, f'Incorrect probability for n=3: {prob}, expected 0.75'
print('Assertion passed successfully!')

prob = get_card_probability_of_being_of_n_types(n=2)
assert prob == 0.50, f'Incorrect probability for n=3: {prob}, expected 0.50'
print('Assertion passed successfully!')

prob = get_card_probability_of_being_of_n_types(n=1)
assert prob == 0.25, f'Incorrect probability for n=1: {prob}, expected 0.25'
print('Assertion passed successfully!')