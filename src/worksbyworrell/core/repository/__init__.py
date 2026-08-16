import os

from worksbyworrell.core.repository.agent import GithubAgentRepository, LocalAgentRepository
from worksbyworrell.core.repository.base import (
    AgentRepository,
    ResourceRepository,
    SkillMetadataRepository,
    UserProfileRepository,
)
from worksbyworrell.core.repository.profile import (
    GithubUserProfileRepository,
    LocalUserProfileRepository,
)
from worksbyworrell.core.repository.resource import (
    GithubResourceRepository,
    LocalResourceRepository,
)
from worksbyworrell.core.repository.skill import (
    GithubSkillMetadataRepository,
    LocalSkillMetadataRepository,
)


def get_agent_repository() -> AgentRepository:
    if os.environ.get("GITHUB_TOKEN"):
        return GithubAgentRepository()
    return LocalAgentRepository()


def get_profile_repository() -> UserProfileRepository:
    if os.environ.get("GITHUB_TOKEN"):
        return GithubUserProfileRepository()
    return LocalUserProfileRepository()


def get_resource_repository() -> ResourceRepository:
    if os.environ.get("GITHUB_TOKEN"):
        return GithubResourceRepository()
    return LocalResourceRepository()


def get_skill_repository() -> SkillMetadataRepository:
    if os.environ.get("GITHUB_TOKEN"):
        return GithubSkillMetadataRepository()
    return LocalSkillMetadataRepository()
