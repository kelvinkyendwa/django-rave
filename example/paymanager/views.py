# stdlib imports

# django imports
from django.views.generic import TemplateView

# 3rd party imports

# project imports
from djangorave.models import PaymentTypeModel


class SignUpView(TemplateView):
    """Sign Up view"""

    template_name = "paymanager/signup.html"

    def get_context_data(self, **kwargs):
        """Add plan to context data"""
        context_data = super().get_context_data(**kwargs)
        context_data["pro_plan"] = PaymentTypeModel.objects.filter(
            payment_plan__isnull=False
        ).first()
        context_data["buy_now"] = PaymentTypeModel.objects.filter(
            payment_plan__isnull=True
        ).first()
        return context_data

