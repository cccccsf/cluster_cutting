#!/usr/bin/python3
import os
from components import read_info_from_CRYSTAL_INPUT
from components import read_info_from_ini_file

def test_CRYSTAL_INPUT_reader():

    path = r'C:\Users\ccccc\PycharmProjects\cutting_cluster\test'
    file = 'INPUT'
    file_path = os.path.join(path, file)
    dimen, lattice_vec, geometry = read_info_from_CRYSTAL_INPUT.read_CrystalInput(file_path, transfer_fraction=True)
    # print(dimen)
    #print(lattice_vec)
    #print(geometry)


def test_ini_reader():
    path = r'C:\Users\ccccc\PycharmProjects\cutting_cluster\test'
    file = 'geo.ini'
    file_path = os.path.join(path, file)
    Reader = read_info_from_ini_file.GeoIniReader(file_path)
    # Reader.read_geometry()
    # Reader.read_lattice_vector()


def test_suite():
    test_CRYSTAL_INPUT_reader()
    test_ini_reader()
    pass

test_suite()
