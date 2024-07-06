requirements = [
    ('ply', 'ply'),
    ('chardet', 'chardet'),
    # ('GitPython', 'git'),
    ('colorama', 'colorama'),
    ('requests', 'requests'),
]


tuna = 'https://pypi.tuna.tsinghua.edu.cn/simple/'

def test_requirements():
    import importlib
    import sys
    import os
    import pip

    for package_name, import_name in requirements:
        try:
            importlib.import_module(import_name)
        except:
            print(f'Missing Important Dependence `{package_name}`\nTrying to Install for You...')
            if os.environ.get('CODESPACES'):
                pip.main(['install', package_name])
                # os.system(f'"{sys.executable}" -m pip install {package_name}')
            else:
                pip.main(['install', package_name, '-i', {tuna}])
                # os.system(f'"{sys.executable}" -m pip install {package_name} -i {tuna}')
