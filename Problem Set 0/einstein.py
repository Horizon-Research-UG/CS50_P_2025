# Even if you haven’t studied physics (recently or ever!), you might have heard that 𝐸 =𝑚⁢𝑐2, wherein 𝐸 represents energy (measured in Joules), 𝑚 represents mass (measured in kilograms), and 𝑐 represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

# In a file called einstein.py, 
# 
# 
# implement a program in Python that prompts the user for mass as an integer (in kilograms) 
# 

def einstein():
    int(input("Wie viel Kilo?: "))

# 
# and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

# 𝐸(Joules) =𝑚(Kilo)⁢𝑐(konstante)^2, wherein 𝐸 represents energy (measured in Joules), 
# 𝑚 represents mass (measured in kilograms), 
# and 𝑐 represents the speed of light (measured approximately as 300000000 meters per second)

#e=mc^2 #/c^2
# e/c^2 = m

def einstein():
    m = int(input("Wie viel Kilo?: "))
    print(m * 300000000**2, "Joules")

einstein()

# läuft