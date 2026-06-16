# 🧪 Automated API Testing Suite — Project test_pytest

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/Pytest-Framework-orange?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest" />
  <img src="https://img.shields.io/badge/Docker-Isolated%20Env-blueviolet?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/API-ServeRest-green?style=for-the-badge" alt="ServeRest" />
</p>

---

## 📌 About the Project

Based directly on the strategic goals established in our QA planning, this repository houses a comprehensive automated testing suite built to validate the integrity, resilience, and correctness of the business rules and data contracts exposed by the **ServeRest API**. 

The entire framework is designed to prevent code regressions during parallel branch development and ensure absolute stability before merging features into the main branch.

---

## 🛠️ Technologies & Tools

| Component | Tool / Technology | Strategic Purpose within the Project |
| :--- | :--- | :--- |
| **Language** | `Python 3.10+` | Core programming language for writing scalable test scripts. |
| **Framework** | `Pytest` | Main testing engine for assertions, parametrization, and fixtures. |
| **HTTP Client** | `Requests` | Library used to trigger, manipulate, and validate HTTP API endpoints. |
| **Metrics** | `Pytest-cov` | Coverage utility to measure and audit validated code lines. |
| **Infrastructure**| `Docker & Compose` | Containerization tool ensuring environment parity across any machine. |

---

## 🧠 Architectural Design & Implementation

| Pattern / Pillar | Technical Approach | Benefit & Quality Impact |
| :--- | :--- | :--- |
| **AAA Structure** | `Arrange, Act, Assert` | Rigidly separates test data setup (**Arrange**), HTTP execution (**Act**), and payload verification (**Assert**). |
| **State Management**| `Pytest Fixtures` | Centralizes authentication lifecycles (JWT generation) and dynamic data instantiation in `conftest.py`. |
| **Idempotency** | `Isolated Setup/Teardown` | Every test case generates its own unique database state and cleans up immediately, preventing flaky test behaviors. |

---

## 📁 Repository Map

| Path / File | Type | Architectural Role |
| :--- | :--- | :--- |
| **`.github/workflows/`** | `CI/CD` | Automated pipelines (GitHub Actions) executing tests on every Push/PR. |
| **`tests/`** | `Directory` | Root folder containing all automated test script classes. |
| ├── `test_login.py` | `Script` | Authentication edge cases and JSON schema validations. |
| ├── `test_usuarios.py` | `Script` | Full CRUD lifecycle validations for user management. |
| └── `test_produtos.py` | `Script` | Role-restricted inventory and product creation scenarios. |
| **`conftest.py`** | `Configuration` | Global hooks and shared fixtures for dynamic payload injection. |
| **`Dockerfile`** | `Infrastructure`| Image definition blueprints to package dependencies and Python runtime. |
| **`docker-compose.yml`** | `Orchestration` | Multi-container environment settings for single-command executions. |
| **`TEST-PLAN.md`** | `Documentation`| Detailed strategic testing tables, quality gates, and project goals. |

---

## ⚙️ Execution Guide

### 🐳 1. Multi-Container Docker Isolation (Recommended)
```bash
# Build the test runtime environment and execute all test cases automatically
docker-compose up --build test
```

### 💻 2. Native Local Environment
```bash
# Clone the repository & enter directory
git clone [https://github.com/thaymacegossa/test_pytest.git](https://github.com/thaymacegossa/test_pytest.git) && cd test_pytest

# Create, activate virtual environment & install core dependencies
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt

# Execution options
pytest          # Run suite silently
pytest -v       # Run suite in verbose mode (detailed names)
```

---

## 📊 Test Coverage Analysis

This automation framework adopts the **API Route and HTTP Verb Coverage** methodology, tracking verified live endpoints against the designated project scope.

### 🧮 Functional Coverage Formula
$$\text{API Functional Coverage} = \left( \frac{\text{Total Tested Verbs/Routes}}{\text{Total Verbs/Routes in Project Scope}} \right) \times 100$$

### 📈 Scope Coverage Matrix
| Endpoint | HTTP Method | Target Validation Scope | Coverage Status | Coverage % |
| :--- | :---: | :--- | :---: | :---: |
| `/usuarios` | `POST` | Admin & Client Creation / Duplicate E-mail Prevention | 🟢 Covered | 100% |
| `/usuarios` | `GET` | Query by Valid Unique ID / Non-existent ID Error | 🟢 Covered | 100% |
| `/usuarios` | `DELETE`| Permanent Record Erasure and Database Cleanup | 🟢 Covered | 100% |
| `/login` | `POST` | Valid JWT Issuance / Credentials Failures / Schema Blocks | 🟢 Covered | 100% |
| `/produtos` | `POST` | Admin Privilege Verification / Tokenless Block | 🟢 Covered | 100% |
| `/produtos` | `PUT` | Mid-flight Product Modification and Update Validity | 🟢 Covered | 100% |

> **Consolidated Audit Metric:** The test suite successfully achieves **100% Functional Coverage** regarding the planned repository scope.

---

## 🧪 Automated Test Cases Matrix

