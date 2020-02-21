class Sequence:
    """This class represents an object that is an ordered sequence"""
    def __init__(self, components=None):
        """components : list containing the components of the sequence"""
        assert components is None or isinstance(components, (list, tuple)), \
            "Components must be of type (list, tuple) or equal to None"
        if components is None:
            components = list()
        elif isinstance(components, tuple):
            components = list(components)
        self._components = components

    def __len__(self):
        return len(self._components)

    def __iter__(self):
        return iter(self._components)

    def __getitem__(self, item):
        return self._components[item]

    def append(self, obj):
        self._components.append(obj)

class SequenceC(Sequence):
    """This class represents an sequence composed at the lowest level of characters."""
    def __init__(self, components=list()):
        super().__init__(components)
        self.length = len(self.__str__())

    def __str__(self):
        s = ""
        for c in self._components:
            s += str(c)
        return s

    def append(self, obj):
        super().append(obj)
        self.length += len(str(obj))

class Word(SequenceC):
    """Represents a word"""
    pass

class Separator(SequenceC):
    """Represents a separator"""
    pass

class Sentence(SequenceC):
    """Represents a sentence"""
    pass

class Punctuation(SequenceC):
    """Represents a punctuation"""
    pass

class Text(SequenceC):
    """Represents a text"""
    pass
