from django.contrib import admin
from .models import Consumer ,Film ,Film_message,Food,Bill,Comment,Node,Usermessage,Transaction_Records

# Register your models here.

# class Transaction_RecordsAdmin(admin.ModelAdmin):
#     list_display = ('consumer', 'trans_num', 'trans_date', 'count', 'trans_info', 'trans_valid')
#     search_fields = ('trans_num',)

# 顾客
admin.site.register(Consumer)
# 电影
admin.site.register(Film)
# 售票记录
admin.site.register(Film_message)
# 零食
admin.site.register(Food)
# 用户消费表(千万注意和交易表同步)
# 用户看的
admin.site.register(Bill)
# 评论
admin.site.register(Comment)
# 点赞
admin.site.register(Node)
# 用户消息表(用户交易信息,账号变化)
admin.site.register(Usermessage)
# 交易表
# 管理员看的
admin.site.register(Transaction_Records)
