from groups.models import Group
from teachers.models import Teacher


def test_get_teachers_list(client_api):
    response = client_api.get('/api/v1/teachers/')
    assert response.status_code == 200
    assert response.json()['count']
    assert response.json()['results']


def test_teachers_post_empty_payload(client_api):
    response = client_api.post('/api/v1/teachers/', data={})
    assert response.status_code == 400
    assert response.json() == {
        'first_name': ['This field is required.'],
        'last_name': ['This field is required.'],
        'occupation': ['This field is required.']
    }


def test_teachers_post_valid_payload(client_api):
    payload = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'occupation': 'Python',
    }
    response = client_api.post('/api/v1/teachers/', data=payload, format='json')
    assert response.status_code == 201, response.json()
    assert response.json()['first_name'] == payload['first_name']


def test_teachers_put_valid_payload(client_api):
    teacher = Teacher.objects.last()
    payload = {
        'first_name': 'FirstName_1',
        'last_name': 'LastName_1',
        'occupation': 'PHP'
    }
    response = client_api.put(f'/api/v1/teachers/{teacher.id}/', data=payload)
    assert response.status_code == 200, response.json()
    assert response.json()['first_name'] == payload['first_name']


def test_teachers_put_delete_success(client_api):
    teacher = Teacher.objects.last()
    response = client_api.delete(f'/api/v1/teachers/{teacher.id}/')
    assert response.status_code == 204, response.json()
    assert not response.content


def test_get_groups_list(client_api):
    response = client_api.get('/api/v1/groups/')
    assert response.status_code == 200
    assert response.json()['count']
    assert response.json()['results']


def test_groups_post_empty_payload(client_api):
    response = client_api.post('/api/v1/groups/', data={})
    assert response.status_code == 400
    assert response.json() == {
        'name': ['This field is required.'],
        'course': ['This field is required.']
    }


def test_groups_post_valid_payload(client_api):
    payload = {
        'name': 'NameTest',
        'course': 'CourseTest',
        'start_date': '2021-09-27',
    }
    response = client_api.post('/api/v1/groups/', data=payload, format='json')
    assert response.status_code == 201, response.json()
    assert response.json()['name'] == payload['name']


def test_groups_put_valid_payload(client_api):
    group = Group.objects.last()
    payload = {
        'name': 'NameTestNew',
        'course': 'CourseTestNew',
        'start_date': '2021-09-27'
    }
    response = client_api.put(f'/api/v1/groups/{group.id}/',
                              data=payload, format='json')
    assert response.status_code == 200
    assert response.json()['name'] == payload['name']


def test_groups_delete_success(client_api):
    group = Group.objects.last()
    response = client_api.delete(f'/api/v1/groups/{group.id}/')
    assert response.status_code == 204, response.json()
    assert not response.content


