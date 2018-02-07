#!/usr/bin/env cwl-runner
#
# Author: Allison Creason

cwlVersion: v1.0
class: CommandLineTool
baseCommand: [minimap2]

doc: "Minimap2: A versatile pairwise aligner for genomic and spliced nucleotide sequences."

stdout: aln.sam

hints:
  DockerRequirement:
    dockerPull: alliecreason/minimap2:2.7-r654

requirements:
  - class: InlineJavascriptRequirement

inputs:
  ref:
    type: File
    inputBinding:
      position: 2

  fastq:
    type: File
    inputBinding:
      position: 3

  sam:
    type: boolean
    default: true
    inputBinding:
      position: 1
      prefix: "-a"

  preset:
    type: string
    default: "splice"
    inputBinding:
      position: 1
      prefix: "-x"

  kmer:
    type: int
    default: 15
    inputBinding:
      position: 1
      prefix: "-k"

  strand:
    type: string
    default: "f"
    inputBinding:
      position: 1
      prefix: "-u"

outputs:
  output:
    type: stdout
