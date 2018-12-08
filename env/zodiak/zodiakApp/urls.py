from django.conf.urls import patterns, include, url
from django.conf import settings
import views
# from custom_functions import calculator,export_csv

urlpatterns = [
	        url(r'^$', views.adminPage, name='adminPage'),

			# url(r'^$', views.homepage, name='homepage'),
			# url(r'^index/$', views.index, name='index'),
	  		url(r'^accounts/login/$', views.user_login,  name="login"),
			url(r'^logout/$', views.user_logout, name='logout'),
	  		url(r'^register/$', views.register,  name="register"),
	  		url(r'^users/$', views.clientpage,  name="clientpage"),
	        url(r'^viewjobs/(?P<jobtype>.+)$',views.view_jobs, name = "view_jobs"),
	        url(r'^addjob/$',views.add_job, name = "add_job"),
	        # url(r'^new-category/$',views.add_category, name = "add_category"),
	        url(r'^jobedit/(?P<pk>.+)/$',views.job_edit, name = "job_edit"),
	        url(r'^jobview/(?P<pk>.+)/$',views.job_view, name = "job_view"),
	        url(r'^jobdelete/(?P<pk>.+)/$',views.job_delete, name = "job_delete"),
	        # url(r'^get-item/$',views.getItem, name = "get_item"),
	        # url(r'^edit-item/$',views.edit_item, name = "edit_item"),
	        # url(r'^shoppingCart/$',views.view_cart, name = "view_cart"),
	        # url(r'^getPage/(?P<identifier>.+)$',views.get_page, name = "get_page"),
	        # url(r'^newRecord/(?P<identifier>.+)$',views.add_record, name = "newrecord"),
	        # # url(r'^categoryPassed/(?P<value>.+)$',views.getPassedCategory, name = "getPassedCategory"),
	        # url(r'^confirm-order/$',views.get_confirmation_order, name = "get_confirmation_order"),
	        # # url(r'^Contact-us/$',views.contact, name = "contact"),
	        # url(r'^customer-list/$',views.all_customers, name = "all_customers"),
	        # url(r'^customer-payment-list/$',views.customer_payments, name = "all_customers_payments"),
	        # # url(r'^userComment/$',views.user_comment, name = "user_comment"),
	        # # url(r'^search-results/(?P<action>[-\w]+)/$',views.user_search, name = "user_search"),
	        # url(r'^remove-from-cart/(?P<item_pk>[-\w]+)/$',views.remove_from_cart, name = "remove_from_cart"),
	        # url(r'cart-box/$',views.cart_box, name = "cart_box"),
	        # url(r'^items/(?P<category>[-\w]+)/$',views.allStoreItems, name = "all-items"),
	        # url(r'^getRecord/(?P<action>.+)/(?P<identifier>.+)/(?P<pk>.+)/$',views.get_record, name = "get_record"),
	        # url(r'^viewService/(?P<identifier>.+)/(?P<pk>.+)/$',views.view_service, name = "view_service"),
	        # url(r'^storeitems/(?P<category>[-\w]+)/(?P<subcategory>[-\w]+)/$',views.storeItems, name = "store-items"),
	        # url(r'invoice/(?P<tracking_id>.+)/$', views.package_invoice_page, name="package_invoice"),
	        # # url(r'^calculator/$', calculator, name ="calculator"),
	        # # url(r'^export/csv/$', export_csv, name='export_csv'),
	        # # url(r'^staff-login-access/$', views.staff_login_access, name="staff_login_access"),
	        # url(r'^customer-orders/$', views.customer_orders, name="all_customer_orders"),
	        # url(r'^packages/$', views.customer_packages, name="all_customer_packages"),
	        # # url(r'^vendor/play/$', views.get_play_event, name="get_play_event"),   
	        # # url(r'^export/tradingDetails/(?P<useracc_obj>[-\w]+)/$', views.tradingDetails, name='tradingDetails'),
	        # # url(r'^closing/djp/$', views.close_djp_client, name="close_djp_client"),
	        # # pay-pal
	        # url(r'^confirm_paypal_payment/$', views.confirm_paypal_payment, name="confirm_paypal_payment"),

	        
	]

