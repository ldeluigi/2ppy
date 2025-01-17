from tuprolog.solve import ExecutionContext
from ._definitions import SyntaxError


def syntax_error(
        context: ExecutionContext,
        message: str
) -> SyntaxError:
    return SyntaxError.of(context, message)


def syntax_error_while_parsing_term(
        context: ExecutionContext,
        input: str,
        row: int,
        column: int,
        message: str
) -> SyntaxError:
    return SyntaxError.whileParsingTerm(context, input, row, column, message)


def syntax_error_while_parsing_clauses(
        context: ExecutionContext,
        input: str,
        index: int,
        row: int,
        column: int,
        message: str
) -> SyntaxError:
    return SyntaxError.whileParsingClauses(context, input, index, row, column, message)


def error_detector(text: str, line: int, column: int, message: str = None) -> str:
    return SyntaxError.errorDetector(text, line, column, message)