### 👤 Module: `/usuarios`
| ID | Method | Test Scenario Context | Expected API Behavior | Status |
| :--- | :---: | :--- | :--- | :---: |
| **CT-001** | `POST` | Register a valid admin user with a unique dynamic email. | User successfully created and ID returned. | `201 Created` |
| **CT-002** | `POST` | Attempt to register a profile utilizing a pre-existing email. | Return conflict error message regarding duplication. | `400 Bad Request` |
| **CT-003** | `GET`  | Fetch account details using a valid and registered ID. | Return detailed payload matching the target profile. | `200 OK` |
| **CT-004** | `GET`  | Query a user profile using an invalid or non-existent ID. | Return an error stating the record was not found. | `404 Not Found` |
| **CT-005** | `DELETE`| Execute absolute deletion of an active user record. | Wipe database entry and return success confirmation. | `200 OK` |

### 🔑 Module: `/login`
| ID | Method | Test Scenario Context | Expected API Behavior | Status |
| :--- | :---: | :--- | :--- | :---: |
| **CT-006** | `POST` | Authenticate an active profile with correct credentials. | Grant API access and return authorization JWT Token. | `200 OK` |
| **CT-007** | `POST` | Attempt authentication using incorrect password or email. | Deny access with a standardized unauthorized payload. | `401 Unauth` |
| **CT-008** | `POST` | Attempt authentication omitting the mandatory `email` field. | Trigger validation contract: "email is required". | `400 Bad Request` |
| **CT-009** | `POST` | Attempt authentication omitting the mandatory `password` field.| Trigger validation contract: "password is required".| `400 Bad Request` |
| **CT-010** | `POST` | Attempt login with a blank string `""` inside the email field. | Return a bad request message blocking empty strings. | `400 Bad Request` |
| **CT-011** | `POST` | Attempt login sending an unformatted email structure (no `@`). | Catch formatting violation and reject the payload. | `400 Bad Request` |

### 📦 Module: `/produtos`
| ID | Method | Test Scenario Context | Expected API Behavior | Status |
| :--- | :---: | :--- | :--- | :---: |
| **CT-012** | `POST` | Create a new stock product using a verified admin JWT token. | Register item in stock and generate a unique product ID. | `201 Created` |
| **CT-013** | `POST` | Attempt product creation without providing an auth token header. | Block operations and return lack of privileges warning. | `401 Unauth` |
| **CT-014** | `PUT`  | Modify data points of an existing item using its unique ID. | Commit shifts to database and return success report. | `200 OK` |

---

## 📖 Strategy & Architecture Documentation

For a deep dive into the underlying quality gates, branch governance, and specific contract criteria, reference our master architecture planning:

👉 **[Strategic Test Plan (TEST-PLAN.md)](./TEST-PLAN.md)**

---

# 📋 Strategic Test Plan — Project test_pytest

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/Pytest-Framework-orange?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest" />
  <img src="https://img.shields.io/badge/Docker-Isolated%20Env-blueviolet?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/Git%20Flow-Active%20Branches-lightgrey?style=for-the-badge&logo=git&logoColor=white" alt="Git Flow" />
</p>

---

## 🎯 1. Test Suite Objective

| Parameter | Strategic Definition and Purpose |
| :--- | :--- |
| **Main Focus** | Validate the integrity, resilience, and correctness of the business rules and data contracts exposed by the implemented endpoints of the ServeRest API. |
| **Risk Mitigation** | Prevent code regressions during parallel branch development and ensure stability before merging into the main branch (`main`). |
| **Delivery Assurance** | Ensure that any code changes or refactoring maintain the expected behavior of HTTP endpoints without breaking API contracts. |

---

## 🛠️ 2. Test Strategy

| Test Layer | Test Type | Tools Used | Technical Approach |
| :--- | :--- | :--- | :--- |
| **Component / Isolated** | `Unit` | Python 3.10+, Pytest | Test utility functions and core validation logic isolated from external dependencies. |
| **Integration / Contract** | `Functional (API)` | Pytest, Requests | Validate raw HTTP calls, JSON Schema validation, and response payload verification. |
| **Service Isolation** | `Mocking / Stubbing` | Pytest-mock | Simulate third-party service unavailability and infrastructure failures. |
| **Orchestration** | `Isolated Env` | Docker, Docker Compose | Run the entire test suite inside a standardized image to avoid local machine environment variations. |

---

## 🚀 3. Scope of Validation & Coverage

| Component Technical | Target Validation Details | Scope Status | QA Engineering Focus |
| :--- | :--- | :---: | :--- |
| **Endpoints Verbs** | Validation of HTTP methods for `/usuarios`, `/login`, and `/produtos`. | 🟢 **IN** | Verifying payloads, query params, and specific header inputs. |
| **Status Handlers** | Validation of HTTP status codes (`200`, `201`, `400`, `401`, `404`). | 🟢 **IN** | Ensuring correct categorical mapping of server responses. |
| **Negative Contexts**| Handling of invalid payloads, missing fields, and duplicate data. | 🟢 **IN** | Forcing schema rejections and validation message parity. |
| **Data Contracts** | Verification of data structures and JSON response data types. | 🟢 **IN** | Ensuring contract consistency to block API breakdowns. |
| **UI Automation** | Graphical User Interface / Frontend testing. | 🔴 **OUT** | Project focused strictly on backend logic and automation cores. |
| **Performance** | Mass load, stress, and infrastructure performance testing. | 🔴 **OUT** | High-volume concurrency simulations are out of current scope. |

