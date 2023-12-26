from abc import ABC, abstractmethod


class GitInterface(ABC):
    """
    Abstract base class for interacting with a Git repository.

    This class defines the interface for performing common Git operations such as cloning, 
    pulling, committing, pushing, and retrieving file content and history against a remote repository.

    Concrete implementations of this class should provide the actual implementation
    for these operations.

    Attributes:
        remote_url (str): The URL of the remote Git repository.
        local_directory (str): The local directory where the repository is or will be cloned.
        auth: Authentication credentials or tokens for accessing the remote repository.
        config: Additional configuration settings.
    """

    def __init__(self, remote_url, local_directory, auth=None, config=None):
        """
        Initialize the Git repository interface with remote repository details.

        Args:
            remote_url (str): The URL of the remote Git repository.
            local_directory (str): The local directory where the repository is or will be cloned.
            auth: Authentication credentials or tokens for accessing the remote repository.
            config: Additional configuration settings.
        """
        self.remote_url = remote_url
        self.local_directory = local_directory
        self.auth = auth
        self.config = config

    @abstractmethod
    async def clone(self):
        """
        Clone a remote Git repository to its local directory.

        Returns:
            bool: True if the clone was successful, False otherwise.
        """
        pass

    @abstractmethod
    def pull(self):
        """
        Pull the latest changes from the remote Git repository.

        Returns:
            bool: True if the pull was successful, False otherwise.
        """
        pass

    @abstractmethod
    def commit(self, message):
        """
        Commit the changes in the Git repository.

        Args:
            message (str): The commit message.

        Returns:
            bool: True if the commit was successful, False otherwise.
        """
        pass

    @abstractmethod
    def push(self):
        """
        Push the committed changes to the remote Git repository.

        Returns:
            bool: True if the push was successful, False otherwise.
        """
        pass

    @abstractmethod
    def get_file_content(self, file_path):
        """
        Get the content of a file in the Git repository.

        Args:
            file_path (str): The path of the file.

        Returns:
            str: The content of the file.
        """
        pass

    @abstractmethod
    def update_file_content(self, file_path, content):
        """
        Update the content of a file in the Git repository.

        Args:
            file_path (str): The path of the file.
            content (str): The new content of the file.

        Returns:
            bool: True if the update was successful, False otherwise.
        """
        pass

    @abstractmethod
    def get_file_history(self, file_path):
        """
        Get the commit history of a file in the Git repository.

        Args:
            file_path (str): The path of the file.

        Returns:
            list: A list of commit objects representing the history of the file.
        """
        pass

    @abstractmethod
    def add_file(self, file_path):
        """
        Add a file to the Git repository.

        Args:
            file_path (str): The path of the file.

        Returns:
            bool: True if the add was successful, False otherwise.
        """
        pass

    @abstractmethod
    def get_changed_files(self):
        """
        Get the list of changed files in the Git repository.

        Returns:
            list: A list of changed files.
        """
        pass

    @abstractmethod
    def get_branches(self):
        """
        Get the list of branches in the Git repository.

        Returns:
            list: A list of branches.
        """
        pass

    @abstractmethod
    def checkout(self, branch):
        """
        Checkout a branch in the Git repository.

        Args:
            branch (str): The name of the branch.

        Returns:
            bool: True if the checkout was successful, False otherwise.
        """
        pass

    @abstractmethod
    async def fetch(self):
        """
        Fetch the latest changes from the remote Git repository.

        Returns:
            bool: True if the fetch was successful, False otherwise.
        """
        pass

    @abstractmethod
    def status(self):
        """
        Get the status of the Git repository.

        Returns:
            str: The status of the Git repository.
        """
        pass
