from pathlib import Path
import shutil
import os

try:
    os.mkdir("build/ttf/gf")
except FileExistsError:
    pass

for font in ["CascadiaCode.ttf","CascadiaCodeItalic.ttf","CascadiaMono.ttf","CascadiaMonoItalic.ttf"]:
	origin = "build/ttf/"
	if "Italic" in font:
		shutil.copy(Path(origin+font),Path(origin+"gf/"+font.replace("Italic.ttf","[wght]-Italic.ttf")))
	else:
		shutil.copy(Path(origin+font),Path(origin+"gf/"+font.replace(".ttf","[wght].ttf")))