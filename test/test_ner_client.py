import unittest
from ner_client import NamedEntityClient
from ner_client import SpacyNLP
class TestNerClient(unittest.TestCase):
    # { ents: [{...}],
    #   html: "<span>"  }
    #
    def test_get_ents_returns_dicitonary_given_empty_string_spacy_doc_ents(self):
        model = SpacyNLP()
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dictionary_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = SpacyNLP()
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Madison is a city in wisconson")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = SpacyNLP()
        ner = NamedEntityClient(model)
        ents = ner.get_ents('Mark Wahlberg')
        expected_result = { 'ents': [{'ent': 'Mark Wahlberg', 'label': 'Person'}], 'html': '' }
        self.assertListEqual(ents['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = SpacyNLP()
        ner = NamedEntityClient(model)
        ents = ner.get_ents('The Australian')
        expected_result = { 'ents': [{'ent': 'Australian', 'label': 'Group'}], 'html': '' }
        self.assertListEqual(ents['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_GPE_is_returned_Location(self):
        model = SpacyNLP()
        ner = NamedEntityClient(model)
        ents = ner.get_ents('We are in Budapest')
        expected_result = { 'ents': [{'ent': 'Budapest', 'label': 'Location'}], 'html': '' }
        self.assertListEqual(ents['ents'], expected_result['ents'])  

    def test_get_ents_given_spacy_LOC_is_returned_Location(self):
        model = SpacyNLP()
        ner = NamedEntityClient(model)
        ents = ner.get_ents('The Ocean is by The Station')
        expected_result = { 'ents': [{'ent': 'Ocean', 'label': 'Location'}], 'html': '' }
        self.assertListEqual(ents['ents'], expected_result['ents'])  

    def test_get_ents_given_spacy_LANGUAGE_is_returned_Language(self):
        model = SpacyNLP()
        ner = NamedEntityClient(model)
        ents = ner.get_ents('ASL is a language')
        expected_result = { 'ents': [{'ent': 'ASL', 'label': 'Language'}], 'html': '' }
        self.assertListEqual(ents['ents'], expected_result['ents'])  

    def test_get_ents_given_multiple_ents_returns_serialises_all(self):
        model = SpacyNLP()
        ner = NamedEntityClient(model)
        ents = ner.get_ents('Esperanto the sea Australia Judith Polgar Australian')
        expected_result = { 'ents': [
        {'ent': 'Esperanto', 'label': 'Language'},
        {'ent': 'the sea', 'label': 'Location'},
        {'ent': 'Australia', 'label': 'Location'},
        {'ent': 'Judith Polgar', 'label': 'Person'},
        {'ent': 'Australian', 'label': 'Group'}
        ]
        , 'html': '' 
        }
        self.assertListEqual(ents['ents'], expected_result['ents'])  

    def test_get_ents_returns_mark_entity_with_personAttr_given_person(self):
        model = SpacyNLP()
        ner = NamedEntityClient(model)
        ents = ner.get_ents('Charles Bronson')
        expected_result = { 'ents': [{'ent': 'Charles Bronson', 'label': 'Person'}], 'html': {"""<div class="entities" style="line-height: 2.5; direction: ltr">
        <mark class="entity" style="background: #aa9cfc; padding: 0.45em 0.6em; margin: 0 0.25em; line-height: 1; border-radius: 0.35em;">
        Charles Bronson
        <span style="font-size: 0.8em; font-weight: bold; line-height: 1; border-radius: 0.35em; vertical-align: middle; margin-left: 0.5rem">PERSON</span>
        </mark>
        </div>""" }
        }
        self.assertEqual(ents['html'], expected_result['html'])  