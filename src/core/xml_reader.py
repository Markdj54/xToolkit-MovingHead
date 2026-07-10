import xml.etree.ElementTree as ET

from core.model import Model


class XMLReader:

    def __init__(self):
        self.tree = None
        self.root = None
        self.models = []

    # ---------------------------------------------
    # Load XML
    # ---------------------------------------------

    def load(self, filename):

        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()

        self.models = []

        models_section = self.root.find("models")

        if models_section is None:
            return False

        for xml_model in models_section:

            model = Model(xml_model.attrib)

            self.models.append(model)

        self.models.sort(key=lambda m: m.name.lower())

        return True

    # ---------------------------------------------
    # Return all models
    # ---------------------------------------------

    def get_models(self):

        return self.models

    # ---------------------------------------------
    # Return only names
    # ---------------------------------------------

    def get_model_names(self):

        return [m.name for m in self.models]

    # ---------------------------------------------
    # Find model by name
    # ---------------------------------------------

    def get_model(self, name):

        for model in self.models:

            if model.name == name:
                return model

        return None

    # ---------------------------------------------
    # Return Moving Heads only
    # ---------------------------------------------

    def get_moving_heads(self):

        return [m for m in self.models if m.is_moving_head()]

    # ---------------------------------------------
    # Count models
    # ---------------------------------------------

    def count(self):

        return len(self.models)