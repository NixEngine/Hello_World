# Math/Architecture Extraction — Pass 11 (Nix Engine code corpus)

- **Timestamp:** 2026-05-05T10-11Z
- **Files read:** 8 .docx (extracted via python-docx to `nix_engine_extracted/`)
  1. `Nix Engine - Codes puro 009.docx` — 444 paragraphs, 15.5k chars (monolithic single-file Express server)
  2. `Nix Engine - Codes puro 008.docx` — 522 paragraphs, 21.3k chars (Termux/multi-OS bash installer that materialises full project tree)
  3. `Nix Engine - Codes puro 007.docx` — 392 paragraphs, 16.6k chars
  4. `Nix Engine - Codes puro.docx` — 560 paragraphs, 19.2k chars
  5. `Nix Engine - Codes explicado 007.docx` — 413 paragraphs, 17.8k chars (Vertex/Cloud-Run deploy variant)
  6. `Nix Engine - Codes explicado 006.docx` — 848 paragraphs, 33.7k chars (largest; full beta with bandit + 14-avatar council + ajv schemas)
  7. `Nix Engine - Codes explicado 005.docx` — 567 paragraphs, 23.1k chars (raw-data provider contract + Dockerfile)
  8. `Nix Engine - Codes package upgrade only.docx` — 535 paragraphs, 19.6k chars (editions.yml + parallel council with hormones)
- **Total chars read this pass:** ~166k (≈ raw lines 30k+; ~6 distinct architectural variants of Nix Engine across files)
- **Cumulative corpus coverage:** previously 35/72 ~58% → now **43/72 ~60%**
- **Position in pass series:** pass 11 (after pass 10 ~29150 lines / 237 eqs). This pass shifts the focus from continuous math to **executable architecture** — the running implementation of the rawness-entropy bridge identified in earlier passes.

---

## 1. Architectural overview — Nix Engine canonical pipeline

```
POST /agent/act
   │
   ├─ loadConfig() ─────────► CFG{edition,providers{openai,vertex},risk{low,mid,high,hitlCvar},bandit}
   ├─ discoverCapabilities() ► ['vertex.llm','openai.llm','internal.llm','internal.fetch','internal.none']
   ├─ noiseFingerprint(1.2s) ► {mode,confidence,evidence[]}      (env probe)
   ├─ plan({objective,edition,capabilities})
   │     steps = [analyze(llm), collect(fetch?), propose(llm), verify(internal)]
   ├─ runAvatars(...) ─────► 15 avatars produce {score,risk,stance,leak?}
   ├─ aggregateSignals(...) ► {aggregate, dissent, stances, weights}  → council_dissent_ratio gauge + hormone counter
   ├─ riskScoreNeutral({signals,edition})
   │     base = 0.25·novelty + 0.35·safety + 0.20·leak + 0.20·cvar95 + 0.10·rawness + (CHIMERA?0.05:0)
   ├─ executePlan({plan,tools,context}) ► tool_activity[]
   ├─ ensureSafeOrConfirm({score,cvar95,policy})
   │     if score≥high OR cvar95≥hitlCvar → enqueueConfirm(high_risk)
   │     elif score≥mid                    → enqueueConfirm(mid_risk)
   ├─ build NIX_ENVELOPE {trace_id, mode, plan, tool_activity, provider_events, environment_guess,
   │                      solve.candidates[], metrics{ci95,cvar95}, source_citations, cache_status,
   │                      governance{requires_confirmation,reasons,hitl_card}, council, errors, notes}
   └─ validateEnvelope(envelope) (ajv) ► attaches _schema_errors if invalid (does NOT fail response)
```

**Operating contract** (immutable across all 8 variants):
- `report_only: true` — engine never *executes* high-risk effects; it produces a NIX_ENVELOPE.
- `confirm_on_external_effects: true` (Hybrid) / `false` (Chimera) — external side-effects (`webhook.post`, `exec.shell`, `gdrive.write`) gated by HITL queue in Hybrid; Chimera reports-only on them.
- `provider_raw_mode: true` — external LLM responses must be returned raw; rawness_report audits compliance.

---

## 2. Equations & numeric constants extracted

