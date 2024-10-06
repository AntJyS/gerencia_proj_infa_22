# https://pyinstaller.org/en/stable/hooks-config.html#adding-an-option-to-the-hook `hook_api` is a PostGraphAPI
# Nothing in this module is meant to be initialized externally.
# Instances are exposed through hooks during build.

from _typeshed import StrOrBytesPath
from collections.abc import Generator, Iterable
from types import CodeType
from typing import Literal

from PyInstaller.building.build_main import Analysis
from PyInstaller.building.datastruct import TOC
from PyInstaller.depend.analysis import PyiModuleGraph
from PyInstaller.lib.modulegraph.modulegraph import Package

# https://pyinstaller.org/en/stable/hooks.html#the-pre-safe-import-module-psim-api-method
class PreSafeImportModuleAPI:
    module_basename: str
    module_name: str
    def __init__(
        self, module_graph: PyiModuleGraph, module_basename: str, module_name: str, parent_package: Package | None
    ) -> None: ...
    @property
    def module_graph(self) -> PyiModuleGraph: ...
    @property
    def parent_package(self) -> Package | None: ...
    def add_runtime_module(self, module_name: str) -> None: ...
    def add_runtime_package(self, package_name: str) -> None: ...
    def add_alias_module(self, real_module_name: str, alias_module_name: str) -> None: ...
    def append_package_path(self, directory: str) -> None: ...

# https://pyinstaller.org/en/stable/hooks.html#the-pre-find-module-path-pfmp-api-method
class PreFindModulePathAPI:
    search_dirs: Iterable[StrOrBytesPath]
    def __init__(self, module_graph: PyiModuleGraph, module_name: str, search_dirs: Iterable[StrOrBytesPath]) -> None: ...
    @property
    def module_graph(self) -> PyiModuleGraph: ...
    @property
    def module_name(self) -> str: ...

# https://pyinstaller.org/en/stable/hooks.html#the-hook-hook-api-function
class PostGraphAPI:
    module_graph: PyiModuleGraph
    module: Package
    def __init__(self, module_name: str, module_graph: PyiModuleGraph, analysis: Analysis) -> None: ...
    @property
    def __file__(self) -> str: ...
    @property
    def __path__(self) -> tuple[str, ...] | None: ...
    @property
    def __name__(self) -> str: ...
    # Compiled code. See stdlib.builtins.compile
    @property
    def co(self) -> CodeType: ...
    @property
    def analysis(self) -> Analysis: ...
    @property
    def name(self) -> str: ...
    @property
    def graph(self) -> PyiModuleGraph: ...
    @property
    def node(self) -> Package: ...
    @property
    def imports(self) -> Generator[Package, None, None]: ...
    def add_imports(self, *module_names: str) -> None: ...
    def del_imports(self, *module_names: str) -> None: ...
    def add_binaries(self, binaries: TOC | Iterable[tuple[StrOrBytesPath, StrOrBytesPath]]) -> None: ...
    def add_datas(self, datas: TOC | Iterable[tuple[StrOrBytesPath, StrOrBytesPath]]) -> None: ...
    def set_module_collection_mode(
        self, name: str | None, mode: Literal["pyz", "pyc", "py", "pyz+py", "py+pyz"] | None
    ) -> None: ...
