# Pro-Models

Simulation models (MuJoCo MJCF, URDF, meshes) for the ProHand. There is one
product line per branch. `main` carries no models: pick the line that matches
your hardware and clone that branch.

| Product line | Branch | Formats | Status |
|---|---|---|---|
| ProHand Gen1 (Gen1.D) | `release/gen1` | MJCF, URDF, USD | maintenance |
| ProHand Gen2 Power | `release/gen2` | MJCF, URDF | current |

The SDK for each line is in [prohand-sdk](https://github.com/Proception-AI/prohand-sdk)
on the branch with the same name.

## Get a line

```bash
git clone --branch release/gen2 --single-branch https://github.com/Proception-AI/pro-models.git
# or
git clone --branch release/gen1 --single-branch https://github.com/Proception-AI/pro-models.git
```

Already cloned? `git fetch origin && git checkout release/gen2`.

## Releases

Every release is a tag named `<line>/<date>`:

```bash
git tag -l 'gen2/*'            # releases of the Gen2 Power line
git checkout gen2/2026.10.13   # pin to one
```

Each branch has its own README, example viewer and model files for that line.

## License

Code and model description files are BSD 3-Clause ([LICENSE.txt](LICENSE.txt)).
Mesh geometry is proprietary ([MESHES-LICENSE](MESHES-LICENSE)).

## Support

- Issues: https://github.com/Proception-AI/pro-models/issues
- Email: contact@proception.ai
