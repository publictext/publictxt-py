# git_exceptions.py

class GitError(Exception):
    """Base exception for git-related errors."""

    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class CloneError(GitError):
    """Raised when a clone operation fails."""
    pass


class PullError(GitError):
    """Raised when a pull operation fails."""
    pass


class CommitError(GitError):
    """Raised when a commit operation fails."""
    pass


class PushError(GitError):
    """Raised when a push operation fails."""
    pass


class FileContentError(GitError):
    """Raised when an operation involving file content fails."""
    pass


class UpdateFileError(GitError):
    """Raised when updating a file in the repository fails."""
    pass


class FileHistoryError(GitError):
    """Raised when retrieving the file history fails."""
    pass


class AddFileError(GitError):
    """Raised when adding a file to the repository fails."""
    pass


class ChangedFilesError(GitError):
    """Raised when an operation to retrieve changed files fails."""
    pass


class BranchesError(GitError):
    """Raised when retrieving branches fails."""
    pass


class CheckoutError(GitError):
    """Raised when checking out a branch fails."""
    pass


class FetchError(GitError):
    """Raised when fetching from the remote repository fails."""
    pass


class StatusError(GitError):
    """Raised when retrieving the status of the repository fails."""
    pass


