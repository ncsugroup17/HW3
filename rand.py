"""
Import for subprocess
"""
import subprocess

def random_array(arr):
    """
    Shuffle the array with random numbers.
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
