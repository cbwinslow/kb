# configuration-and-portability Specification

## Purpose
Enforces cross-platform portability and centralized configuration management using Pydantic Settings and environment variables, guaranteeing zero hardcoded credentials or paths.

## Requirements

### Requirement: Centralized Pydantic Configuration
The system SHALL resolve all database connections, SSH settings, file paths, embedding models, and device selections through a unified Pydantic `Settings` model (`kb.config.Settings`).

#### Scenario: Resolving settings from environment or .env
- **WHEN** any `kb` module accesses configuration
- **THEN** settings resolve from environment variables with fallback to `.env`, respecting type annotations and validation rules

### Requirement: Cross-Platform Path Handling
The system SHALL use standard Python `pathlib.Path` for all local filesystem manipulations, ensuring clean cross-platform operation on Windows, Linux, and macOS.

#### Scenario: Running on Windows or Linux
- **WHEN** paths are constructed for data, cache, or logs
- **THEN** system normalizes path separators dynamically without hardcoded drive letters or backslashes

### Requirement: Zero Hardcoded Secrets & Repository Cleanliness
The system SHALL reject hardcoding of hostnames, IP addresses, database passwords, or private keys in tracked git files.

#### Scenario: Validating configuration security
- **WHEN** developer or CI inspects the source repository
- **THEN** all credential fields default to empty or local development defaults, and `.env.example` provides annotated setup instructions
