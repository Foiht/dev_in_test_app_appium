import logging
import shlex
import subprocess


def run_cmd_with_output(cmd: str, shell: bool = False):
    logging.debug(f"Executing {cmd=}")
    if not shell:
        cmd = shlex.split(cmd)
    resp = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=shell)
    return resp.stdout, resp.stderr


def release_port(port_num: int) -> None:
    cmd_lsof = f'lsof -t -i tcp:{port_num}'
    out, err1 = run_cmd_with_output(cmd_lsof)
    out, err2 = run_cmd_with_output(f"kill -9 {out}")
    if err1 or err2:
        logging.debug(f"Errors occurred,\n{err1}\n{err2}")
