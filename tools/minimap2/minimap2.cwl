#!/usr/bin/env cwl-runner
#
# Author: Allison Creason

cwlVersion: v1.0
class: CommandLineTool
baseCommand: [minimap2]

doc: ""

stdout:

hints:
  DockerRequirement:
    dockerPull: alliecreason/minimap2:

requirements:
  - class: InlineJavascriptRequirement

inputs:

outputs:
  output:
    type: stdout
