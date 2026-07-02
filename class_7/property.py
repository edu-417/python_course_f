# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y


#     def get_x(self):
#         return self._x
    
#     def set_x(self, x):
#         self._x = x
    
#     def get_y(self):
#         return self._y
    
#     def set_y(self, y):
#         self._y = y
    

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius


#     def _get_radius(self):
#         print("Getting radius")
#         return self._radius
    
#     def _set_radius(self, value):
#         print("Setting radius")
#         self._radius = value

#     def _del_radius(self):
#         print("Deleting radius")
#         del self._radius

#     radius = property(
#         fget=_get_radius,
#         fset=_set_radius,
#         fdel=_del_radius,
#         doc="Radius Property" 
#     )

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     def radius(self):
#         print("Getting radius")
#         return self._radius
    
#     @radius.setter
#     def radius(self, value):
#         print("Setting radius")
#         self._radius = value



# class WritePointError(Exception):
#     pass

# class Point:
#     def __init__(self, x, y):
#         self._x = x
#         self._y = y

#     @property
#     def x(self):
#         return self._x
    
#     @x.setter
#     def x(self, value):
#         raise WritePointError("x is read only")

    
#     @property
#     def y(self):
#         return self._y



# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     def radius(self):
#         print("Getting radius")
#         return self._radius
    
#     @radius.setter
#     def radius(self, value):
#         print("Setting radius")
#         self._radius = value

#     @property
#     def diameter(self):
#         return self.radius * 2
    
#     @diameter.setter
#     def diameter(self, value):
#         self.radius = value / 2


def hash(value):
    return value + 'asdad'
class LoginUser:
    def __init__(self, name: str, password: str):
        self._name = name
        self._password = password

    @property
    def password(self):
        raise AttributeError("Password is write only")
    
    @password.setter
    def password(self, value):
        self._password = hash(value)