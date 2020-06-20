from staticjinja import Site
from csscompressor import compress
import os

OUTPATH = os.environ.get("OUTPATH",default="/var/www/html")
APPVERSION = os.environ.get("APPVERSION",default="testBuild")
STATIC_PATH = os.environ.get("STATIC_PATH",default="static/")

if __name__ == "__main__":
    site = Site.make_site(
        env_globals={
            "app_version":APPVERSION
        },
        searchpath="./templates",
        outpath=OUTPATH,
        staticpaths=[STATIC_PATH]
    )
    site.render()

    # css compression
    print("Compressiong CSS files.")
    for css_file in os.listdir(os.path.join(OUTPATH,STATIC_PATH,"css")):
        with open(os.path.join(OUTPATH,STATIC_PATH,"css",css_file) ,"r") as f:
            original_content = f.read()
        with open(os.path.join(OUTPATH,STATIC_PATH,"css",css_file) ,"w") as f:
            f.write(compress(original_content))