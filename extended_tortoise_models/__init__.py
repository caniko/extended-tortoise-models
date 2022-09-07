from typing import Optional
from uuid import UUID

from tortoise import Model, fields


class UuidModel(Model):
    id: Optional[UUID] = fields.UUIDField(pk=True)

    class Meta:
        abstract = True


"""
Kudos to Dr. Rina for picking the mountain emoji ⛰ for the description
"""
