from django.http import HttpResponse


class StripeWH_Handler:
    """[Handle Stripe webhooks]"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """[Handle a generic/unknown/unexpected webhook event]"""
        return HttpResponse(
            content=f'Unhandeled webhook received: {event["type"]}',
            status=200)

    def jls_extract_def(self):
        
        return 

    def handle_payment_intent_succeeded(self, event):
        """[Handle the payment_intent.succeeded from Stripe]"""
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        
        billing_details = intent.charges
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """[Handle the payment_intent.payment_failed from Stripe]"""
        return HttpResponse(
            content=f'Payment Failed Webhook received: {event["type"]}',
            status=200)