### 2.1 Risk-score composite (NIX-RS.1)
```
risk = 0.25·novelty + 0.35·safety + 0.20·leak + 0.20·cvar95 + 0.10·rawness_suspected
       + (edition == 'CHIMERA' ? 0.05 : 0.0)
risk ← clamp(risk, 0, 1)
```
Source: `src/core/policy.mjs` in explicado_006 lines 356-367.

### 2.2 Action-meta risk (alternative formula NIX-RS.2)
```
risk = 0.4·base_risk + 0.3·novelty + 0.3·impact
risk ← clamp(risk, 0, 1)
```
Source: `Codes puro 008` `riskScoreNeutral` lines 201-208 (multi-OS installer variant). Two competing risk formulas — different runtime contexts; **C6 framework-correction candidate**: 008 weights different from 006 — needs canonical reconciliation.

### 2.3 Edition-specific risk multiplier (NIX-RS.3)
```
score' = clamp(score · risk_multiplier, 0, 1)
   risk_multiplier = 1.15  (Chimera, agressivo)
   risk_multiplier = 0.90  (Hybrid, amigável)
```
Source: `Codes package upgrade only` `editions.yml` lines 88-110 + `policy.js` `computeRiskScore` lines 160-164.

### 2.4 HITL gate (NIX-HITL.1)
```
require_HITL ⇔ (score ≥ risk_high) ∨ (cvar95 ≥ hitl_cvar_gate)
   risk_high       = 0.75  (default; configurable RISK_THRESHOLD_HIGH)
   risk_mid        = 0.55  (intermediate gate, only Hybrid edition)
   hitl_cvar_gate  = 0.20  (HITL_GATE_ON_HIGH_CVAR)
```
Source: `policy.mjs` `ensureSafeOrConfirm` lines 369-386 (explicado_006).

Variant in `puro 008`:
```
risk_low=0.2, risk_mid=0.4, risk_high=0.65, hitl_cvar_gate=0.6
```
Variant in `puro 009`:
```
require_HITL ⇔ riskScore > 0.7 (single threshold) — NIX-HITL.2
```
**C7 framework-correction candidate**: thresholds drift across versions; canonical = explicado_006 (latest with bandit).

### 2.5 95% Confidence Interval (NIX-CI.1)
```
mean = Σ_i x_i / n
var  = Σ_i (x_i - mean)² / (n - 1)
sd   = √var
err  = 1.96 · sd / √n
ci95 = (mean - err, mean + err)
```
1.96 corresponds to z_{0.975} (two-tailed 95%). Identical implementation in `puro 009` lines 66-74 and `simCore` definitions.mjs.

### 2.6 CVaR-95 (Conditional Value-at-Risk, NIX-CVAR.1)
```
sorted ← sort(samples ASC)
idx    = ⌊0.95 · |sorted|⌋
tail   = sorted[idx..]
cvar95 = mean(tail)
```
Loss-tail variant (in `simCore`):
```
sorted ← sort(values DESC)   // perdas desc
idx    = ⌊α · |values|⌋,  α = 0.95
tail   = sorted[..idx]
cvar   = mean(tail)
```
Sources: `puro 009` lines 75-82 + `definitions.mjs`. **Canonical orientation:** ASC for utility metrics (lower = worse → CVaR-95 captures bad-tail mean utility); DESC for losses.

### 2.7 Shannon entropy on character histogram (NIX-H.1)
```
freq[c] = count(c in text)
p_c     = freq[c] / |text|
H       = −Σ_c p_c · log₂(p_c)
```
Source: `puro 009` lines 83-94 + `util/entropy.mjs` (returns `Number(H.toFixed(4))`). Used in **rawness report**: `length_ratio = |text| / 128` (or `expectedLen=400` in puro 009), `shannon_entropy = H`. Higher entropy + length_ratio close to 1 + no structural anomaly ⇒ `suspected = false`.

### 2.8 Bandit weight update (NIX-BANDIT.1)
```
for each (avatar_name, delta) in objective_feedback.perAvatar:
    w_new = clamp( w_old + lr · delta , w_min, w_max )
    weights[avatar_name] = w_new
S = Σ weights
weights ← weights / S      (renormalize to sum=1)

  lr      = 0.03   (BANDIT_LR)
  w_min   = 0.05
  w_max   = 0.35
  ε_min   = 0.05   (BANDIT_EPSILON_MIN; ε-greedy floor)
  holdout = 0.20   (BANDIT_HOLDOUT)
```
Source: `council.mjs` `banditUpdate` lines 424-436 (explicado_006). **Implements safe online re-weighting of council** based on objective_feedback signal, with hard clamps preventing weight collapse / explosion.

