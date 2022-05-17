from groups.models import Group


def test_groups_get_group_item_by_id(admin_client, group):
    response = admin_client.get(f'/groups/{group.id}')
    assert response.status_code == 200


def test_groups_put_valid_payload(admin_client, group):
    payload = {
        'name': "NameNew",
        'course': "CourseNew",
        'start_date': "2021-09-27"
    }
    response = admin_client.put(f'/groups/edit/{group.id}', data=payload)
    assert response.status_code == 200
    assert response.context_data['form'].errors == {
        'name': ['This field is required.'],
        'course': ['This field is required.'],
        'start_date': ['This field is required.']
    }
