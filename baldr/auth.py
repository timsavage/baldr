# -*- coding: utf-8 -*-
from baldr.api import ResourceApiBase
from baldr.exceptions import ImmediateErrorHttpResponse


class LoginRequiredMixin(ResourceApiBase):
    """
    """
    def handle_authorisation(self, request):
        """
        Evaluate if a request is authorised.

        :param request: The current Django request object.

        """
        if not request.user.is_authenticated:
            raise ImmediateErrorHttpResponse(403, 0, 'Login required')