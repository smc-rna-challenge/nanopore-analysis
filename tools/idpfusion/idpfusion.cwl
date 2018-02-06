#!/usr/bin/env cwl-runner
#
# Author: Allison Creason

cwlVersion: v1.0
class: CommandLineTool
baseCommand: [idp-fusion]

doc: ""

stdout:

hints:
  DockerRequirement:
    dockerPull: alliecreason/idpfusion:1.1.1

requirements:
  - class: InlineJavascriptRequirement

inputs:

outputs:
  output:
    type: stdout
