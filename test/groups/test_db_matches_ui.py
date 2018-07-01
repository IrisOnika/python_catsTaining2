from model.group import Group


def test_group_list(appl, db):
    ui_list = appl.group.get_group_list()

    def clean(group):
        return Group(_id=group.id, _name=appl.clear_dobble_space(group.name.strip()))  #remove spaces from a start or an emd of name

    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=appl.sorted_by_id) == sorted(db_list, key=appl.sorted_by_id)