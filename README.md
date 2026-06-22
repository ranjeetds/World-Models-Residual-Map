# World Models Residual Map

Companion artifact for the survey paper:

> **From Pattern Completion to Counterfactual Simulation: A Survey of World Models as the Residual Frontier of Foundation AI**

Author: **Ranjeet Dhumal**  
Affiliation: **Senior Data Scientist, Wolters Kluwer India Private Limited**
Repository: **https://github.com/ranjeetds/World-Models-Residual-Map**

This repository is a curated map of world-model systems, open-source implementations, open-weight releases, benchmarks, datasets, and evaluation criteria. It is intentionally kept as a single human-readable document so a reviewer can understand the artifact without opening JSON files.

The core thesis is simple: world models should be compared by the residual capabilities they address after LLMs, vision models, and generative media models are accounted for. Those residuals include action semantics, state persistence, physical law extrapolation, counterfactual reasoning, uncertainty calibration, planning utility, sim-to-real transfer, spatial consistency, social-physical coupling, and governance readiness.

The JSON files in `data/` remain the machine-readable backend; this README is generated from them.

## How to Use This Artifact

| Reader goal | Start with | What to look for |
|---|---|---|
| Understand the paper's evidence base | Current Snapshot and Residual Capability Taxonomy | Counts behind the residual map and why a residual was credited. |
| Find runnable baselines | Open Code and Open Weight Systems | Code/weight status, domain, and caveat before attempting reproduction. |
| Identify paper ideas | Research Gap Map | Missing capability, what to build, and what evidence would convince reviewers. |
| Extend the catalog | Coding Methodology and Contributing | Required fields, evidence levels, residual definitions, and validation commands. |
| Prepare a citable release | Public Release Quality Gates | Validation, generated artifacts, DOI, and citation metadata. |

## Headline Findings

1. **The field is dense where model-based RL already gave it tools.** Action semantics and planning utility dominate the coded systems, with 28 and 21 systems respectively.
2. **The defining world-model claims are thinly evidenced.** Counterfactual reasoning, calibrated uncertainty, and social-physical coupling remain the weakest system-side residuals in this snapshot.
3. **Evaluation is uneven.** State persistence and physical-law extrapolation have multiple benchmarks, but counterfactual reasoning and uncertainty calibration still need stronger dedicated measurement.
4. **Open code is not the same as reproducibility.** Several systems release code without weights, or release platform components whose exact model claims need upstream license and model-card checks.
5. **The catalog should be read as evidence tracking, not leaderboard ranking.** Counts measure whether a residual is credibly attacked, not whether the residual is solved.

| Residual | Systems | Benchmarks | Reading |
|---|---:|---:|---|
| Action semantics | 28 | 1 | Widely claimed; needs more action-contrast benchmarks. |
| Planning utility | 21 | 1 | Strong MBRL lineage; planner exploitation remains under-tested. |
| Counterfactual reasoning | 2 | 0 | A central gap for decision-facing world models. |
| Uncertainty calibration | 3 | 0 | Crucial for risk-aware planning but rarely measured directly. |
| Social-physical coupling | 0 | 3 | Benchmarks exist, but system evidence is essentially absent. |

## Current Snapshot

| Item | Count |
|---|---:|
| World-model systems | 32 |
| Benchmarks and evaluation suites | 11 |
| Datasets and simulators | 8 |
| Residual capability families | 10 |
| Method categories | 18 |
| Open-code systems | 20 |
| Open-weight systems | 9 |
| Closed reference systems | 7 |

The counts are conservative. A system is not marked open unless an upstream source clearly exposes code and/or weights.

## Research Gap Map

This table turns the residual map into a workbench for researchers. Each row is a possible paper contribution if paired with a clear method and convincing evidence.

| Gap | Why it matters | What a contribution could add | Evidence target |
|---|---|---|---|
| Counterfactual consequence | World models should answer what changes under a different action, not only what happens next. | Paired-intervention data, causal state updates, or counterfactual rollout objectives. | Matched-history tests where changed actions or layouts cause the expected outcome shift. |
| Calibrated uncertainty for planning | A planner needs to know when imagined futures are unreliable. | Uncertainty-aware dynamics, abstention, ensembles, distributional rollouts, or risk-aware planning heads. | Calibration under off-policy and rare-state shifts; lower regret when planning uses uncertainty. |
| Social-physical dynamics | Real agents move through spaces governed by physics, goals, norms, and other agents. | Multi-agent world models with hidden beliefs, social rules, contact, affordances, and strategic response. | Human or agent response prediction under interventions; better decisions in mixed social-physical tasks. |
| Persistent state with correction | Long rollouts drift unless memory can be corrected by new observations. | Memory architectures that preserve identity, inventory, maps, and latent state over long horizons. | Occlusion and re-observation tests; stable object identity and map consistency across long rollouts. |
| Action abstraction | Actions may be torques, skills, language instructions, social moves, or tool calls. | Hierarchical action representations that bridge language-level intent and executable controls. | Action-contrast tests across abstraction levels and transfer to unseen tasks. |
| Geometry-to-dynamics bridge | 3D assets can look navigable without obeying contact, support, material, or affordance dynamics. | Representations that bind metric geometry to dynamics and interaction constraints. | Multi-view consistency plus collision, support, conservation, and affordance diagnostics. |
| Planner-in-the-loop robustness | Passive replay can hide model exploitation by optimizers. | Benchmarks where planners actively search against the learned model. | Exploitation rate, closed-loop regret, recovery behavior, and transfer to real or high-fidelity simulators. |
| Validity and governance envelope | Deployment-facing simulators need known limits, provenance, and audit trails. | World-model model cards, datasheets, operational design domains, and risk registers. | Public invalid regions, monitoring hooks, audit logs, and safety-case evidence. |

## Residual Capability Taxonomy

These residuals are the conceptual bridge between the paper and the repository. They describe what world models must prove beyond fluent text, static perception, or visually plausible video.

