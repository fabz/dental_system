from customers.models import Customer

def create_customer_data(clean_form):
    Customer.objects.create(customer_type=clean_form['type'], name=clean_form['name'], phone_number1=clean_form['phone number 1'], 
                             phone_number2=clean_form['phone number 2'], place_of_birth=clean_form['place of birth'], 
                             date_of_birth=clean_form['dob'], email=clean_form['email'], address=clean_form['address'],
                             id_number=clean_form['id'], photo=clean_form['photo'])

#def create_dentist_data(clean_form):
#    Dentists.objects.create(name=clean_form['name'], email=clean_form['email'], address=clean_form['address'],
#                            phone_number=clean_form['phone_number'], specialization=clean_form['specialization'])
