import datetime as dt
from datetime import date, datetime

from schoolmanagement_api.apps.subscription.models import MonthlySubscription


def get_subscription_status():
    first_date_object = MonthlySubscription.objects.first()
    if first_date_object is None:
        subscription = MonthlySubscription(status="active", date_paid=date.today())
        subscription.save()

    subscription_date = first_date_object.date_paid

    if datetime.today().date() >= subscription_date + dt.timedelta(days=30):
        first_date_object.status = "expired"
        first_date_object.save()
        return {"subscription": "expired"}
    return {"subscription": "expired"}

    # date_now = datetime.now()
    # # date_now = dt.date(2023,3,28)
    # fixed_date = dt.date(int(date_now.year), int(date_now.month), 28)
    #
    # if date_now.date() < fixed_date:
    #     return {"subscription": "active"}
