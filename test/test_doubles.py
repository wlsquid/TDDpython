class NerModelTestDouble:
    #Test double for spaCy NLP model this replicates behvaiour of spaCy for testing or other language processor
    def __init__(self, model):
        self.model = model

    def __call__(self, sent):
        return