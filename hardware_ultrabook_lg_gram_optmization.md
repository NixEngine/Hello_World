# Intel Tiger Lake i7-1165G7: complete mathematical and compute reference

The Intel Core i7-1165G7 (Tiger Lake, Willow Cove microarchitecture) is one of the most ISA-rich mobile processors ever shipped, supporting **20 AVX-512 subsets** — more than any prior Intel client CPU — alongside hardware-accelerated cryptography, neural network inference, and a 96-EU Xe-LP integrated GPU capable of **~2 TFLOPS FP32**. This document catalogs every instruction set extension, mathematical operation, optimization framework, and compute capability available in the LG Gram configuration with 16 GB LPDDR4x and Intel Iris Xe Graphics.

The i7-1165G7's mathematical capabilities span three compute domains: a 4-core/8-thread Willow Cove CPU with 512-bit SIMD, an Xe-LP GPU with 768 FP32 ALUs, and a dedicated GNA 2.0 ultra-low-power neural accelerator. Combined with **~68 GB/s** memory bandwidth from quad-channel LPDDR4x-4267 and Intel's oneAPI ecosystem, this platform offers a surprisingly deep compute stack for a 15–28 W ultrabook.

---

## Processor instruction set extensions: the complete catalog

### SSE through AVX2

The i7-1165G7 supports every generation of x86 SIMD from the original SSE through AVX2. Each generation expanded the width and richness of parallel mathematical operations:

**SSE (128-bit FP32 SIMD):** `ADDPS`, `MULPS`, `DIVPS`, `SQRTPS`, `RCPPS`, `RSQRTPS`, `MAXPS`, `MINPS`. **SSE2** extended this to **128-bit FP64 and integer SIMD**: `ADDPD`, `MULPD`, `PADDD`, `PMULLW`, `PMULUDQ`. **SSE3** added horizontal operations (`HADDPS`, `HADDPD`, `ADDSUBPS`) for complex arithmetic. **SSSE3** introduced the critical `PSHUFB` byte shuffle plus packed horizontal add/multiply-accumulate (`PMADDUBSW`, `PMULHRSW`). **SSE4.1** brought dot products (`DPPS`, `DPPD`), rounding (`ROUNDPS/PD`), 32-bit integer multiply (`PMULLD`), and blend instructions. **SSE4.2** added string comparison instructions (`PCMPESTRI/M`, `PCMPISTRI/M`), hardware CRC32, and `POPCNT`.

**AVX (256-bit FP SIMD)** doubled vector width with three-operand VEX encoding: `VADDPS/PD`, `VMULPS/PD`, `VDIVPS/PD`, `VBROADCASTSS/SD`, `VPERM2F128`, `VMASKMOVPS/PD`. **AVX2 (256-bit integer SIMD)** extended 256-bit operation to integers: `VPADDD`, `VPMULLD`, `VPMULUDQ`, `VPMADDWD`, `VPSHUFB`, `VPERMD`, `VPERMQ`, `VPGATHERDD/QD`, variable-shift instructions (`VPSLLVD/Q`, `VPSRAVD`), and broadcast loads (`VPBROADCASTD/W/B`).

### AVX-512: Tiger Lake's 20 supported subsets

Tiger Lake supports the **broadest AVX-512 feature set** of any Intel client processor, including VP2INTERSECT — unique among consumer CPUs. All 20 subsets and their mathematical significance:

