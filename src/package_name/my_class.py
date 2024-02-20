class MyClass:
    """
    this is my class
    """
    def __init__(self, name):
        """
        this is my constructor
        """
        self._name = name

    def greet(self, greeting):
        """
        This is my method
        :param greeting:
        :type greeting:
        :return:
        :rtype:
        """
        print(f"{greeting}, {self._name}!")
