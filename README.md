Private collection of [pre-commit hooks](https://pre-commit.com/)


## Available hooks

### `verify-git-email`

This hook verifies that a committer's email address matches a domain.

This hook can serve two use cases:
- Ensure people hide their private email addresses, e.g. by using the respective [GitHub setting](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address). `--domains` is set to `users.noreply.github.com` by default to cover this use case. Note that GitHub provides a way to [block pushes that contain private email addresses](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/blocking-command-line-pushes-that-expose-your-personal-email-address) that are enforced on push, while this hook enforces on commit.

- Ensure that people within an organisation commit with their org email address instead of their private address. This is most useful for private repositories where the email does not need to be hidden and where people should be prevented to accidentially commit with their private email address.


## How to use the hooks

You can include the hooks like this in your repo:

```yaml
# in .pre-commit-config.yaml in your git repo root
repos:

  - repo: https://github.com/lorenzwalthert/pre-commit-hooks
    rev: 4305ba8
    hooks:
      - id: verify-git-email
        args: [--domains=my.domain]
```
