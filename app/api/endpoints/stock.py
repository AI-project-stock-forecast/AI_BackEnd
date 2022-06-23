from typing import Type, Union

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from app.ai.data_crawling import *

router = InferringRouter()


@cbv(router)
class Stock:
    @router.get("/{event}")
    def get_jongmok_list(self, event: str):
        return get_jongmok_list(event)

    @router.get("/")
    def get_quant_list(self):
        return get_quant_list()

    @router.get("/prediction/{code}")
    def get_predict(self, code: str):
        sise_datas = get_sise_data(code)
        sise_datas = list(map(lambda data: data[1], sise_datas))
        return predict(sise_datas)

    @router.get("/price/{code}")
    def get_sise_data(self, code: str):
        return get_sise_data(code)
