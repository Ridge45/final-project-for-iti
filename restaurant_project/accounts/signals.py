from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from customers.models import Customer

@receiver(post_save, sender=User)
def create_or_update_customer(sender, instance, created, **kwargs):
    if created:
        # Create a corresponding Customer entry when a new User is created
        Customer.objects.create(
            name=instance.get_full_name() or instance.username
        )
    else:
        # Update existing Customer info if User is updated
        try:
            customer = Customer.objects.get(name=instance.get_full_name() or instance.username)
            customer.name = instance.get_full_name() or instance.username
            customer.save()
        except Customer.DoesNotExist:
            # If no customer exists with this name, create one
            Customer.objects.create(
                name=instance.get_full_name() or instance.username
            )
