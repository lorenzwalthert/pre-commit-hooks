import pytest
from personal_pre_commit_hooks import verify_git_email


@pytest.mark.usefixtures("_ch_tempdir", "_git_init", "_git_config_icloud_email")
def test_verify_domain():
    # one domain
    assert verify_git_email.verify_git_email("icloud.com") is None
    # multiple domains
    assert verify_git_email.verify_git_email("icloud.com,gmail.com") is None
    assert verify_git_email.verify_git_email("gmail.com,icloud.com") is None


@pytest.mark.usefixtures("_ch_tempdir", "_git_init", "_git_config_icloud_email")
def test_failed_verify_domain():
    with pytest.raises(
        verify_git_email.DomainMisconfiguredError,
        match="but an email address matching ",
    ):
        verify_git_email.verify_git_email("hotmail.com")
