# class InstanceCounter:
#     num_instances = 0

#     def __init__(self):
#         InstanceCounter.num_instances += 1


# class Dog:
#     specie = 'canis familiaris'

#     def __init__(self, name: str):
#         self.name = name


class InstanceCounter:

    def __init__(self):
        self.num_instances = 0

    
    def increment(self):
        self.num_instances += 1