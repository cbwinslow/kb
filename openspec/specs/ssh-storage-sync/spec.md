# ssh-storage-sync Specification

## Purpose
Manages secure remote archival of scientific PDFs and tabular benchmark datasets to the homelab storage vault via encrypted SSH/SFTP, while enforcing workstation local disk space preservation.

## Requirements

### Requirement: Encrypted SSH/SFTP File Synchronization
The system SHALL transfer research PDFs and Parquet fixtures to designated remote directory paths on the homelab host (`cbwdellr720`) via paramiko SSH/SFTP using private key authentication.

#### Scenario: Testing SSH connectivity
- **WHEN** user executes `kb sync ssh-check`
- **THEN** system establishes an SSH connection, verifies SFTP directory readability and write permissions, and reports connection status

#### Scenario: Uploading PDF to homelab vault
- **WHEN** a scientific paper PDF is ingested on the local worker
- **THEN** system uploads the PDF to the configured remote path (`KB_SSH_REMOTE_PDF_DIR`) and verifies successful transfer

### Requirement: Workstation Local Disk Space Protection
The system SHALL enforce a minimum local disk free space threshold ($\ge 1.5$ GB) on workstation `cbwwin` and automatically clean up temporary downloaded files.

#### Scenario: Enforcing disk threshold before batch run
- **WHEN** a batch ingestion is initiated
- **THEN** system queries host drive free space and halts with a warning if free space is below the safe threshold

#### Scenario: Unlinking local temporary PDF after upload
- **WHEN** a PDF has been parsed, embedded, and synced to homelab storage
- **THEN** system deletes the local copy from the temporary download directory, preserving host drive space
