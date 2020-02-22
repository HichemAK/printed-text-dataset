from printed_text_dataset.sequence.sequence import Text, Sentence, Word, Punctuation, Separator
from printed_text_dataset.text_generation.distribution import Distribution

from PIL import ImageFont


class TextPreprocessor:
    def __init__(self, paragraph_spacing_distrib : Distribution, word_spacing_distrib : Distribution,
                 line_spacing_distrib : Distribution, shape : (tuple, list), margin_distrib : dict,
                 font_distrib : Distribution, font_size_distrib : Distribution, font_level : Level):

        self.paragraph_spacing_distrib = paragraph_spacing_distrib
        self.word_spacing_distrib = word_spacing_distrib
        self.line_spacing_distrib = line_spacing_distrib
        self.shape = shape
        self.margin_distrib = margin_distrib
        self.font_distrib = font_distrib
        self.font_size_distrib = font_size_distrib
        self.font_level = font_level

    def preprocess(self, text : Text) -> TextR:
        text_r = TextR()
        text_r.shape = self.shape

        # Sampling text_r.margin
        margin = dict()
        for k in self.margin_distrib:
            margin[k] = self.margin_distrib[k].sample()

        text_r.margin = margin

        for sent_sep in text:
            if isinstance(sent_sep, Sentence):
                for word_sep_pun in sent_sep:
                    if isinstance(word_sep_pun, (Word, Punctuation)):
                        word_r = WordR(components=word_sep_pun)
                        word_r.spacing = self.word_spacing_distrib.sample()
                        if self.font_level = Level.WORD:
                            word_r.setFont(self.sample_font())
                            word_r.generate_bb()

    def sample_font(self):
        font_name, size = self.font_distrib.sample(), self.font_size_distrib.sample()
        font = ImageFont.truetype(font_name, size)
        return font



