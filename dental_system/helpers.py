from datetime import date

from transactions.models import Transactions


def set_attributes(update_data, model_obj):
    for key in update_data.keys():
        setattr(model_obj, key, update_data[key])

def create_invoice_number(cust_id, counter):
    today = date.today()
    year = today.strftime('%Y')
    month = today.strftime('%m')
    day = today.strftime('%d')

    return 'INV/' + year + '/' + month + '/' + day + '/' + str(cust_id) + '/' + str(counter)

def get_counter_from_cust_id(cust_id):
    try:
        cust_trx = Transactions.objects.filter(customer_id=cust_id).order_by('-counter')
        counter = cust_trx[0].counter
        print("cust_trx", counter)

        return counter + 1
    except:
        return 1