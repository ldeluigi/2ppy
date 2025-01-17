from tuprolog.core import Term, Substitution
from ._definitions import Unificator, DEFAULT_UNIFICATOR


def strict_unificator(context: Substitution = None) -> Unificator:
    if context is None:
        return Unificator.strict()
    else:
        return Unificator.strict(context)


def naive_unificator(context: Substitution = None) -> Unificator:
    if context is None:
        return Unificator.naive()
    else:
        return Unificator.naive(context)


def cached_unificator(unificator: Unificator, cache_size: int = Unificator.DEFAULT_CACHE_CAPACITY) -> Unificator:
    return Unificator.cached(unificator, cache_size)


def unificator(context: Substitution = None) -> Unificator:
    return cached_unificator(strict_unificator(context))


def mgu(x: Term, y: Term, occur_check: bool = True) -> Substitution:
    return DEFAULT_UNIFICATOR.mgu(x, y, occur_check)


def unify(x: Term, y: Term, occur_check: bool = True) -> Term:
    return DEFAULT_UNIFICATOR.unify(x, y, occur_check)


def match(x: Term, y: Term, occur_check: bool = True) -> bool:
    return DEFAULT_UNIFICATOR.match(x, y, occur_check)
