"""GitLab API service for subscription app."""
import logging

import gitlab

logger = logging.getLogger(__name__)


class GitLabService:
    """
    Service class for interacting with GitLab API.

    Provides methods to fetch project information, branches, and file trees.
    """

    def __init__(self, gitlab_url, token):
        """
        Initialize the GitLab service.

        Args:
            gitlab_url: GitLab instance URL (e.g., https://gitlab.com)
            token: Personal Access Token or Project Access Token
        """
        self.gl = gitlab.Gitlab(gitlab_url, private_token=token)

    def get_project_info(self, project_id):
        """
        Fetch basic project information from GitLab.

        Args:
            project_id: GitLab project ID

        Returns:
            dict: Project information including name, description, default branch
        """
        try:
            project = self.gl.projects.get(project_id)
            return {
                "id": project.id,
                "name": project.name,
                "name_with_namespace": project.name_with_namespace,
                "description": project.description or "",
                "default_branch": project.default_branch or "main",
                "web_url": project.web_url,
                "visibility": project.visibility,
            }
        except gitlab.exceptions.GitlabGetError as e:
            logger.error("Failed to get GitLab project %s: %s", project_id, e)
            raise

    def get_branches(self, project_id):
        """
        Fetch list of branches for a GitLab project.

        Args:
            project_id: GitLab project ID

        Returns:
            list: List of branch information dicts
        """
        try:
            project = self.gl.projects.get(project_id)
            branches = project.branches.list(all=True)
            return [
                {
                    "name": branch.name,
                    "default": branch.default,
                    "protected": branch.protected,
                    "commit": {
                        "id": branch.commit["id"],
                        "message": branch.commit.get("message", ""),
                        "authored_date": branch.commit.get("authored_date", ""),
                    },
                }
                for branch in branches
            ]
        except gitlab.exceptions.GitlabGetError as e:
            logger.error("Failed to get branches for project %s: %s", project_id, e)
            raise

    def get_file_tree(self, project_id, path="", branch="main", recursive=False):
        """
        Fetch the file tree for a GitLab project at a specific path and branch.

        Args:
            project_id: GitLab project ID
            path: Directory path to list (empty for root)
            branch: Branch name
            recursive: Whether to list recursively

        Returns:
            list: List of file/directory entries
        """
        try:
            project = self.gl.projects.get(project_id)
            items = project.repository_tree(
                path=path,
                ref=branch,
                recursive=recursive,
                all=True,
            )
            return [
                {
                    "id": item["id"],
                    "name": item["name"],
                    "type": item["type"],  # "tree" (dir) or "blob" (file)
                    "path": item["path"],
                    "mode": item.get("mode", ""),
                }
                for item in items
            ]
        except gitlab.exceptions.GitlabGetError as e:
            logger.error("Failed to get file tree for project %s path %s: %s", project_id, path, e)
            raise

    def validate_token(self, project_id):
        """
        Validate that the provided token can access the project.

        Args:
            project_id: GitLab project ID

        Returns:
            bool: True if token is valid and has access
        """
        try:
            self.gl.auth()
            self.gl.projects.get(project_id)
            return True
        except (gitlab.exceptions.GitlabAuthenticationError, gitlab.exceptions.GitlabGetError):
            return False
