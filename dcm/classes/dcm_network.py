# Copyright 2016 Fachrizal Oktavian
# This file is part of DracOS Connection Manager.
#
# DracOS Connection Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DracOS Connection Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DracOS Connection Manager.  If not, see <http://www.gnu.org/licenses/>.

"""
dcm_network
"""
import subprocess
import dcm.classes.dcm_iw_parse
from terminaltables import AsciiTable
from colorama import Fore, Back, Style, init


class Dcm_network(object):

    init(autoreset=True)
    parsed_cells = []

    def __init__(self):
        self.iface = ''

    def exec_iwlist(self, iface):
        try:
            iw_result = subprocess.Popen(
                ['sudo', 'iwlist', iface, 'scanning'],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            self.parsed_cells = dcm_iw_parse.get_parsed_cells(iw_result.stdout)
            return True
        except:
            return False

    def get_scanning_result(self, iface):
        indent = ' ' * 1
        flagExec = self.exec_iwlist(iface)
        if flagExec:
            header = indent + 'Scanning WiFi networks using interface \'' + iface + '\'\n'
            network_table = [['SSID', 'AP Address', 'Channel', 'Encryption', 'Quality']]
            for dict_network in self.parsed_cells:
                network_table.append([
                    dict_network['Name'],
                    dict_network['Address'],
                    dict_network['Channel'],
                    dict_network['Encryption'],
                    dict_network['Quality']
                ])
            table = AsciiTable(network_table)
            print (Fore.YELLOW + Style.DIM + header + table.table)
            return True
        else:
            return False
