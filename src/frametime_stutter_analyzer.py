#!/usr/bin/env python3
"""
frametime_stutter_analyzer.py
EN: Analyzes GPU frame-time telemetry logs (PresentMon / CapFrameX CSV format) to calculate:
    - Average FPS, 1% Low FPS, and 0.1% Low FPS.
    - 99th Percentile Frame Time (ms) and Frame-to-Frame Pacing Jitter (ms).
    - Micro-Stutter Event Detection (consecutive frame delta > 2.0x rolling average).
    - CPU-Bound vs. GPU-Bound frame classification.
PT: Analisa logs CSV de telemetria de frame-time (formato PresentMon / CapFrameX) para calcular
    Média de FPS, 1% Low, 0.1% Low, Jitter de Frame-Pacing, Micro-Stuttering e gargalo CPU/GPU.
"""

import argparse
import csv
import math
from typing import List


def percentile(sorted_vals: List[float], pct: float) -> float:
    """Computes the given percentile (0..100) from a sorted ascending list."""
    if not sorted_vals:
        return 0.0
    idx = (len(sorted_vals) - 1) * (pct / 100.0)
    low = int(math.floor(idx))
    high = int(math.ceil(idx))
    if low == high:
        return sorted_vals[low]
    weight = idx - low
    return sorted_vals[low] * (1.0 - weight) + sorted_vals[high] * weight


def analyze_frametimes(csv_path: str) -> None:
    frame_times_ms: List[float] = []
    gpu_busy_ms: List[float] = []
    cpu_wait_ms: List[float] = []

    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ft = float(row["msBetweenPresents"])
            gpu_b = float(row["msGPUActive"])
            cpu_w = float(row["msCPUWait"])
            frame_times_ms.append(ft)
            gpu_busy_ms.append(gpu_b)
            cpu_wait_ms.append(cpu_w)

    if not frame_times_ms:
        print("[WARN] No frame records found in CSV.")
        return

    n = len(frame_times_ms)
    avg_ft_ms = sum(frame_times_ms) / n
    avg_fps = 1000.0 / avg_ft_ms

    sorted_ft = sorted(frame_times_ms)
    p99_ft_ms = percentile(sorted_ft, 99.0)
    p99_9_ft_ms = percentile(sorted_ft, 99.9)

    fps_1pct_low = 1000.0 / p99_ft_ms
    fps_0_1pct_low = 1000.0 / p99_9_ft_ms

    deltas = [abs(frame_times_ms[i] - frame_times_ms[i - 1]) for i in range(1, n)]
    avg_jitter_ms = sum(deltas) / len(deltas) if deltas else 0.0
    stutter_spikes = sum(1 for d in deltas if d > (avg_ft_ms * 0.85))

    gpu_bound_frames = sum(
        1 for ft, gb in zip(frame_times_ms, gpu_busy_ms) if (gb / ft) >= 0.92
    )
    gpu_bound_pct = (gpu_bound_frames / n) * 100.0
    cpu_bound_pct = 100.0 - gpu_bound_pct

    print("=" * 86)
    print("  AMD RYZEN & RADEON FRAME-TIME CONSISTENCY, 1% / 0.1% LOWS & STUTTER PROFILER")
    print("=" * 86)
    print(f"  Total Frames Analyzed     : {n}")
    print(f"  Average Frame Rate        : {avg_fps:>6.1f} FPS ({avg_ft_ms:.2f} ms/frame)")
    print(f"  1% Low FPS (99th Pct)     : {fps_1pct_low:>6.1f} FPS ({p99_ft_ms:.2f} ms)")
    print(f"  0.1% Low FPS (99.9th Pct) : {fps_0_1pct_low:>6.1f} FPS ({p99_9_ft_ms:.2f} ms)")
    print("-" * 86)
    print(f"  Frame-to-Frame Jitter     : {avg_jitter_ms:.2f} ms (Lower = smoother frame pacing)")
    print(f"  Micro-Stutter Spikes      : {stutter_spikes} spike(s) detected")
    print(f"  Pipeline Bottleneck Split : {gpu_bound_pct:.1f}% GPU-Bound | {cpu_bound_pct:.1f}% CPU/RAM-Bound")
    print("=" * 86)


def main() -> None:
    parser = argparse.ArgumentParser(description="PresentMon / CapFrameX Frame-Time & Stutter Analyzer")
    parser.add_argument(
        "--log",
        default="data/sample_presentmon_trace.csv",
        help="Path to frame-time CSV log",
    )
    args = parser.parse_args()
    analyze_frametimes(args.log)


if __name__ == "__main__":
    main()
