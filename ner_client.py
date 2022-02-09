import spacy
from spacy import displacy
import abc

class NamedEntityClient:
    def __init__(self, model):
        self.model = model
    
    def get_doc(self, sentence):
        doc = self.model.returns_doc(sentence)
        return doc

    def get_ents(self, sentence):
        doc = self.model.returns_doc(sentence)
        html = self.model.returns_html(doc)
        entities = [{'ent': ent.text, 'label' : self.map_label(ent.label_) } for ent in doc.ents]
        return {'ents': entities, 'html': html}

    @staticmethod
    def map_label(label):
        label_map = {
            'PERSON': 'Person',
            'NORP' : 'Group',
            'GPE' : 'Location',
            'LOC' : 'Location',
            'LANGUAGE' : 'Language'
        }

        return label_map.get(label)

class NPLinterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'returns_doc') and
                callable (subclass.returns_doc_ents) and
                hasattr(subclass, 'returns_html') and
                callable (subclass.returns_html) or
                NotImplemented)
    
    @abc.abstractmethod
    def returns_doc(self, sentence: str):
        raise NotImplementedError

    @abc.abstractmethod
    def returns_html(self, doc):
        raise NotImplementedError
    
class SpacyNLP(NPLinterface):
    def returns_doc(self, sentence):
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(sentence)
        return doc
    
    def returns_html(self, doc):
        html = displacy.render(doc, style="ent")
        return html
