def patternProperties(validator, patternProperties, instance, schema) -> None: ...
def propertyNames(validator, propertyNames, instance, schema) -> None: ...
def additionalProperties(validator, aP, instance, schema) -> None: ...
def items(validator, items, instance, schema) -> None: ...
def const(validator, const, instance, schema) -> None: ...
def contains(validator, contains, instance, schema) -> None: ...
def exclusiveMinimum(validator, minimum, instance, schema) -> None: ...
def exclusiveMaximum(validator, maximum, instance, schema) -> None: ...
def minimum(validator, minimum, instance, schema) -> None: ...
def maximum(validator, maximum, instance, schema) -> None: ...
def multipleOf(validator, dB, instance, schema) -> None: ...
def minItems(validator, mI, instance, schema) -> None: ...
def maxItems(validator, mI, instance, schema) -> None: ...
def uniqueItems(validator, uI, instance, schema) -> None: ...
def pattern(validator, patrn, instance, schema) -> None: ...
def format(validator, format, instance, schema) -> None: ...
def minLength(validator, mL, instance, schema) -> None: ...
def maxLength(validator, mL, instance, schema) -> None: ...
def dependentRequired(validator, dependentRequired, instance, schema) -> None: ...
def dependentSchemas(validator, dependentSchemas, instance, schema) -> None: ...
def enum(validator, enums, instance, schema) -> None: ...
def ref(validator, ref, instance, schema) -> None: ...
def dynamicRef(validator, dynamicRef, instance, schema) -> None: ...
def type(validator, types, instance, schema) -> None: ...
def properties(validator, properties, instance, schema) -> None: ...
def required(validator, required, instance, schema) -> None: ...
def minProperties(validator, mP, instance, schema) -> None: ...
def maxProperties(validator, mP, instance, schema) -> None: ...
def allOf(validator, allOf, instance, schema) -> None: ...
def anyOf(validator, anyOf, instance, schema) -> None: ...
def oneOf(validator, oneOf, instance, schema) -> None: ...
def not_(validator, not_schema, instance, schema) -> None: ...
def if_(validator, if_schema, instance, schema) -> None: ...
def unevaluatedItems(validator, unevaluatedItems, instance, schema) -> None: ...
def unevaluatedProperties(validator, unevaluatedProperties, instance, schema) -> None: ...
def prefixItems(validator, prefixItems, instance, schema) -> None: ...
