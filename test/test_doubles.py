class NerModelTestDouble:
    #Test double for spaCy NLP model this replicates behvaiour of spaCy for testing or other language processor
    def __init__(self, model):
        self.model = model
    
    def returns_doc_ents(self, ents):
        self.ents = ents

    def __call__(self, sent):
        return DocTestDouble(sent, self.ents)

class DocTestDouble:
    #Test double for spaCy Doc

    def __init__(self, sent, ents):
        self.ents = [SpanTestDouble(ent['text'], ent['label_']) for ent in ents]

# class SpanTestDouble:
#     def __init__(self, text, label):
#         self.text = text
#         self.label_ = label

# class NerHtmlTestDouble:
#     def __init__(self, displacy):
#         self.displacy = displacy

#     def returns_ents_html(self, html):
#         self.html = html

#     def __call__(self, sent):
#         return HTMLTestDouble(sent, self.html)

# class HTMLtestdouble:
#     def __init__(self, sent, html):
#         self.html = 

