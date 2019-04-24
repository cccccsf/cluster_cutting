#!/usr/bin/python3
import components
from components import ClusterCutter


def cluster_cutting():

    print('Cluster Cutting begins...')

    Ini = components.IniReader()
    path, output_file, name = Ini.get_basic_info()
    fixed_atoms = Ini.read_fixed_atoms()
    central_atoms = Ini.read_central_atoms_info()
    cutting_factors = Ini.read_factors()
    deleted_atoms = Ini.read_deleted_atoms()
    out_layer_number = Ini.if_out_with_layer_number()
    cutting_setting = Ini.get_cutting_setting()

    Clu = ClusterCutter(
        path,
        output_file,
        factors = cutting_factors,
        name=name,
        central_atoms=central_atoms,
        fixed_atoms=fixed_atoms,
        cutting_setting=cutting_setting,
        deleted_atoms=deleted_atoms)
    Clu.get_cluster()
    
    if out_layer_number is True:
        Clu.write_xyz_with_layernumber()
    else:
        Clu.write_xyz()


if __name__ == "__main__":
    cluster_cutting()
