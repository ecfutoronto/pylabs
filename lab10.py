# Question 1
def generate_as():
    str = ''
    while True:
        yield str
        str += 'a'

# Question 2 
def dosido(it):
    j = 0
    # new_lst = []
    while j < len(it) and len(it) % 2 == 0:
        # new_lst.append(it[j+1])
        yield it[j+1]
        # new_lst.append(it[j])
        yield it[j]
        j += 2
    if len(it) % 2 != 0:
        yield it[len(it)-1]
    # return new_lst

# Question 3

def bakhshali_square_root(S):
    x = [600]
    j = 0
    while True:
        a_n = (S - x[j]*x[j])/(2*x[j])
        b_n = x[j] + a_n
        x_n1 = b_n - (a_n*a_n)/ (2*b_n)
        j += 1
        x.append(x_n1)
        yield x_n1


# Question 4

def babylonian_square_root(S):
    x = [S/2]
    j = 0
    while True:
        x_n1 = (x[j] + S/x[j])/2
        x.append(x_n1)
        yield x_n1
        j = j+1