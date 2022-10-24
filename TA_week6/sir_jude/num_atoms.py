def num_atoms(amount, atomic_weight = 196.97):
    amount = amount 
    moles = amount / atomic_weight
    print(moles *(6.022 * 10**23))
num_atoms(10)