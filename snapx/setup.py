from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="snapx",
        author="snap.stanford.edu",
        version="0.0.1",
        packages=find_packages(),
        description="""SnapX: An experimental SNAP API with NetworkX-like interface"""
    )
