import os
import sys
from typing import Dict
import yaml

languages: Dict[str, dict] = {}
languages_present: Dict[str, str] = {}

# Path to the language files directory
lang_dir = r"./strings/langs/"

# Load English first (as a base)
try:
    with open(os.path.join(lang_dir, "en.yml"), encoding="utf8") as f:
        languages["en"] = yaml.safe_load(f)
        languages_present["en"] = languages["en"]["name"]
except Exception as e:
    print(f"[Error] Problem loading English file: {e}")
    sys.exit(1)

# Now process all other languages
for filename in os.listdir(lang_dir):
    if not filename.endswith(".yml") or filename == "en.yml":
        continue  # Skip non-yml and English file

    language_name = filename[:-4]
    # Load the language file
    try:
        with open(os.path.join(lang_dir, filename), encoding="utf8") as f:
            lang_dict = yaml.safe_load(f)
            # If file is empty, start with empty dict
            if lang_dict is None:
                lang_dict = {}

            # Add missing English keys
            for item in languages["en"]:
                if item not in lang_dict:
                    lang_dict[item] = languages["en"][item]

            languages[language_name] = lang_dict

        languages_present[language_name] = languages[language_name]["name"]
    except Exception as e:
        print(f"[Error] Problem with language file '{filename}': {e}")
        sys.exit(1)

def get_string(lang: str):
    return languages[lang]
