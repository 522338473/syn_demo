from django.db import models


class Channel(models.Model):
    memo = models.CharField(max_length=255, null=True, blank=True, verbose_name="渠道备注")
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="渠道名称")

    class Meta:
        verbose_name_plural = "渠道信息表"

    def __str__(self):
        return self.memo


class UserOrder(models.Model):
    token = models.CharField(max_length=255, null=True, blank=True, verbose_name="唯一标识")  # 认证通过才有
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name="手机号")
    password = models.CharField(max_length=255, null=True, blank=True, verbose_name="密码")
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name="姓名")
    age = models.CharField(max_length=255, null=True, blank=True, verbose_name="年龄")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="家庭住址")
    card_num = models.CharField(max_length=255, null=True, blank=True, verbose_name="身份证号")
    position_range = models.CharField(max_length=255, null=True, blank=True, verbose_name="贷款额度")
    time_range = models.CharField(max_length=255, null=True, blank=True, verbose_name="贷款期限")
    channel = models.ForeignKey(to="Channel", null=True, blank=True, verbose_name="所属渠道")
    reg_time = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="注册时间")

    class Meta:
        verbose_name_plural = "用户信息表"

    def __str__(self):
        return self.phone


class Position(models.Model):
    position_low = models.CharField(max_length=255, blank=True, null=True, verbose_name="最低额度")
    position_high = models.CharField(max_length=255, blank=True, null=True, verbose_name="最高额度")

    class Meta:
        verbose_name_plural = "贷款额度表"

    def __str__(self):
        return self.position_low + "-" + self.position_high


class Timer(models.Model):
    time_low = models.CharField(max_length=255, blank=True, null=True, verbose_name="最低期限")
    time_high = models.CharField(max_length=255, blank=True, null=True, verbose_name="最高期限")

    class Meta:
        verbose_name_plural = "贷款期限表"

    def __str__(self):
        return self.time_low + "-" + self.time_high


class Month(models.Model):
    month_low = models.CharField(max_length=255, blank=True, null=True, verbose_name="最低月利率")
    month_high = models.CharField(max_length=255, blank=True, null=True, verbose_name="最高月利率")

    class Meta:
        verbose_name_plural = "月利率表"

    def __str__(self):
        return self.month_low + "-" + self.month_high


class Approve(models.Model):
    ranges = models.CharField(max_length=255, null=True, blank=True, verbose_name="审批时长")

    class Meta:
        verbose_name_plural = "审批时长表"

    def __str__(self):
        return self.ranges


class Provider(models.Model):
    product_brief = models.CharField(max_length=255, null=True, blank=True, verbose_name="机构介绍")
    product_icon = models.FileField(upload_to="media/upload", null=True, blank=True, verbose_name="产品图标")
    product_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="产品名称")
    product_num = models.CharField(max_length=255, null=True, blank=True, verbose_name="放款人数")
    position_range = models.ForeignKey(to="Position", null=True, blank=True, verbose_name="额度范围")
    time_range = models.ForeignKey(to="Timer", null=True, blank=True, verbose_name="期限范围")
    month_range = models.ForeignKey(to="Month", null=True, blank=True, verbose_name="月利率")
    approve_range = models.ForeignKey(to="Approve", null=True, blank=True, verbose_name="审批时长")

    class Meta:
        verbose_name_plural = "客户信息表"

    def __str__(self):
        return self.product_name
