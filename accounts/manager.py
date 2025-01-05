from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def normalize_phone(self, phone):
        """نرمال‌سازی شماره تلفن (حذف فاصله‌ها و کاراکترهای اضافی)"""
        return phone.strip().replace(' ', '').replace('-', '')

    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('شماره تلفن الزامی است')
        phone = self.normalize_phone(phone)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone, password, **extra_fields)
