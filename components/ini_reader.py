#!/usr/bin/python3
import os
import configparser
from configparser import ConfigParser


class IniReader(object):

    def __init__(self, path=''):
        self.ini_path = path
        self.set_default_path()

        self.cfg = ConfigParser()
        self.job_path = ''
        self.output_file = ''
        self.name = ''
        self.read_basic_info()

        self.central_atoms = []
        self.factors = []
        self.fixed_atoms = []

        self.deleted_atoms = []
        self.coord = True
        self.add_h = False
        self.out_layer_number = True

    def set_default_path(self):
        if self.ini_path == '':
            self.ini_path = os.path.dirname(
                os.path.dirname(os.path.realpath(__file__)))
            self.ini_path = os.path.join(self.ini_path, 'input.ini')

    def read_basic_info(self):
        try:
            self.cfg.read(self.ini_path, encoding='utf-8')

            self.job_path = self.cfg.get('Ini', 'path')
            self.output_file = self.read_geo_opt_out_file()
            self.name = self.cfg.get('Ini', 'name')
        except Exception as e:
            print(e)

    def read_geo_opt_out_file(self):
        output = ''
        try:
            output = self.cfg.get('Ini', 'output')
            if '\\' in output or '/' in output:
                pass
            else:
                output = os.path.join(self.job_path, output)
        except configparser.NoOptionError:
            print('Output file info not found in input.ini.')
            print('Program will choose output file automatically.')
        return output

    def get_basic_info(self):
        return self.job_path, self.output_file, self.name

    def read_central_atoms_info(self):
        try:
            upper_center_atoms = self.cfg.get('Cluster', 'upper_center_atoms')
        except configparser.NoOptionError:
            upper_center_atoms = []
        try:
            under_center_atoms = self.cfg.get('Cluster', 'under_center_atoms')
        except configparser.NoOptionError:
            under_center_atoms = []
        upper_center_atoms = self.split_atoms(upper_center_atoms)
        under_center_atoms = self.split_atoms(under_center_atoms)
        self.central_atoms = self.process_center_atoms(
            upper_center_atoms, under_center_atoms)
        return self.central_atoms

    @staticmethod
    def split_atoms(atoms):
        if atoms == '' or atoms is None or atoms == []:
            atoms = []
        else:
            atoms = atoms.split()
        return atoms

    @staticmethod
    def process_center_atoms(upper_atoms, under_atoms):
        if upper_atoms != [] and under_atoms != []:
            atoms = [upper_atoms, under_atoms]
        elif upper_atoms == [] and under_atoms != 0:
            atoms = under_atoms
        elif upper_atoms != [] and under_atoms == []:
            atoms = upper_atoms
        else:
            atoms = []
        return atoms

    def read_factors(self):
        try:
            factors_upper = self.cfg.get('Cluster', 'upper_factors')
        except configparser.NoOptionError:
            factors_upper = []
        try:
            factors_under = self.cfg.get('Cluster', 'under_factors')
        except configparser.NoOptionError:
            factors_under = []
        factors_upper = self.split_factors(factors_upper)
        factors_under = self.split_factors(factors_under)
        if len(factors_upper) > 0 and len(factors_under) > 0:
            factors = [factors_upper, factors_under]
        elif len(factors_upper) > 0 and len(factors_under) == 0:
            factors = [factors_upper, factors_upper]
        elif len(factors_upper) == 0 and len(factors_under) > 0:
            factors = [factors_under, factors_under]
        else:
            factors = []
        self.factors = factors
        return factors

    @staticmethod
    def split_factors(factors):
        if factors == '' or factors == []:
            factors = []
        else:
            try:
                factors = factors.split()
                factors = [float(fac) for fac in factors]
            except Exception as e:
                print(e)
        return factors

    def read_fixed_atoms(self):
        try:
            self.fixed_atoms = self.cfg.get('Cluster', 'fixed_atoms')
            self.fixed_atoms = self.split_atoms(self.fixed_atoms)
        except configparser.NoOptionError:
            self.fixed_atoms = []
        return self.fixed_atoms

    def read_coord(self):
        try:
            self.coord = self.cfg.get('Cluster', 'coord')
            if self.coord.lower() == 'false':
                self.coord = False
            else:
                self.coord = True
        except configparser.NoOptionError:
            self.coord = False
        return self.coord

    def read_deleted_atoms(self):
        try:
            self.deleted_atoms = self.cfg.get('Cluster', 'deleted_atoms')
            self.deleted_atoms = self.split_atoms(self.deleted_atoms)
        except configparser.NoOptionError:
            self.deleted_atoms = []
        return self.deleted_atoms

    def read_if_add_h(self):
        try:
            self.add_h = self.cfg.get('Cluster', 'add_h')
            if self.add_h.lower() == 'false' or self.add_h == '':
                self.add_h = False
            else:
                self.add_h = True
        except configparser.NoOptionError:
            self.add_h = False
        return self.add_h

    def if_out_with_layer_number(self):
        try:
            self.out_layer_number = self.cfg.get('Cluster', 'output_with_layer_numer')
            if self.out_layer_number.lower() == 'false' or self.out_layer_number == '':
                self.out_layer_number = False
            else:
                self.out_layer_number = True
        except configparser.NoOptionError:
            self.out_layer_number = False
        return self.out_layer_number
    
    def get_cutting_setting(self):
        self.coord = self.read_coord()
        self.add_h = self.read_if_add_h()
        cutting_setting = [self.coord, self.add_h]
        return cutting_setting
