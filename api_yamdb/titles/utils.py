from django.utils import timezone


def current_year():
    """Определение текущего года."""
    return timezone.now().year
