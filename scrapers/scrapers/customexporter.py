import json
from scrapy.exporters import BaseItemExporter

class CustomJSONExporter(BaseItemExporter):
    def __init__(self, **kwargs):
        super(CustomJSONExporter, self).__init__(**kwargs)
        self.json_kwargs = {
            'ensure_ascii': False,
            'indent': 4
        }

    def export_item(self, item):
        return json.dumps(dict(self._get_serialized_fields(item)), **self.json_kwargs)
