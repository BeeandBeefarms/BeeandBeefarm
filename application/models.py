# from django.db import models
#
# # Create your models here.
#
# class log_in_dtl_tbl(models.Model):
#     log_in_email=models.CharField(max_length=40)
#     log_in_pwd=models.CharField(max_length=14)
#     user_id=models.CharField(max_length=10,primary_key=True)
#     class Meta:
#         app_label='log_in_dtl_tbl'
#         managed = True
#
#
# class user_dtl_tbl(models.Model):
#     user_id=models.CharField(max_length=10,primary_key=True)
#     user_first_name=models.CharField(max_length=40)
#     user_last_name=models.CharField(max_length=40)
#     user_loc_state=models.CharField(max_length=30)
#     user_loc_distict=models.CharField(max_length=100)
#     user_loc_area=models.CharField(max_length=100)
#     user_loc_pincode=models.IntegerField()
#     user_mob_number=models.CharField(max_length=15)
#     class Meta:
#         app_label='user_dtl_tbl'
#         managed = True
#
#
# class user_input_data(models.Model):
#     user_id=models.CharField(max_length=10,primary_key=True)
#     req_item=models.CharField(max_length=40)
#     req_qty=models.CharField(max_length=40)
#     bid_amount=models.CharField(max_length=40)
#     order_date=models.DateField()
#     class Meta:
#         app_label='user_input_data'
#         managed = True
#
# class order_dtl_tbl(models.Model):
#     user_id = models.CharField(max_length=10, primary_key=True)
#     user_first_name=models.CharField(max_length=40)
#     user_last_name=models.CharField(max_length=40)
#     user_loc_state=models.CharField(max_length=30)
#     user_loc_distict=models.CharField(max_length=100)
#     user_loc_area=models.CharField(max_length=100)
#     user_loc_pincode=models.IntegerField()
#     user_mob_number=models.CharField(max_length=15)
#     alt_user_mob_number = models.CharField(max_length=15)
#     req_item=models.CharField(max_length=40)
#     req_qty=models.CharField(max_length=40)
#     bid_amount=models.CharField(max_length=40)
#
#     class Meta:
#         app_label='order_dtl_tbl'
#         managed = True
#
