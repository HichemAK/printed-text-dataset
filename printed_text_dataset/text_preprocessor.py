from printed_text_dataset.text_generation.distribution import Distribution


class TextPreprocessor:
    def __init__(self, paragraph_spacing_distrib : Distribution, word_spacing_distrib : Distribution,
                 line_spacing_distrib : Distribution, shape : tuple, margin_distrib : list, font_distrib : Distribution,
                 font_size_distrib : Distribution,):
        self