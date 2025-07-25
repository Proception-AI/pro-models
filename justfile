default:
    @just --list

# ==============================================================================
# TEST MODELS UPLOADED TO (INTERNAL/PRIVATE) "modules/models"
# ==============================================================================
run_mjcf_py := if os() == "macos" { "mjpython" } else { "python3" }

mjcf:
    python3 -m mujoco.viewer

example_mjcf_hand scene="right":
    {{run_mjcf_py}} example/hand_viewer.py {{scene}}

show_left_hand:
    @just example_mjcf_hand left
show_right_hand:
    @just example_mjcf_hand right
show_both_hands:
    @just example_mjcf_hand both