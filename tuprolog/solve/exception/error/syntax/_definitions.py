from tuprolog import logger
import jpype.imports  # noqa: F401
import it.unibo.tuprolog.solve.exception.error as _errors  # type: ignore


SyntaxError = _errors.SyntaxError


logger.debug("Loaded JVM classes from it.unibo.tuprolog.solve.exception.error.SyntaxError.*")