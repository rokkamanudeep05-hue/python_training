from datetime import date, timedelta

from storage import load_data, save_data
from exceptions import (
    BookUnavailableError,
    BookNotFoundError,
    MemberNotFoundError,
    InvalidMembershipError,
)


class IssueManager:
    LOAN_DAYS = 14
    FINE_PER_DAY = 5

    def __init__(self, books, members):
        self.book_manager = books
        self.member_manager = members
        self.issues = load_data("issues.json")

    def issue_book(self, book_id, member_id):
        book = self.book_manager.get_book(str(book_id))

        if not book["available"]:
            raise BookUnavailableError(
                "This book is already borrowed."
            )

        member = self.member_manager.validate_membership(
            str(member_id)
        )

        today = date.today()
        due_date = today + timedelta(days=self.LOAN_DAYS)

        issue = {
            "id": str(
                max(
                    (int(item["id"]) for item in self.issues),
                    default=0,
                ) + 1
            ),
            "book_id": book["id"],
            "member_id": member["id"],
            "issue_date": today.isoformat(),
            "due_date": due_date.isoformat(),
            "return_date": None,
            "fine": 0,
        }

        book["available"] = False
        self.issues.append(issue)

        self.book_manager._save()
        self._save()

        return issue

    def return_book(self, book_id, member_id):
        book_id = str(book_id)
        member_id = str(member_id)

        issue = next(
            (
                item for item in self.issues
                if item["book_id"] == book_id
                and item["member_id"] == member_id
                and item["return_date"] is None
            ),
            None,
        )

        if issue is None:
            raise ValueError(
                "No active borrowing record found for this book "
                "and member."
            )

        today = date.today()
        due_date = date.fromisoformat(issue["due_date"])

        late_days = max((today - due_date).days, 0)
        fine = late_days * self.FINE_PER_DAY

        issue["return_date"] = today.isoformat()
        issue["fine"] = fine

        book = self.book_manager.get_book(book_id)
        book["available"] = True

        self.book_manager._save()
        self._save()

        return {
            "book_id": book_id,
            "member_id": member_id,
            "late_days": late_days,
            "fine": fine,
        }

    def list_issues(self):
        return self.issues.copy()

    def _save(self):
        save_data("issues.json", self.issues)