---

## 📊 4. Branch Strategy & Governance (Git Flow)

Because the repository operates with unmerged development branches, QA governance enforces pre-merge checkpoint mandates:

| Branch Type | Repository Context | Mandatory QA Checkpoint | Merge Authorization Criteria |
| :--- | :--- | :--- | :--- |
| `feature/*` / `task/*` | Active functionality in isolated workspaces. | Local Docker test execution + implementation of corresponding assertions. | 100% test success rate within the branch; no regression found. |
| `develop` | Baseline integration thread for code consolidation. | Complete test execution triggered upon Pull Request creation. | Zero failures detected; coverage log exported successfully. |
| `main` / `master` | Stable deployment state for production delivery. | Final robust regression run over entire endpoint spectrum. | Strict execution block on any failure. Overall stability preserved. |

---

## 🧪 5. Test Scenarios Matrix

| ID | Endpoint | Method | Test Scenario Context | Expected Behavior |
| :--- | :--- | :---: | :--- | :--- |
| **CT-001** | `/usuarios` | `POST` | Register a valid admin user with a unique dynamic email. | User successfully created and ID returned (`201 Created`). |
| **CT-002** | `/usuarios` | `POST` | Attempt to register a profile utilizing a pre-existing email. | Return conflict error message (`400 Bad Request`). |
| **CT-003** | `/usuarios` | `GET`  | Fetch account details using a valid and registered ID. | Return detailed payload matching profile (`200 OK`). |
| **CT-004** | `/usuarios` | `GET`  | Query a user profile using an invalid or non-existent ID. | Return an error stating record was not found (`404 Not Found`). |
| **CT-005** | `/usuarios` | `DELETE`| Execute absolute deletion of an active user record. | Wipe database entry and return success (`200 OK`). |
| **CT-006** | `/login` | `POST` | Authenticate an active profile with correct credentials. | Grant API access and return authorization Token (`200 OK`). |
| **CT-007** | `/login` | `POST` | Attempt authentication using incorrect password or email. | Deny access with a standardized unauthorized payload (`401 Unauth`). |
| **CT-008** | `/login` | `POST` | Attempt authentication omitting the mandatory `email` field. | Trigger validation contract: "email is required" (`400 Bad Request`). |
| **CT-009** | `/login` | `POST` | Attempt authentication omitting the mandatory `password` field.| Trigger validation contract: "password is required" (`400 Bad Request`).|
| **CT-010** | `/login` | `POST` | Attempt login with a blank string `""` inside the email field. | Return a bad request message blocking empty strings (`400 Bad Request`). |
| **CT-011** | `/login` | `POST` | Attempt login sending an unformatted email structure (no `@`). | Catch formatting violation and reject the payload (`400 Bad Request`). |
| **CT-012** | `/produtos` | `POST` | Create a new stock product using a verified admin JWT token. | Register item in stock and generate product ID (`201 Created`). |
| **CT-013** | `/produtos` | `POST` | Attempt product creation without providing an auth token header. | Block operations and return lack of privileges (`401 Unauth`). |
| **CT-014** | `/produtos` | `PUT`  | Modify data points of an existing item using its unique ID. | Commit shifts to database and return success report (`200 OK`). |

---

## ⚙️ 6. Command Execution Matrix

| Execution Environment | Command Line Terminal Target | Technical Behavior Breakdown |
| :--- | :--- | :--- |
| **Docker Container** | `docker-compose up --build test` | Compiles isolated container layers and runs full suite end-to-end. |
| **Local Terminal** | `pytest` | Direct native scan and run of all available `test_*.py` files. |
| **Verbose Mode** | `pytest -v` | Outputs comprehensive validation sheets listing individual test functions. |
| **Coverage Metrics** | `pytest --cov=src --cov-report=term` | Executes test sweeps while outputting terminal line coverage tracking. |

---

## 🏁 7. Quality Gates (Definition of Done)

| Gate Phase | Rule Parameter Mandate | Metrics & Target Acceptance Criteria |
| :--- | :--- | :--- |
| **Entry Criteria** | Code Readiness & Context | Codebase compiles cleanly without syntax failures; environment variables set up. |
| **Exit Criteria** | Suite Success Rates | **100% of automated test cases must pass** successfully; zero failures tolerated. |
| **Exit Criteria** | Target Code Coverage | Comprehensive branch coverage metrics must track at or above **85%**. |
| **Exit Criteria** | Regression Assurance | Verification that changes in active feature branches cause zero functional breaks on master lanes. |

---

<p align="center">
  Developed by <b>Thayani Macegossa</b> 🚀
</p>
<p align="center">
  <i>Document structured according to Quality Engineering excellence standards.</i>
</p>