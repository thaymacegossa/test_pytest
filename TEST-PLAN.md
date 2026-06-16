# 📋 Automated Test Plan — Project Python with Pytest

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/Pytest-Framework-orange?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest" />
  <img src="https://img.shields.io/badge/Docker-Isolated%20Env-blueviolet?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/API-ServeRest-green?style=for-the-badge" alt="ServeRest" />
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

## 🚀 3. Test Scope

| 🟢 In-Scope | 🔴 Out-of-Scope |
| :--- | :--- |
| Validation of HTTP methods for the `/usuarios`, `/login`, and `/produtos` endpoints. | Automation of other base API endpoints (such as `/carrinhos`). |
| Validation of HTTP status codes (`200`, `201`, `400`, `401`, `404`). | Graphical User Interface (UI) automation / Screen testing (UI testing with Selenium/Playwright). |
| Handling of invalid payloads, missing mandatory fields, and duplicate data. | Mass load, stress, and infrastructure performance testing (Locust/JMeter). |
| Verification of the structure and data types of returned data (Contracts). | Deep digital security audits and penetration testing (Pentest). |
| | Production cloud environment configurations (AWS, GCP, Azure). |

---

## 🧪 4. Test Scenarios (Organized by Endpoint)

### 👤 Endpoint: `/usuarios`
| ID | Method | Test Scenario | Expected Behavior | HTTP Status |
| :--- | :---: | :--- | :--- | :---: |
| **CT-001** | `POST` | Register a valid admin user with a unique email. | User successfully created and ID returned. | `201 Created` |
| **CT-002** | `POST` | Try to register a user with a duplicate email. | Return an error message indicating duplication. | `400 Bad Request` |
| **CT-003** | `GET`  | Fetch user data using a valid and existing ID. | Return detailed data of the corresponding user. | `200 OK` |
| **CT-004** | `GET`  | Fetch user data using a non-existent ID. | Return a message stating the user was not found. | `404 Not Found` |
| **CT-005** | `DELETE`| Delete a valid user registered in the system. | Record successfully deleted from the database. | `200 OK` |

### 🔑 Endpoint: `/login`
| ID | Method | Test Scenario | Expected Behavior | HTTP Status |
| :--- | :---: | :--- | :--- | :---: |
| **CT-006** | `POST` | Authenticate a user with valid and registered credentials. | Login authorized and JWT Token returned in the payload. | `200 OK` |
| **CT-007** | `POST` | Try to authenticate with an incorrect email or password. | Access denied with error message "Este email ou senha incorretos". | `401 Unauthorized` |
| **CT-008** | `POST` | Try to authenticate omitting the `email` field from the payload. | Schema validation triggered: "email é obrigatório". | `400 Bad Request` |
| **CT-009** | `POST` | Try to authenticate omitting the `password` field from the payload. | Schema validation triggered: "password é obrigatório". | `400 Bad Request` |
| **CT-010** | `POST` | Try to authenticate with a blank `email` field (`""`). | Error message: "email não pode ficar em branco". | `400 Bad Request` |
| **CT-011** | `POST` | Try to authenticate with an invalid email format. | Error message: "email deve ser um email válido". | `400 Bad Request` |

### 📦 Endpoint: `/produtos`
| ID | Method | Test Scenario | Expected Behavior | HTTP Status |
| :--- | :---: | :--- | :--- | :---: |
| **CT-012** | `POST` | Register a new product with a valid admin token. | Product registered in stock with a generated ID. | `201 Created` |
| **CT-013** | `POST` | Try to register a product without sending an authorization token. | Block creation due to lack of privileges. | `401 Unauthorized` |
| **CT-014** | `PUT`  | Update the data of an existing product by ID. | Information successfully updated in the database. | `200 OK` |

---

## 🏁 5. Quality Criteria (Definition of Done)

| Quality Dimension | Required Parameter | Test Complete Indicator |
| :--- | :--- | :--- |
| **Writing Standard** | AAA Structure | Test code must strictly follow the division: **Arrange** (Setup), **Act** (Execution), and **Assert** (Verification). |
| **Data Isolation** | Autonomous Fixtures | Each test must generate and clean its own test data (`setup` and `teardown`), never depending on the state of another test. |
| **Assertiveness** | Clear Assertions | Use explicit and specific assertions for the payload (avoid generic assertions like just checking if the response is a JSON). |
| **Coverage Metric** | Minimum Coverage | The test file is only considered done if the branch coverage reaches at least **85%** of the core lines. |
| **Technical Resilience** | Error Handling | Negative scenario tests must validate the exact text of the error message returned by the API. |
| **Clean Execution** | Container Execution | The script must run and pass successfully within the Docker environment without relying on local machine configurations. |

---
<p align="center">
  <i>Document structured according to Quality Engineering excellence standards.</i>
</p>