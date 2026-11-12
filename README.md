# PCIe 4.0 / 5.0, AMD Smart Access Memory (ReBAR) & Frame-Time Micro-Stutter Profiler

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![AMD Radeon](https://img.shields.io/badge/AMD_Radeon-RDNA_Architecture-ED1C24?style=for-the-badge&logo=amd&logoColor=white)

> **Live Interactive PCIe Bandwidth & ReBAR Frame-Time Profiler (GitHub Pages):** [https://hipolitopeedro.github.io/pcie-rebar-frametime-profiler/](https://hipolitopeedro.github.io/pcie-rebar-frametime-profiler/)
>
> **English:** Low-level GPU/PCIe subsystem diagnostics and frame-time consistency profiler designed for **AMD Ryzen (AM4 / AM5) + AMD Radeon (RDNA 2 / RDNA 3 / RDNA 4)** platforms. Audits **Resizable BAR / Smart Access Memory (`Large Memory Range`)**, **MSI (Message Signaled Interrupts)** mode, and **HAGS**, and processes PresentMon/CapFrameX logs to compute **1% Low / 0.1% Low FPS**, **99th percentile frame times (`ms`)**, and **frame-to-frame micro-stutter variance**.
>
> **Português:** Ferramenta de diagnóstico de barramento GPU/PCIe e análise de consistência de *frame-time* projetada para plataformas **AMD Ryzen (AM4 / AM5) + AMD Radeon (RDNA 2 / RDNA 3 / RDNA 4)**. Audita alocação de **Resizable BAR / Smart Access Memory (`Large Memory Range`)**, interrupções **MSI (Message Signaled Interrupts)** e **HAGS**, e processa logs do PresentMon/CapFrameX para calcular **1% Low / 0.1% Low FPS**, **percentil 99 de frame-time (`ms`)** e **micro-stuttering**.

---

## Included Tools / Ferramentas Inclusas

| File | Description (EN) | Descrição (PT-BR) |
| :--- | :--- | :--- |
| [`src/frametime_stutter_analyzer.py`](src/frametime_stutter_analyzer.py) | Parses PresentMon / CapFrameX CSV frame traces (`msBetweenPresents`, `msGPUActive`, `msCPUWait`) to compute Average FPS, **1% Low / 0.1% Low FPS**, frame-to-frame pacing jitter (`ms`), and CPU vs. GPU bottleneck ratios. | Analisa logs CSV de captura de quadros (PresentMon / CapFrameX) para calcular Média de FPS, **1% Low / 0.1% Low FPS**, jitter entre quadros consecutivos (`ms`) e percentual de gargalo de CPU vs. GPU. |
| [`scripts/Test-PCIeAndReBarTopology.ps1`](scripts/Test-PCIeAndReBarTopology.ps1) | PowerShell hardware auditor that inspects the GPU PCIe bus, verifies **Message Signaled Interrupts (MSI)** in the Windows Registry, checks **Hardware-Accelerated GPU Scheduling (HAGS)**, and confirms **Smart Access Memory / Resizable BAR** status. | Auditor em PowerShell que inspeciona o barramento PCIe da GPU, verifica se o modo **MSI (Message Signaled Interrupts)** está ativo no Registro, checa status do **HAGS** e valida o **Smart Access Memory (ReBAR)**. |
| [`data/sample_presentmon_trace.csv`](data/sample_presentmon_trace.csv) | Sample frame-time trace comparing Smart Access Memory (ReBAR) frame-pacing consistency. | Captura de exemplo de tempos de quadro (`ms`) com Smart Access Memory ativo. |

---

## Quick Start / Como Executar

### 1. Analyze Frame-Time Consistency, 1% / 0.1% Lows & Micro-Stutter (Python)
```bash
python src/frametime_stutter_analyzer.py --log data/sample_presentmon_trace.csv
```

### 2. Audit GPU PCIe Bus, MSI Interrupt Mode & Resizable BAR in Windows (PowerShell)
```powershell
.\scripts\Test-PCIeAndReBarTopology.ps1
```
