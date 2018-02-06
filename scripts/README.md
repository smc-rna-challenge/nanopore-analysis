## Scripts for Nanopore analysis

### Convert sam files to psl (required for GMAP)
`sam_to_psl.py [samfile] [chrom.sizes] [output]`

### Annotates psl files with genes
`infer_strand_for_psl.py [psl file] [gtf annotation] [output]`

### Detect fusions from psl file
`identify_fusions.py [annotated psl] [output]`

### Quantify minimap2 alignment into counts per gene
`count_sam_genes.py [minimap sam] [output]` 