| Subset | Key instructions | Mathematical capability |
|---|---|---|
| **AVX-512F** (Foundation) | `VADDPS/PD zmm`, `VMULPS/PD zmm`, `VFMADD231PS/PD zmm` | Core 512-bit FP/integer math; opmask registers k0–k7; merge/zero masking; embedded broadcast |
| **AVX-512CD** (Conflict Detection) | `VPCONFLICTD/Q`, `VPLZCNTD/Q` | Vectorizes histogram and scatter loops with address conflicts; leading-zero count |
| **AVX-512BW** (Byte/Word) | `VPADDW/B zmm`, `VPMULLW zmm`, `VPSHUFB zmm`, `VPCMPB/W` | 8/16-bit integer SIMD at 512-bit width for text, image, and signal processing |
| **AVX-512DQ** (Doubleword/Quadword) | `VPMULLQ`, `VCVTQQ2PS`, `VCVTPS2QQ`, `VFPCLASSPS/PD`, `VREDUCEPS/PD` | 64-bit integer multiply; FP classification; range reduction |
| **AVX-512VL** (Vector Length) | EVEX-encoded 128/256-bit variants | All AVX-512 features (masking, 32 registers) at XMM/YMM widths |
| **AVX-512IFMA** (Integer FMA) | `VPMADD52LUQ`, `VPMADD52HUQ` | **52-bit integer fused multiply-add** for RSA/ECC big-number arithmetic |
| **AVX-512VBMI** | `VPERMB`, `VPERMI2B`, `VPERMT2B`, `VPMULTISHIFTQB` | Byte-granularity permutations for compression, encoding, parsing |
| **AVX-512VBMI2** | `VPCOMPRESSB/W`, `VPEXPANDB/W`, `VPSHLDW/D/Q`, `VPSHRDW/D/Q` | Byte/word compress-expand; concatenate-and-shift (funnel shifts) |
| **AVX-512VNNI** (DL Boost) | `VPDPBUSD`, `VPDPBUSDS`, `VPDPWSSD`, `VPDPWSSDS` | INT8/INT16 multiply-accumulate for neural network inference |
| **AVX-512BITALG** | `VPOPCNTB/W`, `VPSHUFBITQMB` | Byte/word population count; bit shuffle to mask |
| **AVX-512VPOPCNTDQ** | `VPOPCNTD`, `VPOPCNTQ` | 32/64-bit element population count for database analytics |
| **AVX-512VP2INTERSECT** | `VP2INTERSECTD`, `VP2INTERSECTQ` | **Tiger Lake exclusive**: vector-pair intersection into mask pairs for database joins |
| **AVX-512 GFNI** | `VGF2P8AFFINEINVQB`, `VGF2P8AFFINEQB`, `VGF2P8MULB` | Galois Field GF(2^8) arithmetic for cryptographic S-boxes (Camellia, ARIA, SM4) |
| **AVX-512 VAES** | `VAESENC`, `VAESENCLAST`, `VAESDEC`, `VAESDECLAST` on YMM/ZMM | **Vectorized AES**: 2×/4× throughput processing 256/512-bit vectors |
| **AVX-512 VPCLMULQDQ** | `VPCLMULQDQ` on YMM/ZMM | Vectorized carry-less multiplication for AES-GCM GHASH at 256/512-bit width |

**Not supported on Tiger Lake:** AVX-512ER, AVX-512PF (Knights Landing only); AVX-512 4FMAPS, 4VNNIW (Knights Mill only); **AVX-512 BF16** (added in Cooper Lake/Alder Lake); AVX-512 FP16 (Sapphire Rapids).

### FMA3, bit manipulation, and other mathematical extensions

**FMA3 (Fused Multiply-Add)** is arguably the single most important mathematical instruction family. Tiger Lake supports all FMA variants at 128/256/512-bit widths with **4-cycle latency** (reduced from 5 cycles in Skylake): `VFMADD132PS/PD`, `VFMADD213PS/PD`, `VFMADD231PS/PD` (and `SS/SD` scalar forms), plus `VFMSUB*`, `VFNMADD*`, `VFNMSUB*`, `VFMADDSUB*`, `VFMSUBADD*`. A single `VFMADD231PS zmm` performs **32 single-precision FLOPs** (16 multiplies + 16 adds fused) per instruction.

**BMI1:** `ANDN`, `BEXTR`, `BLSI`, `BLSMSK`, `BLSR`, `TZCNT`. **BMI2:** `BZHI`, `MULX` (flag-free unsigned multiply), `PDEP`, `PEXT` (parallel bit deposit/extract), `RORX`, `SARX`, `SHLX`, `SHRX`. **ADX:** `ADCX`, `ADOX` — two independent carry chains for multi-precision arithmetic (critical for big-integer crypto). **F16C:** `VCVTPH2PS`, `VCVTPS2PH` — half-precision ↔ single-precision conversion (no FP16 compute). Additional: `MOVBE` (big-endian byte-swap), `POPCNT` (1-cycle latency), `LZCNT`, `TZCNT`, `RDRAND`, `RDSEED`, **CET** (Control-flow Enforcement — new in Tiger Lake), `WAITPKG` (`UMONITOR`, `UMWAIT`, `TPAUSE`), `MOVDIRI`/`MOVDIR64B`, `CLFLUSHOPT`/`CLWB`, `PKU`.

