import json
import sys

from subprocess import check_output
from pathlib import Path
from typing import Optional, List

extension_lang_map = {
    "py": "python",
    "cpp": "cpp",
    "cc": "cpp",
    "h": "cpp",
    "java": "java"
}

base_path = Path(__file__).parent


def check_args() -> bool:
    if len(sys.argv) < 3:
        return False
    if sys.argv[2] != "message":
        return False
    return True

def has_attempt() -> Optional[int]:
    config_file_path = (base_path / "../config.json").resolve()
    with open(config_file_path) as config_f:
        config = json.load(config_f)
        if "attempt" in config:
            return config["attempt"]
    return None

def filter_code_files() -> List[str]:
    changed_files_str = check_output(["git",
                                      "diff",
                                      "--cached",
                                      "--name-only",
                                      "--diff-filter=ACM"]).decode()
    changed_files_list = changed_files_str.split("\n")
    changed_code_files = []
    for cf in changed_files_list:
        # A code should have atleast one char in name + dot + one char ext
        if len(cf) > 2:
            changed_code_files.append(cf)
    return changed_code_files

def get_lang(files: List[str]) -> str:
    lang = ""
    for f in files:
        f_name_ext = f.rsplit(".", 1)
        if len(f_name_ext) > 1:
            name, ext = f_name_ext[0], f_name_ext[1]
            # Only "epi_judge_" prefix folders are considered as attempt
            if name.startswith("epi_judge_") and ext in extension_lang_map:
                if not lang:
                    lang = extension_lang_map[ext]
                elif lang != extension_lang_map[ext]:
                    print("WARNING: Multiple language files found, "
                          "switching off language prefix")
                    lang = ""
    return lang

def update_commit_message(attempt: int, lang: str):
    commit_msg_filepath = sys.argv[1]
    with open(commit_msg_filepath, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        commit_prefix = f"A{attempt}-{lang}: "
        f.write(f"{commit_prefix}{content}")

def main():
    if not check_args():
        return 0
    attempt = has_attempt()
    if attempt:
        files = filter_code_files()
        lang = get_lang(files)
        if lang:
            update_commit_message(attempt, lang)
    return 0

main()
