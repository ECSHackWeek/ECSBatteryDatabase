#!/usr/bin/env python
"""
"""

import click

@click.command()
@click.option('-i', '--input_file', 'input_file', type=str, required=False,
                help='an input metdata file to be modified')
@click.option('-o', '--output_file', 'output_file', type=str, required=True,
                help='an input metdata file to be modified')
def meta_master(output_file, input_file=None):
    """
    """
    print(output_file)

if __name__ == '__main__':
    meta_master
