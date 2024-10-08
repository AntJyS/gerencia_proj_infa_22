__all__ = ["NamedType", "OptionalNamedType", "DefaultedNamedType", "NamedTypes"]

class NamedType:
    isOptional: bool
    isDefaulted: bool
    def __init__(self, name, asn1Object, openType: type | None = None) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __hash__(self): ...
    def __getitem__(self, idx): ...
    def __iter__(self): ...
    @property
    def name(self): ...
    @property
    def asn1Object(self): ...
    @property
    def openType(self): ...
    def getName(self): ...
    def getType(self): ...

class OptionalNamedType(NamedType):
    isOptional: bool

class DefaultedNamedType(NamedType):
    isDefaulted: bool

class NamedTypes:
    def __init__(self, *namedTypes, **kwargs) -> None: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __hash__(self): ...
    def __getitem__(self, idx): ...
    def __contains__(self, key) -> bool: ...
    def __iter__(self): ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def values(self): ...
    def keys(self): ...
    def items(self): ...
    def clone(self): ...

    class PostponedError:
        def __init__(self, errorMsg) -> None: ...
        def __getitem__(self, item) -> None: ...

    def getTypeByPosition(self, idx): ...
    def getPositionByType(self, tagSet): ...
    def getNameByPosition(self, idx): ...
    def getPositionByName(self, name): ...
    def getTagMapNearPosition(self, idx): ...
    def getPositionNearType(self, tagSet, idx): ...
    @property
    def minTagSet(self): ...
    @property
    def tagMap(self): ...
    @property
    def tagMapUnique(self): ...
    @property
    def hasOptionalOrDefault(self): ...
    @property
    def hasOpenTypes(self): ...
    @property
    def namedTypes(self): ...
    @property
    def requiredComponents(self): ...
