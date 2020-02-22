from printed_text_dataset.sequence.sequence import Word, Sequence
from printed_text_dataset.sequence_r.bounding_box import BoundingBox


class _SequenceRendering(Sequence):
    """abstract class"""

    def set_font(self, font: str):
        for component in self._components:
            component.setFont(font)

    def render_image(self):
        pass


class WordR(_SequenceRendering):
    def __init__(self, word: Word, font: str, spacing: int=None):
        super().__init__(word)
        self.font = font
        self.spacing = spacing
        self.bb = None

    def set_font(self, font: str):
        self.font = font


class LineR(_SequenceRendering):
    def __init__(self, word_seq: _SequenceRendering, spacing: int=None):
        super().__init__(word_seq)
        self.spacing = spacing
        self.bb = None


class ParagraphR(_SequenceRendering):
    def __init__(self, line_seq: _SequenceRendering, spacing: int=None):
        super().__init__(line_seq)
        self.spacing = spacing
        self.bb = None


class TextR(_SequenceRendering):
    def __init__(self, par_seq: _SequenceRendering, shape: tuple, margin: dict):
        super().__init__(par_seq)
        self.shape = shape
        self.margin = margin
        self.bb = BoundingBox(margin['left'],
                              margin['top'],
                              self.shape[0] - margin['bot'] - margin['top'],
                              self.shape[1] - margin['right'] - margin['left'])
