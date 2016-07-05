from customers.models import Customer

def create_customer_data(clean_form):
    Customer.objects.create(customer_type=clean_form['customer_type'], name=clean_form['name'], phone_number1=clean_form['phone_number1'], 
                             phone_number2=clean_form['phone_number2'], place_of_birth=clean_form['place_of_birth'], 
                             date_of_birth=clean_form['date_of_birth'], email=clean_form['email'], address=clean_form['address'])

#def create_dentist_data(clean_form):
#    Dentists.objects.create(name=clean_form['name'], email=clean_form['email'], address=clean_form['address'],
#                            phone_number=clean_form['phone_number'], specialization=clean_form['specialization'])
