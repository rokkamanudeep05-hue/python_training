from storage import load_data, save_data
from validator import validate_text, validate_id
from exceptions import (
    MemberNotFoundError,
    DuplicateRecordError,
)


class MemberManager:
    def __init__(self):
        self.members = load_data("members.json")

    def _find_member(self, member_id):
        for member in self.members:
            if member["id"] == member_id:
                return member

        raise MemberNotFoundError(
            f"Member with ID {member_id} was not found."
        )

    def register_member(self, name, email):
        name = validate_text(name, "Name")
        email = validate_text(email, "Email")

        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Please enter a valid email address.")

        if any(
            member["email"].lower() == email.lower()
            for member in self.members
        ):
            raise DuplicateRecordError(
                "A member with this email already exists."
            )

        member_id = str(
            max(
                (int(member["id"]) for member in self.members),
                default=0,
            ) + 1
        )

        member = {
            "id": member_id,
            "name": name,
            "email": email,
            "active": True,
        }

        self.members.append(member)
        self._save()
        return member

    def update_member(self, member_id, name=None, email=None):
        member_id = validate_id(member_id, "Member ID")
        member = self._find_member(member_id)

        if name is not None:
            member["name"] = validate_text(name, "Name")

        if email is not None:
            email = validate_text(email, "Email")

            if "@" not in email or "." not in email.split("@")[-1]:
                raise ValueError("Please enter a valid email address.")

            if any(
                other["id"] != member_id
                and other["email"].lower() == email.lower()
                for other in self.members
            ):
                raise DuplicateRecordError(
                    "Another member already uses this email."
                )

            member["email"] = email

        self._save()
        return member

    def delete_member(self, member_id):
        member_id = validate_id(member_id, "Member ID")
        member = self._find_member(member_id)

        self.members.remove(member)
        self._save()

    def validate_membership(self, member_id):
        member = self._find_member(
            validate_id(member_id, "Member ID")
        )

        if not member["active"]:
            raise ValueError("This membership is inactive.")

        return member

    def list_members(self):
        return self.members.copy()

    def _save(self):
        save_data("members.json", self.members)