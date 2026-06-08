import pytest
from pep_pre_commit_hooks.verify_git_email import (
    DomainMisconfiguredError,
    main,
    parse_args,
)


def test_parse_args():
    args = parse_args(["--domains", "icloud.com"])
    assert args.domains == "icloud.com"


@pytest.mark.usefixtures("_ch_tempdir", "_git_init", "_git_config_icloud_email")
def test_success():
    assert main(["--domains", "icloud.com"]) == 0


@pytest.mark.usefixtures("_ch_tempdir", "_git_init", "_git_config_icloud_email")
def test_not_correctly_configured_email():
    with pytest.raises(DomainMisconfiguredError) as excinfo:
        main(["--domains", "gmail.com"])

    assert "but an email address matching one of `['gmail.com']` was expected." in str(
        excinfo.value,
    )


@pytest.mark.usefixtures("_ch_tempdir", "_git_init", "_git_config_icloud_email")
def test_missing_domain(capsys):
    with pytest.raises(SystemExit) as excinfo:
        main([])

    captured = capsys.readouterr()
    assert "usage: verify-git-email" in captured.err
    assert "the following arguments are required: --domains" in captured.err
    assert excinfo.value.code == 2
