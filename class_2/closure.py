scope = 'global'
def power_factory(exponent):
     scope = 'nonlocal'
     print(vars())
     def power(base):
         scope = 'local'
         print(vars())
         return base ** exponent

     return power


# power_factory(2)

# def power(base):
#     return base ** 2

# power_factory(3)

# def power(base):
#     return base ** 3