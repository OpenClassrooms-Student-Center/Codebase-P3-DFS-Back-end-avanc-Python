from django.db import transaction

from .models import Equipment


class EquipmentNotFoundError(Exception):
    pass


class EquipmentUnavailableError(Exception):
    pass


class EquipmentAlreadyAvailableError(Exception):
    pass


class EquipmentService:
    def find_equipment(self, equipment_id: int) -> Equipment:
        try:
            return Equipment.objects.get(pk=equipment_id)
        except Equipment.DoesNotExist as exc:
            raise EquipmentNotFoundError from exc

    @transaction.atomic
    def borrow_equipment(self, equipment_id: int, first_name: str, last_name: str) -> Equipment:
        raise NotImplementedError

    @transaction.atomic
    def return_equipment(self, equipment_id: int) -> Equipment:
        raise NotImplementedError