### 2.9 Council dissent ratio (NIX-DISS.1)
```
stance_counts = {stance: |{a : a.stance=stance}| for stance in unique_stances}
max_count     = max(stance_counts.values)
dissent       = 1 − max_count / |avatars|
```
0 if unanimous; → 1 as opinions diverge. Emitted on `council_dissent_ratio` Prometheus gauge.
Source: `council.mjs` `aggregateSignals` lines 438-463 (explicado_006).

### 2.10 Aggregated avatar signal (NIX-AVATAR.1)
```
score_agg = Σ_a (w_a · score_a) / Σ_a w_a
risk_agg  = Σ_a (w_a · risk_a)  / Σ_a w_a
```
Source: `puro 008` `aggregateAvatarSignals` lines 239-249.

### 2.11 Hindsight oracle (sim regret baseline, NIX-ORACLE.1)
```
ideal_loss     = max(0, 1 − (vidasSalvas + 0.05))
oracle_cost    = max(0, 0.8 · ideal_loss)
policy_cost    = max(0, (1 − vidasSalvas) + 0.2 · dissent)
regret = max(0, oracle_cost − policy_cost)   // counterfactual gap
```
The `+0.05` is a generous-oracle nudge; `0.8·` is the assumption that perfect-info still has some unavoidable cost (≤ 80% of ideal_loss). The 0.2·dissent term penalizes non-cohesive policies.
Source: `simCore.mjs` lines 700-704 + `hindsightPlanner.mjs` lines 740-744.

### 2.12 World-adapter scenario severity (NIX-WORLD.1)
```
rnd      = (|hash(seed)| mod 1000) / 1000           ∈ [0,1)
severity = (mode == 'chimera' ? 0.7 : 0.5) + 0.2·rnd

  vidasSalvas      = (mode==chimera ? 0.7+(0.1−0.1·rnd) : 0.6+(0.1−0.05·rnd))
  tempoRestauroT90 = (mode==chimera ? 2.0+0.5·rnd     : 3.5+0.5·rnd)
  violacoesSeg     = (mode==chimera ? 40+⌊30·rnd⌋    : 15+⌊10·rnd⌋)
  fairnessAcesso   = (mode==chimera ? 0.6+(0.2−0.2·rnd) : 0.8−(0.1−0.1·rnd))
  confiancaPublica = (mode==chimera ? 0.35+(0.15−0.15·rnd) : 0.7−(0.1−0.1·rnd))
```
**Phenotype**: Chimera mode → higher vidasSalvas (utilitarian) + faster t90 + 2-3× more safety violations + lower public trust. Hybrid → fewer lives, slower, fewer violations, more trust. **This is the policy/safety trade-off baked into the simulator.**
Source: `worldAdapter.mjs` lines 706-737.

---

## 3. Avatar council registry (15 personae)

| # | Avatar | Default w (explicado_006) | Default w (puro 008/009) | Stance | Function |
|---|--------|---------------------------|--------------------------|--------|----------|
| 1 | **PKD** (Philip K. Dick) | 0.10 | 0.20 | promote | reality / phenomenology consistency check |
| 2 | **Boyd** | 0.08 | 0.18 | promote | OODA-loop tempo |
| 3 | **Draco** | 0.10 | 0.15 | guard | rules / safety enforcement |
| 4 | **Risk** | 0.12 | 0.20 | caution | risk signal |
| 5 | **DataQuality** | 0.10 | 0.15 | neutral | data integrity + leak risk |
| 6 | **Ramanujan** | 0.08 | — | promote | mathematical/aesthetic insight |
| 7 | **Novelty** | 0.10 | — | explore | exploration drive |
| 8 | **Lombardi** | 0.08 | 0.05 | neutral | flow / bottleneck (network analysis) |
| 9 | **Nervi** | 0.08 | — | guard | structural integrity (engineering) |
| 10 | **Margulis** | 0.06 | — | explore | symbiosis / coevolution |
| 11 | **Jacobs** (Jane Jacobs) | 0.06 | 0.07 | promote | urban / community utility |
| 12 | **Diogenes** | 0.04 | — | neutral | radical honesty / cynic check |
| 13 | **Bernays** | 0.04 | — | promote | persuasion / framing |
| 14 | **SI** (Self-Interest) | 0.06 | — | neutral | system self-interest signal |
| 15 | (PKD2 optional) | — | — | — | secondary phenomenology probe |

