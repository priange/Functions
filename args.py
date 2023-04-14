#1.A function named concatenate_args that takes any number of string arguments
#in positional arguments format and concatenates them into a single string
def concatenate_args(*numbers):
    assurance=""
    for num in numbers:
        assurance+=num

    return assurance

#2.A function named concatenate_kwargs that takes any number of string arguments
#in keyword arguments  format and concatenates them into a single string

def concatenate_kwargs(**keys):
    sured=""
    for key,value in keys.items():
        sured+=value
    
    return sured
