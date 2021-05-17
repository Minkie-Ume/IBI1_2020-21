n = 84
#set the initial number of patients
r = 1.2
#assuming that the r rate equals to 1.2
i = 1
#calculate n in 5 generations.
while i in range(1,6):
        n = n + n * r#calculate the new total number of n after a new generation
        i = i + 1
print(n)