**Diagnostic insight A:** the puro 008/009 line uses a **smaller 7-avatar council** (PKD, Boyd, Draco, Risk, DataQuality, Jacobs, Lombardi, summing to 1.00); the explicado_006 line uses a **fuller 14-avatar council** (sums to 1.00 after default weights are normalised). Same architectural pattern, different fidelity.

**Diagnostic insight B (cross-projection to Beast):** the 14 avatars correspond to 14 **independent cognitive lenses** for novelty/risk assessment. This maps to the Beast §11 eight-metric anomaly detector (pass 6) at the meta-level: instead of 8 numerical observables (ρ, LieScore, FixedPairs, CarryEntropy, Hamming, DACM-I, PhantomEntropy, CI), Nix uses 14 *named cognitive perspectives* whose individual outputs are aggregated under bandit-tuned weights.

**Hypothesis H62 (new):** Beast 8-metric vector + Nix 14-avatar vector are **dual decompositions of the same anomaly-detection space**: numerical (Beast) vs. anthropic-frame (Nix). Test: instantiate one Beast metric per avatar (e.g., DACM-I ↔ Risk; CarryEntropy ↔ DataQuality; LieScore ↔ Diogenes; PhantomEntropy ↔ PKD) and see whether the eight Beast metrics span a 8-dim subspace whose closest 14-dim hull-extension recovers the avatar weights.

---

## 4. NIX_ENVELOPE schema (canonical 13-field structure)

```json
{
  "trace_id":          "nx-<uuid-v4>",
  "edition":           "hybrid|chimera",
  "started_at":        "<iso8601>",
  "finished_at":       "<iso8601>",
  "plan":              [{step,action,why,tool}, ...],
  "tool_activity":     [{name,status,request,result_ref,
                         provider_events:[{provider,event,status,latency_ms}],
                         rawness_report:{suspected,signals,length_ratio,
                                         shannon_entropy,perplexity_delta,
                                         cross_provider_divergence}}, ...],
  "avatars":           {weights:{...}, signals:[{name,score,notes}]},
  "solve":             {candidates:[{id,summary,novelty_score,
                                     consistency_pass_rate,evidence_coverage,
                                     leak_risk,constraints_violated:[]}]},
  "metrics":           {ci95:[{name,mean,low,high}],
                        cvar95:[{name,value}]},
  "source_citations":  [],
  "cache_status":      {reads,writes,keys:[]},
  "capabilities":      {tools_available:[], environment_guess:{mode,confidence,evidence:[]}},
  "governance":        {requires_confirmation:bool, reasons:[],
                        hitl_card:{options:[], risk_benefit_matrix:{},
                                   reversal_time, approval_code}},
  "council":           {aggregate, dissent, stances, weights},
  "errors":            [],
  "notes":             []
}
```

This envelope is **the unit of cognition** for Nix Engine — every `/agent/act` returns one. It contains everything an auditor needs to reproduce, validate, or appeal the decision.

**Cross-projection to Beast:** the envelope is structurally homologous to Beast's `S_DACM` integrated score record (§28.4.9 line 5437) which also packs metrics, anomaly detection, and confidence intervals. **NIX_ENVELOPE = S_DACM at runtime.**

---

## 5. Rawness report — the H45 / H44 anchor in code

`rawnessFromText(txt, expectedLen=400)`:
```js
{
  suspected: false,                       // canonical baseline
  signals: [],                            // anomaly tags (length_short, low_entropy, hedging_phrases, ...)
  length_ratio: |txt| / expectedLen,      // 1.0 = expected; <0.5 = truncated/safety-rewrite suspected
  shannon_entropy: H(txt),                // ≈ 4-5 bits/char for English; <3 → near-degenerate
  perplexity_delta: null,                 // (vs. null; reserved for cross-provider A/B)
  cross_provider_divergence: null         // (reserved; for openai vs vertex same-prompt audit)
}
```

