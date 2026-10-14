# Pro-Models: Professional Hand Simulation Models

A comprehensive collection of high-fidelity robotic hand simulation models for MuJoCo, featuring the ProHand Gen2 Power (left and right) with multiple collision representations and optimized meshes.

|              Both Hand Example Demo               |
| :-----------------------------------------------: |
| ![Both Hand Model](./example/media/both_hands.png) |

## Overview

This repository contains professional-grade robotic hand models designed for simulation and research applications:

- **ProHand Gen2 Power (Left Hand)**: 5-finger anthropomorphic hand on forearm with 22 degrees of freedom
- **ProHand Gen2 Power (Right Hand)**: mirrored counterpart with matching kinematics

Both models feature:
- **Finger Configuration**: 5 fingers (thumb, index, middle, ring, pinky)
- **Joint Structure**: 22 degrees of freedom per hand (including 2 DOF wrist)
- **Collision Models**: Convex hull and capsule hybrid representations
- **Mesh Quality**: Both convex and optimized mesh variants
- **Applications**: Research, development, and simulation

## Model Structure

```
assets/
├── meshes/
│   ├── gen_2_5_L/                 # ProHand Gen2 Power (Left)
│   └── gen_2_5_R/                 # ProHand Gen2 Power (Right)
│       ├── convex/                # Convex hull meshes
│       └── optimized/             # Optimized detailed meshes
├── mjcf/
│   ├── gen_2_5_L/                 # MJCF configuration files
│   └── gen_2_5_R/                 # MJCF configuration files
│       ├── include_ASY__RIGHT_HAND_GEN25_ON_FOREARM_GEN1E_convex_chain.xml
│       ├── include_ASY__RIGHT_HAND_GEN25_ON_FOREARM_GEN1E_convex_config.xml
│       ├── include_ASY__RIGHT_HAND_GEN25_ON_FOREARM_GEN1E_capsule_hybrid_chain.xml
│       └── include_ASY__RIGHT_HAND_GEN25_ON_FOREARM_GEN1E_capsule_hybrid_config.xml
└── urdf/
    ├── gen_2_5_L/                 # URDF exports (convex, optimized)
    └── gen_2_5_R/                 # URDF exports (convex, optimized)
```

## Collision Representations

Each hand model provides two collision representation options:

### Convex Hull Representation
- **File Pattern**: `*_convex_*.xml`
- **Advantages**: Fast collision detection, suitable for real-time simulation
- **Use Cases**: Control development, real-time applications

### Capsule Hybrid Representation
- **File Pattern**: `*_capsule_hybrid_*.xml`
- **Advantages**: Faster and simpler collision detection, for contact-rich simulation
- **Use Cases**: Research, fast simulation, contact analysis

## Quick Start

### Installation
```bash
# Clone the repository
git clone --branch release/gen2 --single-branch https://github.com/Proception-AI/pro-models.git
cd pro-models

# Install dependencies
pip install -r example/requirements.txt
```

### Running the Example Viewer

The repo ships with a [`justfile`](./justfile) for convenience. With [`just`](https://github.com/casey/just) installed:

```bash
just show_left_hand     # ProHand Gen2 Power (left)
just show_right_hand    # ProHand Gen2 Power (right)
just show_both_hands    # Both hands side-by-side
```

Or invoke the viewer directly:

```bash
# Linux
python3 example/hand_viewer.py {left|right|both}

# macOS (MuJoCo's passive viewer requires mjpython on macOS)
mjpython example/hand_viewer.py {left|right|both}
```

See [`example/README.md`](./example/README.md) for more details.

## Joint Configuration

Both hands feature similar joint structures:
- **Wrist**: 2 DOF (`wrist_abd`, `wrist_flex`)
- **Thumb**: 4 DOF (`t0_TM_abd`, `t1_TM`, `t2_MCP`, `t3_DIP`)
- **Fingers**: 4 DOF each (`CMC_abd`, `MCP`, `PIP`, `DIP`)

Joint names carry an `L_` or `R_` prefix.

## Performance Considerations

### Mesh Selection
- **Convex Meshes**: ~50% faster simulation, suitable for real-time applications
- **Optimized Meshes**: Better visual quality, recommended for research and analysis

### Collision Detection
- **Convex Hull**: Fastest collision detection, good for control development
- **Capsule Hybrid**: More accurate contact modeling, better for research

## Contributing

We welcome contributions to improve the models, add new features, or enhance documentation. Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This repository uses a dual license:

- **Code, MJCF/URDF model description, and documentation** are released under the
  **BSD 3-Clause License** — free for academic, research, **and commercial** use. See
  [LICENSE.txt](./LICENSE.txt) for the full text.
- **Mesh geometry** is **proprietary** — © Proception Inc., provided for
  evaluation and simulation of the ProHand series only. This covers all
  `*.obj` and `*.stl` files under `assets/meshes/`. Using the geometry to
  reproduce a competing product, redistribution, modification-and-redistribution,
  and commercial use require prior written permission. See
  [MESHES-LICENSE](./MESHES-LICENSE) for the full terms.


For everything BSD-licensed, you may use, modify, redistribute, and build
products on top of it; the conditions are that the copyright notice and
disclaimer are preserved and that Proception's name is not used to endorse
derived products. The software is provided "as is", without warranty of any
kind.

We welcome research partnerships, commercial collaborations, and contributions.
Reach out at 📧 **contact@proception.ai**.

## Citation

If you use these models in your research, please cite:

```bibtex
@misc{pro_models_2025,
  title={Pro-Models: Proception Inc. Simulation Models for MuJoCo},
  author={Proception Inc., Jianxiang Xu, etc.},
  year={2025},
  url={https://github.com/Proception-AI/pro-models}
}
```

## Support

If you have questions, encounter issues, or would like to request a feature, feel free to open a GitHub issue.

## Related Projects

- **ProHand SDK** — driver and client SDK for this hand: [prohand-sdk `release/gen2`](https://github.com/Proception-AI/prohand-sdk/tree/release/gen2)

<eof>

---
Rights Reserved @ Proception AI, Inc. 2024-2025
</eof>
