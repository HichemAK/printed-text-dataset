class Sequence:
    """This class represents an object that is an ordered sequence"""
    def __init__(self, components=None):
        """components : list containing the components of the sequence"""
        assert components is None or isinstance(components, (list, tuple)), \
            "Components must be of type (list, tuple) or equal to None"
        self.components = components

    def __len__(self):
        return len(self.components)

    def __str__(self):
        s = ""
        for c in self.components:
            s += str(c)
        return s

    def __iter__(self):
        return iter(self.components)

    def __getitem__(self, item):
        return self.components[item]

    def append(self, obj):
        self.components.append(obj)

class Word(Sequence):
    """Represents a word"""
    pass

class Separator(Sequence):
    """Represents a separator"""
    pass

class Sentence(Sequence):
    """Represents a sentence"""
    pass

class Punctuation(Sequence):
    """Represents a punctuation"""
    pass

class Text(Sequence):
    """Represents a text"""
    pass
