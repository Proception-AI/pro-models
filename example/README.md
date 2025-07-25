# Hand Viewer

A simple MuJoCo viewer for ProHand models.

## Usage

### With `just` (recommended)

From the repository root:

```bash
just show_left_hand     # ProHand 1D (left)
just show_right_hand    # ProHand 1D (right)
just show_both_hands    # Both hands
```

The `justfile` automatically picks the right Python launcher for your platform
(`mjpython` on macOS, `python3` elsewhere).

### Direct invocation

The viewer takes a single positional argument selecting which scene to load:

```bash
# Linux
python3 hand_viewer.py {left|right|both}

# macOS — MuJoCo's passive viewer requires mjpython
mjpython hand_viewer.py {left|right|both}
```

> **macOS note:** `python hand_viewer.py ...` will fail with a threading /
> Cocoa error on macOS. Use `mjpython` (installed with the `mujoco` pip
> package) so the viewer runs on the main thread.

## Scenes

| File | Description |
| --- | --- |
| `scenes/left_hand_scene.xml`  | ProHand 1D left hand |
| `scenes/right_hand_scene.xml` | ProHand 1D right hand |
| `scenes/both_hands_scene.xml` | Both hands together |
| `scenes/common_scene.xml`     | Shared lighting / ground plane include |

## Requirements

- Python 3.7+
- MuJoCo 3.3.0+ (provides `mjpython` on macOS)
- GLFW
- PyOpenGL
- NumPy

Install dependencies with:

```bash
pip install -r requirements.txt
```