| Residual | Question | Minimum evidence | Systems | Benchmarks |
|---|---|---|---:|---:|
| Action Semantics | Do different actions cause distinguishably correct futures? | action contrast, intervention replay, action-conditioned likelihood | 28 | 1 |
| State Persistence | Are object identity, inventory, map, and hidden state maintained over horizon? | long-horizon probes, occlusion tests, memory stress tests | 18 | 9 |
| Physical Law Extrapolation | Does the model generalize rules beyond visually similar cases? | OOD physics splits, conservation tests, contact or collision tests | 5 | 6 |
| Counterfactual Reasoning | Can the model answer alternative-action or alternative-layout queries? | matched histories, changed actions, changed layouts, measurable expected changes | 2 | 0 |
| Uncertainty Calibration | Does uncertainty grow in ambiguous, off-policy, or rare states? | calibration curves, ensemble or distributional metrics, abstention-error correlation | 3 | 0 |
| Planning Utility | Does using the world model improve decisions? | return, regret, planner-in-the-loop robustness, policy improvement | 21 | 1 |
| Sim-to-Real Transfer | Do generated rollouts or policies help outside the learned simulator? | real-world validation, sim-to-real gap, recovery from perturbations | 14 | 3 |
| Spatial Consistency | Is geometry metric and persistent across views and edits? | multi-view consistency, occupancy or LiDAR checks, mesh or scale checks | 8 | 3 |
| Social-Physical Coupling | Do agents respond to actions, information, norms, and physical constraints? | multi-agent scenarios, strategic adaptation, human-behavior validation | 0 | 3 |
| Governance Readiness | Are validity limits, data provenance, and failure modes documented? | model cards, datasheets, risk register, safety case | 4 | 0 |

Detailed residual mapping is encoded in `data/capability_families.json` and `data/systems.json`.

## Open Code and Open Weight Systems

This is the most important table for readers who want to inspect, run, or build on existing work. It deliberately separates code openness from weight openness.

