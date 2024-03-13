class Author :
    def __init__(self, name) :
        self.name = name

    @property
    def name(self) :
        """The name property"""
        return self._name 
    
    @name.setter
    def name(self, name) :
        """ Name must be a string longer than 0 characters in length"""
        if isinstance (name, string) and len(name) > 0 :
            self._name = name
        else :
            raise ValueError(" Name must be a string longer than 0 characters")
        
    def __setattr__(self, name, value):
        if hasattr(self, name):
            raise AttributeError("Attribute '{}' cannot be modified".format(name))
        super().__setattr__(name, value)
        