"""Jitclass.

jit compile decorator to generate jitclasses when appropriate. Useful
for class inheritance
"""

from typing import Callable, Type, TypeVar

from numba.experimental import jitclass
from numba.experimental.jitclass.base import JitClassType

T = TypeVar("T")


def jit_compile(
    GLOBAL_NAME, MODULE_NAME
) -> Callable[[Type[T]], JitClassType | T]:
    """_summary_.

    Args:
        GLOBAL_NAME (_type_): _description_
        MODULE_NAME (_type_): _description_

    Returns:
        Callable[[Type[T]], JitClassType | T]: _description_
    """
    # print(f"GLOBAL_NAME: {GLOBAL_NAME}", flush=True)
    # print(f"MODULE_NAME: {MODULE_NAME}", flush=True)
    def apply_jitclass(cls: T) -> JitClassType | T:
        """_summary_.

        Args:
            cls (T): _description_

        Returns:
            JitClassType | T: _description_
        """
        # print(f"__name__: {__name__}")
        if MODULE_NAME == GLOBAL_NAME:
            return jitclass(cls)  # type: ignore
        return cls

    return apply_jitclass
