import pandas as pd
import argparse

arg_parser = argparse.ArgumentParser("Estructura de la que se tomó la muestra")

arg_parser.add_argument("-f", "--FILE",
                    metavar="path/to/file",
                    help="archivo con expresión génica",
                    required=True)

args = arg_parser.parse_args()

dataset_df = pd.read_csv(args.FILE)

str_col = dataset_df["structure_name"].values.tolist()

tmp_crt = str_col.count("temporal neocortex")
w_mtr = str_col.count("white matter of forebrain")
hipp = str_col.count("hippocampus (hippocampal formation)")
par_neo = str_col.count("parietal neocortex")
