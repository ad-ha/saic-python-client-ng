from dataclasses import dataclass


@dataclass
class LoginResp():
    @dataclass
    class LoginRespDetail():
        languageType: str = None,

    access_token: str = None,
    account: str = None,
    avatar: str = None
    client_id: str = None,
    dept_id: str = None,
    detail: LoginRespDetail = None,
    expires_in: int = None,
    jti: str = None,
    languageType: str = None,
    license: str = None,
    oauth_id: str = None,
    post_id: str = None,
    refresh_token: str = None,
    role_id: str = None,
    role_name: str = None,
    scope: str = None,
    tenant_id: str = None,
    token_type: str = None,
    user_id: str = None,
    user_name: str = None,
