from model.contact import Contact


def test_group_list(appl, db):
    ui_list = appl.contact.get_contact_list()

    def clean(contact):
        return Contact(_id=contact.id,                       #remove spaces from a start or an emd of name
                       _firstname=appl.clear_dobble_space(contact.firstname.strip()),
                       _lastname=appl.clear_dobble_space(contact.lastname.strip()),
                       _address=appl.clear_dobble_space(contact.address.strip()),
                       _all_phones=contact.all_phones,
                       _all_emails=contact.all_emails
                       )

    db_list = map(clean, db.get_contact_list())
    assert sorted(ui_list, key=appl.sorted_by_id) == sorted(db_list, key=appl.sorted_by_id)