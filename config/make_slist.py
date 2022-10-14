import pathlib
import pandas as pd
import numpy as np

DATA_DIR = pathlib.Path("/home/abod/projects/def-njohnson/RAW_DATA/rrDLBCL_CAPP_seq/IDT/pool_2").expanduser()

fqr1 = list(filter(pathlib.Path.is_file, DATA_DIR.glob('**/*R1*')))
fqr2 = list(filter(pathlib.Path.is_file, DATA_DIR.glob('**/*R2*')))

samples = sorted(list(set([x.stem for x in fqr1])))
samples = [x.split("." , -1)[4] for x in samples]
samples = [x.split("_" , -1)[0] for x in samples]

fqread1 = sorted(list(set([x for x in fqr1])))
fqread2 = sorted(list(set([x for x in fqr2])))

samples = np.array(samples)

samplesdf = pd.DataFrame().assign(Sample=samples, R1_file=fqread1, R2_file=fqread2)

samplesdf.to_csv('samplelist.tsv', sep = "\t" , header = False, index = False)