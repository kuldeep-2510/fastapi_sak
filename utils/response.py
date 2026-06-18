from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

def success_response(
    data=None,
    message="Success",
    status_code=200,
    pagination=None
):

    return JSONResponse(
    status_code=status_code,
    content=jsonable_encoder(
        {
            "success": True,
            "status_code": status_code,
            "message": message,
            "pagination":pagination,
            "data": data,
        
        }
    )
)


def error_response(
    message="Failed",
    status_code=400,
    data=None
):

    return JSONResponse(
    status_code=status_code,
    content=jsonable_encoder(
        {
            "success": False,
            "status_code": status_code,
            "message": message,
            "data": data
        }
    )
)