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

    def __init__(self, resource_type, resource_id, attributes, relationships):
        self.s = {}
        self.s['type'] = resource_type
        self.s['id'] = resource_id
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
