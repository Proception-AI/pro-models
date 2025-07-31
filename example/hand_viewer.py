#!/usr/bin/env python3
"""Simple script to load and view hand models with joint control."""

import mujoco
import mujoco.viewer
import numpy as np
import time
import sys
import argparse

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='View hand models with joint control')
    parser.add_argument('scene', choices=['left', 'right', 'both'], 
                       help='Scene to load: left, right, or both hands')
    args = parser.parse_args()
    
    # Map scene choice to XML file
    scene_files = {
        'left': 'scenes/left_hand_scene.xml',
        'right': 'scenes/right_hand_scene.xml', 
        'both': 'scenes/both_hands_scene.xml'
    }
    
    xml_path = scene_files[args.scene]
    
    # Load the model
    model = mujoco.MjModel.from_xml_path(xml_path)
    data = mujoco.MjData(model)
    
    # Disable gravity to keep the hands stable
    model.opt.gravity[:] = 0.0
    
    # Launch the viewer with joint control
    with mujoco.viewer.launch_passive(model, data) as viewer:
        # Main simulation loop
        while viewer.is_running():
            # Only update positions, don't run physics
            mujoco.mj_forward(model, data)
            
            # Sync the viewer
            viewer.sync()
            
            # Small delay to prevent too fast updates
            time.sleep(0.02)

if __name__ == "__main__":
    main() 