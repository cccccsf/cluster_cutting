#!/usr/bin/python3
import components


def cluster_cutting(atom):

    Ini = components.IniReader()
    path, output_file, name = Ini.get_basic_info()
    fixed_atoms = Ini.read_fixed_atoms()
    central_atoms = Ini.read_central_atoms_info()
    cutting_factors = Ini.read_factors()
    deleted_atoms = Ini.read_deleted_atoms()
    out_layer_number = Ini.if_out_with_layer_number()
    cutting_setting = Ini.get_cutting_setting()

    FacCal = components.FactorCalculator(
        atom,
        path,
        output_file,
        factors = cutting_factors,
        name=name,
        central_atoms=central_atoms,
        fixed_atoms=fixed_atoms,
        cutting_setting=cutting_setting)
    #FacCal.get_cluster()

    print('***'*30)
    print(atom)
    dimen = FacCal.dimensionality
    if dimen == 2:
        print('central axis: {}'.format(FacCal.center))
    else:
        print('central point: {}'.format(FacCal.center))
    print('---'*30)
    dis_fac = FacCal.get_distance_to_center(fraction=True)
    print('factor of distance: ', dis_fac)
    print('---'*30)
    a_fac = FacCal.get_distance_to_vector(vec=1, fraction=True)
    print('factor of lattice vector 1: ', a_fac)
    print('---'*30)
    b_fac = FacCal.get_distance_to_vector(vec=2, fraction=True)
    print('factor of lattice vector 2: ', b_fac)
    if dimen != 2:
        c_fac = FacCal.get_distance_to_vector(vec=3, fraction=True)
        print('---'*30)
        print('factor of lattice vector 3: ', c_fac)
    print('***'*30)


if __name__ == "__main__":

    # please write down the atom infomation here
    element = 15
    x = 0
    y = 0
    z = 0


    atom = components.Atom(element, x, y, z)
    cluster_cutting(atom)
