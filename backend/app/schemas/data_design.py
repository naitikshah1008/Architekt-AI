from pydantic import BaseModel, Field
from typing import List

class FieldSpec(BaseModel):
    name: str
    type: str
    nullable: bool
    description: str

class TableSpec(BaseModel):
    name: str
    fields: List[FieldSpec]
    primary_key: List[str]
    indexes: List[str]

class RelationshipSpec(BaseModel):
    table: str
    field: str
    linked_table: str
    linked_field: str

class DataDesignSpec(BaseModel):
    tables: List[TableSpec]
    relationships: List[RelationshipSpec] = Field(default_factory=list)
    partitioning_strategy: List[str] = Field(default_factory=list)
    caching_strategy: List[str] = Field(default_factory=list)