# Permission Policy

This package ships no executable scripts. Its runtime contract is a reviewed
workflow for public-market research and editable listing materials, so it does
not request network, file-write, subprocess, or interactive permissions from an
installer.

The policy is intentionally marked `not_required`. If a future version adds a
script or target adapter, the policy must be replaced with explicit reviewer
approval and target-enforcement evidence before release.
