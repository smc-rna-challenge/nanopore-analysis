#!/usr/bin/env cwl-runner
#
# Author: Allison Creason

cwlVersion: v1.0
class: CommandLineTool
baseCommand: [splicemap]

doc: ""

stdout:

hints:
  DockerRequirement:
    dockerPull: alliecreason/splicemap

requirements:
  - class: InlineJavascriptRequirement

inputs:

outputs:
  output:
    type: stdout
