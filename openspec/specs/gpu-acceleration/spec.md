# gpu-acceleration Specification

## Purpose
Manages hardware acceleration (CUDA / PyTorch) for document layout analysis, OCR, and dense vector embedding generation while ensuring memory safety and VRAM reclamation.

## Requirements

### Requirement: CUDA GPU Acceleration
The system SHALL utilize NVIDIA CUDA acceleration for Docling layout extraction and BGE-M3 dense vector embedding generation when a compatible GPU is available.

#### Scenario: Running on workstation with NVIDIA RTX 3060
- **WHEN** `KB_EMBEDDING_DEVICE=cuda` and PyTorch detects CUDA
- **THEN** models load to GPU memory in FP16 precision, accelerating inference throughput

### Requirement: Automatic CPU Fallback
The system SHALL automatically fall back to CPU execution when CUDA is unavailable or unconfigured, ensuring portability across developer laptops.

#### Scenario: Running on machine without dedicated GPU
- **WHEN** CUDA is unavailable
- **THEN** system automatically initializes embedding generator on CPU without crashing

### Requirement: VRAM Reclamation and Memory Safety
The system SHALL actively release unused PyTorch GPU memory between batch processing iterations to prevent memory fragmentation and desktop UI lag.

#### Scenario: Running batch ingestion
- **WHEN** a batch of document embeddings completes
- **THEN** system invokes garbage collection and `torch.cuda.empty_cache()` to free unused VRAM
