from discount_service import DiscountService
from diwali_dis import DiwaliDis
from holi_dis import HoliDis

dd=DiwaliDis()
hd=HoliDis()

ds=DiscountService(dd)
ds.process()
ds.set_str(hd)
ds.process()
