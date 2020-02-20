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
        return sum(str(c) for c in self.components)

    def __iter__(self):
        return iter(self.components)

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
