# UNTESTED WITH API
import json


class Document(object):

    def __init__(self):
        self.s = {}

    def set_data(self, data):
        if data.__class__.__name__ == 'Resource':
            self.s['data'] = data.s

    def to_json(self, **kwargs):
        if kwargs.get('indent') is not None:
            return json.dumps(self.s, indent=kwargs['indent'])
        return json.dumps(self.s)


class Link(object):

    def __init__(self, resource_type, resource_name):
        self.s = {'type': resource_type, 'id': resource_name}


class Resource(object):

    def __init__(self, resource_type, attributes, relationships):
        self.s = {}
        self.s['type'] = resource_type
        self.s['attributes'] = {}
        self.s['relationships'] = {}

        for attr_name in attributes:
            self.s['attributes'][attr_name] = attributes[attr_name]

        for relationship_name in relationships:
            if relationships[relationship_name].__class__.__name__ == 'Link':
                # only one Link and should be added when object is created
                rel = relationships[relationship_name]
                self.s['relationships'][relationship_name] = {}
                self.s['relationships'][relationship_name]['data'] = rel.s

    def add_relationship(self, relationship_name, resource):
        if self.s['relationships'].get(relationship_name) is None:
            self.s['relationships'][relationship_name] = {}
            self.s['relationships'][relationship_name]['data'] = []
        if resource.__class__.__name__ == 'Link':
            self.s['relationships'][relationship_name][
                'data'].append(resource.s)


# SAMPLE USAGE
survey_doc = Document()

question_ids = [
    '5647fe7c9bf910ffbbcae5db',
    '5647fe14f374f67c68805ff4',
    '5647fe1de409e792e71e14e0',
    '5647fe0d8599ac3a29754988',
    '565d0d7a71c5442e2b136378',
    '5647fe3e781d026d0b77695b',
    '5647fe4b0dd50ccc027da8c1',
    '5647fe54c64745a657ec39d1',
    '5647fe685f92f23c34bc893b'
]

# define attributes
survey_attributes = {
    'title': 'Tech@NYU Feedback: Venture Capital Panel',
    'URI': 'https://techatnyu.typeform.com/to/iyscbb',
    'responseVisibleTo': ['TEAM_MEMBER']
}

# define single item Link
survey_relationships = {
    'addedBy': Link('people', '544195bba07c236a039e9016')
}

survey_resource = Resource('surveys', survey_attributes, survey_relationships)

# how to add multi-Link relationship
for qid in question_ids:
    survey_resource.add_relationship('questions', Link('questions', qid))

survey_doc.set_data(survey_resource)

# output json for api
print survey_doc.to_json()
# prettyprint
print survey_doc.to_json(indent=2)
