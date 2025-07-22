[![Python 3.13+](https://img.shields.io/badge/Python-3.13+-black.svg)](https://www.python.org/)
[![PyTest](https://img.shields.io/badge/PyTest-blue?logo=pytest)](https://pytest.org/)
[![Requests](https://img.shields.io/badge/Requests-grey?logo=python)](https://requests.readthedocs.io/)
[![Allure TestOps](https://img.shields.io/badge/Allure-blueviolet?logo=allure)](https://docs.qameta.io/allure-testops/)

## API & E2E Test Automation for LumaireJ 🖤✨

#### The test framework for for [LumaireJ](https://github.com/darliaro/LumaireJ).

It includes **integration-level API tests** using **Pytest**, **Requests**, and **Allure reporting**,
and is designed to run independently via **GitHub Actions dispatch workflow** from the main application repository.

> Future plans include adding **Playwright-based E2E tests** for frontend validation.

---

### Initial Setup (Local Dev)

- [ ] Install [Python 3.13+](https://www.python.org/downloads/)
- [ ] Install [PDM](https://pdm-project.org/latest/#recommended-installation-method)
- [ ] Install dev-dependencies:
`pdm install -G :all`
- [ ] Install pre-commit hooks:
`pdm run pre-commit install`
- [ ] Set up local environment:
`cp .env.template .env`
- [ ] Install [Allure CLI](https://docs.qameta.io/allure/#_installing_a_commandline)

> All project dependencies must be added to the `dev` group. Use the alias `pdm-dev <package>` or run `pdm add -G dev <package>` manually.

---

### Running API Tests Locally

- Run all tests:
  `pdm run pytest -sv tests/api/`

- Custom target (e.g., dev/stage):
  `pdm run pytest --base-url=http://localhost:8000`

- Run with Allure results:
  `pdm run pytest --alluredir=allure-results`

---

### Allure Report Setup

- Generate local report:
  `allure generate allure-results --clean -o allure-report`

- Open in browser:
  `allure open allure-report`

> You can also configure CI to upload Allure artifacts after each run.

---

### Running Tests in GitHub Actions

Tests are triggered automatically by the [main backend repo](https://github.com/darliaro/LumaireJ) via a `repository_dispatch` event.

#### Manual Trigger
- Push or merge to `main` in `LumaireJ`
- GitHub Actions workflow sends dispatch signal to this repo
- This repo runs its own workflow to:
  - Checkout both codebases
  - Start backend service via Docker
  - Run API tests
  - Generate Allure results (optional)
  - Upload test logs or artifacts (TBD)

---

### Linting and Formatting ([ruff](https://github.com/astral-sh/ruff))

- Check code quality:
  `pdm run ruff check tests/`

- Auto-fix and format:
  `pdm run ruff check tests/ --fix && pdm run ruff format tests/`

---

### Tips

- Add test-level fixtures in `conftest.py` and use `--base-url` to control environment
- Use `allure-results/` as the output directory for Pytest + Allure
- Keep `.env` untracked, use `.env.template` for defaults