| System | Year | Category | Code | Weights | Domains | Main link | Caveat |
|---|---:|---|---|---|---|---|---|
| World Models | 2018 | Latent MBRL | yes | no | car racing, reinforcement learning | [link](https://github.com/hardmaru/WorldModelsExperiments) | Classic compact latent world model; useful baseline but narrow by modern foundation-model standards. |
| PlaNet | 2019 | Latent MBRL | yes | no | deepmind control, reinforcement learning | [link](https://github.com/google-research/planet) | Strong model-based control reference; not a general visual simulator. |
| DriveDreamer | 2023 | Driving World Model | yes | unknown | autonomous driving, nuScenes, controllable video | [link](https://github.com/JeffWang987/DriveDreamer) | Driving-video generation is not by itself closed-loop safety validation. |
| DIAMOND | 2024 | Diffusion Game World Model | yes | yes | Atari, counter-strike gameplay, reinforcement learning | [link](https://github.com/eloialonso/diamond) | Best read as a strong game-domain diffusion world model, not evidence of broad real-world physical simulation. |
| IRASim | 2024 | Robot Video Action Simulator | yes | yes | robot manipulation, real robot video | [link](https://github.com/bytedance/IRASim) | Robot-arm manipulation focus; contact validity should be evaluated beyond video preference. |
| Navigation World Models | 2024 | Navigation Video World Model | yes | yes | egocentric navigation, robot navigation | [link](https://github.com/facebookresearch/nwm) | Navigation-focused; not a general manipulation or social simulator. |
| Open-Genie | 2024 | Generative Interactive Environment | yes | unknown | genie reproduction, interactive environments | [link](https://github.com/myscience/open-genie) | Unofficial implementation; should not be treated as DeepMind's released system. |
| RoboDreamer | 2024 | Robot Video World Model | yes | unknown | robot imagination, robot manipulation, rt-x | [link](https://github.com/rainbow979/robodreamer) | Focuses on compositional robot video imagination; action grounding should be checked per task. |
| TD-MPC2 | 2024 | Latent MBRL | yes | yes | continuous control, DMControl, MetaWorld | [link](https://github.com/nicklashansen/tdmpc2) | Strong control system; world model is optimized for decision utility rather than photorealistic rendering. |
| V-JEPA | 2024 | Joint Embedding Predictive Architecture | yes | yes | video representation, self-supervised learning | [link](https://github.com/facebookresearch/jepa) | Representation-first; not by itself an action-conditioned simulator. |
| CarDreamer | 2025 | Driving World Model Platform | yes | no | autonomous driving, world model evaluation, urban driving | [link](https://github.com/ucd-dare/CarDreamer) | Platform for autonomous-driving world model research; model claims depend on configured backbones. |
| Cosmos Predict-2 | 2025 | Physical AI World Foundation Model | yes | partial | physical AI, world simulation, video prediction | [link](https://github.com/nvidia-cosmos/cosmos-predict2) | Intermediate Cosmos release; treat separately from Cosmos 3 and Predict-2.5. |
| Cosmos Predict-2.5 | 2025 | Physical AI World Foundation Model | yes | yes | physical AI, world simulation, video generation | [link](https://github.com/nvidia-cosmos/cosmos-predict2.5) | Verify model-card restrictions for each checkpoint before using in downstream work. |
| DreamerV3 | 2025 | Latent MBRL | yes | unknown | reinforcement learning, Minecraft, robotics | [link](https://github.com/danijar/dreamerv3) | Open repository states it is a reimplementation based on DreamerV2 code and unrelated to Google or DeepMind. |
| GenieRedux | 2025 | Generative Interactive Environment | yes | unknown | multi-environment world models, games | [link](https://github.com/insait-institute/genieredux) | Framework inspired by Genie-style interactive world models; evaluate independently from DeepMind Genie. |
| HunyuanWorld 1.0 | 2025 | Spatial 3D World Generation | yes | yes | 3D world generation, interactive worlds, creative tools | [link](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0) | Spatial generation evidence should be separated from calibrated dynamics or robotics claims. |
| Matrix-Game | 2025 | Interactive Game World Model | yes | yes | Minecraft, game world simulation | [link](https://github.com/SkyworkAI/Matrix-Game) | Primarily Minecraft-centered; avoid claiming broad real-world generality. |
| NVIDIA Cosmos | 2025 | Physical AI World Foundation Model | yes | partial | physical AI, robotics, autonomous vehicles | [link](https://github.com/nvidia/cosmos) | Platform-level release with multiple components; check each sub-repository license and model terms. |
| V-JEPA 2 | 2025 | Joint Embedding Predictive Architecture | yes | yes | video understanding, robot planning | [link](https://github.com/facebookresearch/vjepa2) | Action-conditioned planning is specific to V-JEPA 2-AC fine-tuning; do not overstate the base encoder. |
| LeWorldModel | 2026 | Joint Embedding Predictive Architecture | yes | unknown | 2D control, 3D control, latent planning | [link](https://github.com/lucas-maes/le-wm) | New 2026 result; independent replication and broader domain tests remain important. |

## Full Systems Catalog

Systems are grouped by method family. Each entry includes the evidence domain and a caveat so the catalog is useful without opening JSON files.

### Commercial General World Model

#### Runway GWM-1 (2025)

- **Organizations:** Runway
- **Domains:** explorable worlds, avatars, robotics
- **Modalities:** video, actions, multimodal prompts
- **Action conditioned:** yes
- **Openness:** code no; weights no; closed_reference
- **Residuals:** Action Semantics, State Persistence, Planning Utility
- **Evaluation modes:** vendor reports, demos
- **Links:** [project](https://runwayml.com/research/introducing-runway-gwm-1)
- **Caveat:** Commercial system; independent benchmarks and openness status should be updated if releases change.

### Commercial World Simulation

#### Odyssey-2 Max (2026)

- **Organizations:** Odyssey
- **Domains:** causal world simulation, interactive scenes
- **Modalities:** video, actions, multimodal prompts
- **Action conditioned:** yes
- **Openness:** code no; weights no; closed_reference
- **Residuals:** Action Semantics, State Persistence, Planning Utility
- **Evaluation modes:** vendor reports, demos
- **Links:** [project](https://odyssey.ml/introducing-odyssey-2-max)
- **Caveat:** Mostly vendor-reported evidence in this snapshot.

### Diffusion Game World Model

#### DIAMOND (2024)

- **Organizations:** University of Geneva, University of Edinburgh, Independent
- **Domains:** Atari, counter-strike gameplay, reinforcement learning
- **Modalities:** pixels, actions, diffusion latents
- **Action conditioned:** yes
- **Openness:** code yes; weights yes; official_open
- **Residuals:** Action Semantics, Planning Utility, State Persistence
- **Evaluation modes:** Atari 100k, agent trained in world model, playable rollouts
- **Links:** [paper](https://arxiv.org/abs/2405.12399), [project](https://diamond-wm.github.io/), [code](https://github.com/eloialonso/diamond)
- **Caveat:** Best read as a strong game-domain diffusion world model, not evidence of broad real-world physical simulation.

#### GameNGen (2024)

- **Organizations:** Google Research, Tel Aviv University
- **Domains:** DOOM, game simulation
- **Modalities:** video frames, actions
- **Action conditioned:** yes
- **Openness:** code no; weights no; closed_reference
- **Residuals:** Action Semantics, State Persistence, Planning Utility
- **Evaluation modes:** real-time interactive simulation, human evaluation, PSNR
- **Links:** [paper](https://arxiv.org/abs/2408.14837), [project](https://gamengen.github.io/)
- **Caveat:** Impressive real-time DOOM simulation; no verified official public code or weights.

### Driving World Model

#### DriveDreamer (2023)

- **Organizations:** GigaAI, academic
- **Domains:** autonomous driving, nuScenes, controllable video
- **Modalities:** driving video, text, structured traffic constraints, actions
- **Action conditioned:** yes
- **Openness:** code yes; weights unknown; official_open
- **Residuals:** Action Semantics, Spatial Consistency, Sim-to-Real Transfer, State Persistence
- **Evaluation modes:** controllable driving video, nuScenes, future prediction
- **Links:** [project](https://drivedreamer.github.io/), [code](https://github.com/JeffWang987/DriveDreamer)
- **Caveat:** Driving-video generation is not by itself closed-loop safety validation.

#### GAIA-1 (2023)

- **Organizations:** Wayve
- **Domains:** autonomous driving, generative driving simulation
- **Modalities:** video, text, actions
- **Action conditioned:** yes
- **Openness:** code no; weights no; closed_reference
- **Residuals:** Action Semantics, State Persistence, Sim-to-Real Transfer
- **Evaluation modes:** vendor experiments, driving video generation
- **Links:** [paper](https://arxiv.org/abs/2309.17080), [project](https://anthonyhu.github.io/gaia1)
- **Caveat:** Important driving-world-model reference, but not an open-source release.

#### Waymo World Model (2026)

- **Organizations:** Waymo, Google DeepMind
- **Domains:** autonomous driving, camera simulation, LiDAR simulation
- **Modalities:** camera, LiDAR, language, scene layout, driving actions
- **Action conditioned:** yes
- **Openness:** code no; weights no; closed_reference
- **Residuals:** Action Semantics, Counterfactual Reasoning, Sim-to-Real Transfer, Spatial Consistency, Governance Readiness
- **Evaluation modes:** vendor reports, driving simulation, rare event generation
- **Links:** [project](https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation/)
- **Caveat:** February 2026 closed reference; safety claims require independent closed-loop validation.

### Driving World Model Platform

#### CarDreamer (2025)

- **Organizations:** UC Davis DARE Lab
- **Domains:** autonomous driving, world model evaluation, urban driving
- **Modalities:** simulator state, observations, actions
- **Action conditioned:** yes
- **Openness:** code yes; weights no; official_open
- **Residuals:** Planning Utility, Action Semantics, Sim-to-Real Transfer
- **Evaluation modes:** open-source platform, urban driving tasks, world-model baselines
- **Links:** [code](https://github.com/ucd-dare/CarDreamer)
- **Caveat:** Platform for autonomous-driving world model research; model claims depend on configured backbones.

### Generative Interactive Environment

#### Genie (2024)

- **Organizations:** Google DeepMind
- **Domains:** 2D platform games, unlabeled video, interactive environments
- **Modalities:** video, latent actions, image prompts
- **Action conditioned:** yes
- **Openness:** code no; weights no; closed_reference
- **Residuals:** Action Semantics, State Persistence, Planning Utility
- **Evaluation modes:** interactive rollouts, qualitative demos, paper benchmarks
- **Links:** [paper](https://arxiv.org/abs/2402.15391), [project](https://sites.google.com/view/genie-2024/home)
- **Caveat:** Central comparator, but no verified official public code or weights.

#### Open-Genie (2024)

- **Organizations:** community
- **Domains:** genie reproduction, interactive environments
- **Modalities:** video, latent actions
- **Action conditioned:** yes
- **Openness:** code yes; weights unknown; unofficial_open
- **Residuals:** Action Semantics, State Persistence
- **Evaluation modes:** reimplementation, training code
- **Links:** [paper](https://arxiv.org/abs/2402.15391), [code](https://github.com/myscience/open-genie)
- **Caveat:** Unofficial implementation; should not be treated as DeepMind's released system.

#### GenieRedux (2025)

- **Organizations:** INSAIT
- **Domains:** multi-environment world models, games
- **Modalities:** video, actions, environment traces
- **Action conditioned:** yes
- **Openness:** code yes; weights unknown; official_open
- **Residuals:** Action Semantics, State Persistence, Planning Utility
- **Evaluation modes:** multi-environment training, interactive rollout
- **Links:** [code](https://github.com/insait-institute/genieredux)
- **Caveat:** Framework inspired by Genie-style interactive world models; evaluate independently from DeepMind Genie.

### Interactive Game World Model

#### Oasis (2024)

- **Organizations:** Decart, Etched
- **Domains:** Minecraft-like world, interactive video
- **Modalities:** video, keyboard and mouse actions
- **Action conditioned:** yes
- **Openness:** code no; weights unknown; official_partial
- **Residuals:** Action Semantics, State Persistence
- **Evaluation modes:** public demo, interactive rollout
- **Links:** [project](https://oasis-model.github.io/)
- **Caveat:** Publicly visible interactive system, but code/weights openness should be verified before labeling open source.

#### Matrix-Game (2025)

- **Organizations:** SkyworkAI
- **Domains:** Minecraft, game world simulation
- **Modalities:** video, actions, long-horizon memory
- **Action conditioned:** yes
- **Openness:** code yes; weights yes; official_open
- **Residuals:** Action Semantics, State Persistence, Planning Utility
- **Evaluation modes:** streaming generation, interactive rollout, domain benchmarks
- **Links:** [paper](https://arxiv.org/abs/2506.18701), [project](https://matrix-game-homepage.github.io/), [code](https://github.com/SkyworkAI/Matrix-Game), [model](https://huggingface.co/Skywork/Matrix-Game-3.0)
- **Caveat:** Primarily Minecraft-centered; avoid claiming broad real-world generality.

### Joint Embedding Predictive Architecture

#### V-JEPA (2024)

- **Organizations:** Meta AI, FAIR
- **Domains:** video representation, self-supervised learning
- **Modalities:** video, embeddings
- **Action conditioned:** no
- **Openness:** code yes; weights yes; official_open
- **Residuals:** State Persistence, Spatial Consistency
- **Evaluation modes:** representation benchmarks, video understanding
- **Links:** [project](https://ai.meta.com/research/v-jepa/), [code](https://github.com/facebookresearch/jepa)
- **Caveat:** Representation-first; not by itself an action-conditioned simulator.

#### V-JEPA 2 (2025)

- **Organizations:** Meta AI, FAIR
- **Domains:** video understanding, robot planning
- **Modalities:** video, embeddings, robot trajectories
- **Action conditioned:** partial
- **Openness:** code yes; weights yes; official_open
- **Residuals:** Action Semantics, State Persistence, Planning Utility, Spatial Consistency
- **Evaluation modes:** robot planning, representation benchmarks, video understanding
- **Links:** [paper](https://arxiv.org/abs/2506.09985), [project](https://ai.meta.com/research/vjepa/), [code](https://github.com/facebookresearch/vjepa2)
- **Caveat:** Action-conditioned planning is specific to V-JEPA 2-AC fine-tuning; do not overstate the base encoder.

#### LeWorldModel (2026)

- **Organizations:** academic
- **Domains:** 2D control, 3D control, latent planning
- **Modalities:** pixels, actions, embeddings
- **Action conditioned:** yes
- **Openness:** code yes; weights unknown; official_open
- **Residuals:** Action Semantics, Planning Utility, State Persistence
- **Evaluation modes:** latent planning, control benchmarks
- **Links:** [paper](https://arxiv.org/abs/2603.19312), [project](https://le-wm.github.io/), [code](https://github.com/lucas-maes/le-wm)
- **Caveat:** New 2026 result; independent replication and broader domain tests remain important.

### Latent MBRL

#### World Models (2018)

- **Organizations:** Independent / academic
- **Domains:** car racing, reinforcement learning
- **Modalities:** pixels, latent state, actions
- **Action conditioned:** yes
- **Openness:** code yes; weights no; official_open
- **Residuals:** Planning Utility, Action Semantics
- **Evaluation modes:** closed-loop control, environment return
- **Links:** [paper](https://arxiv.org/abs/1803.10122), [project](https://worldmodels.github.io/), [code](https://github.com/hardmaru/WorldModelsExperiments)
- **Caveat:** Classic compact latent world model; useful baseline but narrow by modern foundation-model standards.

#### PlaNet (2019)

- **Organizations:** Google Research
- **Domains:** deepmind control, reinforcement learning
- **Modalities:** pixels, latent state, actions, rewards
- **Action conditioned:** yes
- **Openness:** code yes; weights no; official_open
- **Residuals:** Action Semantics, Planning Utility, Uncertainty Calibration
- **Evaluation modes:** latent planning, environment return, open-loop prediction
- **Links:** [paper](https://arxiv.org/abs/1811.04551), [project](https://planetrl.github.io/), [code](https://github.com/google-research/planet)
- **Caveat:** Strong model-based control reference; not a general visual simulator.

#### TD-MPC2 (2024)

- **Organizations:** UC San Diego, independent academic
- **Domains:** continuous control, DMControl, MetaWorld, ManiSkill2, MyoSuite
- **Modalities:** states, pixels, actions, rewards, latent state
- **Action conditioned:** yes
- **Openness:** code yes; weights yes; official_open
- **Residuals:** Planning Utility, Action Semantics, Uncertainty Calibration, Sim-to-Real Transfer
- **Evaluation modes:** model predictive control, multi-task evaluation, benchmarks
- **Links:** [paper](https://arxiv.org/abs/2310.16828), [project](https://www.tdmpc2.com/), [code](https://github.com/nicklashansen/tdmpc2)
- **Caveat:** Strong control system; world model is optimized for decision utility rather than photorealistic rendering.

#### DreamerV3 (2025)

- **Organizations:** DeepMind, University of Toronto
- **Domains:** reinforcement learning, Minecraft, robotics, control
- **Modalities:** pixels, latent state, actions, rewards, continuation
- **Action conditioned:** yes
- **Openness:** code yes; weights unknown; official_open
- **Residuals:** Action Semantics, Planning Utility, Uncertainty Calibration, Sim-to-Real Transfer
- **Evaluation modes:** imagined rollouts, closed-loop control, environment return
- **Links:** [paper](https://www.nature.com/articles/s41586-025-08744-2), [project](https://danijar.com/project/dreamerv3/), [code](https://github.com/danijar/dreamerv3)
- **Caveat:** Open repository states it is a reimplementation based on DreamerV2 code and unrelated to Google or DeepMind.

### Navigation Video World Model

#### Navigation World Models (2024)

- **Organizations:** Meta AI, UC Berkeley
- **Domains:** egocentric navigation, robot navigation
- **Modalities:** egocentric video, navigation actions
- **Action conditioned:** yes
- **Openness:** code yes; weights yes; official_open
- **Residuals:** Action Semantics, Planning Utility, Spatial Consistency, State Persistence
- **Evaluation modes:** navigation planning, trajectory ranking, visual rollout
- **Links:** [paper](https://arxiv.org/abs/2412.03572), [project](https://www.amirbar.net/nwm/), [code](https://github.com/facebookresearch/nwm)
- **Caveat:** Navigation-focused; not a general manipulation or social simulator.

### Omnimodal World Model

#### Cosmos 3 (2026)

- **Organizations:** NVIDIA
- **Domains:** physical AI, robotics, autonomous vehicles
- **Modalities:** text, image, video, audio, actions
- **Action conditioned:** yes
- **Openness:** code partial; weights partial; official_partial
- **Residuals:** Action Semantics, Physical Law Extrapolation, Sim-to-Real Transfer, Governance Readiness
- **Evaluation modes:** omnimodal generation, physical AI benchmarks, vendor reports
- **Links:** [paper](https://arxiv.org/abs/2606.02800), [project](https://www.nvidia.com/en-us/ai/cosmos/)
- **Caveat:** Very recent 2026 release; code/weight details should be rechecked before submission.

### Physical AI World Foundation Model

#### Cosmos Predict-2 (2025)

- **Organizations:** NVIDIA
- **Domains:** physical AI, world simulation, video prediction
- **Modalities:** video, text, image, actions
- **Action conditioned:** partial
- **Openness:** code yes; weights partial; official_open
- **Residuals:** Physical Law Extrapolation, Sim-to-Real Transfer, Action Semantics
- **Evaluation modes:** video generation, custom fine-tuning, physical AI workflows
- **Links:** [project](https://research.nvidia.com/labs/dir/cosmos-predict2/), [code](https://github.com/nvidia-cosmos/cosmos-predict2)
- **Caveat:** Intermediate Cosmos release; treat separately from Cosmos 3 and Predict-2.5.

#### Cosmos Predict-2.5 (2025)

- **Organizations:** NVIDIA
- **Domains:** physical AI, world simulation, video generation
- **Modalities:** text, image, video, world state
- **Action conditioned:** partial
- **Openness:** code yes; weights yes; official_open
- **Residuals:** Physical Law Extrapolation, Sim-to-Real Transfer, Spatial Consistency, Governance Readiness
- **Evaluation modes:** Text2World, Image2World, Video2World, benchmarks
- **Links:** [paper](https://arxiv.org/abs/2511.00062), [code](https://github.com/nvidia-cosmos/cosmos-predict2.5), [model](https://huggingface.co/nvidia/Cosmos-Predict2.5-2B)
- **Caveat:** Verify model-card restrictions for each checkpoint before using in downstream work.

#### NVIDIA Cosmos (2025)

- **Organizations:** NVIDIA
- **Domains:** physical AI, robotics, autonomous vehicles, smart infrastructure
- **Modalities:** video, text, actions, tokens, datasets, tooling
- **Action conditioned:** partial
- **Openness:** code yes; weights partial; official_open
- **Residuals:** Sim-to-Real Transfer, Physical Law Extrapolation, Action Semantics, Governance Readiness
- **Evaluation modes:** foundation model platform, tooling, customization workflows
- **Links:** [paper](https://arxiv.org/abs/2501.03575), [project](https://www.nvidia.com/en-us/ai/cosmos/), [code](https://github.com/nvidia/cosmos)
- **Caveat:** Platform-level release with multiple components; check each sub-repository license and model terms.

### Robot Manipulation World Model

#### SWIM (2023)

- **Organizations:** Carnegie Mellon University
- **Domains:** robot manipulation, human video pretraining
- **Modalities:** human video, robot trajectories, affordances
- **Action conditioned:** yes
- **Openness:** code no; weights unknown; official_partial
- **Residuals:** Action Semantics, Sim-to-Real Transfer, Planning Utility
- **Evaluation modes:** real robot manipulation, few-shot robot data
- **Links:** [paper](https://arxiv.org/abs/2308.10901), [project](https://human-world-model.github.io/)
- **Caveat:** Important robotics result; no verified code release found in this snapshot.

### Robot Video Action Simulator

#### IRASim (2024)

- **Organizations:** ByteDance, HKUST
- **Domains:** robot manipulation, real robot video
- **Modalities:** robot video, action trajectories
- **Action conditioned:** yes
- **Openness:** code yes; weights yes; official_open
- **Residuals:** Action Semantics, Sim-to-Real Transfer, State Persistence, Physical Law Extrapolation
- **Evaluation modes:** robot video prediction, benchmark, human evaluation
- **Links:** [paper](https://arxiv.org/abs/2406.14540), [project](https://gen-irasim.github.io/), [code](https://github.com/bytedance/IRASim)
- **Caveat:** Robot-arm manipulation focus; contact validity should be evaluated beyond video preference.

### Robot Video World Model

#### RoboDreamer (2024)

- **Organizations:** academic
- **Domains:** robot imagination, robot manipulation, rt-x
- **Modalities:** video, language instructions, goal images
- **Action conditioned:** partial
- **Openness:** code yes; weights unknown; official_open
- **Residuals:** Planning Utility, Sim-to-Real Transfer, Action Semantics
- **Evaluation modes:** video planning, simulation execution, compositional generalization
- **Links:** [paper](https://arxiv.org/abs/2404.12377), [project](https://robovideo.github.io/), [code](https://github.com/rainbow979/robodreamer)
- **Caveat:** Focuses on compositional robot video imagination; action grounding should be checked per task.

### Spatial 3D World Generation

#### HunyuanWorld 1.0 (2025)

- **Organizations:** Tencent Hunyuan
- **Domains:** 3D world generation, interactive worlds, creative tools
- **Modalities:** text, image, panorama, mesh, 3D world
- **Action conditioned:** partial
- **Openness:** code yes; weights yes; official_open
- **Residuals:** Spatial Consistency, State Persistence, Planning Utility
- **Evaluation modes:** 3D generation, mesh export, interactive exploration
- **Links:** [paper](https://arxiv.org/abs/2507.21809), [code](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0), [model](https://huggingface.co/tencent/HunyuanWorld-1)
- **Caveat:** Spatial generation evidence should be separated from calibrated dynamics or robotics claims.

#### World Labs Marble (2025)

- **Organizations:** World Labs
- **Domains:** spatial intelligence, 3D world generation, creative worlds
- **Modalities:** text, image, video, 3D layout, Gaussian splats, meshes
- **Action conditioned:** partial
- **Openness:** code no; weights no; closed_reference
- **Residuals:** Spatial Consistency, State Persistence, Planning Utility
- **Evaluation modes:** vendor demos, 3D export, interactive world creation
- **Links:** [project](https://www.worldlabs.ai/blog/marble-world-model)
- **Caveat:** Spatial world-generation evidence should not be treated as validated physical simulation without additional tests.

### Universal Interactive Simulator

#### UniSim (2023)

- **Organizations:** Google Research, UC Berkeley, MIT
- **Domains:** robotics, navigation, real-world interaction
- **Modalities:** images, video, robot actions, navigation controls, language instructions
- **Action conditioned:** yes
- **Openness:** code no; weights no; official_partial
- **Residuals:** Action Semantics, Planning Utility, Sim-to-Real Transfer
- **Evaluation modes:** sim-trained policy transfer, video generation, zero-shot deployment
- **Links:** [paper](https://arxiv.org/abs/2310.06114), [project](https://universal-simulator.github.io/)
- **Caveat:** Important conceptual and experimental system; no verified public code or weights.

### Value Equivalent Planning

#### MuZero open implementations (2020)

- **Organizations:** DeepMind, community implementations
- **Domains:** board games, Atari, planning
- **Modalities:** observations, actions, rewards, values, policies
- **Action conditioned:** yes
- **Openness:** code partial; weights no; unofficial_open
- **Residuals:** Planning Utility, Counterfactual Reasoning, Action Semantics
- **Evaluation modes:** tree search, game performance, value prediction
- **Links:** [paper](https://www.nature.com/articles/s41586-020-03051-4), [pseudocode](https://arxiv.org/src/1911.08265v2/anc/pseudocode.py), [community_code](https://github.com/michaelnny/muzero)
- **Caveat:** DeepMind released pseudocode rather than a full official training codebase; community implementations vary in completeness.

## Benchmarks and Evaluation Suites

Benchmarks are included with explicit limitations because world-model validity cannot be reduced to one media-quality score.

| Benchmark | Year | What it tests | Residuals | Links | Limitation |
|---|---:|---|---|---|---|
| Waymo Open Dataset Evaluation | 2020 | LiDAR, camera, 3D detection, motion prediction, scenario evaluation | Spatial Consistency, State Persistence, Sim-to-Real Transfer | [paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.html), [code](https://github.com/waymo-research/waymo-open-dataset) | Dataset and evaluation code aid validation, but a learned simulator must also be tested under interventions. |
| nuScenes Prediction / Planning Evaluations | 2020 | minADE, minFDE, maps, actors, camera, LiDAR | Spatial Consistency, State Persistence, Sim-to-Real Transfer | [paper](https://arxiv.org/abs/1903.11027), [devkit](https://github.com/nutonomy/nuscenes-devkit) | Open-loop logs and devkits do not by themselves provide closed-loop counterfactual simulation. |
| Physion | 2021 | physical prediction, scenario-based dynamics, human-machine comparison | Physical Law Extrapolation, State Persistence | [project](https://physion-benchmark.github.io/), [code](https://github.com/cogtoolslab/physics-benchmarking-neurips2021) | Useful physics probe; older than frontier video-generation systems and not action-policy oriented. |
| EgoSchema | 2023 | long temporal reasoning, multiple-choice QA, egocentric understanding | State Persistence, Social-Physical Coupling | [paper](https://proceedings.neurips.cc/paper_files/paper/2023/hash/90ce332aff156b910b002ce4e6880dec-Abstract-Datasets_and_Benchmarks.html), [project](https://egoschema.github.io/), [code](https://github.com/egoschema/EgoSchema) | QA over video, not action-conditioned closed-loop simulation. |
| BEHAVIOR-1K | 2024 | 1000 everyday activities, rigid objects, deformables, liquids, long-horizon mobile manipulation | Planning Utility, Sim-to-Real Transfer, Social-Physical Coupling, Physical Law Extrapolation | [paper](https://arxiv.org/abs/2403.09227), [project](https://behavior.stanford.edu/index.html), [code](https://github.com/StanfordVL/BEHAVIOR-1K) | Simulation benchmark; learned world-model claims still need transfer and simulator-exploitation checks. |
| OpenEQA | 2024 | open-vocabulary questions, episodic memory EQA, active EQA, LLM-Match scoring | State Persistence, Spatial Consistency, Social-Physical Coupling | [paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Majumdar_OpenEQA_Embodied_Question_Answering_in_the_Era_of_Foundation_Models_CVPR_2024_paper.pdf), [project](https://open-eqa.github.io/) | Embodied understanding benchmark; correct answers do not prove intervention-valid simulation. |
| VBench | 2024 | motion smoothness, subject consistency, temporal flickering, prompt consistency, aesthetic quality | State Persistence | [paper](https://arxiv.org/abs/2311.17982), [project](https://vchitect.github.io/VBench-project/), [code](https://github.com/Vchitect/VBench) | Strong media-quality diagnostic but not sufficient for action semantics, counterfactual validity, or planning utility. |
| VBench 2.0 / VBench++ | 2025 | human fidelity, controllability, creativity, physics, commonsense | State Persistence, Physical Law Extrapolation | [paper](https://arxiv.org/abs/2503.21755), [pypi](https://pypi.org/project/vbench2/) | Improves faithfulness evaluation but still does not by itself validate closed-loop decisions. |
| WorldModelBench | 2025 | instruction following, physical consistency, world-model failures | Physical Law Extrapolation, State Persistence, Action Semantics | [paper](https://arxiv.org/abs/2502.20694) | Useful for video-world-model failures; should be extended for robotics, driving, and planner-in-the-loop tests. |
| PhyGround | 2026 | 13 physical laws, criteria-grounded prompts, human annotations, PhyJudge-9B | Physical Law Extrapolation, State Persistence | [paper](https://arxiv.org/abs/2605.10806), [project](https://phyground.github.io/) | Law-specific video evaluation; not a substitute for robot or driving closed-loop validation. |
| Physics-IQ | 2026 | solid mechanics, fluid dynamics, optics, thermodynamics, magnetism | Physical Law Extrapolation | [project](https://physics-iq.github.io/), [code](https://github.com/google-deepmind/physics-iq-benchmark) | Targets physics understanding in generated video; does not directly measure policy improvement. |

## Datasets and Simulators

Datasets and simulators are listed separately because they support evaluation and training claims but are not world models by themselves.

| Dataset / simulator | Year | Access | Modalities | Relevance | Links | Caveat |
|---|---:|---|---|---|---|---|
| DeepMind Control Suite | 2018 | open_code | states, pixels, actions, rewards | Common control suite for latent dynamics and model-based RL systems such as Dreamer and TD-MPC2. | [code](https://github.com/google-deepmind/dm_control) | Simulated physics and relatively narrow tasks; not enough for deployment claims. |
| Atari 100k | 2020 | open_environments | pixels, actions, rewards | Common benchmark for sample-efficient model-based RL and DIAMOND-style world-model agents. | [ale](https://github.com/Farama-Foundation/Arcade-Learning-Environment) | Game domain; results should not be overgeneralized to real-world physics. |
| Waymo Open Dataset | 2020 | restricted_download | camera, LiDAR, maps, annotations, scenarios | Important for multi-sensor driving prediction, evaluation, and scenario analysis. | [paper](https://openaccess.thecvf.com/content_CVPR_2020/html/Sun_Scalability_in_Perception_for_Autonomous_Driving_Waymo_Open_Dataset_CVPR_2020_paper.html), [project](https://waymo.com/open/about/), [code](https://github.com/waymo-research/waymo-open-dataset) | Terms restrict use; dataset page warns it is for research and not real-life vehicle performance evaluation. |
| nuScenes | 2020 | restricted_download | camera, LiDAR, radar, maps, annotations | Common source for driving world models, trajectory prediction, occupancy, and scenario generation. | [paper](https://arxiv.org/abs/1903.11027), [project](https://www.nuscenes.org/), [devkit](https://github.com/nutonomy/nuscenes-devkit) | Requires account and terms; logs are not equivalent to counterfactual closed-loop simulation. |
| EgoSchema | 2023 | open_with_dataset_terms | video, question-answer pairs | Useful probe for long temporal memory and human activity understanding. | [project](https://egoschema.github.io/), [code](https://github.com/egoschema/EgoSchema), [kaggle](https://www.kaggle.com/competitions/egoschema-public/overview) | QA benchmark, not an intervention simulator. |
| BEHAVIOR-1K | 2024 | open_code_restricted_assets | simulation, 3D assets, tasks, object states | Tests long-horizon household tasks and physical-social interactions relevant to embodied world models. | [paper](https://arxiv.org/abs/2403.09227), [project](https://behavior.stanford.edu/index.html), [code](https://github.com/StanfordVL/BEHAVIOR-1K) | Task success in simulation does not automatically prove real-world transfer. |
| IRASim Benchmark | 2024 | open_or_gated_check_upstream | real-robot videos, action trajectories | Tests real-robot action-conditioned video simulation. | [project](https://gen-irasim.github.io/), [code](https://github.com/bytedance/IRASim) | Contact and control validity require task-level robot checks, not only video metrics. |
| OpenEQA | 2024 | open_with_terms | episodic memory, environment observations, natural-language questions | Evaluates grounded environment understanding from memory and exploration. | [project](https://open-eqa.github.io/), [blog](https://ai.meta.com/blog/openeqa-embodied-question-answering-robotics-ar-glasses/) | Does not directly measure whether a model can roll out action-conditioned futures. |

## Related Community Lists

These lists are useful for auditing missing work. Entries from them should still be verified against primary sources before being added here.

| List | Focus | Link | How to use |
|---|---|---|---|
| Awesome World Models | general world-model papers and resources | [link](https://github.com/knightnemo/Awesome-World-Models) | Cross-check broad coverage and discover missing systems; do not copy entries without verification. |
| Learning to Model the World survey repository | survey-related world-model resources | [link](https://github.com/JiahuaDong/Awesome-World-Models) | Useful related survey artifact for comparison. |
| Awesome World Models for Autonomous Driving | autonomous-driving world model papers | [link](https://github.com/LMD0311/Awesome-World-Model) | Use to expand driving-specific coverage. |
| Awesome Papers World Models Autonomous Driving | driving world-model paper list | [link](https://github.com/chaytonmin/Awesome-Papers-World-Models-Autonomous-Driving) | Use to audit driving methods such as DriveDreamer, Panacea, Drive-WM, and OccWorld. |
| Awesome World Models for Manipulation | robot manipulation world models | [link](https://github.com/jacob-zietek/awesome-world-models-manipulation) | Use to expand manipulation-specific coverage. |
| Awesome Embodied World Model | embodied and robotic world models | [link](https://github.com/tsinghua-fib-lab/Awesome-Embodied-World-Model) | Use to track newer embodied world-model releases. |
| Awesome Interactive World Model | interactive video world modeling | [link](https://github.com/liujiuming123/Awesome-Interactive-World-Model) | Use to expand interactive-video coverage after verifying sources. |

## Coding Methodology

The catalog follows three rules.

1. **Be conservative about openness.** If code or weights are unclear, they are marked `unknown`, `partial`, or `no`.
2. **Separate demos from evidence.** A visually impressive rollout is not treated as proof of general physical simulation.
3. **Code by residual, not hype.** Each system is mapped to the residual capability it plausibly attacks, such as action semantics or planning utility.

### Evidence Levels

| Label | Meaning |
|---|---|
| `official_open` | Official code and/or weights are available. |
| `official_partial` | Official paper/project exists, but release is incomplete, limited, or partly open. |
| `unofficial_open` | Community implementation exists, but not an official release. |
| `closed_reference` | Important comparator, but no verified public implementation or weights. |
| `dataset_or_benchmark` | Evaluation resource rather than a model. |

### Inclusion Criteria

Included systems must have at least one reliable upstream source: paper, project page, official repository, model page, or benchmark page. The catalog excludes social-media-only claims, unclear forks, and copied third-party assets.

## Reproducing and Updating the Artifact

The single README is generated from the JSON files in `data/`. Edit the JSON, then regenerate.

```bash
python3 scripts/validate_artifact.py
python3 scripts/export_tables.py
python3 scripts/export_figures.py
```

The scripts update this README, the paper-facing LaTeX table at `generated/tables/open_systems_table.tex`, and the system-by-residual coverage figure at `generated/figures/residual_heatmap.tikz`.

Recommended submission workflow:

1. Finalize metadata before submission.
2. Run validation and export.
3. Commit `README.md`, `data/`, `scripts/`, and `generated/tables/open_systems_table.tex`.
4. Tag a paper snapshot, for example `v0.1-paper-submission`.
5. Archive the tag on Zenodo or a similar archival service.
6. Cite the DOI in the paper.

## Public Release Quality Gates

Before creating the public GitHub repository or a Zenodo archive, run these checks:

- `python3 scripts/validate_artifact.py` passes with no warnings.
- `python3 scripts/export_tables.py` and `python3 scripts/export_figures.py` have been run after the last data edit.
- `README.md` contains the same counts as the paper abstract and residual-coverage table.
- `CITATION.cff` has the final release date, version, and repository URL after the GitHub repository exists.
- `paper/repository_note.md` has the final GitHub URL and DOI after the archived snapshot exists.
- Every new entry has an upstream source and a caveat that prevents overclaiming.
- Generated files are committed only when they are deterministic outputs of the JSON source.

Known limits of the current snapshot: it is a curated corpus rather than an exhaustive census; closed systems are evidence-limited; openness can change after release; and residual labels are conservative binary codings rather than full capability scores.

## Repository Files

```text
README.md                         # single human-readable artifact
data/*.json                       # machine-readable source of truth
scripts/validate_artifact.py       # schema and consistency checks
scripts/export_tables.py           # regenerates README and LaTeX table
scripts/export_figures.py          # regenerates the residual coverage figure
generated/tables/open_systems_table.tex
generated/figures/residual_heatmap.tikz
CITATION.cff
CONTRIBUTING.md
LICENSE
paper/repository_note.md
```

## License and Disclaimer

This repository's original metadata, documentation, and generated tables are licensed under CC BY 4.0. External repositories, papers, model weights, datasets, and benchmarks remain governed by their upstream licenses and terms.

This artifact is a research index, not an endorsement of any model's safety, licensing terms, or deployment readiness. Always review upstream licenses, acceptable-use policies, model cards, and dataset terms before use.

Views are personal and do not represent Wolters Kluwer.
