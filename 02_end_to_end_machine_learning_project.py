#파이썬 버전 확인
import sys
assert sys.version_info >= (3,7)

#scikit-learn 버전 확인
from packaging import version
import sklearn
assert version.parse(sklearn.__version__) >= version.parse("1.0.1")

#필요한 모듈 임포트
## Path: 파일 및 디렉터리 작업을 위해 사용
## pandas: data analysis, 조작 라이브러리
## tarfile:.tar or .tar.gz file 추출
## urllib.request: URL에서 파일 다운롣,
from pathlib import Path
import pandas as pd
import tarfile
import urllib.request


def load_housing_data():
    tarball_path = Path("datasets/housing.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok = True)
        url = "https://github.com/ageron/data/raw/main/housing.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as housing_tarball:
            housing_tarball.extractall(path="datasets")
    return pd.read_csv(Path("datasets/housing/housing.csv"))

#함수 호출
housing=load_housing_data()

print(housing.head())
