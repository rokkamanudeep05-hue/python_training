from datetime import date


class ReportManager:
    def __init__(self, books, members, issues):
        self.book_manager = books
        self.member_manager = members
        self.issue_manager = issues

    def available_books(self):
        return [
            book for book in self.book_manager.list_books()
            if book["available"]
        ]

    def borrowed_books(self):
        return [
            book for book in self.book_manager.list_books()
            if not book["available"]
        ]

    def top_borrowers(self):
        counts = {}

        for issue in self.issue_manager.list_issues():
            member_id = issue["member_id"]
            counts[member_id] = counts.get(member_id, 0) + 1

        members = {
            member["id"]: member["name"]
            for member in self.member_manager.list_members()
        }

        ranking = [
            {
                "member_id": member_id,
                "name": members.get(member_id, "Deleted member"),
                "books_borrowed": count,
            }
            for member_id, count in counts.items()
        ]

        return sorted(
            ranking,
            key=lambda item: item["books_borrowed"],
            reverse=True,
        )

    def fine_report(self):
        report = []
        today = date.today()

        for issue in self.issue_manager.list_issues():
            if issue["return_date"] is not None:
                fine = issue["fine"]
                late_days = max(
                    (
                        date.fromisoformat(issue["return_date"])
                        - date.fromisoformat(issue["due_date"])
                    ).days,
                    0,
                )
            else:
                late_days = max(
                    (
                        today
                        - date.fromisoformat(issue["due_date"])
                    ).days,
                    0,
                )
                fine = late_days * self.issue_manager.FINE_PER_DAY

            if fine > 0:
                report.append({
                    "book_id": issue["book_id"],
                    "member_id": issue["member_id"],
                    "late_days": late_days,
                    "fine": fine,
                    "returned": issue["return_date"] is not None,
                })

        return report