from _typeshed import Incomplete

class MeasurementSchemaCreateRequest:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, name: Incomplete | None = None, columns: Incomplete | None = None) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def columns(self): ...
    @columns.setter
    def columns(self, columns) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
