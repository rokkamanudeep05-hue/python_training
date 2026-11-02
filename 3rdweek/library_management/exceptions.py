class LibraryError(Exception):
    """Base exception for library operations."""
    pass


class BookNotFoundError(LibraryError):
    pass


class MemberNotFoundError(LibraryError):
    pass


class BookUnavailableError(LibraryError):
    pass


class InvalidMembershipError(LibraryError):
    pass


class DuplicateRecordError(LibraryError):
    pass