#!/usr/bin/env python

import argparse
import subprocess

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("genome_dir",help="Directory of the chromosome files in FASTA format")
    parser.add_argument("reads1")
    parser.add_argument("reads2")
    parser.add_argument("read_format", help="Format of the sequencer reads: FASTA, FASTQ, RAW")
    parser.add_argument("quality_format", help="Format of the quality string if FASTQ is used: phred-33, phred-64, solexa")
    parser.add_argument("mapper", help="The short reads mapper used: bowtie, eland, seqmap")
    parser.add_argument("--annotations", help="Annotations used to find novel junctions, in ref or bed format")
    parser.add_argument("temp_path", default="/tmp", help="Directory name of the directory that stores temporary files")
    parser.add_argument("--out-path", default="output", help="Directory name of the directory that stores the output files")
    parser.add_argument("--max-intron", default=400000, help="Maximum intron size, this is absolute 99th-percentile maximum.")
    parser.add_argument("--min-intron", default=20000, help="25-th intron size, this is the lower 25th-percentile intron size")
    parser.add_argument("--max-multi-hit", default=10, help="Maximum number of multi-hits")
    parser.add_argument("--full-read-length", help="Full read length")
    parser.add_argument("--head-clip-length", help="Number of bases to clip off the head of the read")
    parser.add_argument("--seed-mismatch",default=1, help="Maximum number of mismatches allowed in seeding for junction search: 0, 1, 2")
    parser.add_argument("--read-mismatch", default=2, help="Maximum number of mismatches allowed in entire read")
    parser.add_argument("--max-clip-allowed", help="Maximum number of bases allowed to be soft clipped from the ends of reads during alignment.")
    parser.add_argument("--sam-file", default="cuff", help="Generate a SAM file: cuff or sam")
    parser.add_argument("--ud-coverage", default="yes")
    parser.add_argument("--chromosome-wildcard", )
    parser.add_argument("--num-chromosome-together", default=2, help="Number of chromosomes to process at once, to take advantage of multi-core systems.")
    parser.add_argument("--bowtie-base-dir", help="Base of bowtie index, this should be the same genome as the chromosome files")
    parser.add_argument("--num-threads", default=2, help="Number of threads to use for mapping")
    parser.add_argument("--try-hard", default="yes", help="Try hard?")

    args = parser.parse_args()

    # write config
    print args.try_hard
    with open("splicemap.cfg", "w") as handle:
        handle.write("genome_dir = %s\n" % (args.genome_dir) +\
                "reads_list1 = %s\n" % (args.reads1) +\
                "reads_list2 = %s\n" % (args.reads2) +\
                "read_format = %s\n" % (args.read_format) +\
                "quality_format = %s\n" % (args.quality_format) +\
                "mapper = %s\n" % (args.mapper) +\
                "temp_path = %s\n" % (args.temp_path) +\
                "out_path = %s\n" % (args.out_path) +\
                "max_intron = %s\n" % (args.max_intron) +\
                "min_intron = %s\n" % (args.min_intron) +\
                "max_multi_hit = %s\n" % (args.max_multi_hit) +\
                "seed_mismatch = %s\n" % (args.seed_mismatch) +\
                "read_mismatch = %s\n" % (args.read_mismatch) +\
                "sam_file = %s\n" % (args.sam_file) +\
                "ud_coverage = %s\n" % (args.ud_coverage) +\
                "chromosome_wildcard = %s\n" % (args.chromosome_wildcard) +\
                "num_chromosome_together = %s\n" % (args.num_chromosome_together) +\
                "bowtie_base_dir = %s\n" % (args.bowtie_base_dir) +\
                "num_threads = %s\n" % (args.num_threads) +\
                "try_hard = %s\n" % (args.try_hard)
                )
        if args.annotations:
            handle.write("annotations = %s" % (args.annotations))

        if args.full_read_length:
            handle.write("full_read_length = %s" % (args.full_read_length))

        if args.head_clip_length:
            handle.write("head_clip_length = %s" %(args.head_clip_length))

        if args.max_clip_allowed:
            handle.write("max_clip_allowed = %s" %(args.max_clip_allowed))

    # subprocess
    subprocess.check_call(["splicemap","splicemap.cfg"])
