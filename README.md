# PCIe 4.0, AMD Smart Access Memory (ReBAR) & Frame-Time Micro-Stutter Profiler

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![AMD Radeon](https://img.shields.io/badge/RDNA_2-RX_6750_XT_12GB-ED1C24?style=for-the-badge&logo=amd&logoColor=white)

> **English:** Low-level GPU/PCIe subsystem diagnostics and frame-time consistency profiler designed for the **AMD Ryzen 7 5700X + Radeon RX 6750 XT 12GB (PCIe 4.0 x16 + Smart Access Memory)** platform. Audits **Resizable BAR (`Large Memory Range`)**, **MSI (Message Signaled Interrupts)** mode, and **HAGS**, and processes PresentMon/CapFrameX logs to compute **1% Low / 0.1% Low FPS**, **99th percentile frame times (`ms`)**, and **frame-to-frame micro-stutter variance**.
>
> **Português:** Ferramenta de diagnóstico de barramento GPU/PCIe e análise de consistência de *frame-time* projetada para a plataforma **AMD Ryzen 7 5700X + Radeon RX 6750 XT 12GB (PCIe 4.0 x16 + Smart Access Memory)**. Audita alocação de **Resizable BAR (`Large Memory Range`)**, interrupções **MSI (Message Signaled Interrupts)** e **HAGS**, e processa logs do PresentMon/CapFrameX para calcular **1% Low / 0.1% Low FPS**, **percentil 99 de frame-time (`ms`)** e **micro-stuttering**.

---

## Included Tools / Ferramentas Inclusas

| File | Description (EN) | Descrição (PT-BR) |
| :--- | :--- | :--- |
| [`src/frametime_stutter_analyzer.py`](src/frametime_stutter_analyzer.py) | Parses PresentMon / CapFrameX CSV frame traces (`msBetweenPresents`, `msGPUActive`, `msCPUWait`) to compute Average FPS, **1% Low / 0.1% Low FPS**, frame-to-frame pacing jitter (`ms`), and CPU vs. GPU bottleneck ratios. | Analisa logs CSV de captura de quadros (PresentMon / CapFrameX) para calcular Média de FPS, **1% Low / 0.1% Low FPS**, jitter entre quadros consecutivos (`ms`) e percentual de gargalo de CPU vs. GPU. |
| [`scripts/Test-PCIeAndReBarTopology.ps1`](scripts/Test-PCIeAndReBarTopology.ps1) | PowerShell hardware auditor that inspects the GPU PCIe bus, verifies **Message Signaled Interrupts (MSI)** in the Windows Registry, checks **Hardware-Accelerated GPU Scheduling (HAGS)**, and confirms **Smart Access Memory / Resizable BAR** status. | Auditor em PowerShell que inspeciona o barramento PCIe da GPU, verifica se o modo **MSI (Message Signaled Interrupts)** está ativo no Registro, checa status do **HAGS** e valida o **Smart Access Memory (ReBAR)**. |
| [`data/sample_presentmon_rx6750xt.csv`](data/sample_presentmon_rx6750xt.csv) | Sample frame-time trace comparing Smart Access Memory (ReBAR) + DDR4-3200 CL16 performance on the RX 6750 XT 12GB. | Captura de exemplo de tempos de quadro (`ms`) na RX 6750 XT 12GB com Smart Access Memory e DDR4-3200 CL16. |

---

## Quick Start / Como Executar

### 1. Analyze Frame-Time Consistency, 1% / 0.1% Lows & Micro-Stutter (Python)
```bash
python src/frametime_stutter_analyzer.py --log data/sample_presentmon_rx6750xt.csv
```

### 2. Audit GPU PCIe Bus, MSI Interrupt Mode & Resizable BAR in Windows (PowerShell)
```powershell
.\scripts\Test-PCIeAndReBarTopology.ps1
```