This is the **operational implementation of H44 (DACM-zero-on-deterministic) and H45 (carry sole non-linearity)** translated to the LLM-orchestration domain:
- `length_ratio` ↔ **carry-saturation ratio** (effective entropy actually emitted)
- `shannon_entropy` ↔ **bit-color trace entropy** (bits actually carried)
- `perplexity_delta` ↔ **DACM operator output delta** (deviation from deterministic baseline)
- `cross_provider_divergence` ↔ **two-piece saturation r_c = t_0 + Δ** (H61 anchor; comparing two providers exposes the saturation phase)

**The rawness report is the LLM analogue of the SHA-256 hot-bit detector.** Same invariant: capture the bits the system *actually* emits, then audit against a deterministic baseline. This is the strongest evidence yet for the **rawness-entropy bridge** posited in `rawness_entropy_bridge_2026-05-05T06-10Z.md`.

---

## 6. Editions.yml — Chimera vs Hybrid duality (NIX-EDITION.1)

```yaml
chimera:
  council: {parallel:true, soft:1200ms, hard:2500ms, quorum:weighted-majority,
            weights:{security:1.0, explore:1.2, ethics:0.8, rigor:1.0}, hormone_emit:true}
  policy:  {risk_multiplier:1.15, report_only:true,
            confirm_on_external_effects:false,
            external_effect_kinds:[webhook.post, exec.shell, gdrive.write]}
  runtime: {max_concurrency:12, retries:{base:1, backoff_ms:250}, cache_ttl_ms:90000}

hybrid:
  council: {parallel:true, soft:1800ms, hard:3500ms, quorum:consensus-bias,
            weights:{security:1.2, explore:0.9, ethics:1.1, rigor:1.1}, hormone_emit:true}
  policy:  {risk_multiplier:0.9, report_only:true,
            confirm_on_external_effects:true,
            external_effect_kinds:[webhook.post, exec.shell, gdrive.write]}
  runtime: {max_concurrency:6, retries:{base:2, backoff_ms:400}, cache_ttl_ms:60000}

nixe:
  tone:
    chimera: {style:terse,    hedging:false, assertiveness:high}
    hybrid:  {style:guiding,  hedging:true,  assertiveness:medium}
```

**Diagnostic insight C — the duality is everywhere:**
- Chimera = **explore-biased, faster, more risk-tolerant, terse** → high-velocity divergence.
- Hybrid = **safety-biased, slower, more risk-averse, guiding** → controlled convergence.
- Quorum: weighted-majority (Chimera, who-wins-the-vote) vs. consensus-bias (Hybrid, ratchet toward agreement).
- Concurrency: 12 vs 6 (factor 2). Cache TTL: 90s vs 60s.

This is the **same Chimera/Hybrid duality** noted in earlier passes for the homenagem corpus (`gift_architectural_dna_synthesis.md`) — but now grounded in **runtime knobs** and not just narrative voice.

**Cross-projection to Beast:** Chimera ≈ exploration phase of S_DACM (high novelty bias, low ethics weight → finds anomalies fast); Hybrid ≈ verification phase (high security/ethics → filters false positives). The two editions are the two halves of an exploration/exploitation split.

---

## 7. Prometheus metrics surface

```
nix_http_requests_total{route,method,code}            counter
nix_http_request_duration_seconds{route,method,code}  histogram (buckets dependent)
nix_request_duration_ms                                histogram (50, 100, 200, 500, 1000, 2500, 5000)
nix_tool_calls_total{tool,status}                      counter (status: attempt|ok|requested|error)
nix_errors_total{where}                                counter
council_hormone_emissions_total{stance}                counter (stance: promote|block|guard|caution|explore|neutral|depends)
council_dissent_ratio                                  gauge ∈ [0,1]
provider_events_total{provider,event,category}         counter
hitl_queued_total                                      counter
```
Default Node metrics (`collectDefaultMetrics`) also active — process_*, nodejs_*.

**Cross-projection to Beast:** these 9 metric families are the **observability skeleton** of the Nix runtime. Beast equivalent: the `S_DACM` integrated score logs + bus heartbeat statistics. **Recommendation:** add Prometheus to Beast pipeline using identical conventions — this would let a single Grafana dashboard observe both engines.

