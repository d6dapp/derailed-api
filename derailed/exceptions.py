# The Derailed API
#
# Copyright 2022 Derailed Inc. All rights reserved.
#
# Sharing of any piece of code to any unauthorized third-party is not allowed.
from fastapi import HTTPException


class DerailedException(Exception):
    pass


class NoAuthorizationError(HTTPException):
    def __init__(self) -> None:
        super().__init__(401, 'No Authorization')
