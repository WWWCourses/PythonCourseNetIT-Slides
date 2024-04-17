class A:
    @staticmethod
    def static_method():
        """Static method: Does not access any class or instance specific data."""
        print("STATIC method fired!")
        print("Nothing is bound to me (but I'm defined inside a class)")
        print("~" * 30)

    @classmethod
    def class_method(cls):
        """Class method: Accesses class object through 'cls', not instance specific."""
        print("CLASS method fired!")
        print(f"{cls} is bound to me")
        print("~" * 30)

    def instance_method(self):
        """Instance method: Accesses instance specific data through 'self'."""
        print("'instance_method' fired!")
        print(f"{self} is bound to me")
        print("~" * 30)

# Creating an instance of class A
a = A()

# Calling static method using the instance (not typical but valid)
a.static_method()  # Typically called using A.static_method()

# Calling class method using the instance (not typical but valid)
a.class_method()  # Typically called using A.class_method()

# Calling instance method using the instance (the intended way)
a.instance_method()
