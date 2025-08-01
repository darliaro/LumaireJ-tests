[![Python 3.13+](https://img.shields.io/badge/Python-3.13+-black.svg)](https://www.python.org/)
[![PyTest](https://img.shields.io/badge/PyTest-blue?logo=pytest)](https://pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-lightblue?logo=playwright)](https://playwright.dev/)
[![Requests](https://img.shields.io/badge/Requests-grey?logo=python)](https://requests.readthedocs.io/)
[![Faker](https://img.shields.io/badge/Faker-violet?logo=python)](https://faker.readthedocs.io/)
[![Allure TestOps](https://img.shields.io/badge/Allure-blueviolet?logo=allure)](https://docs.qameta.io/allure-testops/)

## API & E2E Test Automation for LumaireJ 🖤✨

#### The test framework for [LumaireJ](https://github.com/darliaro/LumaireJ).

It includes **integration-level API tests** using **Pytest**, **Requests**, and **Allure reporting**,
and **Playwright-based E2E tests** for frontend validation with **Faker** for test data generation.

The framework is designed to run independently via **GitHub Actions dispatch workflow** from the main application repository.

---

### Initial Setup (Local Dev)

- [ ] Install [Python 3.13+](https://www.python.org/downloads/)
- [ ] Install [PDM](https://pdm-project.org/latest/#recommended-installation-method)
- [ ] Install Dependencies:
   ```bash
   pdm install -G dev
- [ ] Install Playwright browsers:
   ```bash
   pdm run playwright install
- [ ] Install pre-commit hooks:
  ```bash
  pdm run pre-commit install
- [ ] Set up a local environment:
   ```bash
  cp .env.template .env
- [ ] Install [Allure CLI](https://docs.qameta.io/allure/#_installing_a_commandline)

> All project dependencies must be added to the `dev` group. Use the alias `pdm-dev <package>` or run `pdm add -G dev <package>` manually.

---

### Running Tests Locally

#### All Tests
- Run the complete test suite:
   ```bash
  pdm run test

- Run with Allure results:
   ```bash
  pdm run test-allure

#### API Tests
- Run all API tests:
   ```bash
  pdm run pytest -m api

- Custom target (e.g., dev/stage):
   ```bash
  pdm run pytest --base-url=http://localhost:8000

#### E2E Tests
- Run all E2E tests:
   ```bash
  pdm run pytest -m e2e

- Run a specific test suite:
   ```bash
  pdm run pytest -m journal

---

### Allure Report Setup

- Generate local report:
   ```bash
  pdm run report

- Open in the browser:
   ```bash
  pdm run open_report

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
  - Run API and E2E tests
  - Generate Allure results (optional)
  - Upload test logs or artifacts (TBD)

---

### Linting and Formatting ([ruff](https://github.com/astral-sh/ruff))

- Check code quality:
   ```bash
  pdm lint

- Auto-fix and format:
   ```bash
  pdm lint --fix && pdm format

---

### Test Strategy

#### API Tests verify:
- HTTP response correctness
- Data validation
- Business logic at API level
- JSON response structure
- Error codes

#### E2E Tests verify:
- UI integration with API
- User scenarios
- Visual display
- Element interactivity
- Page navigation

#### Avoiding Duplication:
1. **API tests** focus on API contract verification
2. **E2E tests** focus on user scenarios
3. **Shared data** is used in both test types
4. **Different markers** for clear separation

---

### Tips

- Add test-level fixtures in `conftest.py` and use `--base-url` to control environment
- Use `allure-results/` as the output directory for Pytest + Allure
- Keep `.env` untracked, use `.env.template` for defaults
- Use Faker for generating realistic test data
- Follow Page Object Model pattern for E2E tests
- Use modern Python 3.13+ syntax throughout the codebase