---

## Willow Cove microarchitecture and execution engine

### Front-end and back-end pipeline

The Willow Cove core is architecturally identical to Sunny Cove (Ice Lake) in its execution engine, with significant cache hierarchy improvements and 10nm SuperFin process refinements. The front-end features **5-wide decode** (1 complex + 4 simple decoders), a **~2,304-entry µOP cache**, and delivers up to **6 fused µOPs/cycle** to the allocator. The **reorder buffer holds 352 entries** (57% larger than Skylake's 224), with a **160-entry unified scheduler** and **128-entry load buffer / 72-entry store buffer**.

Execution uses **10 ports** — a major expansion over Skylake's 8:

| Port | Function |
|---|---|
| **Port 0** | INT ALU, Vec ALU, Vec Shift, 256-bit FMA/MUL, FP/Int DIV, Branch |
| **Port 1** | INT ALU, Vec ALU, Vec Shuffle, 256-bit FMA/MUL, Slow INT (IMUL) |
| **Port 5** | INT ALU, Vec ALU, Vec Shuffle, 256-bit FMA/MUL |
| **Port 6** | INT ALU, Branch |
| **Ports 2, 3** | Load AGU |
| **Ports 4, 9** | Store Data |
| **Ports 7, 8** | Store AGU |

For **AVX-512**, Ports 0 and 1 fuse their 256-bit FMA units to form a single 512-bit execution path. This means Tiger Lake client has **one 512-bit FMA per clock** (vs. two on server Xeons), but **two 256-bit FMAs per clock** when running AVX2.

### Throughput and latency for key mathematical operations

| Instruction | Latency (cycles) | Throughput (CPI) | Port(s) |
|---|---|---|---|
| Integer ADD/SUB (r,r) | 1 | 0.25 (4/clock) | P0/1/5/6 |
| Integer IMUL (r64,r64) | 3 | 1.0 | P1 |
| Integer DIV (r64) | 18–42 | variable | P0 |
| `VADDPS/VADDPD` xmm/ymm | 4 | 0.5 (2/clock) | P0/1 |
| `VADDPS/VADDPD` zmm | 4 | 1.0 (1/clock) | P0+1 fused |
| `VMULPS/VMULPD` xmm/ymm | 4 | 0.5 | P0/1 |
| `VFMADD231PS` xmm/ymm | 4 | 0.5 | P0/1 |
| `VFMADD231PS` zmm | 4 | 1.0 | P0+1 fused |
| `VPADDD` xmm/ymm | 1 | 0.33 (3/clock) | P0/1/5 |
| `VDIVPS` ymm (8 SP) | ~11 | ~5 | P0 |
| `VDIVPS` zmm (16 SP) | ~11 | ~10 | P0 |
| `VSQRTPS` ymm | ~12 | ~6 | P0 |
| `VPDPBUSD` zmm (VNNI) | 5 | 1.0 | P0+1 |
| `VAESENC` xmm | 4 | 1.0 | P0 |
| `SHA256RNDS2` xmm | ~6–8 | ~1.0 | General ports |

**Peak theoretical FLOPS** at 4.7 GHz single-core turbo: **150.4 GFLOPS** (SP) / **75.2 GFLOPS** (DP). This is calculated as 2 × FMA256/clock × 8 FP32 × 2 FLOP × 4.7 GHz, or equivalently 1 × FMA512/clock × 16 FP32 × 2 FLOP × 4.7 GHz.

### Cache hierarchy: Willow Cove's breakthrough L2

| Level | Size | Associativity | Latency | Key detail |
|---|---|---|---|---|
| **L1 Instruction** | 32 KiB/core | 8-way | — | 16 bytes/cycle fetch |
| **L1 Data** | **48 KiB/core** | 12-way | **5 cycles** | 50% larger than Skylake; 2 loads + 2 stores/cycle |
| **L2** | **1.25 MiB/core** | 20-way | **~14 cycles** | **2.5× Sunny Cove's 512 KB**; non-inclusive of L1 |
| **L3 (shared)** | **12 MB** | 12-way | **~37–42 cycles** | Non-inclusive of L2; dual ring interconnect |
| **L2 TLB** | 2,048 entries | 16-way | ~30 cycles | Supports 4 KB + 2 MB pages |

The **1.25 MiB L2** is Willow Cove's signature improvement — it delivers only +1 cycle latency over Sunny Cove's 512 KB despite being 2.5× larger, and its non-inclusive design maximizes effective capacity. For mathematical workloads, this means working sets up to **5 MB** (4 cores × 1.25 MB) stay at L2 latency, dramatically improving matrix operations, FFT butterflies, and neural network layer processing.

### Turbo and thermal characteristics for sustained computation

| Parameter | Value |
|---|---|
| Base frequency (cTDP-up) | 2.80 GHz at 28 W |
| Base frequency (cTDP-down) | 1.20 GHz at 12 W |
| Max single-core turbo | **4.70 GHz** |
| Max all-core turbo | **~4.1 GHz** (thermal/power dependent) |
| PL1 (sustained) | OEM-configurable: 15 W or 28 W |
| PL2 (burst) | ~40–64 W for ~28 seconds |
| Tjunction max | 100°C |

A critical finding: **Tiger Lake has no license-based AVX-512 frequency downclocking** unlike Skylake-X. There is no instruction-type frequency offset — all-core turbo (~4.1 GHz) applies regardless of whether running scalar, AVX2, or AVX-512 code. The only constraint is thermal/power: heavy AVX-512 FMA draws more power per instruction, which in a 15–28 W ultrabook envelope causes thermal throttling to **~3.0–3.5 GHz** under sustained AVX-512 load. At 28 W PL1 with adequate cooling, ~4.1 GHz all-core is sustainable for non-AVX workloads.

---

## LPDDR4x memory: bandwidth, channels, and compute implications

### Bandwidth calculations

The i7-1165G7 uses LPDDR4x-4267 in a **quad-channel** configuration (4 × 16-bit channels = 64-bit total data path). Tiger Lake UP3 has two memory controllers, each driving two LPDDR4x channels:

- **Per-channel bandwidth**: 4267 MT/s × 2 bytes = **8.53 GB/s**
- **Total theoretical bandwidth**: 4 channels × 8.53 GB/s = **~34.1 GB/s** (unidirectional) or **~68.3 GB/s** (bidirectional aggregate, as cited by Intel and WikiChip)
- **Real-world usable bandwidth**: 70–85% of theoretical = **~47.8–58.0 GB/s**

The CPU and Iris Xe GPU **share this bandwidth** through a unified memory architecture. Dual-channel operation is critical — benchmarks show **26% higher GPU scores** with dual-channel versus single-channel, and Intel withholds the "Iris Xe" brand from single-channel configurations.

### Memory specifications

LPDDR4x operating voltage is **1.1V core / 0.6V I/O** (the reduced I/O voltage from 1.1V is LPDDR4x's key power improvement, saving ~17% power versus LPDDR4). Typical timings at 4267 MT/s: CL 36–40, tRCD 36–40, tRP 36–40, yielding an absolute CAS latency of **~16.9 ns**. The i7-1165G7 does **not support ECC** with LPDDR4x — ECC is available only on select embedded/industrial Tiger Lake SKUs.

### Impact on memory-bound computation

With **~34–58 GB/s** effective bandwidth shared between CPU and GPU, the arithmetic intensity threshold (FLOP/byte ratio) required to be compute-bound rather than memory-bound is approximately **4.4 FLOPs/byte** at peak CPU throughput. Sparse matrix operations, large FFTs, and memory-streaming workloads will be bandwidth-limited. The 1.25 MiB L2 per core mitigates this significantly for working sets under 5 MB.

---

## Intel Iris Xe Graphics: 96-EU Xe-LP compute engine

### Architecture and raw throughput

The Iris Xe Graphics uses the **Xe-LP (Gen12.1)** architecture arranged as **1 Slice → 6 Dual Subslices (DSS) → 16 EUs per DSS = 96 EUs**. Each EU contains an **8-wide SIMD FP/INT ALU** plus a **2-wide Extended Math unit** (trigonometric, logarithmic, square root, reciprocal square root) running concurrently. Each EU supports **7 hardware threads** simultaneously.

| Metric | Value |
|---|---|
| FP32 performance | **~1.99 TFLOPS** (at 1300 MHz boost) |
| FP16 performance | **~3.99 TFLOPS** (2× FP32 rate) |
| INT8 performance | **~7.99 TOPS** (4× FP32 rate) |
| FP64 | Not natively supported (~1/16 rate, emulated) |
| GPU base / boost clock | 400 / 1,300 MHz |
| Shading units (ALUs) | 768 (96 × 8-wide) |
| Shared Local Memory | **768 KB total** (128 KB × 6 DSS) |

Calculation: 96 EUs × 8 ops/EU × 2 (FMA) × 1.3 GHz = **1.997 TFLOPS FP32**.

### Memory architecture

The "dedicated 128 MB" shown in system info is **not eDRAM or local VRAM** — it is stolen system memory (DVMT Pre-Allocated) reserved at BIOS level. Additional shared memory is dynamically allocated from system RAM, totaling up to ~8–9 GB on a 16 GB system. The GPU accesses the same LPDDR4x pool as the CPU through the ring interconnect, with up to **16 MB of L3 cache** accessible to the GPU. This unified memory architecture enables **zero-copy** data sharing between CPU and GPU compute.

### OpenCL 3.0 capabilities

Iris Xe reports as **OpenCL 3.0 FULL_PROFILE** with 96 compute units, **max work group size of 256**, sub-group sizes of **8, 16, 32**, and **128 KB SLM per DSS**. FP16 is natively supported (`cl_khr_fp16`). Key Intel-specific extensions include `cl_intel_subgroups` (shuffle, block read/write), `cl_intel_subgroups_short/char/long`, `cl_intel_required_subgroup_size`, `cl_intel_accelerator` (hardware motion estimation), plus full `cl_khr_subgroup_*` extensions for non-uniform vote, ballot, arithmetic, shuffle, and clustered reduce.

### Vulkan 1.2+ compute

With latest drivers, Iris Xe supports **Vulkan 1.3** (up to 1.4 on 2025+ drivers). Compute shaders operate with work group sizes up to **256 invocations** and **64 KB shared memory**. Shader float16 and int8 are both supported (`VK_KHR_shader_float16_int8`). The extension list includes over 95 extensions, with notable compute-relevant ones: `VK_KHR_shader_integer_dot_product`, `VK_KHR_buffer_device_address`, `VK_KHR_shader_atomic_int64`, `VK_EXT_shader_atomic_float`, `VK_EXT_subgroup_size_control`, `VK_INTEL_performance_query`. **Not supported:** ray tracing (`VK_KHR_ray_tracing_pipeline`), mesh shaders (`VK_EXT_mesh_shader`).

### DirectX 12 and Shader Model

Iris Xe supports **DirectX Feature Level 12.1** with **Shader Model 6.6** (partial — some SM 6.6 atomics are unsupported). Notable feature support: **Variable Rate Shading Tier 1 & 2** (yes), **Conservative Rasterization Tier 3** (yes), **DirectML** (yes), **Sampler Feedback Tier 0.9** (yes). Not supported: DXR hardware ray tracing, mesh shaders (both require Xe-HPG/Arc).

### oneAPI, SYCL/DPC++, and Level Zero

The GPU is fully programmable through **Intel oneAPI Level Zero 1.0+**, which provides low-latency kernel dispatch, explicit device/host/shared memory management, and zero-copy surface sharing with media pipelines. **SYCL/DPC++** targets the GPU via Level Zero backend with AOT compilation (`-fsycl-targets=intel_gpu_tgllp`). Unified Shared Memory is especially efficient on integrated GPUs — shared allocations are zero-copy since CPU and GPU access the same physical memory. Sub-group sizes of 8, 16, 32 are controllable, and Intel's **ESIMD** (Explicit SIMD) extension provides register-level control for maximum performance.

### Hardware media engine

Tiger Lake's media engine features **2 Multi-Format Codec (MFX) engines** with the first-ever **hardware AV1 decode** in an Intel CPU. Full codec support: H.264/H.265 (8/10/12-bit decode, 8/10-bit encode), VP9 (8/10/12-bit decode, 8/10-bit LP encode), AV1 (8/10-bit decode only), MPEG-2, VC-1, JPEG (up to 16K×16K). The fixed-function hardware performs **DCT/iDCT**, motion estimation, deblocking, CABAC/CAVLC entropy coding, and SAO filtering — all mathematical transforms that would otherwise require significant CPU/GPU compute.

---

## Cryptographic hardware acceleration

### AES-NI and VAES: vectorized block cipher acceleration

Tiger Lake's AES implementation is a generational leap thanks to **VAES** (AVX-512 VAES). Standard AES-NI provides `AESENC`, `AESENCLAST`, `AESDEC`, `AESDECLAST`, `AESIMC`, `AESKEYGENASSIST` operating on 128-bit XMM registers. VAES extends these to **256-bit (YMM) and 512-bit (ZMM)** — processing 2 or 4 independent AES blocks per instruction. Each `VAESENC` has **4-cycle latency, 1-cycle throughput**.

Performance at 4.7 GHz single-core turbo:

- **AES-128 CTR/ECB** (parallelizable): ~0.16–0.3 cycles/byte → **~15–30 GB/s**
- **AES-256 CTR/ECB**: ~10–20 GB/s (14 rounds vs. 10)
- **AES-CBC encrypt** (serial): ~1.3–1.5 cycles/byte → **~3–3.6 GB/s**
- **AES-256-GCM**: ~2.3–2.6 GB/s (VAES + VPCLMULQDQ combined)
- **AES-XTS** (disk encryption): ~5–10 GB/s estimated — sufficient to saturate NVMe SSDs

Tiger Lake's AVX-512 VAES produces results called "literally absurd" by AnandTech: the i7-1185G7 scored **2.2× higher** than an i9-10900K in GeekBench 5 AES tests, and delivers **~40% more AES-256 throughput** than competing Ryzen laptops.

### SHA-NI: functional but not hardware-accelerated

An important nuance: while Tiger Lake **sets the sha_ni CPUID flag** and supports all SHA instructions (`SHA256RNDS2`, `SHA256MSG1`, `SHA256MSG2`, `SHA1RNDS4`, `SHA1NEXTE`, `SHA1MSG1`, `SHA1MSG2`), **Willow Cove has no dedicated SHA hardware accelerator** (unlike AMD Zen 2+ or Intel's own Tremont Atom core). SHA instructions execute on general-purpose SIMD ports.

Despite this, SHA-NI still provides significant speedup over software. `SHA256RNDS2` processes **2 SHA-256 rounds per instruction**. Measured performance:

- **SHA-256 with SHA-NI**: ~2.06 cycles/byte → **~2.28 GB/s** at 4.7 GHz
- **SHA-256 software-only**: ~8.54 cycles/byte → ~0.55 GB/s
- **Speedup**: ~4.15× from SHA-NI instructions
- **SHA-512**: no hardware support on any x86 processor; software-only

Intrinsics: `_mm_sha256rnds2_epu32()`, `_mm_sha256msg1_epu32()`, `_mm_sha256msg2_epu32()`, `_mm_sha1rnds4_epu32()`, `_mm_sha1nexte_epu32()`, `_mm_sha1msg1_epu32()`, `_mm_sha1msg2_epu32()`.

### PCLMULQDQ and VPCLMULQDQ: Galois Field multiplication

`PCLMULQDQ` performs **carry-less (polynomial) multiplication in GF(2^n)** — multiplying two 64-bit values to produce a 128-bit product without carry propagation. Tiger Lake extends this to 256-bit and 512-bit with `VPCLMULQDQ`, processing 2× or 4× the data per instruction. Latency ~5–7 cycles, throughput ~1 cycle on Willow Cove.

Primary uses: **GHASH computation** in AES-GCM (the authentication tag uses GF(2^128) multiplication), **CRC computation** (CRC-32C and variants), and general polynomial arithmetic. Combined with VAES at 512-bit width, this enables AES-GCM at unprecedented throughput for a mobile processor.

Intrinsics: `_mm_clmulepi64_si128()` (128-bit), `_mm256_clmulepi64_epi64()` (256-bit), `_mm512_clmulepi64_epi64()` (512-bit).

### RDRAND and RDSEED: hardware entropy

Tiger Lake's Digital Random Number Generator (DRNG) is a 3-stage pipeline: a thermal-noise **entropy source** (~3 Gbps), an **AES-128 CBC-MAC conditioner**, and two output paths — a NIST SP 800-90A CTR_DRBG for `RDRAND` and a direct conditioned output for `RDSEED`. Both support 16/32/64-bit output variants.

- **RDRAND throughput**: ~6.4 Gbit/s (shared across all cores), ~460 cycle latency per invocation
- **RDSEED throughput**: limited to ~3 Gbps entropy source rate; can fail if called faster than entropy generation
- **Compliance**: NIST SP 800-90A (DRBG), SP 800-90B (entropy source), SP 800-90C (construction), FIPS 140-2/140-3 certifiable

Note: The CrossTalk vulnerability (CVE-2020-0543) mitigation serializes cross-core RDRAND/RDSEED, impacting multi-threaded throughput.

---

## Neural network and AI acceleration across three engines

### AVX-512 VNNI (DL Boost): INT8 inference on CPU

Tiger Lake's VNNI provides four key instructions for neural network inference:

- **`VPDPBUSD`**: Multiplies unsigned bytes × signed bytes, accumulates into 32-bit integers — 64 INT8 MACs per 512-bit instruction
- **`VPDPBUSDS`**: Saturating variant
- **`VPDPWSSD`**: Multiplies signed 16-bit pairs, accumulates into 32-bit
- **`VPDPWSSDS`**: Saturating variant

`VPDPBUSD` replaces a **3-instruction sequence** (`VPMADDUBSW` + `VPMADDWD` + `VPADDD`) with a single instruction, yielding **~3× theoretical INT8 inference improvement**. With execution on both eligible ports, peak throughput reaches **~128 INT8 MACs per cycle** at 512-bit width, or approximately **~600 GOPS INT8** at 4.7 GHz single-core. Real-world improvement: **2–4× INT8 inference throughput** versus non-VNNI AVX-512 (benchmarked with ResNet-50, MXNet, TensorFlow). Tiger Lake supports VNNI only in **EVEX (AVX-512) encoding** — the VEX-encoded AVX-VNNI variant was introduced later with Alder Lake.

### GNA 2.0: ultra-low-power neural accelerator

Tiger Lake's on-die **Gaussian & Neural Accelerator 2.0** operates at **38 GOPS consuming just ~38 mW** (~1 GOPS/mW). It targets always-on workloads: speech recognition, wake-word detection, noise cancellation, and acoustic context. GNA 2.0 supports affine/fully-connected layers, GMM layers, 1D convolutions, and RNN/LSTM layers using INT8/INT16 precision. It is **not suitable** for computer vision, large transformer models, or 2D convolutions.

Programming is done through **OpenVINO's GNA plugin**, which accepts models from TensorFlow, ONNX, Caffe, and Kaldi. GNA operates while CPU cores sleep, making it ideal for battery-powered always-listening applications. Note: GNA is being **discontinued** after Meteor Lake; the successor is Intel's NPU.

### Iris Xe GPU: DP4a INT8 inference

The GPU provides an additional **~8 TOPS INT8** via DP4a instructions on the 96 EUs at FP16's 2× rate. Combined with CPU via OpenVINO's MULTI plugin (`MULTI:CPU,GPU`), Tiger Lake achieves approximately **~4× Coffee Lake inference throughput** for combined execution.

---

## Optimization frameworks and libraries

### Intel oneAPI ecosystem

**oneMKL** provides AVX-512-optimized BLAS Level 1/2/3, LAPACK, FFT (1D/2D/3D, arbitrary length, mixed radix), sparse matrix operations (SpMV, SpMM in CSR/CSC/COO), Vector Math Library (`vdExp`, `vsSin`, `vdLog`), and random number generators (MT19937, Sobol, Philox4x32-10). Supports both CPU (AVX-512 FMA) and GPU (Iris Xe via Level Zero/SYCL) backends.

**oneDNN** (Deep Neural Network Library) provides JIT-compiled kernels tuned for Tiger Lake's microarchitecture: convolution (direct, Winograd, FFT-based), inner product, pooling, RNN/LSTM/GRU, batch normalization, and post-op fusion chains. Uses AVX-512 VNNI for INT8 inference on CPU and hardware-accelerated INT8 on Iris Xe GPU via Level Zero.

**IPP** offers optimized signal processing (FFT, FIR/IIR filtering, Hilbert), image processing (convolution, morphology, geometric transforms, up to 512 MP), data compression (LZO, LZ4, ZLIB), and cryptographic functions. Runtime platform-aware dispatch automatically selects AVX-512 code paths on Tiger Lake.

**oneTBB** provides the parallel runtime (`parallel_for`, `parallel_reduce`, `parallel_scan`, flow graph), scalable memory allocator (avoiding `malloc` serial bottleneck), and concurrent containers. It powers oneMKL, oneDNN, and oneDAL internally, efficiently distributing work across 4 cores / 8 threads with work-stealing scheduling.

**oneDAL** accelerates scikit-learn via `scikit-learn-intelex` with drop-in patching: up to **100× faster training** for SVM, k-NN, PCA, Random Forest, and XGBoost, leveraging AVX-512 and oneMKL BLAS. Data blocking is optimized for Willow Cove's 1.25 MB L2.

### Compiler optimization flags

The canonical Tiger Lake compilation target:

- **GCC/Clang**: `-march=tigerlake -mtune=tigerlake -O3`
- **Intel ICX**: `-march=tigerlake -qopt-zmm-usage=high`

`-march=tigerlake` enables **all 20 AVX-512 subsets** plus every other ISA extension. Individual AVX-512 flags (`-mavx512f`, `-mavx512vnni`, `-mavx512ifma`, `-mavx512vbmi`, `-mavx512vbmi2`, `-mavx512bitalg`, `-mavx512vpopcntdq`, `-mavx512vp2intersect`, etc.) can be toggled independently. Profile-guided optimization (`-fprofile-generate` / `-fprofile-use`) typically yields **10–20% improvement** for branch-heavy code. Link-time optimization (`-flto` for GCC, `-ipo` for ICX) enables whole-program analysis.

### Intel intrinsics headers and key families

All intrinsics are accessible through `<immintrin.h>`. Key families: `_mm_*` (128-bit SSE), `_mm256_*` (256-bit AVX/AVX2), `_mm512_*` (512-bit AVX-512). Critical mathematical intrinsics for Tiger Lake include `_mm512_fmadd_ps()` (16-wide FP32 FMA), `_mm512_dpbusd_epi32()` (VNNI INT8 dot product), `_mm512_mask_add_ps()` (masked FP32 add), and `_mm512_permutexvar_epi32()` (variable permute).

### OpenVINO inference optimization

OpenVINO leverages Tiger Lake's full compute stack: AVX-512 VNNI for INT8 CPU inference, Iris Xe via oneDNN/Level Zero for GPU inference, and GNA 2.0 for ultra-low-power always-on models. The `AUTO:` plugin automatically selects the best device, while `MULTI:CPU,GPU` distributes inference across both. INT8 quantization via Post-Training Optimization Tool (POT) and Neural Network Compression Framework (NNCF) maximizes throughput on both CPU and GPU.

### MediaSDK and oneVPL

**oneVPL** (oneAPI Video Processing Library) is the successor to MediaSDK, with Tiger Lake being the first natively supported generation. It provides hardware-accelerated decode, encode, and video processing with **zero-copy surface sharing** between media operations and SYCL compute kernels via Level Zero USM. This enables pipelines like decode → GPU compute → encode without memory copies, using the same physical memory throughout.

---

## Conclusion

The i7-1165G7 in this LG Gram represents a uniquely compute-dense mobile platform. Three findings stand out. First, Tiger Lake's **20 AVX-512 subsets** — including the exclusive VP2INTERSECT, VAES, and VPCLMULQDQ — create a cryptographic and mathematical SIMD capability unmatched by any other mobile processor in its generation, with AES-GCM throughput exceeding 2 GB/s per core. Second, the **absence of license-based AVX-512 frequency throttling** (unlike Skylake-X) means this platform can sustain 512-bit workloads at full turbo, limited only by the 15–28 W thermal envelope. Third, the **three-engine AI compute stack** (AVX-512 VNNI on CPU at ~600 GOPS, Iris Xe GPU at ~8 TOPS, GNA 2.0 at 38 GOPS/38 mW) offers heterogeneous inference capabilities that OpenVINO can orchestrate simultaneously. The 1.25 MiB L2 per core — Willow Cove's quiet revolution — keeps moderate working sets at 14-cycle latency, making this configuration surprisingly capable for mathematical workloads that respect the memory hierarchy.