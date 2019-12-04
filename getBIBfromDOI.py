from habanero import cn
import argparse

parser = argparse.ArgumentParser(description='Multiple Doi for BIBtexDownload')
parser.add_argument('-l', '--list', nargs='+',
                    help='<Required> Set flag', required=True)
for _, value in parser.parse_args()._get_kwargs():
    if value is not None:
        print(cn.content_negotiation(ids=value, format="bibentry"))
        print('\n')
