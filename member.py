class Member:

    def __init__(self, member_id, name, phone):
        self.member_id = member_id
        self.name = name
        self.phone = phone
        self.borrowed_books = []

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "phone": self.phone,
            "borrowed_books": self.borrowed_books
        }