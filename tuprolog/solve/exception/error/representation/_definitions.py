from tuprolog import logger
import jpype.imports  # noqa: F401
import it.unibo.tuprolog.solve.exception.error as _errors  # type: ignore


RepresentationError = _errors.RepresentationError


Limit = RepresentationError.Limit


LIMIT_CHARACTER = Limit.CHARACTER


LIMIT_CHARACTER_CODE = Limit.CHARACTER_CODE


LIMIT_IN_CHARACTER_CODE = Limit.IN_CHARACTER_CODE


LIMIT_MAX_ARITY = Limit.MAX_ARITY


LIMIT_MAX_INTEGER = Limit.MAX_INTEGER


LIMIT_MIN_INTEGER = Limit.MIN_INTEGER


LIMIT_OOP_OBJECT = Limit.OOP_OBJECT


LIMIT_TOO_MANY_VARIABLES = Limit.TOO_MANY_VARIABLES


logger.debug("Loaded JVM classes from it.unibo.tuprolog.solve.exception.error.RepresentationError.*")
