class Sequence:
    """This class represents an object that is an ordered sequence"""
    def __init__(self, components=None):
        """components : list containing the components of the sequence"""
        assert components is None or isinstance(components, (list, tuple, Sequence)), \
            "Components must be of type (list, tuple) or equal to None"
        if components is None:
            components = list()
        elif isinstance(components, tuple):
            components = list(components)
        elif isinstance(components, Sequence):
            components = components._components.copy()
        self._components = components

    def __len__(self):
        return len(self._components)

    def __iter__(self):
        return iter(self._components)

    def __getitem__(self, item):
        return self._components[item]

    def append(self, obj):
        self._components.append(obj)

class SequenceCharacter(Sequence):
    """This class represents a sequence composed at the lowest level of characters."""
    def __init__(self, components=None):
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


class Word(SequenceCharacter):
    """Represents a word"""
    pass

class Separator(SequenceCharacter):
    """Represents a separator"""
    pass

class Sentence(SequenceCharacter):
    """Represents a sentence"""
    pass

class Punctuation(SequenceCharacter):
    """Represents a punctuation"""
    pass

class Text(SequenceCharacter):
    """Represents a text"""
    pass