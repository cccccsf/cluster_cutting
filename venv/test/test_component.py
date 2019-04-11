#!/usr/bin/python3
import components

def test_ini_reader():
    Ini = components.IniReader()
    ini_path = Ini.ini_path
    # expected = r'C:\Users\ccccc\PycharmProjects\cutting_cluster\venv\input.ini'
    # assert path == expected
    job_path = Ini.job_path
    output = Ini.output_file

    test_central_atoms_reading(Ini)
    test_factors_reading(Ini)


def test_factors_reading(Ini):
    factors = Ini.read_factors()
    print(factors)


def test_central_atoms_reading(Ini):
    Ini.read_central_atoms_info()
    central_atoms = Ini.central_atoms
    #print(central_atoms)
    



def test_suite():
    test_ini_reader()

test_suite()
