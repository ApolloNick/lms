from teachers.models import Teacher


def test_teacher_form_get(admin_client):
    response = admin_client.get('/teachers/create/')
    assert response.status_code == 200


def test_teacher_form_post(admin_client):
    response = admin_client.post('/teachers/create/')
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'first_name': ['This field is required.'],
        'last_name': ['This field is required.'],
        'age': ['This field is required.'],
        'occupation': ['This field is required.'],
        'email': ['This field is required.'],
        'birth_date': ['This field is required.'],
        'phone_number': ['This field is required.'],
        'group': ['This field is required.'],
        'position': ['This field is required.']
    }


def test_teacher_form_post_valid(admin_client, group):
    position = Teacher.PositionLevel.TEACHER
    payload = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'age': 33,
        'occupation': 'Python',
        'email': 'hello__11@gmail.com',
        'birth_date': '1987-01-01',
        'phone_number': '+38(099)6274709',
        'group': group.id,
        'position': position,
    }
    response = admin_client.post('/teachers/create/', data=payload)
    assert response.status_code == 302
    assert response.url == '/teachers/'


def test_teacher_form_post_invalid_email(admin_client, group, position):
    payload = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'age': 33,
        'occupation': 'Python',
        'email': 'invalid-email',
        'birth_date': '1987-01-01',
        'phone_number': '+38(099)6274709',
        'group': group.id,
        'position': position,
    }
    response = admin_client.post('/teachers/create/', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['Enter a valid email address.']
    }


def test_teacher_form_post_valid_email_already_exists(admin_client, group):
    position = Teacher.PositionLevel.TEACHER
    payload = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'age': 33,
        'occupation': 'Python',
        'email': 'jameswatson@example.org',
        'birth_date': '1987-01-01',
        'phone_number': '+38(099)6274709',
        'group': group.id,
        'position': position,
    }
    response = admin_client.post('/teachers/create/', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'email': ['Such email already exists']
    }
