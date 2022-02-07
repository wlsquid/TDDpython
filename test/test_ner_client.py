import unittest
from ner_client import NamedEntityClient
from test_doubles import NerModelTestDouble
class TestNerClient(unittest.TestCase):
    # { ents: [{...}],
    #   html: "<span>"  }
    #
    def test_get_ents_returns_dicitonary_given_empty_string_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dictionary_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = NerModelTestDouble('eng')
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Madison is a city in wisconson")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Laurent Fressinet', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        ents = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Laurent Fressinet', 'label': 'Person'}], 'html': '' }
        self.assertListEqual(ents['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Lithuanian', 'label_': 'NORP'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        ents = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Lithuanian', 'label': 'Group'}], 'html': '' }
        self.assertListEqual(ents['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_GPE_is_returned_Location(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Budapest', 'label_': 'GPE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        ents = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Budapest', 'label': 'Location'}], 'html': '' }
        self.assertListEqual(ents['ents'], expected_result['ents'])  

    def test_get_ents_given_spacy_LOC_is_returned_Location(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'the ocean', 'label_': 'LOC'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        ents = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'the ocean', 'label': 'Location'}], 'html': '' }
        self.assertListEqual(ents['ents'], expected_result['ents'])  

    def test_get_ents_given_spacy_LANGUAGE_is_returned_Language(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'ASL', 'label_': 'LANGUAGE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        ents = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'ASL', 'label': 'Language'}], 'html': '' }
        self.assertListEqual(ents['ents'], expected_result['ents'])  

    def test_get_ents_given_multiple_ents_returns_serialises_all(self):
        model = NerModelTestDouble('eng')
        doc_ents = [
        {'text': 'German', 'label_': 'LANGUAGE'}, 
        {'text': 'the sea', 'label_': 'LOC'}, 
        {'text': 'Australia', 'label_': 'GPE'}, 
        {'text': 'Judith Polgar', 'label_': 'PERSON'}, 
        {'text': 'Australian', 'label_': 'NORP'} 
        ]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        ents = ner.get_ents('...')
        expected_result = { 'ents': [
        {'ent': 'German', 'label': 'Language'},
        {'ent': 'the sea', 'label': 'Location'},
        {'ent': 'Australia', 'label': 'Location'},
        {'ent': 'Judith Polgar', 'label': 'Person'},
        {'ent': 'Australian', 'label': 'Group'}
        ]
        , 'html': '' 
        }
        self.assertListEqual(ents['ents'], expected_result['ents'])  

    def test_get_ents_returns_mark_entity_with_personAttr_given_person(self):
        model = NerModelTestDouble('eng')
        doc_ents = [{'text': 'Charles Bronson', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        ents = ner.get_ents('...')
        expected_result = { 'ents': [{'ent': 'Charles Bronson', 'label': 'Person'}], 'html': {'<mark data-entity="person">Charles Bronson</mark>' }
        }
        self.assertListEqual(ents['html'], expected_result['html'])  