from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Collection

# Old ASP.Net site members DAO abstraction
class MembershipProvider(ABC):

    #region IApplicationNameHolder
    @abstractmethod
    def get_app_name(self) -> str:
        ...

    @abstractmethod
    def set_app_name(self, app_name: str) -> None:
        ...
    #endregion

    #region IPasswordValidator
    @abstractmethod
    def validate_user(self, user_name: str, password: str) -> bool:
        ...
    #endregion

    #region IPasswordChanger
    @abstractmethod
    def can_reset_password(self) -> bool:
        ...

    @abstractmethod
    def change_password(self, user_name: str, old_password: str, new_password: str) -> bool:
        ...

    @abstractmethod
    def change_password_question_and_answer(self, user_name: str, password: str, new_password_question: str, new_password_answer: str) -> bool:
        ...

    @abstractmethod
    def reset_password(self, user_name: str, answer: str) -> str:
        ...
    #endregion

    #region IPasswordRetriever
    @abstractmethod
    def can_retrieve_password(self) -> bool:
        ...

    @abstractmethod
    def get_password(self, user_name: str, answer: str) -> str:
        ...
    #endregion

    #region IUserRepository
    @abstractmethod
    def create_user(self, 
        user_name: str, password: str, email: str,
        password_question: str, pasword_answer: str, is_approved: bool, provider_user_key: object) -> tuple[MembershipUser, MembershipCreateStatus]:
        ...

    @abstractmethod
    def delete_user(self, user_name: str, delete_all_related_data: bool) -> bool:
        ...

    @abstractmethod
    def unlock_user(self, user_name: str) -> bool:
        ...

    @abstractmethod
    def update_user(self, user: MembershipUser) -> None:
        ...

    @abstractmethod
    def get_all_users(self, page_index: int, page_size: int) -> Collection[MembershipUser]:
        ...


    @abstractmethod
    def get_user_by_name(self, user_name: str, user_is_online: bool) -> MembershipUser:
        ...

    @abstractmethod
    def get_user_by_provider_key(self, provider_user_key: object, user_is_online: bool) -> MembershipUser:
        ...

    @abstractmethod
    def get_user_name_by_email(self, email: str) -> str:
        ...

    @abstractmethod
    def find_users_by_email(self, email_to_match: str, page_index: int, page_size: int) -> Collection[MembershipUser]:
        ...

    @abstractmethod
    def find_users_by_name(self, user_name_to_match: str, page_index: int, page_size: int) -> Collection[MembershipUser]:
        ...

    @abstractmethod
    def get_number_of_online_userS(self) -> int:
        ...
    #endregion

    #region IUserRestrictions
    @abstractmethod
    def requires_unique_email(self) -> bool:
        ...
    #endregion

    #region IPasswordRestrictions
    @abstractmethod
    def requires_question_and_answer(self) -> bool:
        ...
        
    @abstractmethod
    def get_max_invalid_password_attempts(self) -> int:
        ...

    @abstractmethod
    def get_min_required_alphanumberic_characters(self) -> int:
        ...

    @abstractmethod
    def get_min_required_password_length(self) -> int:
        ...

    @abstractmethod
    def get_password_attempt_window(self) -> int:
        ...

    @abstractmethod
    def get_password_format(self) -> MembershipPasswordFormat:
        ...

    @abstractmethod
    def get_password_strength_regular_expression(self) -> str:
        ...
    #endregion

class MembershipUser:
    pass

class MembershipCreateStatus:
    pass

class MembershipPasswordFormat:
    pass