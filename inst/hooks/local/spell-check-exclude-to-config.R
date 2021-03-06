#!/usr/bin/env Rscript
library(magrittr)
exclude_hooks <- yaml::read_yaml(here::here(".pre-commit-hooks.yaml")) %>%
  purrr::keep(~ .x$id == "spell-check") %>%
  magrittr::extract2(1) %>%
  purrr::pluck("exclude")

read_config <- function(path) {
  yaml::read_yaml(path) %>%
    purrr::pluck("repos") %>%
    purrr::keep(~ .x$repo == "https://github.com/lorenzwalthert/precommit") %>%
    purrr::pluck(1, "hooks") %>%
    purrr::keep(~ .x$id == "spell-check") %>%
    purrr::pluck(1, "exclude")
}

if (!identical(exclude_hooks, read_config(here::here("inst/pre-commit-config-pkg.yaml")))) {
  rlang::abort(paste0(
    "The `exclude` key from the spell-check hook should be copied from `.pre-commit-hooks.yaml` to ",
    "`inst/pre-commit-config-pkg.yaml` so the two match."
  ))
}

if (!identical(exclude_hooks, read_config(here::here("inst/pre-commit-config-proj.yaml")))) {
  rlang::abort(paste0(
    "The `exclude` key from the spell-check hook should be copied from `.pre-commit-hooks.yaml` to ",
    "`inst/pre-commit-config-proj.yaml` so the two match."
  ))
}