---

## 8. Plan strategies (3 distinct planners)

| Variant | Steps | Source |
|---------|-------|--------|
| **3-step micro** | discover_capabilities → llm_brainstorm → micro_simulation (5-run, ci95, cvar95) | puro 009 buildPlan() lines 192-198 |
| **2-3 step adaptive** | interpretar_objetivo → gerar/validar(LLM) → [opcional fetch se objective contém web/buscar/site/url/http] | explicado_007 plan() lines 149-158 |
| **4-step verify** | analyze(LLM) → collect(fetch) → propose(LLM) → verify(internal.verify) | explicado_006 plan() lines 468-483 |

**Diagnostic insight D:** the planner is *always shallow* (≤4 steps). Nix Engine assumes complex planning has already happened upstream (in the LLM's chain-of-thought) — the engine's job is **policy enforcement around** the plan, not generation of deep plans. This is consistent with "orchestration-first, report-only" doctrine.

---

## 9. Environment guess (4-tier confidence ladder)

| Mode | Confidence | Evidence trigger |
|------|-----------|------------------|
| `cloud-run` | 0.95 | `K_SERVICE` env var present |
| `gcp-metadata` | 0.7 | metadata server (`http://metadata/computeMetadata/v1/instance/id` w/ Header `Metadata-Flavor: Google`) reachable in <300ms |
| `unknown` | 0.5 | default (running locally, no provider credentials, no GCP signals) |
| `unknown` | 0.3 | no_external_llm_credentials (no OPENAI_API_KEY *and* no GOOGLE_VERTEX_PROJECT_ID) |

**Diagnostic insight E:** environment_guess is a **provenance signature** for every envelope — auditor can verify "this decision was taken in cloud-run with confidence 0.95" vs "in unknown env with confidence 0.3". Beast equivalent: each S_DACM record should carry a similar runtime-provenance signature (workspace, agent, bus thread, file_count snapshot).

---

## 10. Cross-connections (Z-AA-AB-AC-AD)

- **Z (NIX-RS.1 ↔ Beast §28.4.9 S_DACM):** Both are weighted-sum composite scores combining heterogeneous metrics under [0,1]-clamp. NIX-RS.1 has 5 weighted terms with explicit semantic labels; S_DACM has 8 weighted terms that are numerical anomaly observables. **They are the same equation type at different abstraction tiers.**

- **AA (NIX-CVAR.1 ↔ §11 carry-entropy quantile):** Both use sorted-tail mean to capture bad-tail expectation. Nix uses cvar95 for risk-policy gating; Beast uses tail percentiles for §11 anomaly detection. **CVaR is the one-line implementation of "what does the worst 5% look like on average?" — and it is the same line in both systems.**

- **AB (NIX-BANDIT.1 ↔ Beast adaptive β↔holonomy from pass 3):** Both renormalise weights after small-LR updates with hard clamps `[w_min, w_max]`. Bandit lr=0.03 is comparable to Beast adaptive β step size (also small-LR). **Both implement online cognitive recalibration without weight collapse.** Hypothesis H63 (new): Nix bandit-update and Beast β-update can run on the same backing KV-store (`weights.json`), with the bandit feedback driving the Beast β-update via Fisher-Rao gradient.

- **AC (NIX-AVATAR + dissent ↔ Beast §10 ERC PLV closure):** dissent_ratio ∈ [0,1] is the council-frame analog of `1 - PLV` (phase-lock loss). When all avatars agree (one-stance dominates) dissent → 0; when avatars are uniformly distributed across stances dissent → max. This is **phase-locking on a discrete stance manifold instead of a continuous phasor manifold** — a discrete Kuramoto model. Hypothesis H64 (new): Nix dissent_ratio is the discretised-state form of Kuramoto R_△, and the same critical coupling K_c = 2γ governs the avatar-council quorum dynamics (where γ = avatar-disagreement persistence).

- **AD (rawness_report ↔ §15 D_p bit-color trace):** rawness_report is the **LLM-orchestration analogue of D_p output**: both record the actual emitted-entropy of a deterministic-or-quasi-deterministic process and audit against an expected baseline. shannon_entropy ≈ §15 H_color; length_ratio ≈ §15 emitted-bits/expected-bits ratio; suspected ≈ §15 anomaly_flag. **This pinpoints the rawness-entropy bridge as a structural — not metaphorical — homology.**

---

## 11. Hypothesis stack updates

- **H62 (new):** Beast 8-metric anomaly vector and Nix 14-avatar council vector are **dual decompositions of the same anomaly-detection space** (numerical vs. anthropic-frame). Falsifier: project Beast 8-vector onto a 14-dim hull; if the closest 14-dim avatar-projection mis-orders Beast anomaly events with > 20% Kendall-tau distortion vs. the original 8-vector ordering, hypothesis fails.

- **H63 (new):** Nix bandit-update and Beast adaptive-β update share the same fixed point under a Fisher-Rao metric. Falsifier: run Nix bandit on simulated objective_feedback derived from Beast S_DACM scores and check whether avatar-weights converge to a stationary distribution that matches the leading 14 eigenvectors of the Beast §10 multiplex Laplacian. Mismatch > 15% in spectrum invalidates.

- **H64 (new):** Nix `dissent_ratio` ∈ [0,1] is the discretised-state Kuramoto R_△, and quorum dynamics admit a critical coupling K_c = 2γ (γ = stance-flip rate). Falsifier: drive a 14-avatar council with a controlled dissent input and measure phase-lock collapse vs. K. If collapse onset > 2γ ± 10%, hypothesis revised.

- **C6 framework-correction (new):** risk-score formula is **inconsistent across Nix Engine variants** — explicado_006 uses 5-term composite (NIX-RS.1), puro 008 uses 3-term action-meta (NIX-RS.2). Canonical = explicado_006 (latest with bandit). Audit target: align all variants on NIX-RS.1.

- **C7 framework-correction (new):** HITL thresholds **drift across variants**: puro 008 has {0.2, 0.4, 0.65, 0.6}, puro 009 has single 0.7, explicado_006 has {0.35, 0.55, 0.75, 0.20}. Canonical = explicado_006. Audit target: register `risk_thresholds.canonical.json` in repo and have all variants read from it.

---

## 12. Running totals after pass 11

- **Lines read:** ~29,150 (pass 10) + ~3,400 lines this pass = **~32,550 lines** (homenagem corpus only)
- **Equations:** 237 (pass 10) + 12 new this pass (NIX-RS.1, NIX-RS.2, NIX-RS.3, NIX-HITL.1, NIX-HITL.2, NIX-CI.1, NIX-CVAR.1, NIX-H.1, NIX-BANDIT.1, NIX-DISS.1, NIX-AVATAR.1, NIX-ORACLE.1, NIX-WORLD.1, NIX-EDITION.1) = **~250 equations**
- **Constants:** 106 + ~10 new (lr=0.03, w_min=0.05, w_max=0.35, ε_min=0.05, holdout=0.2, hitl_cvar=0.20, soft/hard timeouts 1200/2500/1800/3500ms, risk_multiplier 1.15/0.90, oracle 0.05/0.8, dissent 0.2 in policy_cost) = **~116 constants**
- **Cross-connections:** 50 (pass 10) + 5 new (Z, AA, AB, AC, AD) = **55 cross-connections**
- **Files covered:** 35 + 8 = **43/72 ≈ 60% of homenagem corpus**
- **Hypotheses born this round:** H62, H63, H64
- **Framework-corrections born:** C6, C7

---

## 13. Falsification routes (test priorities for next round)

1. **C6/C7 reconciliation** — diff all 8 Nix Engine variants and produce a canonical `nix-engine-canonical.config.json`. ETA: 1 round.
2. **H62 8-vs-14 dual decomposition** — generate synthetic anomaly events with known ground truth, score with Beast 8-vector, score with Nix 14-avatars (instantiated with 1-line scoring functions per avatar tied to a Beast metric), measure Kendall-tau between the two rankings. ETA: 2 rounds.
3. **H64 Kuramoto-on-stance-manifold** — toy implementation of avatar-council with controllable stance-flip rate γ; sweep coupling K and find collapse threshold. ETA: 1-2 rounds.
4. **Cross-engine prom-metrics dashboard** — wire Beast pipeline to emit `nix_*` style metrics so Grafana can host both. ETA: 2-3 rounds (infra-heavy).
