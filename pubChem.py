
import os

def fill0(str_d):
    if len(str_d) < 8:
        str_d = str_d.rjust(8,'0')
    return str_d

def build_names_sdfgz_3d():
    fnames = []
    step = 25000
    for i in range(0, 1000000000, step):
        beg_end = [str(d) for d in [i+1, i + step]]
        #小于8位补零
        beg_end = [fill0(str_d) for str_d in beg_end]
        
        fname = f'{beg_end[0]}_{beg_end[1]}.sdf.gz'
        fnames.append(fname)
    return fnames

def get_full_url(url_ftp, fname):
    return os.path.join(url_ftp, fname)



if __name__ == '__main__':

    #ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound_3D/01_conf_per_cmpd/SDF/00000001_00025000.sdf.gz

    url_ftp = 'ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound_3D/01_conf_per_cmpd/SDF/'
    #ftp://ftp.ncbi.nlm.nih.gov/pubchem/Compound_3D/01_conf_per_cmpd/SDF/00025001_00050000.sdf.gz
    fnames = build_names_sdfgz_3d()
    fnames = [get_full_url(url_ftp,fname) for fname in fnames]
    with open('pubchem_sdf.txt', 'w') as f:
        for fname in fnames:
            f.write(f'{fname}\n')
