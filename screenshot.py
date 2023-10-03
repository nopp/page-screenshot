import imgkit
import argparse

parser = argparse.ArgumentParser(description="""
This script is going to create screenshot from site . 
""")
parser.add_argument("url", help="Url from site")

args = parser.parse_args()

URL = args.url

imgkit.from_url(URL,"out.png")
