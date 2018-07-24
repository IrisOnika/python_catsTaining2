from model.group import Group
import pytest


def test_group_list(appl, db):
    with pytest.allure.step('Given a group list from ui'):
        ui_list = appl.group.get_group_list()

    def clean(group):
        return Group(_id=group.id, _name=appl.clear_dobble_space(group.name.strip()))  #remove spaces from a start or an emd of name

    with pytest.allure.step('Given a group list from db'):
        db_list = map(clean, db.get_group_list())

    with pytest.allure.step('Then group list from db is equal to a list from ui'):
        assert sorted(ui_list, key=appl.sorted_by_id) == sorted(db_list, key=appl.sorted_by_id)