from dentists.models import Dentists


def create_dentist_data(clean_form):
    Dentists.objects.create(name=clean_form['name'], email=clean_form['email'], address=clean_form['address'],
                            phone_number=clean_form['phone_number'], specialization=clean_form['specialization'], birth_place=clean_form['birth_place'], birth_date=clean_form['birth_date'])
