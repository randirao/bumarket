from fastapi import status

class BumarketException(Exception):
    def __init__(self, message: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.status_code = status_code

class UserNotFoundException(BumarketException):
    def __init__(self):
        super().__init__(
            message="사용자를 찾을 수 없습니다.",
            status_code=status.HTTP_404_NOT_FOUND
        )

class UploadException(Exception):
    def __init__(self, msg, status_code: int = status.HTTP_400_BAD_REQUEST):
        self.msg = msg
        self.status_code = status_code

class InvalidImageFormatException(UploadException):
    def __init__(self):
        super().__init__("Invalid image format")

class ImageFoundException(UploadException):
    def __init__(self, student_id: int):
        super().__init__(
            msg=f"imgnotfound",
            status_code=status.HTTP_404_NOT_FOUND
        )
