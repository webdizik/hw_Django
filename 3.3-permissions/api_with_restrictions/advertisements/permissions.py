from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Разрешение на уровне объекта,
    позволяющее редактировать объект только его владельцам.
    """

    def has_object_permission(self, request, view, obj):
        # Чтение разрешено для любого запроса,
        # поэтому всегда разрешаются запросы GET.
        if request.method == 'GET':
            return True

        return request.user == obj.creator